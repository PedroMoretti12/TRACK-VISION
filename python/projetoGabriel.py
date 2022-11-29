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
 syntax = "insert into caixa values(103, 4, 1,%s,%s)"
 values = [numSerial,dataCompra]
 cursor.execute(syntax,values)
 conn.commit
 cursor.execute("select * from Caixa")

# Formatação das datas
 data = date.today()

 dataCaixa = datetime.strptime(dataCompra, "%d/%m/%Y").date()

 dataAtual = datetime.strptime(data, "%d/%m/%Y").date()

# Calculo da quantidade de dias
 dias = abs((dataCaixa - dataAtual).days)
 print(dias)
