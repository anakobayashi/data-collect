# data-collect
Raspagem de dados 

Este projeto realiza a remoção de informações sobre personagens da franquia Resident Evil a partir do site Resident Evil Database. O código utiliza web scraping para coletar dados sobre cada personagem e salvar os resultados nos formatos CSV e Parquet.

**Tecnologias Utilizada**s:

Python 3

**Bibliotecas:**

requests para realizar requisições HTTP
BeautifulSoup (da biblioteca bs4) para análise do HTML
tqdm para visualizar o progresso da remoção
pandas para manipulação e armazenamento dos dados

**Estrutura do Código:**

**1. Definição de cabeçalhos:** O script utiliza um conjunto de cabeçalhos HTTP para simular uma requisição de navegador e evitar bloqueios por parte do servidor.

**2. Funções Principais:** 

get_content(url): Faz uma requisição HTTP para uma URL especificada e retorna uma resposta. 
get_basic_infos(soup): Extras informações básicas do personagem, como nome e outros detalhes encontrados no site. 
get_aparicoes(soup): Obtém a lista de aparições do personagem nos jogos da franquia. 
get_personagem_infos(url): Usa as funções anteriores para consolidar todas as informações de um personagem. 
get_links(): Coleta todos os links das páginas individuais de personagens específicos no site.

**3. Execução Principal:** O script obtém uma lista de links de personagens, para cada link, ele extrai as informações do personagem e armazena os dados em uma lista, os dados são convertidos para um DataFrame do pandas e salvos nos formatos CSV e Parquet.

**Como Executar:** Certifique-se de ter o Python instalado, sendo assim, instale as dependências necessárias, como: pip install requests beautifulsoup4 tqdm pandas

Execute o script Python. 
python nome_do_arquivo.py 
Os arquivos de saída (dados_re.csv e dados_re.parquet) serão gerados no diretório atual. 
O uso de # %% em código permite que ele seja executado de forma iterativa em notebooks como Jupyter e no VS Code com a extensão Python
