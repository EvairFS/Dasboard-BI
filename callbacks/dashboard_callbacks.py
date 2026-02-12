from dash.dependencies import Input, Output
import plotly.express as px

from app_instance import app
from utils.data_source import get_data
from services.kpi_service import periodo_anterior, variacao


@app.callback(
    Output("produto","options"),
    Input("refresh","n_intervals")
)
def load_products(n):
    df = get_data()
    return [{"label":p, "value":p} for p in df["produto"].unique()]

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

    if start and end:
        ini_ant, fim_ant = periodo_anterior(start, end)
        df_ant = get_data(produto, ini_ant, fim_ant)
        vendas_ant = df_ant["quantidade"].sum()
        faturamento_ant = df_ant["valor"].sum()
    else:
        vendas_ant = faturamento_ant = 0

    kpi1 = f"Total Vendas: {total_vendas} ({variacao(total_vendas,vendas_ant):+.1f}%)"
    kpi2 = f"Produtos: {produtos}"
    kpi3 = f"Faturamento: R$ {faturamento:,.2f} ({variacao(faturamento,faturamento_ant):+.1f}%)"

    for fig in (fig_bar, fig_line, fig_pie):
        fig.update_layout(
            template="plotly_dark",

            font=dict(
                color="white",
                size=14
            ),

            xaxis=dict(
                title_font=dict(color="white"),
                tickfont=dict(color="white"),
                gridcolor="rgba(255,255,255,0.15)"
            ),

            yaxis=dict(
                title_font=dict(color="white"),
                tickfont=dict(color="white"),
                gridcolor="rgba(255,255,255,0.15)"
            ),

            legend=dict(
                font=dict(color="white")
            ),

            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)"
        )

    return fig_bar, fig_line, fig_pie, kpi1, kpi2, kpi3
