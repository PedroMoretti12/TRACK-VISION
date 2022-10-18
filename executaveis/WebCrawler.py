import requests
import pyodbc
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup


#Conexao


server = 'trackvisiondb.database.windows.net'
database = 'trackvisiondb'
username = 'CloudSA49c766d4'
password = 'Urubu1004'
driver= '{ODBC Driver 17 for SQL Server}'

conn = pyodbc.connect('DRIVER='+driver+';'
                      'SERVER=tcp:'+server+';'
                      'PORT=1433;'
                      'DATABASE='+database+';'
                       'UID='+username+';'
                                                                                                 'PWD='+ password)
cursor = conn.cursor()


#Escolhe a Ação do Banco
id = ''
fkBanco = 0
escolha = input('Escolha um Banco: \n'
                '1-Banco do Brasil \n'
                '2-Bradesco \n'
                '3-Banco Pan\n')
if(escolha == '1'):
    id = 'pair_18604'
    fkBanco = 1
elif(escolha == '2'):
    id = 'pair_18605'
    fkBanco = 2
elif(escolha == '3'):
    id = 'pair_18614'
    fkBanco = 3
else:
    print('Nenhuma Opção Válida Encerrando o Web Crawler')

if(id != ''):
 page = requests.get('https://br.investing.com/equities/')
 soup = BeautifulSoup(page.content, 'html.parser')

#Procura os Dados
 tagbanco = soup.find('tr',{'id':id}).contents[1].findNext('a')
 tagultima = soup.find('tr',{'id':id}).contents[1].findNext('td').contents[0]
 tagmaxima = tagultima.findNext('td')
 tagminima = tagmaxima.findNext('td')
 tagvariacao = tagminima.findNext('td')

 banco = tagbanco.contents[0]
 ultima = float(tagultima.replace(',','.'))
 minima = float(tagminima.contents[0].replace(',','.'))
 maxima = float(tagmaxima.contents[0].replace(',','.'))
 variacao = float(tagvariacao.contents[0].replace(',','.'))

 print(banco)

 #INSERT NO BANCO

 syntax = "update cotacao set atual = ?, minimo = ?, maximo = ?, variacao = ? where fkBanco = (select id from Banco where nomeBanco = ?)"
 values = [ultima,minima,maxima,variacao,banco]
 cursor.execute(syntax,values)
 cursor.commit()
 count = cursor.rowcount
 #CASO NÃO ESTEJA NA TABELA COTAÇÃO
 if(count == 0):
    syntax = "insert into cotacao values ((select id from Banco where nomeBanco = ?),0,0,0,0)"
    values = [banco]
    cursor.execute(syntax, values)
    cursor.commit()
    syntax = "update cotacao set atual = ?, minimo = ?, maximo = ?, variacao = ? where fkBanco = (select id from Banco where nomeBanco = ?)"
    values = [ultima, minima, maxima, variacao, banco]
    cursor.execute(syntax, values)
    cursor.commit()

labels = ["Ultima","Minima","Maxima","Variação"]
data = [ultima,minima,maxima,variacao]
fig,ax = plt.subplots(figsize=(8, 5))
ax.bar(labels,data)
ax.set_title("Cotação das Ações do "+banco+'',fontsize=10)
ax.set_ylabel("Valor em R$")
ax.set_xlabel("Contexto")
plt.show()

syntax = "select * from cotacao where fkBanco = (select id from banco where nomeBanco = ?)"
values = (banco)
cursor.execute(syntax,values)
row = cursor.fetchone
for row in cursor:
    print(row)