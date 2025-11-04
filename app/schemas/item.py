"""Item Pydantic schemas."""
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, ConfigDict


class ItemBase(BaseModel):
    """Base item schema."""
    title: str
    description: Optional[str] = None
    is_active: bool = True


class ItemCreate(ItemBase):
    """Schema for creating an item."""
    owner_id: int


class ItemUpdate(BaseModel):
    """Schema for updating an item."""
    title: Optional[str] = None
    description: Optional[str] = None
    is_active: Optional[bool] = None


class ItemInDB(ItemBase):
    """Schema for item in database."""
    id: int
    owner_id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    model_config = ConfigDict(from_attributes=True)


class Item(ItemBase):
    """Schema for item response."""
    id: int
    owner_id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    model_config = ConfigDict(from_attributes=True)
