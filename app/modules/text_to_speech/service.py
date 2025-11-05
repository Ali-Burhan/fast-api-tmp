"""
Text-to-speech service using ElevenLabs API.
Synthesizes emotional speech preserving detected emotion attributes.
"""
import logging
import httpx
from typing import Dict, Optional
from app.core.config import settings
from app.core.utils import map_emotion_to_voice_settings

logger = logging.getLogger(__name__)


class TextToSpeechService:
    """Service for generating speech using ElevenLabs API."""
    
    def __init__(self):
        self.api_key = settings.ELEVENLABS_API_KEY
        self.base_url = "https://api.elevenlabs.io/v1"
        self.voice_id = settings.ELEVENLABS_VOICE_ID
        self.model_id = settings.ELEVENLABS_MODEL_ID
    
    async def generate_audio(
        self,
        text: str,
        emotion: str = "neutral",
        emotion_attributes: Optional[Dict] = None,
        language_code: str = "en",
    ) -> bytes:
        """
        Generate audio from text with emotion preservation.
        
        Args:
            text: Text to synthesize
            emotion: Detected emotion (happy, sad, angry, neutral, surprised)
            emotion_attributes: Emotion attributes from detection
            language_code: Target language code
        
        Returns:
            Binary audio data (MP3)
        
        Raises:
            Exception: If generation fails
        """
        try:
            # Map emotion to voice settings
            voice_settings = map_emotion_to_voice_settings(
                emotion,
                emotion_attributes or {}
            )
            
            url = f"{self.base_url}/text-to-speech/{self.voice_id}"
            
            headers = {
                "xi-api-key": self.api_key,
                "Content-Type": "application/json",
            }
            
            payload = {
                "text": text,
                "model_id": self.model_id,
                "voice_settings": voice_settings,
            }
            
            async with httpx.AsyncClient(timeout=60.0) as client:
                response = await client.post(
                    url,
                    headers=headers,
                    json=payload,
                )
                response.raise_for_status()
                audio_data = response.content
            
            logger.info(f"Audio generation successful. Size: {len(audio_data)} bytes")
            logger.debug(f"Emotion: {emotion}, Language: {language_code}")
            
            return audio_data
        
        except httpx.HTTPStatusError as e:
            logger.error(f"ElevenLabs API error: {e.response.status_code} - {e.response.text}")
            raise Exception(f"Audio generation failed: {e.response.text}")
        except Exception as e:
            logger.error(f"Audio generation error: {str(e)}")
            raise
    
    async def get_available_voices(self) -> list:
        """
        Get list of available voices from ElevenLabs.
        
        Returns:
            List of voice dictionaries
        """
        try:
            url = f"{self.base_url}/voices"
            
            headers = {
                "xi-api-key": self.api_key,
            }
            
            async with httpx.AsyncClient(timeout=30.0) as client:
                response = await client.get(url, headers=headers)
                response.raise_for_status()
                data = response.json()
            
            voices = data.get("voices", [])
            logger.info(f"Retrieved {len(voices)} available voices")
            
            return voices
        
        except Exception as e:
            logger.error(f"Failed to get voices: {str(e)}")
            return []


# Global service instance
text_to_speech_service = TextToSpeechService()


