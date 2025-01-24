from fastapi import FastAPI
from application.routers.users import router
from application.gateways.database import init_db

app = FastAPI(title="Minha API FastAPI")

# ✅ Criar as tabelas do banco ao iniciar a API
@app.on_event("startup")
def startup():
    init_db()

# Registrar as rotas
app.include_router(router)

@app.get("/")
def root():
    return {"message": "API funcionando! Acesse /docs para ver os endpoints"}
