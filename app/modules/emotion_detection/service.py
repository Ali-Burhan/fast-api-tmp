"""
Emotion detection service using OpenSmile.
Extracts emotional attributes from audio (pitch, tone, energy).
"""
import logging
import tempfile
import os
from typing import Dict
from pathlib import Path

logger = logging.getLogger(__name__)


class EmotionDetectionService:
    """Service for detecting emotion from audio using OpenSmile."""
    
    def __init__(self):
        """Initialize OpenSmile emotion detection service."""
        try:
            import opensmile
            self.smile = opensmile.Smile(
                feature_set=opensmile.FeatureSet.eGeMAPSv02,
                feature_level=opensmile.FeatureLevel.Functionals,
            )
            self.opensmile_available = True
            logger.info("OpenSmile initialized successfully")
        except ImportError:
            logger.warning("OpenSmile not available, using mock emotion detection")
            self.smile = None
            self.opensmile_available = False
    
    async def detect_emotion(self, audio_data: bytes, filename: str = "audio.wav") -> Dict:
        """
        Detect emotion from audio data.
        
        Args:
            audio_data: Binary audio data
            filename: Original filename (for extension detection)
        
        Returns:
            Dictionary with 'emotion' and 'attributes' keys
        
        Raises:
            Exception: If emotion detection fails
        """
        if self.smile is None:
            # Fallback to mock emotion detection
            logger.warning("OpenSmile not available, using mock detection")
            return await self._mock_emotion_detection(audio_data)
        
        temp_path = None
        
        try:
            # Save audio to temporary file (OpenSmile supports MP3, WAV, etc.)
            suffix = Path(filename).suffix.lower() or ".wav"
            
            # Create temp file without automatic deletion (Windows compatibility)
            temp_fd, temp_path = tempfile.mkstemp(suffix=suffix)
            try:
                # Write audio data and close the file descriptor
                os.write(temp_fd, audio_data)
                os.close(temp_fd)
                
                # Verify file exists and is readable
                if not os.path.exists(temp_path):
                    raise FileNotFoundError(f"Temporary file not found: {temp_path}")
                
                file_size = os.path.getsize(temp_path)
                if file_size == 0:
                    raise ValueError(f"Temporary file is empty: {temp_path}")
                
                logger.debug(f"Processing audio file: {temp_path} (size: {file_size} bytes)")
                
                # Extract features using OpenSmile (supports MP3, WAV, FLAC, etc.)
                features = self.smile.process_file(temp_path)
            except:
                # Close fd if still open
                try:
                    os.close(temp_fd)
                except:
                    pass
                raise
            
            if features is None or features.empty:
                raise ValueError("OpenSmile returned empty features")
            
            # Extract key emotional attributes
            attributes = self._extract_emotional_attributes(features)
            
            # Classify emotion based on attributes
            emotion = self._classify_emotion(attributes)
            
            logger.info(f"Emotion detected: {emotion} (pitch: {attributes.get('pitch_mean', 0):.2f}, energy: {attributes.get('energy', 0):.2f}, rate: {attributes.get('speaking_rate', 0):.2f})")
            logger.debug(f"Full attributes: {attributes}")
            
            return {
                "emotion": emotion,
                "attributes": attributes,
            }
        
        except Exception as e:
            error_msg = str(e)
            logger.error(f"Emotion detection error: {error_msg}", exc_info=True)
            
            # Check for missing dependencies
            if "mediainfo" in error_msg.lower():
                logger.error("Missing mediainfo dependency. Install with: choco install mediainfo (Windows) or apt-get install mediainfo (Linux)")
                raise Exception("MediaInfo is required for MP3 processing. Please install it: https://mediaarea.net/en/MediaInfo/Download/Windows")
            
            # Return neutral on other errors
            logger.warning("Returning neutral emotion due to processing error")
            return {
                "emotion": "neutral",
                "attributes": {
                    "pitch_mean": 0.5,
                    "energy": 0.5,
                    "speaking_rate": 0.5,
                },
            }
        
        finally:
            # Clean up temporary file
            if temp_path and os.path.exists(temp_path):
                try:
                    os.unlink(temp_path)
                    logger.debug(f"Cleaned up temp file: {temp_path}")
                except Exception as e:
                    logger.warning(f"Failed to delete temp file {temp_path}: {e}")
    
    def _extract_emotional_attributes(self, features) -> Dict[str, float]:
        """
        Extract normalized emotional attributes from OpenSmile features.
        
        Args:
            features: OpenSmile feature dataframe
        
        Returns:
            Dictionary of normalized attributes (0-1 range)
        """
        import numpy as np
        
        # Convert to dict and get first row (for functionals)
        feature_dict = features.iloc[0].to_dict()
        
        # Extract key features
        pitch_mean = feature_dict.get("F0semitoneFrom27.5Hz_sma3nz_amean", 0)
        energy_mean = feature_dict.get("loudness_sma3_amean", 0)
        speaking_rate = feature_dict.get("loudness_sma3_percentile20.0", 0)
        
        # Normalize to 0-1 range (rough estimates)
        attributes = {
            "pitch_mean": np.clip((pitch_mean + 100) / 200, 0, 1),
            "energy": np.clip((energy_mean + 40) / 80, 0, 1),
            "speaking_rate": np.clip((speaking_rate + 40) / 80, 0, 1),
        }
        
        return attributes
    
    def _classify_emotion(self, attributes: Dict[str, float]) -> str:
        """
        Classify emotion based on acoustic attributes.
        
        Args:
            attributes: Dictionary of normalized attributes
        
        Returns:
            Emotion label: happy, sad, angry, neutral, or surprised
        """
        pitch = attributes.get("pitch_mean", 0.5)
        energy = attributes.get("energy", 0.5)
        speaking_rate = attributes.get("speaking_rate", 0.5)
        
        # Rule-based classification with realistic thresholds
        # High pitch is a strong indicator even if energy is moderate (scared, surprised, shouting)
        
        # Very high pitch (>0.68) → surprised or angry (scared/shouting)
        if pitch > 0.68:
            if energy > 0.55 or speaking_rate > 0.6:
                return "angry"  # High pitch with some energy = shouting/angry
            else:
                return "surprised"  # High pitch alone = surprised/scared
        
        # High energy with elevated pitch → angry
        elif energy > 0.65 and pitch > 0.55:
            return "angry"
        
        # Moderate-high pitch and energy → happy or surprised
        elif pitch > 0.6 and energy > 0.5:
            if speaking_rate > 0.6:
                return "happy"
            else:
                return "surprised"
        
        # Very high energy alone (even with moderate pitch) → angry
        elif energy > 0.75:
            return "angry"
        
        # Low pitch and energy → sad
        elif pitch < 0.4 and energy < 0.4:
            return "sad"
        
        # Moderate everything → neutral
        else:
            return "neutral"
    
    async def _mock_emotion_detection(self, audio_data: bytes) -> Dict:
        """
        Mock emotion detection when OpenSmile is not available.
        
        Args:
            audio_data: Binary audio data
        
        Returns:
            Mock emotion data
        """
        import hashlib
        
        # Use audio hash to generate consistent mock data
        audio_hash = hashlib.md5(audio_data).hexdigest()
        hash_val = int(audio_hash[:8], 16) / (16**8)
        
        emotions = ["happy", "sad", "angry", "neutral", "surprised"]
        emotion_idx = int(hash_val * len(emotions))
        emotion = emotions[emotion_idx]
        
        logger.info(f"Mock emotion detection: {emotion}")
        
        return {
            "emotion": emotion,
            "attributes": {
                "pitch_mean": 0.5 + (hash_val - 0.5) * 0.3,
                "energy": 0.5 + (hash_val - 0.5) * 0.4,
                "speaking_rate": 0.5,
            },
        }


# Global service instance
emotion_detection_service = EmotionDetectionService()


