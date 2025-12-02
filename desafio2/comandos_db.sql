CREATE TABLE Usuario (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(50)
);

INSERT INTO Usuario (nome) VALUES ('Davi'), ('Maria'), ('João');

SELECT * FROM Usuario;