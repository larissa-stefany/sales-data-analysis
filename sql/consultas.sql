-- 1. Faturamento total
SELECT ROUND(SUM(faturamento), 2) AS faturamento_total
FROM vendas;

-- 2. Ticket médio por pedido
SELECT ROUND(AVG(faturamento), 2) AS ticket_medio
FROM vendas;

-- 3. Receita por categoria
SELECT categoria,
       ROUND(SUM(faturamento), 2) AS faturamento
FROM vendas
GROUP BY categoria
ORDER BY faturamento DESC;

-- 4. Produtos com maior faturamento
SELECT produto,
       SUM(quantidade) AS unidades_vendidas,
       ROUND(SUM(faturamento), 2) AS faturamento
FROM vendas
GROUP BY produto
ORDER BY faturamento DESC;

-- 5. Evolução mensal
SELECT mes,
       COUNT(DISTINCT pedido_id) AS pedidos,
       ROUND(SUM(faturamento), 2) AS faturamento
FROM vendas
GROUP BY mes
ORDER BY mes;

-- 6. Cidades com maior faturamento
SELECT cidade,
       estado,
       ROUND(SUM(faturamento), 2) AS faturamento
FROM vendas
GROUP BY cidade, estado
ORDER BY faturamento DESC;

-- 7. Formas de pagamento mais utilizadas
SELECT forma_pagamento,
       COUNT(*) AS quantidade_pedidos,
       ROUND(100.0 * COUNT(*) / SUM(COUNT(*)) OVER (), 2) AS percentual
FROM vendas
GROUP BY forma_pagamento
ORDER BY quantidade_pedidos DESC;
