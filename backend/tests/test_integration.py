import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_load_films():
    response = client.post("/load_films")
    assert response.status_code == 200
    assert response.json() == {"message": "Films loaded successfully"}

def test_get_films():
    response = client.get("/films")
    assert response.status_code == 200
    assert "films" in response.json()