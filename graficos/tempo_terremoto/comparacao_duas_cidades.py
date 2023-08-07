from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np

death_valey = Path('weather_data/death_valley_2021_simple.csv')
sitka = Path('weather_data/sitka_weather_2021_simple.csv')

linhas_death = death_valey.read_text().splitlines()
linhas_sitka = sitka.read_text().splitlines()

leitura_death = csv.reader(linhas_death)
leitura_sitka = csv.reader(linhas_sitka)

cabecalho_death = next(leitura_death)
cabecalho_sitka = next(leitura_sitka)

datas_death, datas_sitka, temp_max_death, temp_min_death, temp_max_sitka, temp_min_sitka = [], [], [], [], [], []

for dado in leitura_death:
    try:
        data = datetime.strptime(dado[2], '%Y-%m-%d')
        temp_max = float(dado[4])
        temp_min = float(dado[5])
        datas_death.append(data)
        temp_max_death.append(temp_max)
        temp_min_death.append(temp_min)
    except:
        continue

for dado in leitura_sitka:
    try:
        data = datetime.strptime(dado[2], '%Y-%m-%d')
        temp_max = float(dado[4])
        temp_min = float(dado[5])
        datas_sitka.append(data)
        temp_max_sitka.append(temp_max)
        temp_min_sitka.append(temp_min)
    except:
        continue

fig, ax = plt.subplots()
ax.plot(datas_death, temp_max_death, color='red')
ax.plot(datas_sitka, temp_max_sitka, color='blue')



plt.show()

print(temp_max_death)
