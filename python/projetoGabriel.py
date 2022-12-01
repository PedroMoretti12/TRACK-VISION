import mysql.connector
import datetime
from datetime import date
from datetime import datetime
import time

conn = mysql.connector.connect(user='aluno',password='sptech',database='trackvision',port='3306')
cursor = conn.cursor()


numSerial = input("Qual o número serial do caixa?")
dataCompra = input("Qual é o ano de compra deste caixa?")


if(dataCompra == "" or numSerial == ""): 
 print("Os campos devem ser preenchidos")

else:    
  syntax = "insert into Caixa (fkBanco, fkAgencia, numeroSerial, dataCompra) values(1,1,%s,%s)"
  values = [numSerial,dataCompra]
  cursor.execute(syntax,values)
  conn.commit()
  cursor.execute("select dataCompra from Caixa")


# Formatação das datas
dataAtual = date.today()
data = cursor.fetchall()
i = len(data)

dataCaixa = datetime.strptime(data[i - 1][0],'%d/%m/%Y').date() 

# Calculo da quantidade de dias
dias = (dataAtual - dataCaixa)    
print(dias.days)

# Calculo de vida útil
vidaUtil = 5 * (24 * dias.days)

# Temporizador
print("A vida útil do caixa é de", vidaUtil, "HRs")

syntax = "update Caixa set vidaUtil = %s where id in (select id from (select id from Caixa order by id desc limit 1) as t);"
values = [vidaUtil]
cursor.execute(syntax,values)
conn.commit()
cursor.execute("select vidaUtil from Caixa")

