from fastapi import FastAPI
from routers.users import router
from config.settings import settings

app = FastAPI(title=settings.APP_NAME)

# Registrar as rotas
app.include_router(router)

@app.get("/")
def root():
    return {"message": "API funcionando! Acesse /docs para ver os endpoints"}
