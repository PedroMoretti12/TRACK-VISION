# Team 10: TrackVision -  Felipe Pires RA:03221051 | Isabela Hantke RA:03221007 | Rafaela Dias RA:03221050 | Verônica Zibord RA:03221003 | Vitor Macauba RA:03221002

import psutil
import time
import mysql.connector
import datetime
import platform

try:
    conn = mysql.connector.connect(
        host='localhost', user='root', password='#Gf49535932861', database='trackvision')
    print("Conexão ao banco estabelecida!")
except:
    print("Houve um erro ao conectar-se ao banco.")

#fkCaixa = int(input("Informe o código do caixa: "))
fkAgencia = int(input("Informe o seu código da sua Agência: "))

fkCaixa = 100
fkCaixa2 = 101
fkCaixa3 = 102

print("\n")
cursor = conn.cursor()
inicioSegundos = 0

while True:
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

    for computador in maquinas:
        sql = "INSERT INTO leitura (fkBanco, fkAgencia, fkCaixa, cpuPorcentagem, ramPorcentagem, hdPorcentagem, momento) VALUES (1, 1, 1, %s, %s, %s, (SELECT Now()))"
        values = [computador[1], computador[2], computador[3]]
        cursor.execute(sql, values)
        conn.commit()
        sopera = platform.system()

        print("-"*30)
        print(momento)
        print("Sistema operacional utilizado: ", sopera)
        inicioSegundos += 1
        print(inicioSegundos, "Captura(s) de dados inserida(s).")

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

        print("-"*30)
        print("\n")
        time.sleep(3.0)
