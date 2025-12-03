# Descrição da Solução

A solução consiste em uma aplicação web com integração a banco de dados e cache:

- **Web**: desenvolvida com Flask
- **Database**: PostgreSQL 15
- **Cache**: Redis 7

A aplicação web é responsável por executar uma API com rotas que testam a conexão com o banco de dados e gerenciam dados no cache. Todos os serviços são orquestrados utilizando Docker Compose.

## Estrutura do Projeto

```bash
desafio3
│-- README.md
│-- docker-compose.yml
│-- web
│ │-- app.py
│ │-- Dockerfile
│ │-- requirements.txt
```

# Explicação do Funcionamento

## Web (Flask)

- Implementado com Flask
- Utiliza `psycopg2` para conexão com PostgreSQL
- Utiliza `redis` para gerenciamento de cache
- Possui as seguintes rotas:
  - **GET /db**: testa a conexão com o banco de dados PostgreSQL
  - **GET /cache/set**: armazena um valor no Redis
  - **GET /cache/get**: recupera um valor do Redis

## Database (PostgreSQL)

- PostgreSQL versão 15
- Banco de dados: `appdb`
- Usuário: `admin`
- Dados persistidos em um volume Docker

## Cache (Redis)

- Redis versão 7
- Utilizado para armazenamento em cache
- Integrado com a aplicação Flask

# Instruções de Execução

```bash
# Acessar a pasta
cd desafio3

# Iniciar os containers com Docker Compose
docker-compose up -d

# Verificar o status dos containers
docker-compose ps

# Testar as rotas da aplicação
# Testar conexão com banco de dados
curl http://localhost:8000/db

# Testar set no cache
curl http://localhost:8000/cache/set

# Testar get no cache
curl http://localhost:8000/cache/get

# Ver logs dos containers
docker-compose logs -f web
docker-compose logs -f db
docker-compose logs -f cache

# Parar os containers
docker-compose down

# Parar e remover volumes
docker-compose down -v
```