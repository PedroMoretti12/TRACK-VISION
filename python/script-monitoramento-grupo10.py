

import pyodbc
import psutil
import time
import datetime
import platform
import matplotlib.pyplot
import matplotlib.pyplot as plt
import sys,os



server = 'trackvisiondb.database.windows.net'
database = 'trackvisiondb'
username = 'CloudSA49c766d4'
password = 'Urubu1004'
driver= '{ODBC Driver 18 for SQL Server}'

conn = pyodbc.connect('DRIVER='+driver+';'
                          'SERVER=tcp:'+server+';'
                          'PORT=1433;'
                          'DATABASE='+database+';'
                          'UID='+username+';'
                          'PWD='+ password)

cursor = conn.cursor()

#fkCaixa = int(input("Informe o código do caixa: "))
fkAgencia = int(input("Informe o seu código da sua Agência: "))


fkCaixa = 1
fkCaixa2 = 31
fkCaixa3 = 41
#Vetores
dados_cpu = []
dados_cpu2 = []
dados_cpu3 = []
dados_hd = []
dados_ram = []
medias_cpu = []
medida = []
medidaMaquina = []
i = 0
soma_cpu = 0
soma_cpu2 = 0
soma_cpu3 = 0

 
inicioSegundos = 0


       

while (i < 5):
    cpuPorcentagem = psutil.cpu_percent(interval=1, percpu=False)
    ramPorcentagem = psutil.virtual_memory().percent
    hdPorcentagem = psutil.disk_usage('/').percent
    momento = datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')

    cpuPorcentagem2 = (round(cpuPorcentagem * 1.05, 1)) if (cpuPorcentagem * 1.05 < 100) else 100
    cpuPorcentagem3 = (round(cpuPorcentagem * 1.15, 1)) if (cpuPorcentagem * 1.15 < 100) else 100

    ramPorcentagem2 = (round(ramPorcentagem * 0.90, 1)
                       ) if (ramPorcentagem * 1.05 < 100) else 100
    ramPorcentagem3 = (round(ramPorcentagem * 0.50, 1)
                       ) if (ramPorcentagem * 1.05 < 100) else 100

    hdPorcentagem2 = (round(hdPorcentagem * 0.95, 1)
                   ) if (cpuPorcentagem * 1.05 < 100) else 100
    hdPorcentagem3 = (round(hdPorcentagem * 0.33, 1)
                   ) if (cpuPorcentagem * 1.05 < 100) else 100
    

    maquinas = [
        [fkCaixa, cpuPorcentagem, ramPorcentagem, hdPorcentagem],
        [fkCaixa2, cpuPorcentagem2, ramPorcentagem2, hdPorcentagem2],
        [fkCaixa3, cpuPorcentagem3, ramPorcentagem3, hdPorcentagem3],
    ]

    i+=1
    nmrmedida = str(i)
    medida.append(nmrmedida)
    
    dados_cpu.append(maquinas[0][1])
    dados_cpu2.append(maquinas[1][1])
    dados_cpu3.append(maquinas[2][1])
    dados_hd.append(maquinas[0][3])
    dados_ram.append(maquinas[0][2])
    print(dados_cpu)
    soma_cpu += maquinas[0][1]
    soma_cpu2 += maquinas[1][1]
    soma_cpu3 += maquinas[2][1]
    print(soma_cpu,soma_cpu2,soma_cpu3)
    media_cpu = round ((soma_cpu/len(dados_cpu)/3),2)
    media_cpu2 = round ((soma_cpu2/len(dados_cpu2)/3),2)
    media_cpu3 = round ((soma_cpu3/len(dados_cpu3)/3),2)
    ai = [media_cpu,media_cpu2,media_cpu3]
        
    
    for count, computador in enumerate(maquinas):
        sql = "INSERT INTO Leitura (fkBanco, fkAgencia, fkCaixa, cpuPorcentagem, ramPorcentagem, hdPorcentagem, momento) VALUES (1, 1, ?, ?, ?, ?, (GETDATE()))"
        print(computador[0], computador[1], computador[2], computador[3])
        values = [computador[0], computador[1], computador[2], computador[3]]
        cursor.execute(sql, values)
        cursor.commit()
        sopera = platform.system()

        
#criar variável média pegar a doma e dividir pela length, jogar em um vetor e depois executar o gráfico
        print("-"*30)
        print(momento)
        print("Sistema operacional utilizado: ", sopera)
        print(i, "Captura(s) de dados inserida(s).")

        if computador[1] < 30:
            print('CPU: Baixo uso.')
        elif computador[1] < 70:
            print('CPU: Uso médio (estável).')
        else:
            print('CPU: Alto uso, pode ser um risco!')

        if computador[2] < 30:
            print('Memória RAM: Baixo uso, há bastante espaço livre!')
        elif computador[2] < 70:
            print('Memória RAM: Uso médio (estável).')
        else:
            print('Memória RAM: Alto uso, pode ser um risco!')

        if computador[3] < 30:
            print('Disco: Baixo uso, há bastante espaço livre!')
        elif computador[3] < 70:
            print('Disco: Uso médio (estável).')
        else:
            print('Disco: Alto uso, pode ser um risco!')
            
matplotlib.pyplot.title('Porcentagem de uso da CPU')
matplotlib.pyplot.xlabel('Numero de Identificação do Dado')
matplotlib.pyplot.ylabel('Porcentagem')
matplotlib.pyplot.plot(medida, dados_cpu)
matplotlib.pyplot.ylim(0, 100)
matplotlib.pyplot.show()
dados_cpu = []

print("-"*30)
print("\n")

matplotlib.pyplot.title('Porcentagem de uso da RAM')
matplotlib.pyplot.xlabel('Numero de Identificação do Dado')
matplotlib.pyplot.ylabel('Porcentagem')
matplotlib.pyplot.plot(medida, dados_ram)
matplotlib.pyplot.ylim(0, 100)
matplotlib.pyplot.show()
dados_ram = []

print("-"*30)
print("\n")
        
matplotlib.pyplot.title('Porcentagem de uso do HD')
matplotlib.pyplot.xlabel('Numero de Identificação do Dado')
matplotlib.pyplot.ylabel('Porcentagem')
matplotlib.pyplot.plot(medida, dados_hd)
matplotlib.pyplot.ylim(0, 100)
matplotlib.pyplot.show()
dados_hd = []
medida = []

print("-"*30)
print("\n")

medias_cpu.append(ai)
print(medias_cpu)
x=[fkCaixa,fkCaixa2,fkCaixa3]
plt.bar(x, medias_cpu[0] , color ='yellow',
        width = 0.4) 
plt.xlabel("Id Caixa")
plt.ylabel("Porcentagem de média")
plt.title("Média de uso da CPU por máquina")
plt.ylim(0, 100)
plt.show()
medias_cpu=[]

print("\n")            

print("-"*30)
print("\n")
        
time.sleep(3.0)
