from pathlib import Path
import random
from datetime import date, timedelta

import pandas as pd

SEED = 42
N_REGISTROS = 3000
random.seed(SEED)

produtos = {
    "Notebook": ("Eletrônicos", 3499.90),
    "Monitor": ("Eletrônicos", 899.90),
    "Teclado": ("Acessórios", 159.90),
    "Mouse": ("Acessórios", 89.90),
    "Headset": ("Acessórios", 229.90),
    "Webcam": ("Acessórios", 279.90),
    "Cadeira Office": ("Escritório", 749.90),
    "Mesa Office": ("Escritório", 599.90),
}

localidades = [
    ("Campinas", "SP"),
    ("Indaiatuba", "SP"),
    ("São Paulo", "SP"),
    ("Sorocaba", "SP"),
    ("Curitiba", "PR"),
    ("Belo Horizonte", "MG"),
]

pagamentos = ["Pix", "Cartão de Crédito", "Cartão de Débito", "Boleto"]
inicio = date(2025, 1, 1)
fim = date(2025, 12, 31)
dias = (fim - inicio).days

linhas = []
for id_venda in range(1, N_REGISTROS + 1):
    produto = random.choice(list(produtos))
    categoria, preco_base = produtos[produto]
    cidade, estado = random.choice(localidades)
    data_venda = inicio + timedelta(days=random.randint(0, dias))
    quantidade = random.choices([1, 2, 3, 4], weights=[65, 23, 9, 3])[0]
    variacao = random.uniform(0.92, 1.08)
    preco = round(preco_base * variacao, 2)

    linhas.append(
        {
            "id_venda": id_venda,
            "data": data_venda.isoformat(),
            "produto": produto,
            "categoria": categoria,
            "quantidade": quantidade,
            "preco_unitario": preco,
            "cidade": cidade,
            "estado": estado,
            "forma_pagamento": random.choices(
                pagamentos, weights=[40, 38, 12, 10]
            )[0],
            "cliente_id": f"C{random.randint(1, 850):04d}",
        }
    )

df = pd.DataFrame(linhas).sort_values(["data", "id_venda"])
saida = Path(__file__).resolve().parents[1] / "data" / "vendas.csv"
saida.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(saida, index=False, encoding="utf-8")

print(f"Dataset criado: {saida}")
print(f"Registros: {len(df):,}")
