# Usa a imagem oficial do Python 3.9
FROM python:3.9

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia os arquivos do projeto para dentro do container
COPY . /app

# Instala as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Define o comando para rodar o FastAPI com Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]