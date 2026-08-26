-- Insights adicionais para análise de vendas

-- 1. Participação de faturamento por categoria
SELECT
    categoria,
    ROUND(SUM(faturamento), 2) AS faturamento,
    ROUND(100.0 * SUM(faturamento) / (SELECT SUM(faturamento) FROM vendas), 2) AS participacao_pct
FROM vendas
GROUP BY categoria
ORDER BY faturamento DESC;

-- 2. Receita média por cliente
SELECT
    cliente_id,
    ROUND(SUM(faturamento), 2) AS receita_cliente,
    COUNT(DISTINCT pedido_id) AS pedidos
FROM vendas
GROUP BY cliente_id
ORDER BY receita_cliente DESC
LIMIT 20;

-- 3. Ranking de cidades por faturamento
SELECT
    cidade,
    estado,
    ROUND(SUM(faturamento), 2) AS faturamento
FROM vendas
GROUP BY cidade, estado
ORDER BY faturamento DESC;
