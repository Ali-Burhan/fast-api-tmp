"""
Router for text-to-speech endpoints.
"""
from fastapi import APIRouter, HTTPException
from fastapi.responses import Response
from pydantic import BaseModel
from typing import Optional, Dict
from app.modules.text_to_speech.service import text_to_speech_service

router = APIRouter(prefix="/text-to-speech", tags=["Text-to-Speech"])


class TTSRequest(BaseModel):
    """Request model for text-to-speech."""
    text: str
    emotion: str = "neutral"
    emotion_attributes: Optional[Dict[str, float]] = None
    language_code: str = "en"


@router.post("/generate")
async def generate_speech(request: TTSRequest):
    """
    Generate speech from text with emotion preservation.
    
    Args:
        request: TTS request with text, emotion, and attributes
    
    Returns:
        Audio file (MP3)
    """
    try:
        audio_data = await text_to_speech_service.generate_audio(
            text=request.text,
            emotion=request.emotion,
            emotion_attributes=request.emotion_attributes,
            language_code=request.language_code,
        )
        
        return Response(
            content=audio_data,
            media_type="audio/mpeg",
            headers={
                "Content-Disposition": "attachment; filename=speech.mp3"
            }
        )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/voices")
async def get_voices():
    """
    Get available voices from ElevenLabs.
    
    Returns:
        List of available voices
    """
    try:
        voices = await text_to_speech_service.get_available_voices()
        return {"voices": voices}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


