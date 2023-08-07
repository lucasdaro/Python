from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np

arquivo = Path('weather_data/sitka_weather_2021_full.csv')
linhas = arquivo.read_text().splitlines()
leitura = csv.reader(linhas)
cabecalho = next(leitura)

datas, chuvas = [], []
for linha in leitura:
    data_item = datetime.strptime(linha[2], '%Y-%m-%d')
    try:        
        chuva_item = float(linha[5])
    except:
        continue
    datas.append(data_item)
    chuvas.append(chuva_item)

fig, ax = plt.subplots()
ax.plot(datas, chuvas, color='blue')

ax.set_title("Chuva", fontsize=24)
ax.set_xlabel("Data", fontsize=16)
ax.set_ylabel("Quantidaded", fontsize=16)
ax.tick_params(labelsize=16)



plt.show()

# for indice, valor in enumerate(cabecalho_linha):
#     print(indice, valor)
