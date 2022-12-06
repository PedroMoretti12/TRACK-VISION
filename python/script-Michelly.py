from json import loads
from time import sleep
from tokenize import String
from urllib3 import PoolManager
import datetime
from datetime import datetime
import psutil
import mysql.connector
import time
import os
from mysql.connector import errorcode
import pyodbc
import textwrap

server = 'trackvisiondb.database.windows.net'
database = 'trackvisiondb'
username = 'CloudSA49c766d4'
password = 'Urubu1004'
driver = '{ODBC Driver 18 for SQL Server}'
try:
    conn = pyodbc.connect('DRIVER='+driver+';'
                      'SERVER=tcp:'+server+';'
                      'PORT=1433;'
                      'DATABASE='+database+';'
                       'UID='+username+';'
                                                                                                 'PWD='+ password)
    cursor = conn.cursor()
    # trackvision_bd = mysql.connector.connect(
    #     host = 'localhost', user = 'MichellyMendes', password = 'Urubu100', database = 'Track_vision')

except mysql.connector.Error as error:
    if error.errno == errorcode.ER_BAD_DB_ERROR:
        print("Erro no banco")
    elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Falha na credencial")
    else:
        print(error)
    # CPU
    # print (psutil.cpu_percent(1))


while (True):
    def conversor(valor):
        return float(valor[0:4].replace(",", "."))

    with PoolManager() as pool:
        while True:
            for rep in range(3):
                rep = rep + 1
                rep = rep - 1
                response = pool.request(
                    'GET', 'http://localhost:8085/data.json')
                data = loads(response.data.decode('utf-8'))

                min_caixa1 = conversor(
                    data['Children'][0]['Children'][0]['Children'][1]['Children'][0]['Min'])
                med_caixa1 = conversor(
                    data['Children'][0]['Children'][0]['Children'][1]['Children'][0]['Value'])
                max_caixa1 = conversor(
                    data['Children'][0]['Children'][0]['Children'][1]['Children'][0]['Max'])

                cpuPorcentagem = psutil.cpu_percent(interval=1, percpu=False)

                cursorAzure = cursor

                # min_caixa2 = conversor(data['Children'],[0]['Children'][1]['Children'][1]['Children'][0]['Min'])
                # med_caixa2 = conversor(data['Children'],[0]['Children'][1]['Children'][1]['Children'][0]['Value'])
                # max_caixa2 = conversor(data['Children'],[0]['Children'][1]['Children'][1]['Children'][0]['Max'])

                hora = datetime.now().strftime('%H:%M:%S')
                data = datetime.now().strftime('%Y-%m-%d')

                fkCaixa = 1

                sql = (
                    f"insert into Proj_Michelly (hora, data_data, cpuPorcentagem, tempCpuMin, tempCpuMed, tempCpuMax, fkCaixa) VALUES ('{hora}', '{data}', {cpuPorcentagem}, {min_caixa1},{med_caixa1}, {max_caixa1}, {fkCaixa});")

                cursorAzure.execute(sql)
                conn.commit()

            print(cursorAzure.rowcount, "Inseriu no Banco")
            print("momento:", hora, data, "Temperatura min", min_caixa1)
            print("momento:", hora, data, "Temperatura med", med_caixa1)
            print("momento:", hora, data, "Temperatura max", max_caixa1)
            time.sleep(3)
