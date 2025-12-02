# Descrição da Solução

A solução consiste em um cliente e um servidor:

- **Server**: desenvolvido com FastAPI  
- **Client**: script Python

O server é responsável por executar uma API com uma rota **POST** que recebe uma mensagem em JSON e a retorna.  
O client executa um script que envia uma mensagem para a rota do server.

## Estrutura do Projeto

desafio1
│-- README.md
│-- client
│ │-- client.py
│ │-- Dockerfile
│-- server
│ │-- app.py
│ │-- Dockerfile

# Explicação funcionamento 
## Server

- Implementado com FastAPI  
- Utiliza Pydantic  
- Necessita do Uvicorn para executar o servidor  
- Possui a rota **POST /message**, que recebe um JSON contendo uma mensagem e retorna o mesmo JSON  

## Client

- Implementado em Python  
- Utiliza a biblioteca `requests` para realizar requisições HTTP  
- Envia uma requisição **POST** para o servidor na rota **/message** enviando a mensagem definida  

O script contém um loop que realiza múltiplas requisições ao servidor.

Como as dependências não estão instaladas localmente, é necessário utilizar os Dockerfiles para construir e executar as imagens com tudo configurado.

# Instruções de Execução

```bash
# Criar a rede Docker
docker network create desafio1_rede

# Build das imagens
docker build -t fastapi-server ./server
docker build -t python-client ./client

# Executar os containers na rede criada
docker run -d --name server --network desafio1_rede -p 8080:8080 fastapi-server
docker run -d --name client --network desafio1_rede python-client

# Ver logs dos containers - interação do client com o server
docker logs -f server
docker logs -f client
