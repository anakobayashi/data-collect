# pip install pandas wikipedia-api openpyxl

# %% 

import pandas as pd
import wikipediaapi
import re
import time

# Configuração da API da Wikipédia
wiki_wiki = wikipediaapi.Wikipedia(
    language="pt",
    user_agent="GanhadorOscar/1.0 (natitanaka01@gmail.com)"
)

def get_birth_date(name):
    print(f"🔎 Buscando data de nascimento de: {name}")
    page = wiki_wiki.page(name)
    if not page.exists():
        return "Não encontrado"

    # 1ª tentativa: procurar linha que começa com "Nascimento:"
    for line in page.text.split('\n'):
        if line.strip().startswith("Nascimento:"):
            match = re.search(r'(\d{1,2} de [a-zA-ZçÇ]+ de \d{4})', line)
            if match:
                return match.group(0)

    # 2ª tentativa: procurar qualquer data no texto
    match = re.search(r'(\d{1,2} de [a-zA-ZçÇ]+ de \d{4})', page.text)
    return match.group(0) if match else "Não encontrado"

# Caminho do arquivo
file_path = "/Users/anatanaka/Downloads/nomes_com_datas_na.csv"
output_path = "nomes_com_datas_completos.csv"
col_name = "name"

# Leitura da planilha
df = pd.read_csv(file_path)

# Validação da coluna
if col_name not in df.columns:
    raise ValueError(f"A coluna '{col_name}' não foi encontrada no arquivo.")

# Processamento com delay para evitar bloqueio
datas_nascimento = []
for nome in df[col_name]:
    data = get_birth_date(str(nome))
    datas_nascimento.append(data)
    time.sleep(1)  # Delay de 1 segundo por chamada

# Adiciona a nova coluna
df["Data de Nascimento"] = datas_nascimento

# Salva o resultado
df.to_csv(output_path, index=False)

print(f"✅ Processo concluído! Verifique o arquivo '{output_path}'.")