#Grupo 10: Track Vision

#Felipe Pires | RA: 03221051
#Isabela Hantke | RA: 03221007
#Rafaela Dias | RA: 03221050
#Verônica Zibord | RA: 03221003
#Vitor Macauba | RA: 03221002

import psutil
import time
from prettytable import PrettyTable # importando uma biblioteca de tabelas 

print('-' * 90) # Linha para separar uma leitura da outra 
   
while True:

    tabela1 = PrettyTable() # Criação da tabela 1, com os dados da CPU1 como principal 
    tabela1.field_names = ["1-Cpu", "1-Memória", "1-Disco", "2-Cpu", "2-Memória", "2-Disco", "3-Cpu", "3-Memória", "3-Disco"]

    # Dados de captura da CPU 1, MÉMORIA 1 e DISCO 1
    cpu1 = psutil.cpu_percent(interval=1, percpu=False)
    memo1 = psutil.virtual_memory().percent
    disc1 = psutil.disk_usage("C:\\").percent 

    # Dados de captura da CPU 2, MÉMORIA 2 e DISCO 2 
    cpu2 = round(cpu1 * 1.10, 2)
    memo2 = round(memo1 * 1.15, 2)
    disc2 = round(disc1 * 1.05, 2)

    # Dados de captura da CPU 3, MÉMORIA 3 e DISCO 3
    cpu3 = round(cpu1 * 0.95, 2)
    memo3 = round(memo1 * 1.05, 2)
    disc3 = round(disc1 * 0.3, 2)

    # Tabela de recebe od valores principais e o cálculo sobre as demais simulações referente a cpu, mémoria e disco 2 e 3
    tabela1.add_row(
        [cpu1,
        memo1,
        disc1,
        cpu2,
        memo2,
        disc2,
        cpu3,
        memo3,
        disc3]
    )

    print(tabela1) # Mostra os dados como em uma tabela de forma organizada e horizontal com tempo de 10seg entre uma leitura e outra 
    print("\n\n")

    time.sleep(30)




    
