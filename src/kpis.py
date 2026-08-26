from pathlib import Path

import pandas as pd


def calcular_kpis(caminho_csv: Path) -> dict:
    """Calcula indicadores principais da base de vendas tratada."""
    df = pd.read_csv(caminho_csv)

    faturamento = float(df["faturamento"].sum())
    pedidos = int(df["pedido_id"].nunique())
    itens = int(df["quantidade"].sum())

    return {
        "faturamento_total": faturamento,
        "pedidos": pedidos,
        "itens_vendidos": itens,
        "ticket_medio": faturamento / pedidos if pedidos else 0.0,
    }


if __name__ == "__main__":
    root = Path(__file__).resolve().parents[1]
    arquivo = root / "data" / "vendas_tratadas.csv"
    for nome, valor in calcular_kpis(arquivo).items():
        print(f"{nome}: {valor}")
