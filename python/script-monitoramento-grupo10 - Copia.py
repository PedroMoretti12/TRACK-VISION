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

try:
        trackvision_bd = mysql.connector.connect(
            host = 'localhost', user = 'MichellyMendes', password = 'Urubu100', database = 'Trackvision')

except mysql.connector.Error as error:
    if error.errno == errorcode.ER_BAD_DB_ERROR:
        print("Erro no banco")
    elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:   
        print("Falha na credencial")
    else:
        print(error)    

while (True):
    def conversor(valor):
        return float (valor[0:4].replace(",","."))

    def leitura(trackvision_bd):
        cursorLocal = trackvision_bd.cursor()

    with PoolManager() as pool:
        while True:
            for rep in range(3):
                rep = rep + 1
                rep = rep - 1
                response = pool.request('GET', 'http://localhost:8085/data.json')
                data = loads(response.data.decode('utf-8'))

                min_caixa1 = conversor(data['Children'][0]['Children'][1]['Children'][1]['Children'][0]['Min'])
                med_caixa1 = conversor(data['Children'][0]['Children'][1]['Children'][1]['Children'][0]['Value'])
                max_caixa1 = conversor(data['Children'][0]['Children'][1]['Children'][1]['Children'][0]['Max'])

                cursorLocal = trackvision_bd.cursor()

                # min_caixa2 = conversor(data['Children'],[0]['Children'][1]['Children'][1]['Children'][0]['Min'])
                # med_caixa2 = conversor(data['Children'],[0]['Children'][1]['Children'][1]['Children'][0]['Value'])
                # max_caixa2 = conversor(data['Children'],[0]['Children'][1]['Children'][1]['Children'][0]['Max'])

                # min_caixa3 = conversor(data['Children'],[0]['Children'][1]['Children'][1]['Children'][0]['Min'])
                # med_caixa3 = conversor(data['Children'],[0]['Children'][1]['Children'][1]['Children'][0]['Value'])
                # max_caixa3 = conversor(data['Children'],[0]['Children'][1]['Children'][1]['Children'][0]['Max'])

                hora = datetime.now().strftime('%H:%M:%S')
                data = datetime.now().strftime('%Y-%m-%d')
                fkCaixa = 100
                sql = (f"insert into Proj_Michelly (hora, data_data, tempCpuMin, tempCpuMed, tempCpuMax, fkCaixa) VALUES ('{hora}', '{data}', {min_caixa1},{med_caixa1}, {max_caixa1}, {fkCaixa});")
           
                cursorLocal.execute(sql)

            print(cursorLocal.rowcount, "Inseriu no Banco")
            print("momento:",hora,data, "Temperatura", med_caixa1)
            trackvision_bd.commit()
            time.sleep(3)
