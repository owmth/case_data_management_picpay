# Usa a imagem oficial do Python 3.9
FROM python:3.9

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Adiciona o diretório src ao PYTHONPATH
ENV PYTHONPATH=/app

# Copia os arquivos do projeto para dentro do container
COPY ./src /app
COPY ./requirements /app/requirements

# Instala as dependências
RUN pip install --no-cache-dir -r /app/requirements/base.txt

# Define o comando para rodar o FastAPI com Uvicorn
CMD ["uvicorn", "application.main:app", "--host", "0.0.0.0", "--port", "8000"]
