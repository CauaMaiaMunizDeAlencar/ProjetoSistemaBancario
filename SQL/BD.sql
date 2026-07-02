CREATE DATABASE ProjetoBancario;

USE ProjetoBancario;

CREATE TABLE contas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    saldo DECIMAL(10,2)
);

INSERT INTO contas (nome, saldo)
VALUES
('SEU_NOME_EXEMPLO1',1000),
('SEU_NOME_EXEMPLO2',1000);
