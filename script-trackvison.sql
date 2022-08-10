create database trackvision;
use trackvision;

create table usuario (
idUsuario int primary key auto_increment,
razaoSocial varchar(45),
celular char(11),
cpnj char(18),
senha varchar (20)
) auto_increment = 1000;

create table componentes (
idComponente int primary key auto_increment,
descricao varchar(45)
);

create table caixa (
idCaixa int auto_increment,
fkUsuario int,
foreign key(fkUsuario) references usuario(idUsuario), 
primary key(idCaixa, fkUsuario),
agencia char(4)
) auto_increment= 100;

create table leitura (
fkComponente int,
fkCaixa int,
fkUsuario int,
foreign key(fkComponente) references componentes(idComponente),
foreign key(fkCaixa) references caixa(idCaixa),
foreign key(fkUsuario) references usuario(idUsuario),
capTotal DECIMAL(5,2),
capUso DECIMAL(5,2),
ultimaLeitura DATETIME
);

desc usuario;
desc componentes;
desc caixa;
desc leitura;

insert into usuario values (null, 'Caixa Econômica Federal', '11922223333', '00.360.305/0001-04', 'caixa123');

insert into componentes values (null, 'Processador'),
							   (null, 'Memória RAM'),
                               (null, 'Memória Disco'),
                               (null, 'Wi-Fi'),
                               (null, 'GPU');
                               
insert into caixa values (null, 1000, '1573'),
                         (null, 1000, '0238');
                         
insert into leitura values (2, 100, 1000, '16.00', '8.00', '2022-05-14 20:36:07'),
                           (3, 101, 1000, '447.00', '15.00', '2022-07-30 15:29:23');
                           
select * from usuario, componentes, caixa, leitura where caixa.fkUsuario = idUsuario and leitura.fkUsuario = idUsuario and fkComponente = idComponente and fkCaixa = idCaixa;