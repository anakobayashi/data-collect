# 🎬 GanhadorOscar – Buscar Datas de Nascimento na Wikipédia

Este projeto contém um script em Python que lê nomes de um arquivo CSV, consulta a Wikipédia em português e tenta identificar a **data de nascimento** de cada pessoa.

---

## ✅ O que o script faz

- Lê os nomes do arquivo `nomes_com_datas_na.csv`
- Busca na Wikipédia a data de nascimento de cada nome
- Cria um novo arquivo com os dados encontrados

---

## 🛠️ Como usar

### 1. Instale os pacotes necessários

```bash
pip install pandas wikipedia-api openpyxl
