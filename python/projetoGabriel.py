import mysql.connector
import pyodbc
import datetime
from datetime import date
from datetime import datetime
from tkinter import *

try:
    server = 'trackvisiondb.database.windows.net'
    database = 'trackvisiondb'
    username = 'CloudSA49c766d4'
    password = 'Urubu1004'
    driver = '{ODBC Driver 18 for SQL Server}'

    conn = pyodbc.connect('DRIVER=' + driver + ';'
                           'SERVER=tcp:' + server + ';'
                           'PORT=1433;'
                           'DATABASE=' + database + ';'
                           'UID=' + username + ';'
                           'PWD=' + password)

    cursor = conn.cursor()
    conexao = True
except:
    pass

connn = mysql.connector.connect(user='aluno',password='sptech',database='trackvision',port='3306')
cursorr = connn.cursor()

janela = Tk()
janela.title("Cadastro dos caixa")
janela.geometry('350x240')

# Função cadastrar --------------------------------
def Cadastrar():
  numSerial = Entry_numSerial.get()
  dataCompra = Entry_dataCompra.get()

# Condição de validação ---------------------------
  if(numSerial == '' or dataCompra == ''):

   texto_resposta['text'] = 'Os campos devem ser cadastrados'
   return

  if(len(numSerial) > 8):
   texto_resposta['text'] = 'Digite um número serial válido'
   return

  if(len(dataCompra) > 10):
   texto_resposta['text'] = 'Digite uma data válida'
   return

  else:    
   syntax = "insert into Caixa (fkBanco, fkAgencia, numeroSerial, dataCompra) values(1,1,?,?)"
   values = [numSerial,dataCompra]
   cursor.execute(syntax,values)
   cursor.commit()
   cursor.execute("select dataCompra from Caixa")

   texto_resposta['text'] = 'Dados cadastrados com sucesso'
   print(numSerial, dataCompra)

   
# Formatação das datas --------------------------------
   dataAtual = date.today()
   data = cursor.fetchall()
   i = len(data)

   dataCaixa = datetime.strptime(data[i - 1][0],'%d/%m/%Y').date() 

# Calculo da quantidade de dias ----------------------------------
   dias = (dataAtual - dataCaixa)    
   print(dias.days)

# Calculo de vida útil ------------------------------------------
   vidaUtil = 7 * (24 * dias.days)

   print("A vida útil do caixa é de", vidaUtil, "HRs")

   syntax = "update Caixa set vidaUtil = ? where id in (select id from (select top(1) id from Caixa order by id desc) as t);"
   values = [vidaUtil]
   cursor.execute(syntax,values)
   cursor.commit()
   cursor.execute("select vidaUtil from Caixa")
   
# Temporizador de atualização dos dados ----------------------------------
   texto_resposta2['text'] = 'Dados atualizados com sucesso'

# Número serial ------------------------------------
Label_numSerial = Label(janela, text=("Insira o número serial do caixa:"), font=('Arial 10'), anchor='w')
Label_numSerial.grid(column=0, row=0, padx=5, pady=5, sticky=NSEW)
# Caixa de entrada
Entry_numSerial = Entry(janela, width=15, font=('Arial 10 '))
Entry_numSerial.grid(column=1, row=0, padx=5, pady=5, sticky=NSEW)

# Data de compra do caixa ------------------------------
Label_dataCompra = Label(janela, text=("Insira o ano de compra do caixa:"), font=('Arial 10'), anchor='w')
Label_dataCompra.grid(column=0, row=1, padx=5, pady=5, sticky=NSEW)
# Caixa de entrada
Entry_dataCompra = Entry(janela, width=10, font=('Arial 10 '))
Entry_dataCompra.grid(column=1, row=1, padx=5, pady=5, sticky=NSEW)

# Botão de Cadastrar ----------------------------------
Button_cadastar = Button(janela, width=10, command=Cadastrar, text="Cadastrar", font=('Arial 10'), anchor=CENTER)
Button_cadastar.grid(column=0, row=2, padx=15, pady=15, sticky=NSEW)

# Saída de resposta ------------------------------------
texto_resposta = Label(janela, text="")
texto_resposta.grid(column=0, row=3, padx=10, pady=10, sticky=NSEW)

texto_resposta2 = Label(janela, text="")
texto_resposta2.grid(column=0, row=4, padx=10, pady=10, sticky=NSEW)

janela.mainloop()
