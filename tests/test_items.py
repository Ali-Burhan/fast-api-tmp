"""Test item endpoints."""
from fastapi.testclient import TestClient


def test_create_item(client: TestClient):
    """Test creating an item."""
    # Create a user first
    user_response = client.post(
        "/api/v1/users/",
        json={
            "email": "itemowner@example.com",
            "username": "itemowner",
            "password": "password123",
            "is_active": True,
            "is_superuser": False
        }
    )
    user_id = user_response.json()["id"]
    
    # Create item
    response = client.post(
        "/api/v1/items/",
        json={
            "title": "Test Item",
            "description": "Test Description",
            "owner_id": user_id,
            "is_active": True
        }
    )
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Test Item"
    assert data["owner_id"] == user_id
    assert "id" in data


def test_read_items(client: TestClient):
    """Test reading items."""
    # Create a user and item first
    user_response = client.post(
        "/api/v1/users/",
        json={
            "email": "listowner@example.com",
            "username": "listowner",
            "password": "password123",
            "is_active": True,
            "is_superuser": False
        }
    )
    user_id = user_response.json()["id"]
    
    client.post(
        "/api/v1/items/",
        json={
            "title": "List Item",
            "description": "Description",
            "owner_id": user_id,
            "is_active": True
        }
    )
    
    response = client.get("/api/v1/items/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0


def test_read_item(client: TestClient):
    """Test reading a specific item."""
    # Create a user and item first
    user_response = client.post(
        "/api/v1/users/",
        json={
            "email": "specificitem@example.com",
            "username": "specificitem",
            "password": "password123",
            "is_active": True,
            "is_superuser": False
        }
    )
    user_id = user_response.json()["id"]
    
    item_response = client.post(
        "/api/v1/items/",
        json={
            "title": "Specific Item",
            "description": "Description",
            "owner_id": user_id,
            "is_active": True
        }
    )
    item_id = item_response.json()["id"]
    
    response = client.get(f"/api/v1/items/{item_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == item_id
    assert data["title"] == "Specific Item"


def test_read_nonexistent_item(client: TestClient):
    """Test reading a nonexistent item."""
    response = client.get("/api/v1/items/999")
    assert response.status_code == 404
