"""
Router for speech-to-text endpoints.
"""
from fastapi import APIRouter, UploadFile, File, HTTPException
from pydantic import BaseModel
from app.modules.speech_to_text.service import speech_to_text_service
from app.core.utils import validate_audio_file

router = APIRouter(prefix="/speech-to-text", tags=["Speech-to-Text"])


class TranscriptionResponse(BaseModel):
    """Response model for transcription."""
    language: str
    language_code: str
    text: str


@router.post("/transcribe", response_model=TranscriptionResponse)
async def transcribe(audio: UploadFile = File(...)):
    """
    Transcribe audio file to text with language detection.
    
    Args:
        audio: Audio file (mp3, wav, m4a, flac, ogg, webm)
    
    Returns:
        Transcription with detected language
    """
    try:
        # Validate audio file
        validate_audio_file(audio)
        
        # Read audio data
        audio_data = await audio.read()
        
        # Transcribe
        result = await speech_to_text_service.transcribe_audio(
            audio_data,
            mimetype=audio.content_type or "audio/wav"
        )
        
        return result
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


