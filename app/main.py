from fastapi import FastAPI
from . import models, database
from .routes import router

app = FastAPI()

# Criar tabelas no banco de dados
models.Base.metadata.create_all(bind=database.engine)

# Incluir as rotas
app.include_router(router)
