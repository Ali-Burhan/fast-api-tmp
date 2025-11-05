"""
Redis client for caching audio files and intermediate results.
"""
import redis.asyncio as redis
from typing import Optional
import logging
from app.core.config import settings

logger = logging.getLogger(__name__)


class RedisClient:
    """Async Redis client wrapper for caching operations."""
    
    def __init__(self):
        self.redis: Optional[redis.Redis] = None
    
    async def connect(self):
        """Establish connection to Redis server."""
        try:
            self.redis = redis.Redis(
                host=settings.REDIS_HOST,
                port=settings.REDIS_PORT,
                db=settings.REDIS_DB,
                password=settings.REDIS_PASSWORD,
                decode_responses=False,  # Keep binary for audio files
            )
            await self.redis.ping()
            logger.info("Successfully connected to Redis")
        except Exception as e:
            logger.error(f"Failed to connect to Redis: {e}")
            raise
    
    async def disconnect(self):
        """Close Redis connection."""
        if self.redis:
            await self.redis.close()
            logger.info("Redis connection closed")
    
    async def set_audio(self, key: str, audio_data: bytes, ttl: int = None) -> bool:
        """
        Store audio data in Redis.
        
        Args:
            key: Cache key
            audio_data: Binary audio data
            ttl: Time to live in seconds (default from settings)
        
        Returns:
            True if successful
        """
        try:
            ttl = ttl or settings.REDIS_CACHE_TTL
            await self.redis.setex(key, ttl, audio_data)
            logger.debug(f"Cached audio with key: {key}")
            return True
        except Exception as e:
            logger.error(f"Failed to cache audio: {e}")
            return False
    
    async def get_audio(self, key: str) -> Optional[bytes]:
        """
        Retrieve audio data from Redis.
        
        Args:
            key: Cache key
        
        Returns:
            Binary audio data or None
        """
        try:
            data = await self.redis.get(key)
            if data:
                logger.debug(f"Retrieved audio with key: {key}")
            return data
        except Exception as e:
            logger.error(f"Failed to retrieve audio: {e}")
            return None
    
    async def delete_audio(self, key: str) -> bool:
        """
        Delete audio data from Redis.
        
        Args:
            key: Cache key
        
        Returns:
            True if successful
        """
        try:
            await self.redis.delete(key)
            logger.debug(f"Deleted audio with key: {key}")
            return True
        except Exception as e:
            logger.error(f"Failed to delete audio: {e}")
            return False
    
    async def exists(self, key: str) -> bool:
        """Check if key exists in Redis."""
        try:
            return bool(await self.redis.exists(key))
        except Exception as e:
            logger.error(f"Failed to check key existence: {e}")
            return False


# Global Redis client instance
redis_client = RedisClient()


