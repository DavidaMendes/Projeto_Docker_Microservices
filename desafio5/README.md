# Desafio 5 — API Gateway Centralizando Microsserviços

## Descrição da Solução

A solução implementa uma arquitetura com API Gateway que centraliza o acesso a dois microsserviços independentes:

- **API Gateway (FastAPI)**: gateway centralizado que expõe endpoints `/users` e `/orders` e orquestra as chamadas aos serviços
- **Serviço de Usuários (FastAPI)**: microsserviço que fornece dados de usuários
- **Serviço de Pedidos (Flask)**: microsserviço que fornece dados de pedidos

Os serviços são orquestrados utilizando Docker Compose e se comunicam através de requisições HTTP em uma rede Docker privada.

## Estrutura do Projeto

```bash
desafio5
│-- README.md
│-- docker-compose.yml
│-- gateway
│ │-- app.py
│ │-- Dockerfile
│ │-- requirements.txt
│-- service_users
│ │-- app.py
│ │-- Dockerfile
│ │-- requirements.txt
│-- service_orders
│ │-- app.py
│ │-- Dockerfile
│ │-- requirements.txt
```

## Explicação do Funcionamento

### API Gateway (FastAPI)

Componente central que centraliza o acesso aos microsserviços:

- **Tecnologia**: FastAPI
- **Porta**: 8000
- **Responsabilidades**:
  - Rotear requisições para os serviços apropriados
  - Validar e tratar erros
  - Orquestrar chamadas entre serviços
  - Implementar lógica de negócio que envolve múltiplos serviços

**Endpoints do Gateway**:
  - `GET /health`: verifica saúde do gateway
  - `GET /users`: retorna lista de todos os usuários
  - `GET /users/{user_id}`: retorna um usuário específico
  - `GET /orders`: retorna lista de todos os pedidos
  - `GET /orders/{order_id}`: retorna um pedido específico
  - `GET /users/{user_id}/orders`: retorna pedidos de um usuário específico (orquestra dois serviços)

### Serviço de Usuários (FastAPI)

Microsserviço responsável por fornecer dados de usuários:

- **Tecnologia**: FastAPI
- **Porta**: 8001
- **Endpoints**:
  - `GET /health`: verifica saúde do serviço
  - `GET /usuarios`: retorna lista completa de usuários
  - `GET /usuarios/{usuario_id}`: retorna dados de um usuário específico

### Serviço de Pedidos (Flask)

Microsserviço responsável por fornecer dados de pedidos:

- **Tecnologia**: Flask
- **Porta**: 8002
- **Endpoints**:
  - `GET /health`: verifica saúde do serviço
  - `GET /pedidos`: retorna lista completa de pedidos
  - `GET /pedidos/{pedido_id}`: retorna um pedido específico
  - `GET /pedidos/usuario/{usuario_id}`: retorna pedidos de um usuário

### Comunicação entre Serviços

- O Gateway realiza requisições HTTP para os microsserviços
- **Serviço de Usuários**: `http://service_users:8001`
- **Serviço de Pedidos**: `http://service_orders:8002`
- A comunicação acontece dentro de uma rede Docker privada chamada `desafio5_rede`
- O Gateway aguarda os serviços estarem prontos via `depends_on`

## Instruções de Execução

### Com Docker Compose (Recomendado)

```bash
# Acessar a pasta
cd desafio5

# Iniciar os serviços
docker-compose up -d

# Verificar o status dos containers
docker-compose ps

# Ver logs dos serviços
docker-compose logs -f gateway
docker-compose logs -f service_users
docker-compose logs -f service_orders

# Testar os endpoints
curl http://localhost:8000/health
curl http://localhost:8000/users
curl http://localhost:8000/orders
curl http://localhost:8000/users/1/orders

# Parar os serviços
docker-compose down
```

### Testando os Endpoints do Gateway

**Verificar saúde do gateway**:
```bash
curl http://localhost:8000/health
```

**Listar todos os usuários**:
```bash
curl http://localhost:8000/users
```

**Obter usuário específico**:
```bash
curl http://localhost:8000/users/1
```

**Listar todos os pedidos**:
```bash
curl http://localhost:8000/orders
```

**Obter pedido específico**:
```bash
curl http://localhost:8000/orders/1
```

**Obter usuário com seus pedidos (orquestração)**:
```bash
curl http://localhost:8000/users/1/orders
```

### Testando os Endpoints dos Serviços Diretamente

**Serviço de Usuários (Porta 8001)**:
```bash
curl http://localhost:8001/health
curl http://localhost:8001/usuarios
curl http://localhost:8001/usuarios/1
```

**Serviço de Pedidos (Porta 8002)**:
```bash
curl http://localhost:8002/health
curl http://localhost:8002/pedidos
curl http://localhost:8002/pedidos/1
curl http://localhost:8002/pedidos/usuario/1
```