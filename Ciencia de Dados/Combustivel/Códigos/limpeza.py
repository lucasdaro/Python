import pandas as pd

dados = 'Tabela_Combustivel.csv'

df = pd.read_csv(dados, sep=';', encoding='utf-8', low_memory=False)

novo = df[['Estado - Sigla', 'Municipio', 'Produto', 'Data da Coleta', 'Valor de Venda', 'Ano', 'Semestre']]
print("="*50)
novo.to_csv('Tabela_Combustivel_Limpo.csv', sep=';', index=False, encoding='utf-8')