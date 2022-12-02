import mysql.connector
import datetime
from datetime import date
from datetime import datetime
import time
import tkinter
from tkinter import *

conn = mysql.connector.connect(user='aluno',password='sptech',database='trackvision',port='3306')
cursor = conn.cursor()

janela = Tk()
janela.title("Cadastro dos caixa")
janela.geometry('350x240')

# Função cadastrar --------------------------------
def Cadastrar():
  numSerial = Entry_numSerial.get()
  dataCompra = Entry_dataCompra.get()

  texto_resposta['text'] = 'Dados cadastrados com sucesso' 

  print(numSerial, dataCompra)

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

if(Cadastrar == ""): 
  texto_resposta['text'] = 'Os campos devem ser cadastrados'

# else:    
#   syntax = "insert into Caixa (fkBanco, fkAgencia, numeroSerial, dataCompra) values(1,1,%s,%s)"
#   values = [numSerial,dataCompra]
#   cursor.execute(syntax,values)
#   conn.commit()
#   cursor.execute("select dataCompra from Caixa")


# # Formatação das datas
# dataAtual = date.today()
# data = cursor.fetchall()
# i = len(data)

# dataCaixa = datetime.strptime(data[i - 1][0],'%d/%m/%Y').date() 

# # Calculo da quantidade de dias
# dias = (dataAtual - dataCaixa)    
# print(dias.days)

# # Calculo de vida útil
# vidaUtil = 5 * (24 * dias.days)

# # Temporizador
# print("A vida útil do caixa é de", vidaUtil, "HRs")

# syntax = "update Caixa set vidaUtil = %s where id in (select id from (select id from Caixa order by id desc limit 1) as t);"
# values = [vidaUtil]
# cursor.execute(syntax,values)
# conn.commit()
# cursor.execute("select vidaUtil from Caixa")
# print("Dado atualizado com sucesso!")

janela.mainloop()
