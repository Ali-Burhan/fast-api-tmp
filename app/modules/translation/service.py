"""
Translation service using DeepL API.
Translates text between English and Spanish.
"""
import logging
import httpx
from typing import Dict
from app.core.config import settings

logger = logging.getLogger(__name__)


class TranslationService:
    """Service for translating text using DeepL API."""
    
    def __init__(self):
        self.api_key = settings.DEEPL_API_KEY
        self.base_url = "https://api-free.deepl.com/v2/translate"  # Use api.deepl.com for paid plans
    
    async def translate_text(
        self, 
        text: str, 
        source_lang: str, 
        target_lang: str = None
    ) -> Dict[str, str]:
        """
        Translate text from source language to target language.
        
        Args:
            text: Text to translate
            source_lang: Source language code (en, es)
            target_lang: Target language code (if None, auto-detect opposite)
        
        Returns:
            Dictionary with 'translated_text' and 'target_language' keys
        
        Raises:
            Exception: If translation fails
        """
        try:
            # Auto-determine target language
            if target_lang is None:
                target_lang = self._get_target_language(source_lang)
            
            # Normalize language codes for DeepL
            source_lang_code = self._normalize_language_code(source_lang)
            target_lang_code = self._normalize_language_code(target_lang)
            
            headers = {
                "Authorization": f"DeepL-Auth-Key {self.api_key}",
                "Content-Type": "application/x-www-form-urlencoded",
            }
            
            data = {
                "text": text,
                "source_lang": source_lang_code,
                "target_lang": target_lang_code,
            }
            
            async with httpx.AsyncClient(timeout=30.0) as client:
                response = await client.post(
                    self.base_url,
                    headers=headers,
                    data=data,
                )
                response.raise_for_status()
                result = response.json()
            
            # Extract translation
            translations = result.get("translations", [])
            if not translations:
                raise Exception("No translation returned from DeepL")
            
            translated_text = translations[0].get("text", "")
            detected_source = translations[0].get("detected_source_language", source_lang_code)
            
            logger.info(f"Translation successful: {source_lang_code} -> {target_lang_code}")
            logger.debug(f"Translated text: {translated_text[:100]}...")
            
            return {
                "translated_text": translated_text,
                "source_language": detected_source.lower(),
                "target_language": target_lang_code.lower(),
            }
        
        except httpx.HTTPStatusError as e:
            logger.error(f"DeepL API error: {e.response.status_code} - {e.response.text}")
            raise Exception(f"Translation failed: {e.response.text}")
        except Exception as e:
            logger.error(f"Translation error: {str(e)}")
            raise
    
    def _get_target_language(self, source_lang: str) -> str:
        """
        Get target language based on source language.
        
        Args:
            source_lang: Source language code
        
        Returns:
            Target language code
        """
        lang_map = {
            "en": "es",
            "es": "en",
        }
        return lang_map.get(source_lang.lower()[:2], "en")
    
    def _normalize_language_code(self, lang_code: str) -> str:
        """
        Normalize language code for DeepL API.
        
        Args:
            lang_code: Language code
        
        Returns:
            Normalized language code (uppercase)
        """
        # DeepL uses uppercase codes
        code = lang_code.upper()[:2]
        
        # Map to DeepL supported codes
        if code == "EN":
            return "EN-US"  # or EN-GB
        
        return code


# Global service instance
translation_service = TranslationService()


