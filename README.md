# Sales Data Analysis 📊

Projeto de portfólio focado em **análise de dados de vendas utilizando Python e SQL**.

O objetivo é demonstrar um fluxo simples e reproduzível de análise: geração de uma base de estudo, limpeza e transformação dos dados, consultas SQL, análise exploratória e comunicação de insights de negócio.

## 🎯 Objetivos

- Tratar e validar dados de vendas com Python e Pandas
- Armazenar e consultar os dados utilizando SQL/SQLite
- Calcular indicadores como faturamento, ticket médio e volume de vendas
- Identificar produtos, categorias e cidades de maior desempenho
- Analisar a evolução mensal das vendas
- Produzir visualizações e insights de forma clara

## 🛠️ Tecnologias

- Python
- Pandas
- Matplotlib
- SQL
- SQLite
- Jupyter Notebook
- Git/GitHub

## 📁 Estrutura

```text
sales-data-analysis/
├── data/
│   └── vendas.csv
├── notebooks/
│   └── analise_vendas.ipynb
├── sql/
│   ├── criar_banco.sql
│   └── consultas.sql
├── src/
│   ├── gerar_dados.py
│   └── tratamento_dados.py
├── .gitignore
├── requirements.txt
└── README.md
```

## 📌 Perguntas de negócio

1. Qual é o faturamento total?
2. Qual é o ticket médio por pedido?
3. Quais categorias geram mais receita?
4. Quais produtos apresentam maior faturamento?
5. Como as vendas evoluem ao longo dos meses?
6. Quais cidades concentram maior faturamento?
7. Quais formas de pagamento são mais utilizadas?

## 📊 Dataset

Para que o projeto seja totalmente reproduzível e não atribua os dados a uma empresa real, a base utilizada é **sintética e destinada exclusivamente a fins educacionais**. O script `src/gerar_dados.py` gera os registros de maneira determinística (`seed=42`).

Cada registro representa um item vendido e contém data, produto, categoria, quantidade, preço unitário, cidade, estado, forma de pagamento e cliente.

## ▶️ Como executar

```bash
pip install -r requirements.txt
python src/gerar_dados.py
python src/tratamento_dados.py
```

Depois, execute as consultas presentes em `sql/consultas.sql` ou abra o notebook `notebooks/analise_vendas.ipynb`.

## 💡 Competências demonstradas

`Python` `SQL` `Pandas` `SQLite` `EDA` `ETL` `Data Visualization` `Business Analysis`

## 🤖 Auditoria diária automatizada

O GitHub Actions executa a auditoria da base sintética todos os dias às **07h17 (horário de Brasília; 10h17 UTC)**. O agendamento do GitHub Actions pode sofrer atrasos e depende de Actions estar habilitado e das permissões de escrita do repositório.

- **Workflow:** [`.github/workflows/daily-audit.yml`](.github/workflows/daily-audit.yml)
- **Código da auditoria:** [`src/daily_audit.py`](src/daily_audit.py)
- **Resultados diários:** [`reports/daily/`](reports/daily/) (criados a partir da primeira execução)

A rotina verifica campos obrigatórios, células vazias, duplicidades, quantidades/preços inválidos e datas. Também registra quantidade de pedidos, itens válidos, faturamento **simulado** e um hash SHA-256 da base. Compara o hash com o relatório anterior para indicar se os dados mudaram.

O workflow cria um commit do usuário **github-actions[bot]** somente quando há um arquivo de relatório novo ou atualizado; repetir a execução no mesmo dia sem mudanças não cria outro commit. **Commits de auditoria automática não representam novas funcionalidades nem desenvolvimento manual** e devem ser diferenciados das contribuições técnicas em relatórios de evolução profissional.

Para executar manualmente, abra a aba **Actions**, selecione **Auditoria diária de vendas** e clique em **Run workflow**. A rotina não precisa de pacotes externos: usa apenas a biblioteca padrão do Python.

---

Desenvolvido como projeto de portfólio para consolidar conhecimentos em **Análise de Dados**.