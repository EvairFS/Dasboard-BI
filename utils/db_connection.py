from sqlalchemy import create_engine
import pandas as pd

engine = create_engine(
    "postgresql://postgres:123456@localhost:5432/dashboard_bi"
)

def get_data(produto=None, start_date=None, end_date=None):

    query = """
    SELECT
        v.data_venda AS data,
        p.nome AS produto,
        p.categoria,
        v.quantidade,
        (v.quantidade * p.preco) AS valor
    FROM vendas v
    JOIN produtos p ON v.produto_id = p.id
    """

    df = pd.read_sql(query, engine)

    if produto:
        df = df[df["produto"] == produto]

    if start_date and end_date:
        df = df[(df["data"] >= start_date) & (df["data"] <= end_date)]

    return df
