
import pytest

import sys
import os

# Adiciona `src/` ao caminho do Python automaticamente
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from main import app  # Import correto, pois main.py está dentro de src/
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from main import app
from application.gateways.database import get_db, Base
from application.models.user import User
from application.gateways.database import SessionLocal

client = TestClient(app)

def test_create_user():
    response = client.post(
        "/users/", json={"name": "John Doe", "email": "john@example.com"}
    )
    print(response.json())  # Debug para garantir que a resposta está correta
    assert response.status_code == 200
    assert response.json()["name"] == "John Doe"
    assert response.json()["email"] == "john@example.com"

# ✅ Teste para obter todos os usuários
def test_list_users():
    response = client.get("/users/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


# ✅ Teste para obter um usuário por ID
def test_read_user():
    # Criar um usuário primeiro
    create_response = client.post(
        "/users/", json={"name": "Jane Doe", "email": "jane@example.com"}
    )
    user_id = create_response.json()["id"]

    # Buscar o usuário recém-criado
    response = client.get(f"/users/{user_id}")
    assert response.status_code == 200
    assert response.json()["name"] == "Jane Doe"
    assert response.json()["email"] == "jane@example.com"


# ✅ Teste para atualizar um usuário
def test_update_user():
    # Criar um usuário primeiro
    create_response = client.post(
        "/users/", json={"name": "User1", "email": "user1@example.com"}
    )
    user_id = create_response.json()["id"]

    # Atualizar o usuário
    update_response = client.put(
        f"/users/{user_id}",
        json={"name": "User1 Updated", "email": "user1_updated@example.com"},
    )

    assert update_response.status_code == 200
    assert update_response.json()["name"] == "User1 Updated"
    assert update_response.json()["email"] == "user1_updated@example.com"


# ✅ Teste para deletar um usuário
def test_delete_user():
    # Criar um usuário primeiro
    create_response = client.post(
        "/users/", json={"name": "UserToDelete", "email": "delete@example.com"}
    )
    user_id = create_response.json()["id"]

    # Deletar o usuário
    delete_response = client.delete(f"/users/{user_id}")
    assert delete_response.status_code == 200
    assert delete_response.json()["message"] == "Usuário deletado com sucesso"

    # Tentar buscar o usuário deletado
    response = client.get(f"/users/{user_id}")
    assert response.status_code == 404


# ✅ Teste para erro ao buscar um usuário inexistente
def test_get_non_existing_user():
    response = client.get("/users/9999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Usuário não encontrado"


# ✅ Teste para erro ao atualizar um usuário inexistente
def test_update_non_existing_user():
    response = client.put(
        "/users/9999", json={"name": "Not Found", "email": "notfound@example.com"}
    )
    assert response.status_code == 404
    assert response.json()["detail"] == "Usuário não encontrado"


# ✅ Teste para erro ao deletar um usuário inexistente
def test_delete_non_existing_user():
    response = client.delete("/users/9999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Usuário não encontrado"
