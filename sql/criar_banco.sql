DROP TABLE IF EXISTS vendas;

CREATE TABLE vendas (
    pedido_id TEXT PRIMARY KEY,
    data TEXT NOT NULL,
    cliente_id TEXT NOT NULL,
    produto TEXT NOT NULL,
    categoria TEXT NOT NULL,
    quantidade INTEGER NOT NULL CHECK (quantidade > 0),
    preco_unitario REAL NOT NULL CHECK (preco_unitario > 0),
    cidade TEXT NOT NULL,
    estado TEXT NOT NULL,
    forma_pagamento TEXT NOT NULL,
    faturamento REAL NOT NULL,
    mes TEXT NOT NULL
);
