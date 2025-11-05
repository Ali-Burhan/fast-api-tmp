"""
Pytest configuration and fixtures.
"""
import pytest
import asyncio
from unittest.mock import AsyncMock, patch


@pytest.fixture(scope="session")
def event_loop():
    """Create an instance of the default event loop for the test session."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(autouse=True)
def mock_redis():
    """Mock Redis client for all tests."""
    with patch("app.core.redis_client.redis_client.connect", new=AsyncMock()):
        with patch("app.core.redis_client.redis_client.disconnect", new=AsyncMock()):
            with patch("app.core.redis_client.redis_client.set_audio", new=AsyncMock(return_value=True)):
                with patch("app.core.redis_client.redis_client.delete_audio", new=AsyncMock(return_value=True)):
                    with patch("app.core.redis_client.redis_client.exists", new=AsyncMock(return_value=True)):
                        yield


@pytest.fixture
def sample_audio_data():
    """Sample audio data for testing."""
    return b"fake_audio_content_for_testing"


@pytest.fixture
def sample_transcription():
    """Sample transcription result."""
    return {
        "language": "English",
        "language_code": "en",
        "text": "Hello, how are you?",
    }


@pytest.fixture
def sample_emotion():
    """Sample emotion detection result."""
    return {
        "emotion": "happy",
        "attributes": {
            "pitch_mean": 0.65,
            "energy": 0.72,
            "speaking_rate": 0.55,
        },
    }


@pytest.fixture
def sample_translation():
    """Sample translation result."""
    return {
        "translated_text": "Hola, ¿cómo estás?",
        "source_language": "en",
        "target_language": "es",
    }
