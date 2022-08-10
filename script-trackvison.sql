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

create table componentes (
idComponente int primary key auto_increment,
descricao varchar(45)
);

create table caixa (
idCaixa int auto_increment,
fkEmpresa int,
foreign key(fkEmpresa) references empresa(idEmpresa), 
primary key(idCaixa, fkEmpresa),
agencia char(4)
) auto_increment= 100;

create table leitura (
fkComponente int,
fkCaixa int,
fkEmpresa int,
foreign key(fkComponente) references componentes(idComponente),
foreign key(fkCaixa) references caixa(idCaixa),
foreign key(fkEmpresa) references empresa(idEmpresa),
capTotal DECIMAL(5,2),
capUso DECIMAL(5,2),
ultimaLeitura DATETIME
);

desc empresa;
desc usuario;
desc componentes;
desc caixa;
desc leitura;

insert into empresa values (null, 'Caixa Econômica Federal', '00.360.305/0001-04', 'caixaeletronica@caixa.com');

insert into usuario values (null, 1000, 'Pedro Henrique Ventura', 'pedroventura@caixa.com', 'pedro123_');

insert into componentes values (null, 'Processador'),
							   (null, 'Memória RAM'),
                               (null, 'Memória Disco'),
                               (null, 'Wi-Fi'),
                               (null, 'GPU');
                               
insert into caixa values (null, 1000, '1573'),
                         (null, 1000, '0238');
                         
insert into leitura values (2, 100, 1000, '16.00', '8.00', '2022-05-14 20:36:07'),
                           (3, 101, 1000, '447.00', '15.00', '2022-07-30 15:29:23');
                           
select * from empresa, usuario, componentes, caixa, leitura where usuario.fkEmpresa = idEmpresa and caixa.fkEmpresa = idEmpresa and leitura.fkEmpresa = idEmpresa and fkComponente = idComponente and fkCaixa = idCaixa;