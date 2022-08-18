create database trackvision;
use trackvision;

create table empresa (
idEmpresa int primary key auto_increment,
razaoSocial VARCHAR(45),
cnpj char(18),
email varchar(45)
) auto_increment = 1000;

create table usuario (
idUsuario int auto_increment,
fkEmpresa int,
foreign key(fkEmpresa) references empresa(idEmpresa), 
primary key(idUsuario, fkEmpresa),
nome varchar(45),
email varchar(45),
senha varchar (20)
) auto_increment = 500;

create table caixa (
idCaixa int primary key auto_increment,
fkUsuario int,
foreign key(fkUsuario) references usuario(idUsuario), 
agencia char(4)
) auto_increment= 100;

create table leitura (
fkCaixa int,
fkUsuario int,
foreign key(fkCaixa) references caixa(idCaixa),
foreign key(fkUsuario) references usuario(idUsuario),
primary key(fkCaixa, fkUsuario),
processador1 DECIMAL(3,1),
processador2 DECIMAL(3,1),
processador3 DECIMAL(3,1),
processador4 DECIMAL(3,1),
processador5 DECIMAL(3,1),
processador6 DECIMAL(3,1),
processador7 DECIMAL(3,1),
processador8 DECIMAL(3,1),
memoriaRAM DECIMAL(5,3),
disco DECIMAL(6,3),
ultimaLeitura DATETIME
);

desc empresa;
desc usuario;
desc caixa;
desc leitura;

insert into empresa values (null, 'Caixa Econômica Federal', '00.360.305/0001-04', 'caixaeletronica@caixa.com');

insert into usuario values (null, 1000, 'Pedro Henrique Ventura', 'pedroventura@caixa.com', 'pedro123_');
                               
insert into caixa values (null, 500, '1573'),
                         (null, 500, '0238');
                         
insert into leitura values (100, 500, '42.0', '39.1', '32.8', '34.4', '47.7', '43.8', '21.9', '31.2', '5.174', '24.618', '2022-05-14 20:36:07'),
                           (101, 500, '41.0', '38.1', '31.8', '33.4', '46.7', '42.8', '20.9', '30.2', '4.235', '22.469', '2022-07-30 15:29:23');
                           
select * from empresa, usuario, caixa, leitura where usuario.fkEmpresa = idEmpresa and caixa.fkUsuario = idUsuario and leitura.fkUsuario = idUsuario and leitura.fkCaixa = idCaixa;