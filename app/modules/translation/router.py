"""
Router for translation endpoints.
"""
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.modules.translation.service import translation_service

router = APIRouter(prefix="/translation", tags=["Translation"])


class TranslationRequest(BaseModel):
    """Request model for translation."""
    text: str
    source_lang: str
    target_lang: str = None


class TranslationResponse(BaseModel):
    """Response model for translation."""
    translated_text: str
    source_language: str
    target_language: str


@router.post("/translate", response_model=TranslationResponse)
async def translate(request: TranslationRequest):
    """
    Translate text between languages.
    
    Args:
        request: Translation request with text and languages
    
    Returns:
        Translated text with language info
    """
    try:
        result = await translation_service.translate_text(
            text=request.text,
            source_lang=request.source_lang,
            target_lang=request.target_lang,
        )
        
        return result
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


