oscar-age-analysis/
│
├── data/                   # Dados brutos e tratados (localmente)
│   ├── raw/
│   └── processed/
│
├── notebooks/              # Análises exploratórias
│   └── analysis.ipynb
│
├── src/                    # Scripts Python (ETL)
│   ├── extract.py
│   ├── transform.py
│   └── load.py
│
├── dashboard/              # Código do dashboard (ex: Streamlit ou Power BI export)
│   └── app.py
│
├── requirements.txt        # Dependências do projeto
├── README.md               # Descrição do projeto
└── .gitignore


# Análise da Idade dos Indicados e Vencedores do Oscar

Este projeto tem como objetivo analisar os padrões de idade entre indicados e ganhadores do Oscar ao longo das décadas, utilizando práticas de Engenharia de Dados — da coleta automatizada à visualização.

---

## Objetivos

- Coletar dados de indicados e vencedores ao Oscar (via web scraping)
- Calcular a idade das pessoas no momento da premiação
- Analisar padrões por categoria, ano e gênero
- Criar um pipeline de dados limpo e escalável
- Disponibilizar visualizações interativas com os insights

---

## Tecnologias Utilizadas

- **Python** (Pandas, BeautifulSoup, Requests)
- **Banco de Dados**: PostgreSQL ou BigQuery
- **Visualização**: Streamlit ou Power BI
- **Orquestração (opcional)**: Apache Airflow
- **Ambiente de análise**: Jupyter Notebook
- **Versionamento**: Git + GitHub

---

## Estrutura do Projeto

