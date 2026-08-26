import pandas as pd


COLUNAS_OBRIGATORIAS = {
    "pedido_id",
    "data",
    "produto",
    "categoria",
    "quantidade",
    "preco_unitario",
    "cidade",
    "estado",
    "forma_pagamento",
    "cliente_id",
}


def validar_vendas(df: pd.DataFrame) -> dict:
    """Retorna um resumo simples de qualidade dos dados de vendas."""
    faltantes = sorted(COLUNAS_OBRIGATORIAS - set(df.columns))
    return {
        "linhas": int(len(df)),
        "duplicadas": int(df.duplicated().sum()),
        "nulos": int(df.isna().sum().sum()),
        "colunas_faltantes": faltantes,
        "quantidades_invalidas": int((df["quantidade"] <= 0).sum()) if "quantidade" in df else 0,
        "precos_invalidos": int((df["preco_unitario"] <= 0).sum()) if "preco_unitario" in df else 0,
    }
