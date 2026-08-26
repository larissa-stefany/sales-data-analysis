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
    "Webcam": ("Eletrônicos", 279.90),
    "Cadeira": ("Escritório", 749.90),
    "Mesa": ("Escritório", 599.90),
}

localidades = [
    ("Campinas", "SP"),
    ("Indaiatuba", "SP"),
    ("São Paulo", "SP"),
    ("Sorocaba", "SP"),
    ("Curitiba", "PR"),
    ("Belo Horizonte", "MG"),
]

pagamentos = ["PIX", "Cartão de crédito", "Cartão de débito", "Boleto"]
inicio = date(2026, 1, 1)
fim = date(2026, 6, 30)
dias = (fim - inicio).days

linhas = []
for numero in range(1, N_REGISTROS + 1):
    produto = random.choice(list(produtos))
    categoria, preco_base = produtos[produto]
    cidade, estado = random.choice(localidades)
    data_venda = inicio + timedelta(days=random.randint(0, dias))
    quantidade = random.choices([1, 2, 3, 4], weights=[65, 23, 9, 3])[0]
    preco = round(preco_base * random.uniform(0.92, 1.08), 2)

    linhas.append(
        {
            "pedido_id": f"PED{numero:04d}",
            "data": data_venda.isoformat(),
            "cliente_id": f"CLI{random.randint(1, 850):03d}",
            "produto": produto,
            "categoria": categoria,
            "quantidade": quantidade,
            "preco_unitario": preco,
            "cidade": cidade,
            "estado": estado,
            "forma_pagamento": random.choices(
                pagamentos, weights=[40, 38, 12, 10]
            )[0],
        }
    )

df = pd.DataFrame(linhas).sort_values(["data", "pedido_id"])
saida = Path(__file__).resolve().parents[1] / "data" / "vendas.csv"
saida.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(saida, index=False, encoding="utf-8")

print(f"Dataset criado: {saida}")
print(f"Registros: {len(df):,}")
