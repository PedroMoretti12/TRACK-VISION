create database trackvision;
use trackvision;

create table usuario (
idUsuario int primary key auto_increment,
razaoSocial varchar(45),
cpnj char(12),
email varchar(45),
senha varchar (20)
) auto_increment = 1000;

create table componentes (
idComponente int primary key auto_increment,
processador varchar(45),
memoriaLocal varchar(45),
memoriaRam varchar(45),
wifi varchar(45),
gpu varchar(45)
);

create table caixa (
fkUsuario int,
foreign key(fkUsuario) references usuario(idUsuario),
fkComponentes int,
foreign key(fkComponentes) references componentes(idComponente),
idCaixa int,
primary key(fkUsuario, fkComponentes, idCaixa),
capMax varchar(10),
capMin varchar(10),
ultimaLeitura datetime
);

desc usuario;
desc componentes;
desc caixa;