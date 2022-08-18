import psutil
import time


def exibir_cpu_times():
    inicio_segundos = 0
    while True:
        cpu_percent = psutil.cpu_percent(interval=1, percpu=True)
        count = 0
        while (count < len(cpu_percent)):
           print("CPU",[count+1],": ",cpu_percent[count], "%\n")
           count = count + 1
        print("Memória RAM utilizada: {:.3f}".format(psutil.virtual_memory().used / 1000000000), "GB\n")
        print("Disco: {:.3f}".format(psutil.disk_usage("C:\\") [2] /1000000000), "GB\n")
        inicio_segundos = inicio_segundos + 1
        time.sleep(30)

exibir_cpu_times()