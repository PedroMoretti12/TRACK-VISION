import psutil
import time
import mysql.connector
from mysql.connector import errorcode
import datetime
from datetime import date

try:
    conn = mysql.connector.connect(
    host= 'localhost', user= 'root', password= '#Gf44844181858', database= 'trackvision')
    print("Conexão ao banco estabelecida!")

    fk_caixa = int(input("Informe o caixa: "));
    fk_usuario = int(input("Informe o usuário: "));
    cursor = conn.cursor()
    inicio_segundos = 1

    while True: 
        ram_porcentagem = psutil.virtual_memory().percent
        cpu_percent = psutil.cpu_percent(interval=1, percpu=False)
        disco_usado = psutil.disk_usage("C:\\").percent
        ultimaLeitura = datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')

        sql = "INSERT INTO leitura (fkCaixa, fkUsuario, processadorPorcentagem, memoriaRAM, disco, ultimaLeitura) VALUES (%s, %s, %s, %s, %s, (SELECT Now()))"
        values = [fk_caixa, fk_usuario, cpu_percent, ram_porcentagem, disco_usado]
        cursor.execute(sql, values)
        conn.commit()
        
        print(ram_porcentagem)
        print(ultimaLeitura)
        print(inicio_segundos, "Captura de dados inserida!")
        print("\n")
        inicio_segundos += 1
        time.sleep(60)
        

except:
    print("Houve um erro ao se conectar com o banco")

    # Track Vision - Team 10

    # Felipe Pires, Isabela Hantke, Rafaela Dias, Verônica Zibordi, Vitor Macauba 