import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_index_route():
    response = client.get('/items/1')
    assert response.status_code == 200

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    #assert response.json() == {"items": "Hello World"}
