from fastapi.testclient import TestClient
from app import Application


client = TestClient(Application().app)


def test_init_user():
    response = client.post("/init_user", json={"username": "testuser", "role": "experto"})
    assert response.status_code == 200
    assert "Name" in response.json()
    
def test_ask_chatbot():
    response = client.post("/ask", json={"username": "testuser", "message": "¿Qué es un riesgo laboral?"})
    assert response.status_code == 200
    assert "response" in response.json()