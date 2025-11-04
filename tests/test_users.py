"""Test user endpoints."""
from fastapi.testclient import TestClient


def test_create_user(client: TestClient):
    """Test creating a user."""
    response = client.post(
        "/api/v1/users/",
        json={
            "email": "test@example.com",
            "username": "testuser",
            "full_name": "Test User",
            "password": "testpassword123",
            "is_active": True,
            "is_superuser": False
        }
    )
    assert response.status_code == 201
    data = response.json()
    assert data["email"] == "test@example.com"
    assert data["username"] == "testuser"
    assert "id" in data


def test_create_duplicate_user(client: TestClient):
    """Test creating a user with duplicate email."""
    # Create first user
    client.post(
        "/api/v1/users/",
        json={
            "email": "duplicate@example.com",
            "username": "user1",
            "password": "password123",
            "is_active": True,
            "is_superuser": False
        }
    )
    
    # Try to create duplicate
    response = client.post(
        "/api/v1/users/",
        json={
            "email": "duplicate@example.com",
            "username": "user2",
            "password": "password123",
            "is_active": True,
            "is_superuser": False
        }
    )
    assert response.status_code == 400


def test_read_users(client: TestClient):
    """Test reading users."""
    # Create a user first
    client.post(
        "/api/v1/users/",
        json={
            "email": "read@example.com",
            "username": "readuser",
            "password": "password123",
            "is_active": True,
            "is_superuser": False
        }
    )
    
    response = client.get("/api/v1/users/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0


def test_read_user(client: TestClient):
    """Test reading a specific user."""
    # Create a user first
    create_response = client.post(
        "/api/v1/users/",
        json={
            "email": "specific@example.com",
            "username": "specificuser",
            "password": "password123",
            "is_active": True,
            "is_superuser": False
        }
    )
    user_id = create_response.json()["id"]
    
    response = client.get(f"/api/v1/users/{user_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == user_id
    assert data["email"] == "specific@example.com"


def test_read_nonexistent_user(client: TestClient):
    """Test reading a nonexistent user."""
    response = client.get("/api/v1/users/999")
    assert response.status_code == 404
