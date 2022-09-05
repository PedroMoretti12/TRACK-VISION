# Team 10: TrackVision -  Felipe Pires RA:03221051 | Isabela Hantke RA:03221007 | Rafaela Dias RA:03221050 | Verônica Zibord RA:03221003 | Vitor Macauba RA:03221002

import psutil
import time
import mysql.connector
import datetime
from datetime import date
import platform

try:

    conn = mysql.connector.connect(
        host='localhost', user='root', password='#Gf44844181858', database='trackvision')
    print("Conexão ao banco estabelecida!")

    fkCaixa = int(input("Informe o código do caixa: "))
    fkUsuario = int(input("Informe o seu código de usuário: "))
    print("\n")
    cursor = conn.cursor()
    inicioSegundos = 1

    while True:
        cpuPercent = psutil.cpu_percent(interval=1, percpu=False)
        ramPorcentagem = psutil.virtual_memory().percent
        discoUsado = psutil.disk_usage("C:\\").percent
        ultimaLeitura = datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')

        sql = "INSERT INTO leitura (fkCaixa, fkUsuario, processadorPorcentagem, memoriaRAM, disco, ultimaLeitura) VALUES (%s, %s, %s, %s, %s, (SELECT Now()))"
        values = [fkCaixa, fkUsuario, cpuPercent, ramPorcentagem, discoUsado]
        cursor.execute(sql, values)
        conn.commit()
        sopera = platform.system()

        print(ultimaLeitura)
        print("Sistema operacional utilizado: ", sopera)
        print(inicioSegundos, "Captura(s) de dados inserida(s).")
        inicioSegundos += 1
        time.sleep(5.0)

        if cpuPercent >= 0 and cpuPercent < 5:
            print('Baixo Uso')
            print("\n")
        elif cpuPercent >= 5 and cpuPercent < 10:
            print('Uso estável')
            print("\n")
        elif cpuPercent >= 10:
            print('Alto Uso')
            print("\n")
        else:
            print('--')
            print("\n")

except:
    print("Houve um erro ao conectar-se ao banco.")
