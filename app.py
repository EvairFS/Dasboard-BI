import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
from utils.db_connection import get_data

app = dash.Dash(__name__)
app.title = "Dashboard BI"

app.layout = html.Div([

    html.H1("Dashboard BI - Vendas"),

    html.Div([
        dcc.Dropdown(
            id="produto",
            placeholder="Filtrar produto",
            clearable=True
        ),

        dcc.DatePickerRange(id="datas")

    ], style={"width":"50%"}),

    html.Div(id="kpis", style={
        "display":"flex",
        "justify-content":"space-around",
        "margin":"20px"
    }),

    dcc.Graph(id="bar"),
    dcc.Graph(id="line"),
    dcc.Graph(id="pie"),

    dcc.Interval(
        id="refresh",
        interval=5000,
        n_intervals=0
    )
])

# Popular dropdown
@app.callback(
    Output("produto","options"),
    Input("refresh","n_intervals")
)
def load_products(n):
    df = get_data()
    return [{"label":p, "value":p} for p in df["produto"].unique()]

# Atualizar tudo
@app.callback(
    Output("bar","figure"),
    Output("line","figure"),
    Output("pie","figure"),
    Output("kpis","children"),
    Input("produto","value"),
    Input("datas","start_date"),
    Input("datas","end_date"),
    Input("refresh","n_intervals")
)
def update(produto, start, end, n):

    df = get_data(produto, start, end)

    fig_bar = px.bar(df, x="categoria", y="quantidade")
    fig_line = px.line(df, x="data", y="valor")
    fig_pie = px.pie(df, names="produto", values="quantidade")

    total_vendas = df["quantidade"].sum()
    faturamento = df["valor"].sum()
    produtos = df["produto"].nunique()

    kpis = [
        html.Div(f"Total Vendas: {total_vendas}", className="kpi"),
        html.Div(f"Produtos: {produtos}", className="kpi"),
        html.Div(f"Faturamento: R$ {faturamento:,.2f}", className="kpi")
    ]

    return fig_bar, fig_line, fig_pie, kpis

if __name__ == "__main__":
    app.run(debug=True)