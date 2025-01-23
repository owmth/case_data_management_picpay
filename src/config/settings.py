from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "Minha API FastAPI"
    DATABASE_URL: str = "sqlite:///./users.db"

settings = Settings()
