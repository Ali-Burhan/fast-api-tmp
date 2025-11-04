"""CRUD operations for Item model."""
from typing import Optional, List
from sqlalchemy.orm import Session

from app.models import Item
from app.schemas import ItemCreate, ItemUpdate


def get_item(db: Session, item_id: int) -> Optional[Item]:
    """
    Get item by ID.
    
    Args:
        db: Database session
        item_id: Item ID
        
    Returns:
        Item or None
    """
    return db.query(Item).filter(Item.id == item_id).first()


def get_items(db: Session, skip: int = 0, limit: int = 100) -> List[Item]:
    """
    Get list of items.
    
    Args:
        db: Database session
        skip: Number of records to skip
        limit: Maximum number of records to return
        
    Returns:
        List of items
    """
    return db.query(Item).offset(skip).limit(limit).all()


def create_item(db: Session, item: ItemCreate) -> Item:
    """
    Create a new item.
    
    Args:
        db: Database session
        item: Item data
        
    Returns:
        Created item
    """
    db_item = Item(**item.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def update_item(db: Session, item_id: int, item: ItemUpdate) -> Optional[Item]:
    """
    Update an item.
    
    Args:
        db: Database session
        item_id: Item ID
        item: Updated item data
        
    Returns:
        Updated item or None
    """
    db_item = get_item(db, item_id)
    if not db_item:
        return None
    
    update_data = item.model_dump(exclude_unset=True)
    
    for field, value in update_data.items():
        setattr(db_item, field, value)
    
    db.commit()
    db.refresh(db_item)
    return db_item


def delete_item(db: Session, item_id: int) -> bool:
    """
    Delete an item.
    
    Args:
        db: Database session
        item_id: Item ID
        
    Returns:
        True if deleted, False otherwise
    """
    db_item = get_item(db, item_id)
    if not db_item:
        return False
    
    db.delete(db_item)
    db.commit()
    return True
