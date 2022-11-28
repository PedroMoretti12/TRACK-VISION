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

cursor.execute('SELECT cpuPorcentagem FROM Leitura')
row = cursor.fetchall()
dados_cpu = []

for x in range(len(row)):
    dados_cpu.append(row[x][0])

cursor.execute('SELECT hdPorcentagem FROM Leitura')
row = cursor.fetchall()
dados_hd = []

for x in range(len(row)):
    dados_hd.append(row[x][0])

cursor.execute('SELECT ramPorcentagem FROM Leitura')
row = cursor.fetchall()
dados_ram = []

for x in range(len(row)):
    dados_ram.append(row[x][0])

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