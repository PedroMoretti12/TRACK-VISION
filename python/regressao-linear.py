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

cursor.execute("SELECT TOP(24) cpuPorcentagem FROM [dbo].[Leitura] WHERE FORMAT(momento, 'dd') = FORMAT(DATEADD(DAY, -1 , GETDATE()), 'dd') ORDER BY id DESC;")
row = cursor.fetchall()

cpu_diario = []

if len(row) == 24:
    print("24 Dados do dia anterior capturados.")
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

cursor.execute("SELECT TOP(1) cpuPorcentagem FROM Leitura WHERE FORMAT(momento, 'dd') = FORMAT(DATEADD(DAY, -0, GETDATE()), 'dd') ORDER BY id DESC")
teste = cursor.fetchall()

'''
Código da captura de dados do mês.
'''


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
