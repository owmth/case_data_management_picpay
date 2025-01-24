# Usa a imagem oficial do Python 3.9
FROM python:3.9

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Define o PYTHONPATH para que a aplicação encontre os módulos corretamente
ENV PYTHONPATH=/app/src

# Copia os arquivos da aplicação
COPY ./src /app/src
COPY ./tests /app/tests
COPY ./requirements /app/requirements

# Instala as dependências
RUN pip install --no-cache-dir -r /app/requirements/base.txt
RUN pip install --no-cache-dir -r /app/requirements/dev.txt

# Define o comando para rodar o FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
