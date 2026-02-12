import pandas as pd
from datetime import timedelta

def periodo_anterior(inicio, fim):
    inicio = pd.to_datetime(inicio)
    fim = pd.to_datetime(fim)

    dias = (fim - inicio).days + 1
    novo_fim = inicio - timedelta(days=1)
    novo_inicio = novo_fim - timedelta(days=dias-1)

    return novo_inicio, novo_fim


def variacao(atual, anterior):
    if anterior == 0:
        return 0
    return ((atual - anterior) / anterior) * 100