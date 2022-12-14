CREATE DATABASE Trackvision;
-- DROP DATABASE Trackvision;

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
nome VARCHAR(45),
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
id INT AUTO_INCREMENT, 
fkBanco INT,
fkAgencia INT,
numeroSerial CHAR(8),
dataCompra CHAR(10),
vidaUtil int,
FOREIGN KEY(fkAgencia) REFERENCES Agencia(id),
PRIMARY KEY(id)
) AUTO_INCREMENT = 100;

CREATE TABLE Leitura (
id INT AUTO_INCREMENT,
fkBanco INT,
fkAgencia INT,
fkCaixa INT,
cpuPorcentagem DECIMAL(5,2),
ramPorcentagem DECIMAL(5,2),
hdPorcentagem DECIMAL(5,2),
processosAtivos INT,
servicoAtivos INT,
momento DATETIME,
processosPerigosos INT,
servicosPerigosos INT,
tempCpu DECIMAL (5,2),
FOREIGN KEY(fkAgencia) REFERENCES Agencia(id),
FOREIGN KEY(fkCaixa) REFERENCES Caixa(id),
FOREIGN KEY(fkBanco) REFERENCES Banco(id),
PRIMARY KEY(id)
);

CREATE TABLE Projeto_Julia (
fkBanco INT,
FOREIGN KEY(fkBanco) REFERENCES Banco(id),
fkAgencia INT,
FOREIGN KEY(fkAgencia) REFERENCES Agencia(id),
fkCaixa INT,
FOREIGN KEY (FkCaixa) REFERENCES Caixa(id),
pid INT, 
nomeProcesso VARCHAR(30),
usoCpuProcesso DECIMAL (5,2),
usoMemoriaProcesso DECIMAL (5,2)
);

CREATE TABLE Proj_Michelly(
id INT PRIMARY KEY AUTO_INCREMENT,
hora time,
data_data date,
cpuPorcentagem DECIMAL(5,2),
tempCpuMin DECIMAL (5,2),
tempCpuMed DECIMAL (5,2),
tempCpuMax DECIMAL (5,2),
fkCaixa INT,
FOREIGN KEY (fkCaixa) REFERENCES Caixa (id)
)auto_increment = 200; 

INSERT INTO Banco VALUES (NULL, 'Banco do Brasil', '001', '00000000'),
						 (NULL, 'Bradesco', '237', '60746948'),
                         (NULL, 'Caixa econômica federal', '104', '00360305');
                         
INSERT INTO Agencia VALUES (1, 1, '1234', 'Campo Limpo', '05763470', 'Rua Douglas Costa', 75);

INSERT INTO Caixa (fkBanco, fkAgencia, numeroSerial, dataCompra, vidaUtil) VALUES (1, 1, '12345678', '30/11/2022', 14000),
																(2, 1, '12345678', '11/01/2011', 25500),
																(3, 1, '12345678', '15/12/2020', 10000);
																															
                                                                
<<<<<<< HEAD
select * from Caixa;	
-- update Caixa set vidaUtil = 1000 where id in (select id from (select id from Caixa order by id desc limit 1) as t);	
=======
-- select * from Caixa;	
-- update Caixa set vidaUtil = 25000 where id = (select id from Caixa order by id desc limit 1);

-- update Caixa set vidaUtil = 1000 where id in (select id from (select id from Caixa order by id desc limit 1) as t);
>>>>>>> 2aeec2b71e62ec1a1658b3fbd3479577d49adf45
