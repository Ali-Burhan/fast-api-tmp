"""
Utility functions for the application.
"""
import uuid
import logging
from pathlib import Path
from typing import Optional
from fastapi import UploadFile, HTTPException
from app.core.config import settings

logger = logging.getLogger(__name__)


def generate_audio_key(prefix: str = "audio") -> str:
    """
    Generate a unique key for caching audio.
    
    Args:
        prefix: Prefix for the key
    
    Returns:
        Unique key string
    """
    return f"cache/{prefix}:{uuid.uuid4()}"


def validate_audio_file(file: UploadFile) -> None:
    """
    Validate uploaded audio file.
    
    Args:
        file: Uploaded file
    
    Raises:
        HTTPException: If validation fails
    """
    # Check file extension
    file_ext = Path(file.filename).suffix.lower()
    if file_ext not in settings.SUPPORTED_AUDIO_FORMATS:
        raise HTTPException(
            status_code=400,
            detail=f"Unsupported audio format. Supported: {', '.join(settings.SUPPORTED_AUDIO_FORMATS)}"
        )
    
    # Note: Size validation should be done during upload with Request.body() size limit
    logger.debug(f"Audio file validated: {file.filename}")


def get_target_language(detected_language: str) -> str:
    """
    Determine target language for translation.
    
    Args:
        detected_language: Detected source language
    
    Returns:
        Target language code
    """
    language_map = {
        "en": "es",  # English -> Spanish
        "es": "en",  # Spanish -> English
    }
    
    # Normalize language code
    lang_code = detected_language.lower()[:2]
    return language_map.get(lang_code, "en")


def map_emotion_to_voice_settings(emotion: str, attributes: dict) -> dict:
    """
    Map detected emotion to ElevenLabs voice settings.
    
    Args:
        emotion: Detected emotion (happy, sad, angry, neutral, surprised)
        attributes: Emotion attributes (pitch, energy, etc.)
    
    Returns:
        Voice settings dict for ElevenLabs API
    """
    # Base settings
    voice_settings = {
        "stability": 0.5,
        "similarity_boost": 0.75,
        "style": 0.0,
        "use_speaker_boost": True
    }
    
    # Adjust based on emotion
    emotion_adjustments = {
        "happy": {"stability": 0.4, "similarity_boost": 0.8, "style": 0.3},
        "sad": {"stability": 0.7, "similarity_boost": 0.6, "style": 0.0},
        "angry": {"stability": 0.3, "similarity_boost": 0.9, "style": 0.5},
        "neutral": {"stability": 0.5, "similarity_boost": 0.75, "style": 0.0},
        "surprised": {"stability": 0.4, "similarity_boost": 0.8, "style": 0.4},
    }
    
    if emotion in emotion_adjustments:
        voice_settings.update(emotion_adjustments[emotion])
    
    # Further adjust based on pitch and energy if available
    if attributes:
        pitch_mean = attributes.get("pitch_mean", 0)
        energy = attributes.get("energy", 0)
        
        # Subtle adjustments based on acoustic features
        if pitch_mean > 0.6:
            voice_settings["stability"] = max(0.2, voice_settings["stability"] - 0.1)
        elif pitch_mean < 0.4:
            voice_settings["stability"] = min(0.9, voice_settings["stability"] + 0.1)
    
    logger.debug(f"Voice settings for emotion '{emotion}': {voice_settings}")
    return voice_settings


def format_error_response(error: Exception, context: str = "") -> dict:
    """
    Format error response consistently.
    
    Args:
        error: Exception object
        context: Additional context about the error
    
    Returns:
        Error response dict
    """
    error_message = str(error)
    if context:
        error_message = f"{context}: {error_message}"
    
    logger.error(error_message)
    
    return {
        "error": True,
        "message": error_message,
        "type": type(error).__name__
    }


