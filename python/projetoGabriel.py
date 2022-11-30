import psutil
import mysql.connector
import datetime
from datetime import date
from datetime import datetime

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
print(data[i - 1])

dataCaixa = datetime.strptime(data[i - 1][0],'%d/%m/%Y').date() 

# Calculo da quantidade de dias
dias = (dataAtual - dataCaixa)    
print(dias.days)

vidaUtil = 3 * (24 * dias.days)
print(vidaUtil)
