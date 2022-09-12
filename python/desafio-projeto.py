# Grupo 10: TrackVision
# Felipe Pires | 03221051
# Isabela Hantke | 03221007
# Rafaela Dias | 03221050
# Verônica Zibord | 03221003
# Vitor Macauba | 03221002

import psutil
import time
from prettytable import PrettyTable

while True:

    tabela1 = PrettyTable()
    tabela1.field_names = ["1-Cpu", "1-Memória", "1-Disco",
                           "2-Cpu", "2-Memória", "2-Disco",
                                    "3-Cpu", "3-Memória", "3-Disco"]

    cpu1 = psutil.cpu_percent(interval=1, percpu=False)
    memo1 = psutil.virtual_memory().percent
    disc1 = psutil.disk_usage("C:\\").percent

    cpu2 = round(cpu1 + 10 if (cpu1 <= 90) else 100, 2)
    memo2 = round(memo1 + 15 if (memo1 <= 85) else 100, 2)
    disc2 = round(disc1 - 5 if (disc1 >= 5) else 0, 2)

    cpu3 = round(cpu2 + 5 if (cpu2 <= 95) else 100, 2)
    memo3 = round(memo2 - 5, 2)
    disc3 = round(disc2 * 3 if (disc2 * 3 <= 100) else 100, 2)

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

    print(tabela1)
    print("\n\n")

    time.sleep(5)
