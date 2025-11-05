"""
Unit tests for individual services.
"""
import pytest
from unittest.mock import patch, AsyncMock, MagicMock
from app.modules.speech_to_text.service import SpeechToTextService
from app.modules.emotion_detection.service import EmotionDetectionService
from app.modules.translation.service import TranslationService
from app.modules.text_to_speech.service import TextToSpeechService


@pytest.mark.asyncio
class TestSpeechToTextService:
    """Tests for Speech-to-Text service."""
    
    @patch("httpx.AsyncClient.post")
    async def test_transcribe_audio_success(self, mock_post):
        """Test successful audio transcription."""
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "results": {
                "channels": [
                    {
                        "alternatives": [
                            {"transcript": "Hello world"}
                        ],
                        "detected_language": "en"
                    }
                ]
            }
        }
        mock_response.raise_for_status = MagicMock()
        mock_post.return_value = mock_response
        
        service = SpeechToTextService()
        result = await service.transcribe_audio(b"fake_audio", "audio/wav")
        
        assert result["text"] == "Hello world"
        assert result["language"] == "English"
        assert result["language_code"] == "en"


@pytest.mark.asyncio
class TestEmotionDetectionService:
    """Tests for Emotion Detection service."""
    
    async def test_mock_emotion_detection(self):
        """Test mock emotion detection fallback."""
        service = EmotionDetectionService()
        result = await service._mock_emotion_detection(b"fake_audio")
        
        assert "emotion" in result
        assert "attributes" in result
        assert result["emotion"] in ["happy", "sad", "angry", "neutral", "surprised"]
        assert "pitch_mean" in result["attributes"]
        assert "energy" in result["attributes"]


@pytest.mark.asyncio
class TestTranslationService:
    """Tests for Translation service."""
    
    @patch("httpx.AsyncClient.post")
    async def test_translate_text_success(self, mock_post):
        """Test successful text translation."""
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "translations": [
                {
                    "text": "Hola mundo",
                    "detected_source_language": "EN"
                }
            ]
        }
        mock_response.raise_for_status = MagicMock()
        mock_post.return_value = mock_response
        
        service = TranslationService()
        result = await service.translate_text("Hello world", "en", "es")
        
        assert result["translated_text"] == "Hola mundo"
        assert result["target_language"] == "es"
    
    def test_get_target_language(self):
        """Test automatic target language detection."""
        service = TranslationService()
        
        assert service._get_target_language("en") == "es"
        assert service._get_target_language("es") == "en"


@pytest.mark.asyncio
class TestTextToSpeechService:
    """Tests for Text-to-Speech service."""
    
    @patch("httpx.AsyncClient.post")
    async def test_generate_audio_success(self, mock_post):
        """Test successful audio generation."""
        mock_response = MagicMock()
        mock_response.content = b"fake_audio_data"
        mock_response.raise_for_status = MagicMock()
        mock_post.return_value = mock_response
        
        service = TextToSpeechService()
        audio = await service.generate_audio(
            "Hola mundo",
            emotion="happy",
            language_code="es"
        )
        
        assert audio == b"fake_audio_data"


