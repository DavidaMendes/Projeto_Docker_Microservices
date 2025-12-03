# Projeto 2 - Unidade: Docker e Microsserviços

Repositório contendo soluções para 5 desafios práticos sobre Docker, containerização e arquitetura de microsserviços.

## Desafios

### Desafio 1: Cliente-Servidor com FastAPI
- **Objetivo**: comunicação entre dois containers
- **Solução**: FastAPI (Server) + Python Client (Client)
- **Execução**: Dockerfiles e Rede privada

### Desafio 2: Banco de Dados em Container
- **Objetivo**: executar PostgreSQL em container e gerenciar dados
- **Solução**: PostgreSQL 15 em container com persistência de dados
- **Execução**: Dockerfile com comandos SQL

### Desafio 3: Multi-Serviços com Docker Compose
- **Objetivo**: integração de web, banco de dados e cache
- **Solução**: Flask (Web) + PostgreSQL (DB) + Redis (Cache)
- **Execução**: `docker-compose up -d` (3 serviços orquestrados)

### Desafio 4: Microsserviços Independentes
- **Objetivo**: dois serviços que se comunicam via HTTP
- **Solução**: FastAPI (Serviço A - Usuários) + Flask (Serviço B - Consumidor)
- **Execução**: `docker-compose up -d` com rede privada Docker

### Desafio 5: API Gateway Centralizando Microsserviços
- **Objetivo**: gateway centralizando acesso a múltiplos serviços
- **Solução**: FastAPI Gateway + FastAPI (Usuários) + Flask (Pedidos)
- **Execução**: `docker-compose up -d` com orquestração de chamadas

Consulte o README.md de cada desafio para mais detalhes e exemplos de teste.
