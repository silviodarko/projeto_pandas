import pandas as pd

# Carregar os dados em um DataFrame
dados = pd.read_csv('caminho/do/arquivo.csv')

# Realizar operações e análises com o DataFrame
# ...

# Exemplo: Visualizar as primeiras linhas do DataFrame
print(dados.head())

# Exemplo: Calcular estatísticas descritivas do DataFrame
print(dados.describe())

# Exemplo: Agrupar os dados por fabricante e calcular a média do preço unitário
grupo_fabricante = dados.groupby('Fabricante')
media_preco_unitario = grupo_fabricante['Preço Unitário'].mean()
print(media_preco_unitario)

# Exemplo: Combinar dois DataFrames com base em uma coluna em comum
dados2 = pd.read_csv('caminho/do/outro_arquivo.csv')
dados_combinados = pd.merge(dados, dados2, on='ID Produto')
print(dados_combinados)

