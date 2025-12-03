## Descrição da Solução

A solução implementa dois microsserviços independentes que se comunicam via HTTP:

- **Serviço A (FastAPI)**: microsserviço que fornece uma API retornando uma lista de usuários em JSON
- **Serviço B (Flask)**: microsserviço que consome dados do Serviço A e exibe informações combinadas e formatadas

Os serviços são orquestrados utilizando Docker Compose e se comunicam através de requisições HTTP em uma rede Docker.

## Estrutura do Projeto

```bash
desafio4
│-- README.md
│-- docker-compose.yml
│-- service_a
│ │-- app.py
│ │-- Dockerfile
│ │-- requirements.txt
│-- service_b
│ │-- app.py
│ │-- Dockerfile
│ │-- requirements.txt
```

## Explicação do Funcionamento

### Serviço A (FastAPI)

Microsserviço responsável por fornecer dados de usuários:

- **Tecnologia**: FastAPI
- **Porta**: 8001
- **Endpoints**:
  - `GET /usuarios`: retorna lista completa de usuários
  - `GET /usuarios/{usuario_id}`: retorna dados de um usuário específico

### Serviço B (Flask)

Microsserviço consumidor que processa e exibe dados do Serviço A:

- **Tecnologia**: Flask
- **Porta**: 8002
- **Endpoints**:
  - `GET /usuarios-combinado`: retorna lista de usuários com informações combinadas (dias desde início, status formatado)
  - `GET /usuarios-detalhado/<usuario_id>`: retorna dados detalhados de um usuário específico
  - `GET /health`: verifica a saúde do serviço

### Comunicação entre Serviços

- O Serviço B realiza requisições para o Serviço A pelo endereço `http://service_a:8001`
- A comunicação acontece dentro de uma rede Docker chamada `desafio4_rede`
- O Serviço B aguarda o Serviço A estar pronto via `depends_on`

## Instruções de Execução

```bash
# Acessar a pasta
cd desafio4

# Iniciar os serviços
docker-compose up -d

# Verificar o status dos containers
docker-compose ps

# Ver logs dos serviços
docker-compose logs -f service_a
docker-compose logs -f service_b

# Testar os endpoints
curl http://localhost:8001/usuarios
curl http://localhost:8002/usuarios-combinado
curl http://localhost:8002/usuarios-detalhado/1

# Parar os serviços
docker-compose down
```

### Testando os Endpoints

**Listar todos os usuários (Serviço A)**:
```bash
curl http://localhost:8001/usuarios
```

**Obter usuário específico (Serviço A)**:
```bash
curl http://localhost:8001/usuarios/1
```

**Listar usuários com informações combinadas (Serviço B)**:
```bash
curl http://localhost:8002/usuarios-combinado
```

**Obter usuário detalhado (Serviço B)**:
```bash
curl http://localhost:8002/usuarios-detalhado/1
```

**Verificar saúde do Serviço B**:
```bash
curl http://localhost:8002/health
```