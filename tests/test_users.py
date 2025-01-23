from fastapi.testclient import TestClient
from application.main import app
from gateways.database import get_db, SessionLocal
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine # type: ignore
from models.base import Base

# Configuração do banco de testes
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

def test_create_user():
    response = client.post("/users/", json={"name": "John Doe", "email": "john@example.com"})
    assert response.status_code == 200
    assert response.json()["name"] == "John Doe"

def test_get_non_existing_user():
    response = client.get("/users/9999")
    assert response.status_code == 404

def test_update_user():
    response = client.post("/users/", json={"name": "Jane Doe", "email": "jane@example.com"})
    user_id = response.json()["id"]
    
    update_response = client.put(f"/users/{user_id}", json={"name": "Jane Doe Updated", "email": "jane_updated@example.com"})
    assert update_response.status_code == 200
    assert update_response.json()["name"] == "Jane Doe Updated"

def test_delete_user():
    response = client.post("/users/", json={"name": "Test User", "email": "test@example.com"})
    user_id = response.json()["id"]
    
    delete_response = client.delete(f"/users/{user_id}")
    assert delete_response.status_code == 200
    assert delete_response.json()["message"] == "Usuário deletado com sucesso"
