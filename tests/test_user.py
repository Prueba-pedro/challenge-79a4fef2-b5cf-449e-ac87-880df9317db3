from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_user():
    response = client.post("/users/", json={"username": "testuser", "password": "testpassword"})
    assert response.status_code == 200
    assert response.json() == {"id": 1, "username": "testuser"}

def test_get_user():
    response = client.get("/users/testuser")
    assert response.status_code == 200
    assert response.json() == {"id": 1, "username": "testuser"}

def test_get_users():
    response = client.get("/users/")
    assert response.status_code == 200
    assert response.json() == [{"id": 1, "username": "testuser"}]