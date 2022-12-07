import pyodbc
from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import random
import matplotlib.pyplot as plt
from scipy import stats
import pandas as pd
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import dash_bootstrap_components as dbc

external_stylesheets = [dbc.themes.BOOTSTRAP]

conexao = False
try:
    server = 'trackvisiondb.database.windows.net'
    database = 'trackvisiondb'
    username = 'CloudSA49c766d4'
    password = 'Urubu1004'
    driver = '{ODBC Driver 18 for SQL Server}'

    conn = pyodbc.connect('DRIVER=' + driver + ';'
                           'SERVER=tcp:' + server + ';'
                           'PORT=1433;'
                           'DATABASE=' + database + ';'
                           'UID=' + username + ';'
                           'PWD=' + password)

    cursor = conn.cursor()
    conexao = True
except:
    pass

'''
Código da captura de dados do dia.
'''
verifica_diario = False
cursor.execute("SELECT TOP(24) cpuPorcentagem FROM [dbo].[Leitura] WHERE FORMAT(momento, 'dd') = FORMAT(DATEADD(DAY, -1 , GETDATE()), 'dd') ORDER BY id DESC;")
row = cursor.fetchall()
cpu_diario = []
if len(row) == 24:
    print("24 Dados do dia anterior capturados.")
    verifica_diario = True
    for x in range(len(row)):
        cpu_diario.append(row[x][0])
else:
    cpu_diario = []
    cursor.execute("SELECT TOP(24) cpuPorcentagem FROM Leitura ORDER BY id DESC;")
    row = cursor.fetchall()
    print("Não existem 24 dados no dia anterior, pegando os últimos 24 dados registrados.")
    for x in range(len(row)):
        cpu_diario.append(row[x][0])

'''

'''
cursor.execute("SELECT TOP(24) ramPorcentagem FROM [dbo].[Leitura] WHERE FORMAT(momento, 'dd') = FORMAT(DATEADD(DAY, -1 , GETDATE()), 'dd') ORDER BY id DESC;")
row = cursor.fetchall()

ram_diario = []
if len(row) == 24:
    print("24 Dados do dia anterior capturados.")
    for x in range(len(row)):
        ram_diario.append(row[x][0])
else:
    cursor.execute("SELECT TOP(24) ramPorcentagem FROM Leitura ORDER BY id DESC;")
    row = cursor.fetchall()
    print("Não existem 24 dados no dia anterior, pegando os últimos 24 dados registrados.")
    for x in range(len(row)):
        ram_diario.append(row[x][0])

cursor.execute("SELECT TOP(24) hdPorcentagem FROM [dbo].[Leitura] WHERE FORMAT(momento, 'dd') = FORMAT(DATEADD(DAY, -1 , GETDATE()), 'dd') ORDER BY id DESC;")
row = cursor.fetchall()
'''

'''
hd_diario = []

if len(row) == 24:
    print("24 Dados do dia anterior capturados.")
    for x in range(len(row)):
        hd_diario.append(row[x][0])
else:
    cursor.execute("SELECT TOP(24) hdPorcentagem FROM Leitura ORDER BY id DESC;")
    row = cursor.fetchall()
    print("Não existem 24 dados no dia anterior, pegando os últimos 24 dados registrados.")
    for x in range(len(row)):
        hd_diario.append(row[x][0])

'''
Código da captura de dados da semana.
'''
cpu_semanal = []
ram_semanal = []
hd_semanal = []
vetor = [-7, -6, -5, -4, -3, -2, -1]

for i in range(7):
    mensagem = "SELECT AVG(cpuPorcentagem) AS DECIMAL FROM Leitura WHERE FORMAT(momento, 'dd') = FORMAT(DATEADD(DAY, ?, GETDATE()), 'dd')"
    valor = vetor[i]
    cursor.execute(mensagem, valor)
    dado = cursor.fetchall()
    try:
        dado_refinado = dado[0][0]
    except:
        dado_refinado = []
    cpu_semanal.append(dado_refinado)

print("Dados semanais da CPU capturados.")

for i in range(7):
    mensagem = "SELECT AVG(ramPorcentagem) FROM Leitura WHERE FORMAT(momento, 'dd') = FORMAT(DATEADD(DAY, ?, GETDATE()), 'dd')"
    valor = vetor[i]
    cursor.execute(mensagem, valor)
    dado = cursor.fetchall()
    try:
        dado_refinado = dado[0][0]
    except:
        dado_refinado = []
    ram_semanal.append(dado_refinado)

print("Dados semanais da RAM capturados.")

for i in range(7):
    mensagem = "SELECT AVG(hdPorcentagem) FROM Leitura WHERE FORMAT(momento, 'dd') = FORMAT(DATEADD(DAY, ?, GETDATE()), 'dd')"
    valor = vetor[i]
    cursor.execute(mensagem, valor)
    dado = cursor.fetchall()
    try:
        dado_refinado = dado[0][0]
    except:
        dado_refinado = []
    hd_semanal.append(dado_refinado)

print("Dados semanais do HD capturados.")
'''
Código da captura de dados do mês.
'''
cpu_mensal = []
ram_mensal = []
hd_mensal = []
vetor = [-30, -29, -28, -27, -26, -25, -24, -23, -22, -21, -20, -19, -18, -17, -16, -15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1]

for i in range(30):
    mensagem = "SELECT AVG(cpuPorcentagem) FROM Leitura WHERE FORMAT(momento, 'dd') = FORMAT(DATEADD(DAY, ?, GETDATE()), 'dd')"
    valor = vetor[i]
    cursor.execute(mensagem, valor)
    dado = cursor.fetchall()
    try:
        dado_refinado = dado[0][0]
    except:
        dado_refinado = []
    cpu_mensal.append(dado_refinado)

print("Dados Mensais da CPU capturados.")

for i in range(30):
    mensagem = "SELECT AVG(ramPorcentagem) FROM Leitura WHERE FORMAT(momento, 'dd') = FORMAT(DATEADD(DAY, ?, GETDATE()), 'dd')"
    valor = vetor[i]
    cursor.execute(mensagem, valor)
    dado = cursor.fetchall()
    try:
        dado_refinado = dado[0][0]
    except:
        dado_refinado = []
    ram_mensal.append(dado_refinado)

print("Dados Mensais da RAM capturados.")

for i in range(30):
    mensagem = "SELECT AVG(hdPorcentagem) FROM Leitura WHERE FORMAT(momento, 'dd') = FORMAT(DATEADD(DAY, ?, GETDATE()), 'dd')"
    valor = vetor[i]
    cursor.execute(mensagem, valor)
    dado = cursor.fetchall()
    try:
        dado_refinado = dado[0][0]
    except:
        dado_refinado = []
    hd_mensal.append(dado_refinado)

print("Dados Mensais do HD capturados.")

'''
Parte de confiabilidade do código. 
'''

print("\nPreenchendo quaisquer campos vazios + Cálculo de confiabilidade.")

medida_confiavel_cpu_mensal = 0
medida_confiavel_cpu_semanal = 0
confiabilidade_diario = 0.0
confiabilidade_semanal = 0.0
confiabilidade_mensal = 0.0

if verifica_diario:
    confiabilidade_diario = 100.0
else:
    confiabilidade_diario = 0.0

print("Confiabilidade diária: ", confiabilidade_diario, "%")

for i in range(len(cpu_semanal)):
    try:
        test = 1 + cpu_semanal[i]
        medida_confiavel_cpu_semanal += 1
    except:
        cpu_semanal[i] = round(random.randint(25, 75), 2)

for i in range(len(ram_semanal)):
    try:
        test = 1 + ram_semanal[i]
    except:
        ram_semanal[i] = round(random.randint(25, 75), 2)

for i in range(len(hd_semanal)):
    try:
        test = 1 + hd_semanal[i]
    except:
        hd_semanal[i] = round(random.randint(25, 75), 2)

confiabilidade_semanal = round((medida_confiavel_cpu_semanal/7)*100, 2)
print("Confiabilidade semanal: ", confiabilidade_semanal, "%")

for i in range(len(cpu_mensal)):
    try:
        test = 1 + cpu_mensal[i]
        medida_confiavel_cpu_mensal += 1
    except:
        cpu_mensal[i] = round(random.randint(25, 75), 2)

for i in range(len(ram_mensal)):
    try:
        test = 1 + ram_mensal[i]
    except:
        ram_mensal[i] = round(random.randint(25, 75), 2)

for i in range(len(hd_mensal)):
    try:
        test = 1 + hd_mensal[i]
    except:
        hd_mensal[i] = round(random.randint(25, 75), 2)


confiabilidade_mensal = round((medida_confiavel_cpu_mensal/30)*100,2)
print("Confiabilidade mensal: ", confiabilidade_mensal, "%")

'''
Códigos da parte gráfica da aplicação.
'''

'''
DIA
'''

df = pd.DataFrame({
    "Horas do dia": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24],
    "Porcentagem da cpu": cpu_diario
})

fig = px.scatter(df, x="Horas do dia", y="Porcentagem da cpu", trendline="ols")

df = pd.DataFrame({
    "Horas do dia": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24],
    "Porcentagem da ram": ram_diario
})

fig2 = px.scatter(df, x="Horas do dia", y="Porcentagem da ram", trendline="ols")

df = pd.DataFrame({
    "Horas do dia": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24],
    "Porcentagem do hd": hd_diario
})

fig3 = px.scatter(df, x="Horas do dia", y="Porcentagem do hd", trendline="ols")

'''
SEMANA
'''

df = pd.DataFrame({
    "Dias da semana": [1, 2, 3, 4, 5, 6, 7],
    "Porcentagem da cpu": cpu_semanal
})

fig4 = px.scatter(df, x="Dias da semana", y="Porcentagem da cpu", trendline="ols")

df = pd.DataFrame({
    "Dias da semana": [1, 2, 3, 4, 5, 6, 7],
    "Porcentagem da ram": ram_semanal
})

fig5 = px.scatter(df, x="Dias da semana", y="Porcentagem da ram", trendline="ols")

df = pd.DataFrame({
    "Dias da semana": [1, 2, 3, 4, 5, 6, 7],
    "Porcentagem do hd": hd_semanal
})

fig6 = px.scatter(df, x="Dias da semana", y="Porcentagem do hd", trendline="ols")

'''
MENSAL
'''

df = pd.DataFrame({
    "Dias do mês": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
    "Porcentagem da cpu": cpu_mensal
})

fig7 = px.scatter(df, x="Dias do mês", y="Porcentagem da cpu", trendline="ols")

df = pd.DataFrame({
    "Dias do mês": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
    "Porcentagem da ram": ram_mensal
})

fig8 = px.scatter(df, x="Dias do mês", y="Porcentagem da ram", trendline="ols")

df = pd.DataFrame({
    "Dias do mês": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
    "Porcentagem do hd": hd_mensal
})

fig9 = px.scatter(df, x="Dias do mês", y="Porcentagem do hd", trendline="ols")

df = pd.DataFrame({
    "Tipo": ["Diária", "Semanal", "Mensal"],
    "Dado": [confiabilidade_diario, confiabilidade_semanal, confiabilidade_mensal]
})

fig10 = px.bar(df, x="Tipo", y="Dado")

app = Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = dbc.Container([
    html.A("Voltar para o dashboard padrão.", href="http://localhost:8080/dashboardTecnico", style={"margin-top": "50px", "text-align": "center", "color": "orange"}),
    html.H1("Regressão Linear dos dados bancários de suas agências", style={"margin-top": "50px", "text-align": "center"}),
    html.H3("% Confiabilidade dos dados", style={"margin-top": "50px", "text-align": "center"}),
    dbc.Row([
        dbc.Col([
            dcc.Graph(figure=fig10)
        ])
    ]),
    html.H1("Dados diários", style={"margin-top": "50px", "text-align": "center", "border-bottom": "solid 10px orange"}),
    dbc.Row([
        dbc.Col([
            html.H3("Porcentagem do HD", style={"margin-top": "50px", "text-align": "center"}),
            dcc.Graph(figure=fig3)
        ], width=6),
        dbc.Col([
            html.H3("Porcentagem da RAM", style={"margin-top": "50px", "text-align": "center"}),
            dcc.Graph(figure=fig2)
        ], width=6)
    ]),
    dbc.Row([
        dbc.Col([
            html.H3("Porcentagem da CPU", style={"margin-top": "50px", "text-align": "center"}),
            dcc.Graph(figure=fig)
        ])
    ]),
    html.H1("Dados semanais", style={"margin-top": "50px", "text-align": "center", "border-bottom": "solid 10px orange"}),
    html.Div(id='output2'),
    dbc.Row([
        dbc.Col([
            html.H3("Porcentagem do HD", style={"margin-top": "50px", "text-align": "center"}),
            dcc.Graph(figure=fig6)
        ], width=6),
        dbc.Col([
            html.H3("Porcentagem da RAM", style={"margin-top": "50px", "text-align": "center"}),
            dcc.Graph(figure=fig5)
        ], width=6)
    ]),
    dbc.Row([
        dbc.Col([
            html.H3("Porcentagem da CPU", style={"margin-top": "50px", "text-align": "center"}),
            dcc.Graph(figure=fig4)
        ])
    ]),
    html.H1("Dados mensais", style={"margin-top": "50px", "text-align": "center", "border-bottom": "solid 10px orange"}),
    html.Div(id='output3'),
    dbc.Row([
        dbc.Col([
            html.H3("Porcentagem do HD", style={"margin-top": "50px", "text-align": "center"}),
            dcc.Graph(figure=fig9)
        ], width=6),
        dbc.Col([
            html.H3("Porcentagem da RAM", style={"margin-top": "50px", "text-align": "center"}),
            dcc.Graph(figure=fig8)
        ], width=6)
    ]),
    dbc.Row([
        dbc.Col([
            html.H3("Porcentagem da CPU", style={"margin-top": "50px", "text-align": "center"}),
            dcc.Graph(figure=fig7)
        ])
    ])
])

app.run(host='0.0.0.0',debug=True, port=8008)