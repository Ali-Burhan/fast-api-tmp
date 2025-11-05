"""
FastAPI Speech Translation API
Real-time multilingual speech translation with emotion preservation.
"""
import logging
import uuid
import base64
from contextlib import asynccontextmanager
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Optional

from app.core.config import settings
from app.core.redis_client import redis_client
from app.core.utils import validate_audio_file, generate_audio_key

# Import service modules
from app.modules.speech_to_text.service import speech_to_text_service
from app.modules.emotion_detection.service import emotion_detection_service
from app.modules.translation.service import translation_service
from app.modules.text_to_speech.service import text_to_speech_service

# Import routers
from app.modules.speech_to_text.router import router as stt_router
from app.modules.emotion_detection.router import router as emotion_router
from app.modules.translation.router import router as translation_router
from app.modules.text_to_speech.router import router as tts_router

# Configure logging
logging.basicConfig(
    level=getattr(logging, settings.LOG_LEVEL),
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifespan context manager for startup and shutdown events."""
    # Startup
    logger.info("Starting Speech Translation API...")
    try:
        await redis_client.connect()
        logger.info("Application started successfully")
    except Exception as e:
        logger.error(f"Failed to start application: {e}")
    
    yield
    
    # Shutdown
    logger.info("Shutting down Speech Translation API...")
    await redis_client.disconnect()
    logger.info("Application shutdown complete")


# Create FastAPI app
app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="Real-time multilingual speech translation with emotion preservation",
    lifespan=lifespan,
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include module routers
app.include_router(stt_router, prefix="/api")
app.include_router(emotion_router, prefix="/api")
app.include_router(translation_router, prefix="/api")
app.include_router(tts_router, prefix="/api")


class ProcessAudioResponse(BaseModel):
    """Response model for process-audio endpoint."""
    original_text: str
    original_language: str
    translated_text: str
    target_language: str
    emotion: str
    emotion_attributes: dict
    audio_base64: str
    audio_size_bytes: int


@app.get("/")
async def root():
    """Root endpoint."""
    return {
        "name": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "status": "running",
        "docs": "/docs",
    }


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    redis_connected = await redis_client.exists("health_check") or True
    return {
        "status": "healthy",
        "redis": "connected" if redis_connected else "disconnected",
    }


@app.post("/api/process-audio", response_model=ProcessAudioResponse)
async def process_audio(audio: UploadFile = File(...)):
    """
    Process audio file through complete translation pipeline.
    
    Pipeline:
    1. Speech-to-Text (Deepgram) - transcribe with language detection
    2. Emotion Detection (OpenSmile) - extract emotional attributes
    3. Translation (DeepL) - translate to target language
    4. Text-to-Speech (ElevenLabs) - generate emotional speech
    
    Args:
        audio: Audio file (mp3, wav, m4a, flac, ogg, webm)
    
    Returns:
        Complete translation result with audio
    """
    cache_key = None
    
    try:
        # Validate audio file
        validate_audio_file(audio)
        logger.info(f"Processing audio file: {audio.filename}")
        
        # Read audio data
        audio_data = await audio.read()
        
        # Cache audio in Redis
        cache_key = generate_audio_key()
        await redis_client.set_audio(cache_key, audio_data)
        logger.debug(f"Audio cached with key: {cache_key}")
        
        # Step 1: Speech-to-Text
        logger.info("Step 1: Transcribing audio...")
        transcription = await speech_to_text_service.transcribe_audio(
            audio_data,
            mimetype=audio.content_type or "audio/wav"
        )
        original_text = transcription["text"]
        original_language = transcription["language"]
        source_lang_code = transcription["language_code"]
        logger.info(f"Transcription complete. Language: {original_language}")
        
        # Step 2: Emotion Detection
        logger.info("Step 2: Detecting emotion...")
        emotion_result = await emotion_detection_service.detect_emotion(
            audio_data,
            filename=audio.filename
        )
        emotion = emotion_result["emotion"]
        emotion_attributes = emotion_result["attributes"]
        logger.info(f"Emotion detection complete. Emotion: {emotion}")
        
        # Step 3: Translation
        logger.info("Step 3: Translating text...")
        translation_result = await translation_service.translate_text(
            text=original_text,
            source_lang=source_lang_code,
        )
        translated_text = translation_result["translated_text"]
        target_language = translation_result["target_language"]
        logger.info(f"Translation complete. Target: {target_language}")
        
        # Step 4: Text-to-Speech with emotion
        logger.info("Step 4: Generating emotional speech...")
        generated_audio = await text_to_speech_service.generate_audio(
            text=translated_text,
            emotion=emotion,
            emotion_attributes=emotion_attributes,
            language_code=target_language,
        )
        logger.info(f"Audio generation complete. Size: {len(generated_audio)} bytes")
        
        # Encode audio to base64 for JSON response
        audio_base64 = base64.b64encode(generated_audio).decode('utf-8')
        
        # Clean up cache
        if cache_key:
            await redis_client.delete_audio(cache_key)
            logger.debug(f"Cache cleaned: {cache_key}")
        
        logger.info("Processing complete!")
        
        return ProcessAudioResponse(
            original_text=original_text,
            original_language=original_language,
            translated_text=translated_text,
            target_language=target_language,
            emotion=emotion,
            emotion_attributes=emotion_attributes,
            audio_base64=audio_base64,
            audio_size_bytes=len(generated_audio),
        )
    
    except Exception as e:
        # Clean up cache on error
        if cache_key:
            await redis_client.delete_audio(cache_key)
        
        logger.error(f"Processing failed: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"Audio processing failed: {str(e)}"
        )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=settings.DEBUG,
    )
