from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime


path = Path('weather_data/sitka_weather_2021_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
reader_now = next(reader)

datas, temp_maximas, temp_minimas = [], [], []
for linhas in reader:
    data = datetime.strptime(linhas[2], '%Y-%m-%d')
    datas.append(data)
    temp_maxima = int(linhas[4])
    temp_maximas.append(temp_maxima)
    temp_minima = int(linhas[5])
    temp_minimas.append(temp_minima)


fig, ax = plt.subplots()
plt.style.use('seaborn')
ax.plot(datas, temp_maximas, color='red')
ax.plot(datas, temp_minimas, color='blue')
ax.fill_between(datas, temp_maximas, temp_minimas, facecolor='gray', alpha=0.3)

ax.set_title('Dias de temperatura Maxima e Minima', fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('Temperaturas (F)', fontsize=16)
ax.tick_params(labelsize=16)

plt.show()


# path = Path('weather_data/sitka_weather_07-2021_simple.csv')
# lines = path.read_text().splitlines()

# reader = csv.reader(lines)
# reader_now = next(reader)

# datas, temp_maximas = [], []
# for linhas in reader:
#     data = datetime.strptime(linhas[2], '%Y-%m-%d')
#     datas.append(data)
#     temp_maxima = int(linhas[4])
#     temp_maximas.append(temp_maxima)

# print(temp_maximas)
# print(datas)

# fig, ax = plt.subplots()
# plt.style.use('seaborn')
# ax.plot(datas, temp_maximas, color='red')

# ax.set_title('Dias de temperatura Maxima', fontsize=24)
# ax.set_xlabel('', fontsize=16)
# fig.autofmt_xdate()
# ax.set_ylabel('Temperaturas (F)', fontsize=16)
# ax.tick_params(labelsize=16)

# plt.show()






# path = Path('weather_data/sitka_weather_2021_simple.csv')
# lines = path.read_text().splitlines()

# reader = csv.reader(lines)
# reader_now = next(reader)

# temp_maximas = []
# for linhas in reader:
#     temp_maxima = int(linhas[4])
#     temp_maximas.append(temp_maxima)

# print(temp_maximas)

# path = Path('weather_data/sitka_weather_2021_simple.csv')
# lines = path.read_text().splitlines()

# reader = csv.reader(lines)
# reader_now = next(reader)

# print(reader_now)