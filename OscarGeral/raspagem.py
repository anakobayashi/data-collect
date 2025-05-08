# pip install pandas wikipedia-api openpyxl

# %%
import pandas as pd
import wikipediaapi
import re
import time

# Configura a API da Wikipédia
wiki_wiki = wikipediaapi.Wikipedia(
    language="pt",
    user_agent="GanhadorOscar/1.0 (natitanaka01@gmail.com)"
)

def get_birth_date(name):
    print(name)
    """Busca a data de nascimento na Wikipedia."""
    page = wiki_wiki.page(name)
    if not page.exists():
        return "Não encontrado"

    # Expressão para buscar datas no formato "DD de Mês de AAAA"
    match = re.search(r'(\d{1,2} de [a-zA-Z]+ de \d{4})', page.text)
    return match.group(0) if match else "Não encontrado"

# Carrega a planilha com os nomes
file_path = "/Users/anatanaka/Downloads/the_oscar_award.csv"  # Substitua pelo nome correto do arquivo
df = pd.read_csv(file_path)

# Nome da coluna que contém os nomes das pessoas
col_name = "name"  # Ajuste para o nome correto da coluna na sua planilha

if col_name not in df.columns:
    raise ValueError(f"A coluna '{col_name}' não foi encontrada na planilha.")

# Adiciona um delay para evitar bloqueios por muitas requisições seguidas
df["Data de Nascimento"] = df[col_name].apply(lambda x: get_birth_date(str(x)))
time.sleep(1)

# Salva o resultado em um novo arquivo
df.to_csv("nomes_com_datas.csv", index=False)

print("Processo concluído! Verifique o arquivo 'nomes_com_datas.csv'.")
# %%
