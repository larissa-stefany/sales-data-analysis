# Arquitetura do Projeto

O projeto segue um fluxo simples para demonstrar um processo de análise de dados reproduzível.

```text
src/gerar_dados.py
        ↓
data/vendas.csv
        ↓
src/tratamento_dados.py
        ↓
data/vendas_tratadas.csv + SQLite
        ↓
sql/consultas.sql + sql/insights.sql
        ↓
notebooks/analise_vendas.ipynb
        ↓
KPIs e insights de negócio
```

## Etapas

1. **Geração:** criação de uma base sintética e determinística.
2. **Validação:** checagens de estrutura, nulos, duplicidades, quantidades e preços.
3. **Tratamento:** padronização dos dados e cálculo de faturamento.
4. **Persistência:** armazenamento em CSV tratado e SQLite.
5. **Consulta:** perguntas de negócio respondidas com SQL.
6. **Análise:** exploração e visualizações em Python/Jupyter.

A arquitetura é propositalmente enxuta para manter o foco nas competências de Python e SQL.
