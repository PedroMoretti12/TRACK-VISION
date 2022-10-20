import requests
import pyodbc
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup


#Conexao


server = 'trackvisiondb.database.windows.net'
database = 'trackvisiondb'
username = 'CloudSA49c766d4'
password = 'Urubu1004'
driver = '{ODBC Driver 17 for SQL Server}'

conn = pyodbc.connect('DRIVER='+driver+';'
                      'SERVER=tcp:'+server+';'
                      'PORT=1433;'
                      'DATABASE='+database+';'
                       'UID='+username+';'
                                                                                                 'PWD='+ password)
cursor = conn.cursor()


#Escolhe a Ação do Banco
fkBanco = 0
escolha = input('Escolha um Banco: \n'
                '1-Banco do Brasil \n'
                '2-Bradesco \n'
                '3-Banco Pan\n')
if(escolha == '1'):
    pagehtml = 'https://www.infomoney.com.br/cotacoes/b3/acao/banco-do-brasil-bbas3/'
    fkBanco = 1
elif(escolha == '2'):
    pagehtml = 'https://www.infomoney.com.br/cotacoes/b3/acao/bradesco-bbdc3/'
    fkBanco = 2
elif(escolha == '3'):
    pagehtml = 'https://www.infomoney.com.br/cotacoes/b3/acao/banco-pan-bpan4/'
    fkBanco = 3
else:
    print('Nenhuma Opção Válida Encerrando o Web Crawler')

if(id != ''):
 page = requests.get(pagehtml)
 soup = BeautifulSoup(page.content, 'html.parser')

#Procura os Dados

 corpodado = soup.find('div', {'class':'line-info'})
 tagultima = corpodado.findNext('div').findNext('p').contents[0]
 tagvariacao = tagultima.findNext('div').findNext('p').contents[0]
 tagminima = tagvariacao.findNext('div').findNext('p').contents[0]
 tagmaxima = tagminima.findNext('div').findNext('p').contents[0]

#Transforma em Números
 ultima = float(tagultima.replace(',','.'))
 variacao = float(tagvariacao.replace('%',''))
 minima = float(tagminima.replace(',','.'))
 maxima = float(tagmaxima.replace(',','.'))

 print(ultima)
 print(variacao)
 print(minima)
 print(maxima)
 print('oie')

 #INSERT NO BANCO

 syntax = "update cotacao set atual = ?, minimo = ?, maximo = ?, variacao = ? where fkBanco = ?"
 values = [ultima,minima,maxima,variacao,fkBanco]
 cursor.execute(syntax,values)
 cursor.commit()
 count = cursor.rowcount
 #CASO NÃO ESTEJA NA TABELA COTAÇÃO
 if(count == 0):
    syntax = "insert into cotacao values ?,?,?,?,?)"
    values = [fkBanco,ultima, minima, maxima, variacao]
    cursor.execute(syntax, values)
    cursor.commit()

syntax = "select nomeBanco from Banco where id = ?"
values = (fkBanco)
cursor.execute(syntax, values)
row = cursor.fetchone
for row in cursor:
 print(row)
 banco = row.nomeBanco

labels = ["Ultima","Minima","Maxima","Variação"]
data = [ultima,minima,maxima,variacao]
fig,ax = plt.subplots(figsize=(8, 5))
ax.bar(labels,data)
ax.set_title("Cotação das Ações do "+banco+'',fontsize=10)
ax.set_ylabel("Valor em R$")
ax.set_xlabel("Contexto")
plt.show()

