from pathlib import Path
import sqlite3

import pandas as pd


def carregar_dados(caminho_csv: Path) -> pd.DataFrame:
    return pd.read_csv(caminho_csv, parse_dates=["data"])


def tratar_dados(df: pd.DataFrame) -> pd.DataFrame:
    dados = df.copy()

    dados = dados.drop_duplicates().dropna().reset_index(drop=True)
    dados["quantidade"] = dados["quantidade"].astype(int)
    dados["preco_unitario"] = dados["preco_unitario"].astype(float)

    dados = dados[(dados["quantidade"] > 0) & (dados["preco_unitario"] > 0)]
    dados["faturamento"] = dados["quantidade"] * dados["preco_unitario"]
    dados["mes"] = dados["data"].dt.to_period("M").astype(str)

    return dados


def salvar_banco(df: pd.DataFrame, caminho_banco: Path) -> None:
    caminho_banco.parent.mkdir(parents=True, exist_ok=True)
    with sqlite3.connect(caminho_banco) as conexao:
        df.to_sql("vendas", conexao, if_exists="replace", index=False)


def main() -> None:
    raiz = Path(__file__).resolve().parents[1]
    entrada = raiz / "data" / "vendas.csv"
    saida_csv = raiz / "data" / "vendas_tratadas.csv"
    banco = raiz / "data" / "vendas.db"

    df = carregar_dados(entrada)
    tratados = tratar_dados(df)
    tratados.to_csv(saida_csv, index=False)
    salvar_banco(tratados, banco)

    print(f"Registros tratados: {len(tratados)}")
    print(f"Faturamento total: R$ {tratados['faturamento'].sum():,.2f}")


if __name__ == "__main__":
    main()
