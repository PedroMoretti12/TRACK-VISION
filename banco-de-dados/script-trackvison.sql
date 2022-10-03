CREATE DATABASE Trackvision;

USE Trackvision;

CREATE TABLE Banco (
id INT PRIMARY KEY AUTO_INCREMENT,
nomeBanco VARCHAR(45),
codigo CHAR(3),
ISPB CHAR(8)
);

CREATE TABLE Usuario (
id INT,
fkBanco INT,
nome VARCHAR(5),
email VARCHAR(45),
senha VARCHAR(45),
FOREIGN KEY(fkBanco) REFERENCES Banco(id),
PRIMARY KEY(id)
);

CREATE TABLE Agencia (
id INT,
fkBanco INT,
numeroAgencia CHAR(4),
bairro VARCHAR(45),
cep CHAR(8),
rua VARCHAR(45),
numero INT,
FOREIGN KEY(fkBanco) REFERENCES Banco(id),
PRIMARY KEY(id)
);

CREATE TABLE Caixa (
id INT, 
fkAgencia INT,
numeroSerial CHAR(8),
FOREIGN KEY(fkAgencia) REFERENCES Agencia(id),
PRIMARY KEY(id)
);

CREATE TABLE Leitura (
id INT,
fkAgencia INT,
fkCaixa INT,
cpuPorcentagem DECIMAL(4,2),
ramPorcentagem DECIMAL(4,2),
hdPorcentagem DECIMAL(4,2),
momento DATETIME,
FOREIGN KEY(fkAgencia) REFERENCES Agencia(id),
FOREIGN KEY(fkCaixa) REFERENCES Caixa(id),
PRIMARY KEY(id)
);

INSERT INTO Banco VALUES (NULL, 'Banco do Brasil', '001', '00000000'),
						 (NULL, 'Bradesco', '237', '60746948'),
                         (NULL, 'Caixa econômica federal', '104', '00360305');
                         
INSERT INTO Agencia VALUES (1, 1, '1234', 'Campo Limpo', '05763470', 'Rua Douglas Costa', 75);

INSERT INTO Caixa VALUES (1, 1, '12345678'),
						 (2, 1, '12345678'),
                         (3, 1, '12345678');
                         
SELECT * FROM leitura;	






