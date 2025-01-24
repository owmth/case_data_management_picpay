📌 Aplicacao CRUD com FastAPI e SQLite

🚀 Sobre o Projeto

Este projeto é uma API CRUD para gerenciamento de usuários, desenvolvida utilizando FastAPI, SQLite e SQLAlchemy. A aplicação é containerizada com Docker e possui testes automatizados com Pytest.

📂 Estrutura do Projeto

├── src/
│   ├── main.py            # Inicializa a API FastAPI
│   ├── models/            # Modelos de banco de dados
│   ├── schemas/           # Schemas Pydantic para validacao
│   ├── services/          # Logica de negocio (CRUD)
│   ├── routes/            # Endpoints da API
│   ├── database/          # Configuração do banco SQLite
├── tests/                 # Testes automatizados
├── Dockerfile             # Configuração para rodar no Docker
├── docker-compose.yml     # Configuração do ambiente
├── requirements.txt       # Dependencias do projeto

🛠 Tecnologias Utilizadas

FastAPI: Framework web assíncrono otimizado para APIs

SQLite: Banco de dados leve e embutido

SQLAlchemy: ORM para manipulação do banco

Pydantic: Validação de dados

Pytest: Testes automatizados

Docker: Contêinerização da aplicação

📌 Endpoints da API

Método

Endpoint

Descrição

POST

/users/

Cria um novo usuário

GET

/users/

Lista todos os usuários

GET

/users/{id}

Retorna um usuário pelo ID

PUT

/users/{id}

Atualiza um usuário

DELETE

/users/{id}

Remove um usuário

🔧 Configuração e Execução

1️⃣ Clonar o Repositório

git clone https://github.com/seuusuario/seurepositorio.git
cd seurepositorio

2️⃣ Criar e Ativar um Ambiente Virtual (Opcional)

python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

3️⃣ Instalar Dependências

pip install -r requirements.txt

4️⃣ Executar a Aplicação

uvicorn src.main:app --reload

Acesse a documentação interativa no Swagger UI: http://127.0.0.1:8000/docs

🐳 Executando com Docker

1️⃣ Construir e Subir o Container

docker-compose up --build

2️⃣ Acessar a API

http://localhost:8000/docs

3️⃣ Rodar os Testes dentro do Container

docker-compose exec app pytest tests/

✅ Testes Automatizados

Os testes garantem a qualidade da API e validam os endpoints.

🔹 Executar os Testes Manualmente

pytest tests/

🎯 Conclusão

Esta API CRUD é uma solução eficiente para o gerenciamento de usuários, utilizando tecnologias modernas e melhores práticas de desenvolvimento.

Se tiver dúvidas ou sugestões, sinta-se à vontade para contribuir! 🚀
