# 📌 Aplicacao CRUD com FastAPI e SQLite

## 🚀 Sobre o Projeto
Este projeto é uma API CRUD para gerenciamento de usuários, desenvolvida utilizando **FastAPI**, **SQLite** e **SQLAlchemy**. A aplicação é **containerizada com Docker** e possui **testes automatizados com Pytest**.

## 📂 Estrutura do Projeto
```
├── src/
│   ├── application/
│   │   ├── gateways/       # Configuração de conexão com o banco
│   │   ├── models/         # Modelos do banco de dados (SQLAlchemy)
│   │   ├── routers/        # Rotas/endpoints da API
│   │   ├── schemas/        # Schemas Pydantic para validação
│   │   ├── services/       # Lógica de negócio (CRUD)
│   │   ├── config/         # Configurações gerais
│   │   ├── __init__.py
│   ├── main.py             # Inicializa a API FastAPI
│   ├── users.db            # Banco de dados SQLite
├── tests/                  # Testes automatizados
│   ├── test_users.py       # Testes dos endpoints de usuários
│   ├── conftest.py         # Configuração de testes
├── requirements/           # Diretório para requisitos específicos
│   ├── base.txt            # Dependências essenciais do projeto
│   ├── dev.txt             # Dependências para desenvolvimento
├── .gitignore              # Arquivos ignorados pelo Git
├── pytest.ini              # Configuração do pytest
├── Dockerfile              # Configuração para rodar no Docker
├── docker-compose.yml      # Configuração do ambiente Docker
├── README.md               # Documentação do projeto
```

## 🛠 Tecnologias Utilizadas
- **FastAPI**: Framework web assíncrono otimizado para APIs
- **SQLite**: Banco de dados leve e embutido
- **SQLAlchemy**: ORM para manipulação do banco
- **Pydantic**: Validação de dados
- **Pytest**: Testes automatizados
- **Docker**: Contêinerização da aplicação

## 📌 Endpoints da API
| Método | Endpoint          | Descrição |
|--------|------------------|------------|
| `POST` | `/users/`        | Cria um novo usuário |
| `GET`  | `/users/`        | Lista todos os usuários |
| `GET`  | `/users/{id}`    | Retorna um usuário pelo ID |
| `PUT`  | `/users/{id}`    | Atualiza um usuário |
| `DELETE` | `/users/{id}`  | Remove um usuário |

## 🐳 Executando a Aplicação com Docker
### 1️⃣ Clonar o Repositório
```sh
git clone https://github.com/owmth/case_data_management_picpay
cd case_data_management_picpay
```

### 2️⃣ Construir e Subir o Container
```sh
docker-compose up --build
```

### 3️⃣ Acessar a API
A API estará disponível no navegador em:
```sh
http://localhost:8000/docs
```

### 4️⃣ Rodar os Testes dentro do Container
```sh
docker-compose exec app pytest tests/
```

## 🎯 Conclusão
Esta API CRUD é uma solução eficiente para o gerenciamento de usuários, utilizando tecnologias modernas e **melhores práticas de desenvolvimento**.

Se tiver dúvidas ou sugestões, sinta-se à vontade para contribuir! 🚀

