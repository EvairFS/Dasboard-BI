import dash_bootstrap_components as dbc
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
from utils.db_connection import get_data

app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.CYBORG]
)

app.title = "Dashboard BI"

app.layout = dbc.Container([

    dcc.Interval(id="refresh", interval=5000),
    dcc.DatePickerRange(id="datas"),

    dbc.Row([

        # SIDEBAR
        dbc.Col([
            html.Div([
                html.H3("DASHBOARD", className="sidebar-title"),
                html.H5("FINANCEIRO", className="sidebar-title"),
                html.Hr(),

                html.P("Competência"),
                dcc.Dropdown(
                    id="produto",
                    placeholder="Todos"
                )

            ], className="sidebar")
        ], width=2),

        # CONTEÚDO PRINCIPAL
        dbc.Col([

            # KPIs
            dbc.Row([
                dbc.Col(html.Div([
                    html.Div("Total de Receitas", className="kpi-title"),
                    html.Div(id="kpi1", className="kpi-value")
                ], className="kpi-card")),

                dbc.Col(html.Div([
                    html.Div("CMV", className="kpi-title"),
                    html.Div(id="kpi2", className="kpi-value")
                ], className="kpi-card")),

                dbc.Col(html.Div([
                    html.Div("Lucro Bruto", className="kpi-title"),
                    html.Div(id="kpi3", className="kpi-value")
                ], className="kpi-card")),
            ], className="mb-4"),

            # GRÁFICOS
            dbc.Row([
                dbc.Col(
                    html.Div(dcc.Graph(id="bar"), className="graph-card"),
                    width=12
                )
            ]),

            dbc.Row([
                dbc.Col(
                    html.Div(dcc.Graph(id="line"), className="graph-card"),
                    width=6
                ),
                dbc.Col(
                    html.Div(dcc.Graph(id="pie"), className="graph-card"),
                    width=6
                )
            ])

        ], width=10)

    ])

], fluid=True)

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
    Output("kpi1", "children"),
    Output("kpi2", "children"),
    Output("kpi3", "children"),
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

    kpi1 = f"Total Vendas: {total_vendas}"
    kpi2 = f"Produtos: {produtos}"
    kpi3 = f"Faturamento: R$ {faturamento:,.2f}"

    return fig_bar, fig_line, fig_pie, kpi1, kpi2, kpi3

if __name__ == "__main__":
    app.run(debug=True)