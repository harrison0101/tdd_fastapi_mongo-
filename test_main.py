import pytest
from fastapi.testclient import TestClient
from main import app
from database import usuarios_collection

client = TestClient(app)

# Limpa a coleção antes de cada teste
@pytest.fixture(autouse=True)
def run_around_tests():
    usuarios_collection.delete_many({})
    yield

def test_criar_usuario():
    response = client.post("/usuarios", json={"nome": "Harrison", "email": "harrison@email.com"})
    assert response.status_code == 200
    assert response.json()["nome"] == "Harrison"

def test_listar_usuarios():
    # Adiciona um usuário
    client.post("/usuarios", json={"nome": "Harrison", "email": "harrison@email.com"})
    response = client.get("/usuarios")
    assert response.status_code == 200
    assert len(response.json()) == 1
