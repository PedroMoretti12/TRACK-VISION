# Team 10: TrackVision -  Felipe Pires RA:03221051 | Isabela Hantke RA:03221007 | Rafaela Dias RA:03221050 | Verônica Zibord RA:03221003 | Vitor Macauba RA:03221002

import psutil
import time
import mysql.connector
import datetime
import platform

try:
    conn = mysql.connector.connect(
        host='localhost', user='root', password='#Gf44844181858', database='trackvision')
    print("Conexão ao banco estabelecida!")
except:
    print("Houve um erro ao conectar-se ao banco.")

#fkCaixa = int(input("Informe o código do caixa: "))
fkUsuario = int(input("Informe o seu código de usuário: "))

fkCaixa = 100
fkCaixa2 = 101
fkCaixa3 = 102

print("\n")
cursor = conn.cursor()
inicioSegundos = 0

while True:
    cpuPercent = psutil.cpu_percent(interval=1, percpu=False)
    ramPorcentagem = psutil.virtual_memory().percent
    discoUsado = psutil.disk_usage("C:\\").percent
    ultimaLeitura = datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')

    cpu2 = (round(cpuPercent * 1.05, 1)) if (cpuPercent * 1.05 < 100) else 100
    cpu3 = (round(cpuPercent * 1.15, 1)) if (cpuPercent * 1.15 < 100) else 100

    ramPorcentagem2 = (round(ramPorcentagem * 0.90, 1)
                       ) if (ramPorcentagem * 1.05 < 100) else 100
    ramPorcentagem3 = (round(ramPorcentagem * 0.50, 1)
                       ) if (ramPorcentagem * 1.05 < 100) else 100

    discoUsado2 = (round(discoUsado * 0.95, 1)
                   ) if (cpuPercent * 1.05 < 100) else 100
    discoUsado3 = (round(discoUsado * 0.33, 1)
                   ) if (cpuPercent * 1.05 < 100) else 100

    maquinas = [
        [fkCaixa, cpuPercent, ramPorcentagem, discoUsado],
        [fkCaixa2, cpu2, ramPorcentagem2, discoUsado2],
        [fkCaixa3, cpu3, ramPorcentagem3, discoUsado3]
    ]

    for computador in maquinas:
        sql = "INSERT INTO leitura (fkCaixa, fkUsuario, processadorPorcentagem, memoriaRAM, disco, ultimaLeitura) VALUES (%s, %s, %s, %s, %s, (SELECT Now()))"
        values = [computador[0], fkUsuario,
                  computador[1], computador[2], computador[3]]
        cursor.execute(sql, values)
        conn.commit()
        sopera = platform.system()

        print("-"*30)
        print(ultimaLeitura)
        inicioSegundos += 1
        print(inicioSegundos, "Captura(s) de dados inserida(s).")
        print("Sistema operacional utilizado: ", sopera)

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
        time.sleep(5.0)
