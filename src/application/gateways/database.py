from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from application.models.base import Base
from config.settings import settings

DATABASE_URL = settings.DATABASE_URL
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    print("Criando as tabelas do banco de dados...")
    Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()