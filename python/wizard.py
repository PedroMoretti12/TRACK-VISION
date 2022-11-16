import os
import sys

sopera = sys.platform.lower()
print(sopera)


command = "where python"
resposta = os.popen(command).read()
print(resposta)
command = "cd " + resposta.replace("\python.exe","")
caminho = os.popen(command).read()
command = "dir"
listar = os.popen(command).read()
command = "curl -sSL https://bootstrap.pypa.io/get-pip.py -o get-pip.py"
baixarpip = os.popen(command).read()
command = "dir"
listar = os.popen(command).read()
command = "py get-pip.py"
executarPython = os.popen(command).read()

print(caminho)
print(command)
print(listar)
