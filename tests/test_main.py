"""
Unit tests for main API endpoints.
"""
import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch, AsyncMock
from app.main import app

client = TestClient(app)


def test_root_endpoint():
    """Test root endpoint returns app info."""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "name" in data
    assert "version" in data
    assert "status" in data
    assert data["status"] == "running"


def test_health_check():
    """Test health check endpoint."""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert "status" in data


@pytest.mark.asyncio
@patch("app.modules.speech_to_text.service.speech_to_text_service.transcribe_audio")
@patch("app.modules.emotion_detection.service.emotion_detection_service.detect_emotion")
@patch("app.modules.translation.service.translation_service.translate_text")
@patch("app.modules.text_to_speech.service.text_to_speech_service.generate_audio")
async def test_process_audio_integration(
    mock_tts,
    mock_translation,
    mock_emotion,
    mock_stt,
):
    """Test complete audio processing pipeline with mocked services."""
    
    # Mock service responses
    mock_stt.return_value = {
        "language": "English",
        "language_code": "en",
        "text": "Hello world",
    }
    
    mock_emotion.return_value = {
        "emotion": "happy",
        "attributes": {
            "pitch_mean": 0.65,
            "energy": 0.72,
            "speaking_rate": 0.55,
        },
    }
    
    mock_translation.return_value = {
        "translated_text": "Hola mundo",
        "source_language": "en",
        "target_language": "es",
    }
    
    mock_tts.return_value = b"fake_audio_data"
    
    # Create a fake audio file
    files = {
        "audio": ("test.wav", b"fake_audio_content", "audio/wav")
    }
    
    response = client.post("/api/process-audio", files=files)
    
    assert response.status_code == 200
    data = response.json()
    
    assert "original_text" in data
    assert "translated_text" in data
    assert "emotion" in data
    assert "audio_base64" in data
    assert data["original_text"] == "Hello world"
    assert data["translated_text"] == "Hola mundo"
    assert data["emotion"] == "happy"


def test_process_audio_invalid_file():
    """Test process audio with invalid file format."""
    files = {
        "audio": ("test.txt", b"not an audio file", "text/plain")
    }
    
    response = client.post("/api/process-audio", files=files)
    assert response.status_code == 400


def test_api_docs_available():
    """Test that API documentation is accessible."""
    response = client.get("/docs")
    assert response.status_code == 200
    
    response = client.get("/redoc")
    assert response.status_code == 200
