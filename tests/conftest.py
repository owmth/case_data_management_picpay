import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from application.models.base import Base
from application.gateways.database import get_db
from main import app

# ✅ Criando um banco de testes separado (SQLite em memória)
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# ✅ Criar o banco antes de rodar os testes
@pytest.fixture(scope="function", autouse=True)
def setup_test_database():
    Base.metadata.drop_all(bind=engine)  # 🔥 Limpa todas as tabelas antes de cada teste
    Base.metadata.create_all(bind=engine)  # 🔥 Recria as tabelas
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

# ✅ Substituir a dependência do banco na API pelos testes
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db
