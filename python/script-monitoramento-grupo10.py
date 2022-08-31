# Team 10: TrackVision -  Felipe Pires RA:03221051 | Isabela Hantke RA:03221007 | Rafaela Dias RA:03221050 | Verônica Zibord RA:03221003 | Vitor Macauba RA:03221002

import psutil
import time
import mysql.connector
import datetime
from datetime import date

try:

    conn = mysql.connector.connect(
        host='localhost', user='Ella', password='urubu100', database='trackvision')
    print("Conexão ao banco estabelecida!")

    fkCaixa = int(input("Informe o código do caixa: "))
    fkUsuario = int(input("Informe o seu código de usuário: "))
    cursor = conn.cursor()
    inicioSegundos = 1

    while True:
        ramPorcentagem = psutil.virtual_memory().percent
        cpuPercent = psutil.cpu_percent(interval=1, percpu=False)
        discoUsado = psutil.disk_usage("C:\\").percent
        ultimaLeitura = datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')

        sql = "INSERT INTO leitura (fkCaixa, fkUsuario, processadorPorcentagem, memoriaRAM, disco, ultimaLeitura) VALUES (%s, %s, %s, %s, %s, (SELECT Now()))"
        values = [fkCaixa, fkUsuario, cpuPercent, ramPorcentagem, discoUsado]
        cursor.execute(sql, values)
        conn.commit()

        print(ultimaLeitura)
        print(inicioSegundos, "Captura(s) de dados inserida(s).")
        print("\n")
        inicioSegundos += 1
        time.sleep(5.0)

except:
    print("Houve um erro ao conectar-se ao banco.")
