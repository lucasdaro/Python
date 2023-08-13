import pandas as pd
import numpy as np
dfs = []

for arquivo in (np.arange(2004,2023)):
    arquivo1 = f'ca-{arquivo}-01.csv'
    arquivo2 = f'ca-{arquivo}-02.csv'

    print(f'Lendo arquivos de {arquivo}')
    pandas1 = pd.read_csv(arquivo1, sep=';', encoding='utf-8', low_memory=False)

    try:
        pandas2 = pd.read_csv(arquivo2, sep=';', encoding='utf-8', low_memory=False)
    except:
        print("Não foi possivel Ler o Arquivo com utf-8")
        pandas2 = pd.read_csv(arquivo2, sep=';', encoding='ISO-8859-1', low_memory=False)
    

    print(f'Adicionando Coluna Ano e Semestre em {arquivo}')
    pandas1['Ano'] = int(arquivo)
    pandas1['Ano'] = pandas1['Ano'].astype(int)
    pandas1['Semestre'] = int(1)
    pandas1['Semestre'] = pandas1['Semestre'].astype(int)
    pandas2['Ano'] = int(arquivo)
    pandas2['Ano'] = pandas2['Ano'].astype(int)
    pandas2['Semestre'] = int(2)
    pandas2['Semestre'] = pandas2['Semestre'].astype(int)

    print(f'Fazendo a Concatenização dos dataframes')
    df = pd.concat([pandas1,pandas2], ignore_index=True)
    dfs.append(df)
    print("="*50)

print(f'Lendo arquivos de 2023')
caminho_df2023 = 'ca-2023-01.csv'
df2023 = pd.read_csv(caminho_df2023, encoding='utf-8', sep=';')
print(f'Adicionando Coluna Ano e Semestre em 2023')
df2023['Ano'] = int(2023)
df2023['Semestre'] = int(1)
print(f'Fazendo a Concatenização dos dataframes')
dfs.append(df2023)

df_final = pd.concat(dfs, ignore_index=True)
df_final.to_csv('Tabela_Combustivel.csv', sep=';', index=False, encoding='utf-8')