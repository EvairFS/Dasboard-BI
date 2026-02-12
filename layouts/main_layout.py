from dash import dcc, html
import dash_bootstrap_components as dbc

layout = dbc.Container([

    dcc.Interval(id="refresh", interval=5000),
    dcc.DatePickerRange(id="datas"),

    dbc.Row([

        dbc.Col([
            html.Div([
                html.H3("DASHBOARD", className="sidebar-title"),
                html.H5("FINANCEIRO", className="sidebar-title"),
                html.Hr(),
                html.P("Competência"),
                dcc.Dropdown(id="produto", placeholder="Todos")
            ], className="sidebar")
        ], width=2),

        dbc.Col([

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
                ], className="kpi-card"))
            ], className="mb-4"),

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