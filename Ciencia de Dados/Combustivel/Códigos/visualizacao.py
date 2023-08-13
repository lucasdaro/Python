import pandas as pd
import matplotlib.pyplot as plt

url = 'Tabela_Combustivel_Limpo.csv'

df = pd.read_csv(url, encoding='utf-8', sep=';')
media_precos_ano = df[['Estado - Sigla', 'Produto', 'Valor de Venda', 'Ano', 'Semestre']]
# Convertendo "Valor de Venda" para string
media_precos_ano['Valor de Venda'] = media_precos_ano['Valor de Venda'].astype(str)

# Substituindo vírgulas por pontos
media_precos_ano['Valor de Venda'] = media_precos_ano['Valor de Venda'].str.replace(',', '.')

# Convertendo "Valor de Venda" para float
media_precos_ano['Valor de Venda'] = media_precos_ano['Valor de Venda'].astype(float)
media = media_precos_ano.groupby(['Produto', 'Ano', 'Semestre'])['Valor de Venda'].mean()
produtos_unicos = media.index.get_level_values('Produto').unique()
print(produtos_unicos)


print(media)

media.to_csv('Media_precos.csv', sep=';', encoding='utf-8')