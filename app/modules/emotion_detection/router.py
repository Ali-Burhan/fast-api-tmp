"""
Router for emotion detection endpoints.
"""
from fastapi import APIRouter, UploadFile, File, HTTPException
from pydantic import BaseModel
from typing import Dict
from app.modules.emotion_detection.service import emotion_detection_service
from app.core.utils import validate_audio_file

router = APIRouter(prefix="/emotion", tags=["Emotion Detection"])


class EmotionResponse(BaseModel):
    """Response model for emotion detection."""
    emotion: str
    attributes: Dict[str, float]


@router.post("/detect", response_model=EmotionResponse)
async def detect_emotion(audio: UploadFile = File(...)):
    """
    Detect emotion from audio file.
    
    Args:
        audio: Audio file (mp3, wav, m4a, flac, ogg, webm)
    
    Returns:
        Detected emotion and acoustic attributes
    """
    try:
        # Validate audio file
        validate_audio_file(audio)
        
        # Read audio data
        audio_data = await audio.read()
        
        # Detect emotion
        result = await emotion_detection_service.detect_emotion(
            audio_data,
            filename=audio.filename
        )
        
        return result
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


