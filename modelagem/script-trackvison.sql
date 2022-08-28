-- TRack Vision (Team 10) - Felipe Pires, Isabela Hantke, Rafaela Dias, Verônica Zibordi, Vitor Macauba --
-- drop database trackvision;
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
idLeitura int primary key auto_increment,
fkCaixa int,
fkUsuario int,
foreign key(fkCaixa) references caixa(idCaixa),
foreign key(fkUsuario) references usuario(idUsuario),
processadorPorcentagem float,
memoriaRAM float,
disco float,
ultimaLeitura DATETIME
)auto_increment = 2000;

desc empresa;
desc usuario;
desc caixa;
desc leitura;

insert into empresa values 
(null, 'Caixa Econômica Federal', '00.360.305/0001-04', 'caixaeletronica@caixa.com'),
(null, 'Santander SA.', '12.852.987/0001-45', 'santanderatv@comercial.com'),
(null, 'Banco do Brasil', '25.587.963/0001-45', 'bancodobrasil@bancobb.com');

insert into usuario values 
(null, 1000, 'Pedro Henrique Ventura', 'pedroventura@caixa.com', 'pedro123_'),
(null, 1001, 'Carlos Mederiros Campos', 'carlosmedeiros@comercial.com', 'carlos123_'),
(null, 1002, 'Maria Antônia Camargo', 'mariaacamargo@bancobb.com', 'maria123_');
                        
insert into caixa values 
(null, 500, '1573'),
(null, 501, '0238'),
(null, 502, '8547');

select * from empresa;
-- select * from usuario;
-- select * from caixa;
-- select * from leitura;
						
select * from empresa, usuario, caixa, leitura 
		where usuario.fkEmpresa = idEmpresa 
				and caixa.fkUsuario = idUsuario 
						and leitura.fkUsuario = idUsuario 
							and leitura.fkCaixa = idCaixa;
                            
select idUsuario as 'Cód de Usuário', 
	fkEmpresa as 'Cód da Empresa',
		idCaixa as 'Cód. do ATM', 
			processadorPorcentagem as 'CPU (%)',
				memoriaRAM as 'RAM (%)', 
					disco as 'Disco (%)', 
						ultimaLeitura as 'Data e Hora'
							from usuario join caixa join leitura
								on leitura.fkusuario = idusuario 
									and leitura.fkCaixa = idcaixa;




