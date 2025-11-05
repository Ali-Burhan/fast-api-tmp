"""
Unit tests for utility functions.
"""
import pytest
from fastapi import HTTPException, UploadFile
from unittest.mock import MagicMock
from app.core.utils import (
    generate_audio_key,
    validate_audio_file,
    get_target_language,
    map_emotion_to_voice_settings,
)


def test_generate_audio_key():
    """Test audio key generation."""
    key1 = generate_audio_key()
    key2 = generate_audio_key()
    
    assert key1.startswith("cache/audio:")
    assert key2.startswith("cache/audio:")
    assert key1 != key2  # Should be unique


def test_validate_audio_file_valid():
    """Test validation with valid audio file."""
    mock_file = MagicMock(spec=UploadFile)
    mock_file.filename = "test.mp3"
    
    # Should not raise exception
    validate_audio_file(mock_file)


def test_validate_audio_file_invalid():
    """Test validation with invalid file format."""
    mock_file = MagicMock(spec=UploadFile)
    mock_file.filename = "test.txt"
    
    with pytest.raises(HTTPException) as exc_info:
        validate_audio_file(mock_file)
    
    assert exc_info.value.status_code == 400


def test_get_target_language():
    """Test target language detection."""
    assert get_target_language("en") == "es"
    assert get_target_language("English") == "es"
    assert get_target_language("es") == "en"
    assert get_target_language("Spanish") == "en"


def test_map_emotion_to_voice_settings():
    """Test emotion to voice settings mapping."""
    settings = map_emotion_to_voice_settings("happy", {})
    
    assert "stability" in settings
    assert "similarity_boost" in settings
    assert "style" in settings
    assert isinstance(settings["stability"], float)
    
    # Test different emotions
    emotions = ["happy", "sad", "angry", "neutral", "surprised"]
    for emotion in emotions:
        settings = map_emotion_to_voice_settings(emotion, {})
        assert 0 <= settings["stability"] <= 1
        assert 0 <= settings["similarity_boost"] <= 1


def test_map_emotion_with_attributes():
    """Test emotion mapping with acoustic attributes."""
    attributes = {
        "pitch_mean": 0.8,
        "energy": 0.7,
    }
    
    settings = map_emotion_to_voice_settings("happy", attributes)
    
    assert "stability" in settings
    assert "similarity_boost" in settings


