import pyodbc
from dash import Dash, dcc, html, Input, Output
import plotly.express as px

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
        cpu_diario.append(row[x][0])

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
        cpu_diario.append(row[x][0])

'''
Código da captura de dados da semana.
'''
cpu_semanal = []
ram_semanal = []
hd_semanal = []
vetor = [-7, -6, -5, -4, -3, -2, -1]

for i in range(7):
    mensagem = "SELECT TOP(1) cpuPorcentagem FROM Leitura WHERE FORMAT(momento, 'dd') = FORMAT(DATEADD(DAY, ?, GETDATE()), 'dd') ORDER BY id DESC"
    valor = vetor[i]
    cursor.execute(mensagem, valor)
    dado = cursor.fetchall()
    cpu_semanal.append(dado)

print("Dados semanais da CPU capturados.")

for i in range(7):
    mensagem = "SELECT TOP(1) ramPorcentagem FROM Leitura WHERE FORMAT(momento, 'dd') = FORMAT(DATEADD(DAY, ?, GETDATE()), 'dd') ORDER BY id DESC"
    valor = vetor[i]
    cursor.execute(mensagem, valor)
    dado = cursor.fetchall()
    ram_semanal.append(dado)

print("Dados semanais da RAM capturados.")

for i in range(7):
    mensagem = "SELECT TOP(1) hdPorcentagem FROM Leitura WHERE FORMAT(momento, 'dd') = FORMAT(DATEADD(DAY, ?, GETDATE()), 'dd') ORDER BY id DESC"
    valor = vetor[i]
    cursor.execute(mensagem, valor)
    dado = cursor.fetchall()
    hd_semanal.append(dado)

print("Dados semanais do HD capturados.")

'''
Código da captura de dados do mês.
'''

cpu_mensal = []
ram_mensal = []
hd_mensal = []
vetor = [-30, -29, -28, -27, -26, -25, -24, -23, -22, -21, -20, -19, -18, -17, -16, -15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1]

for i in range(30):
    mensagem = "SELECT TOP(1) cpuPorcentagem FROM Leitura WHERE FORMAT(momento, 'dd') = FORMAT(DATEADD(DAY, ?, GETDATE()), 'dd') ORDER BY id DESC"
    valor = vetor[i]
    cursor.execute(mensagem, valor)
    dado = cursor.fetchall()
    cpu_mensal.append(dado)

print("Dados Mensais da CPU capturados.")

for i in range(30):
    mensagem = "SELECT TOP(1) ramPorcentagem FROM Leitura WHERE FORMAT(momento, 'dd') = FORMAT(DATEADD(DAY, ?, GETDATE()), 'dd') ORDER BY id DESC"
    valor = vetor[i]
    cursor.execute(mensagem, valor)
    dado = cursor.fetchall()
    ram_mensal.append(dado)

print("Dados Mensais da RAM capturados.")

for i in range(30):
    mensagem = "SELECT TOP(1) hdPorcentagem FROM Leitura WHERE FORMAT(momento, 'dd') = FORMAT(DATEADD(DAY, ?, GETDATE()), 'dd') ORDER BY id DESC"
    valor = vetor[i]
    cursor.execute(mensagem, valor)
    dado = cursor.fetchall()
    hd_mensal.append(dado)

print("Dados Mensais do HD capturados.")

'''
Parte de confiabilidade do código. 
'''
medida_confiavel_cpu_mensal = 0
medida_confiavel_cpu_semanal = 0
medida_confiavel_ram = 0
medida_confiavel_hd = 0
confiabilidade_diario = 0.0
confiabilidade_semanal = 0.0
confiabilidade_mensal = 0.0

if verifica_diario:
    confiabilidade_diario = 100.0
else:
    confiabilidade_diario = 0.0

print("Confiabilidade diária: ", confiabilidade_diario, "%")

for i in range(len(cpu_semanal)):
     if(len(cpu_semanal[i]) == 1):
        medida_confiavel_cpu_semanal += 1

confiabilidade_semanal = round((medida_confiavel_cpu_semanal/7)*100, 2)
print("Confiabilidade semanal: ", confiabilidade_semanal, "%")

for i in range(len(cpu_mensal)):
    if(len(cpu_mensal[i]) == 1):
        medida_confiavel_cpu_mensal += 1

confiabilidade_mensal = round((medida_confiavel_cpu_mensal/30)*100,2)
print("Confiabilidade mensal: ", confiabilidade_mensal, "%")

'''
Correção dos dados vazios de cada um dos arrays.
'''

print("Corrigindo quaisquer dados vazios.")


'''
Códigos da parte gráfica da aplicação.
'''
app = Dash(__name__)

app.layout = html.Div([
    html.H4('Life expentancy progression of countries per continents'),
    dcc.Graph(id="graph"),
    dcc.Checklist(
        id="checklist",
        options=["Asia", "Europe", "Africa","Americas","Oceania"],
        value=["Americas", "Oceania"],
        inline=True
    ),
    html.A('Voltar para o dashboard padrão.', href='http://localhost:8080/dashboardTecnico')
])


@app.callback(
    Output("graph", "figure"), 
    Input("checklist", "value"))
def update_line_chart(continents):
    df = px.data.gapminder() # replace with your own data source
    mask = df.continent.isin(continents)
    fig = px.line(df[mask], 
        x="year", y="lifeExp", color='country')
    return fig


app.run_server(debug=True)
