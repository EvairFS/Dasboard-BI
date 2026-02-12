import pandas as pd
import random
from datetime import datetime, timedelta
from utils.cache import cache


@cache.memoize()
def get_data(produto=None, inicio=None, fim=None):
    ...

def get_mock_data(produto=None, start=None, end=None):

    produtos = ["Notebook", "Mouse", "Teclado", "Monitor", "Headset"]
    categorias = ["Eletrônicos", "Acessórios"]

    data_base = datetime.today()

    rows = []

    for i in range(120):
        data = data_base - timedelta(days=i)

        p = random.choice(produtos)

        rows.append({
            "produto": p,
            "categoria": random.choice(categorias),
            "quantidade": random.randint(1, 15),
            "valor": random.uniform(50, 300),
            "data": data
        })

    df = pd.DataFrame(rows)

    if produto:
        df = df[df["produto"] == produto]

    if start:
        df = df[df["data"] >= pd.to_datetime(start)]

    if end:
        df = df[df["data"] <= pd.to_datetime(end)]

    return df
