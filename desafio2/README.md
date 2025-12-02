# Descrição da Solução

A solução consiste na criação imagem Docker personalizada do **PostgreSQL**, juntamente com um volume Docker para armazenar os dados no banco.

A aplicação possui o banco de dados executando dentro de um container configurado a partir de um Dockerfile.

# Explicação do Funcionamento

## Dockerfile

- Baseado em **postgres:15**
- Define as variáveis de ambiente necessárias:
  - `POSTGRES_USER=admin`
  - `POSTGRES_PASSWORD=senha`
  - `POSTGRES_DB=desafio2_db`

O Dockerfile prepara a imagem `desafio2_volume_img`, já configurando o banco no momento da criação do container.

## Volume

É criado um volume chamado **volume_postgres**, que armazena de forma persistente os dados do PostgreSQL no caminho: `/var/lib/postgresql/data`

Mesmo após remover o container, os dados permanecem salvos graças ao volume.

## Container

O container chamado **desafio2_volume** executa o PostgreSQL usando a imagem criada.  
O banco pode ser acessado pelo terminal usando o comando `docker exec`, permitindo rodar comandos SQL do arquivo `comandos_db.sql` manualmente.

# Instruções de Execução

```bash
# Acessar parta
cd desafio2

# Build da imagem
docker build -t desafio2_volume_img .

# Rodar container com volume persistente
docker run -d --name desafio2_volume -v volume_postgres:/var/lib/postgresql/data desafio2_volume_img

# Acessar terminal do PostgreSQL
docker exec -it desafio2_volume psql -U admin -d desafio2_db

# (Dentro do psql) Executar comandos SQL do arquivo comandos_db.sql manualmente.

# Parar e remover o container
docker stop desafio2_volume
docker rm desafio2_volume

# Verificar que o volume ainda existe
docker volume ls

# Recriar outra imagem postgres com o mesmo volume para verificar persistência
docker run -d --name desafio2_volume_2 -e POSTGRES_PASSWORD=senha -e POSTGRES_USER=admin -e POSTGRES_DB=desafio2_db_2 -v volume_postgres:/var/lib/postgresql/data postgres:15

# Acessar terminal do novo container
docker exec -it desafio2_volume_2 psql -U admin -d desafio2_db_2

# Executar comando SQL = SELECT * FROM Usuario; 

```