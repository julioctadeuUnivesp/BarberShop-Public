\c barbershopdb;

CREATE USER appFlask WITH PASSWORD 'abc@1234';
GRANT ALL PRIVILEGES ON DATABASE barbershopdb TO appFlask;

CREATE TABLE usuarios (
        id INTEGER PRIMARY KEY,
        nome TEXT NOT NULL,
        email TEXT NOT NULL,
        telefone TEXT NOT NULL,
        senha TEXT NOT NULL,
        status TEXT NOT NULL
);

CREATE TABLE produtos (
        id INTEGER PRIMARY KEY,
        produto TEXT NOT NULL,
        preco TEXT NOT NULL
);

CREATE TABLE agendamento (
        id INTEGER PRIMARY KEY,
        nome TEXT NOT NULL,
        email TEXT NOT NULL,
        telefone TEXT NOT NULL,
        servico TEXT NOT NULL,
        data TEXT NOT NULL                
);

CREATE TABLE datahora (
        id INTEGER PRIMARY KEY,   
        datahora TEXT NOT NULL
);

