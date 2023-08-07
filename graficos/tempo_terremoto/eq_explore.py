from pathlib import Path
import json
import plotly.express as px


path = Path('eq_data/eq_data_30_day_m1.geojson')
conteudo_arquivo = path.read_text(encoding='utf-8')
conteudo_em_json = json.loads(conteudo_arquivo)

todos_dicionarios = conteudo_em_json["features"]
print(len(todos_dicionarios))

mags, lons, lats, titulos = [], [], [], []

for dicionario in todos_dicionarios:
    mags.append(dicionario['properties']['mag'])
    lons.append(dicionario['geometry']['coordinates'][0])
    lats.append(dicionario['geometry']['coordinates'][1])
    titulos.append(dicionario['properties']['title'])
    


fig = px.scatter_geo(lat=lats, lon=lons, size=mags, title=conteudo_em_json['metadata']['title'],
                     color=mags,
                     color_continuous_scale='Viridis',
                     labels={'color': 'Magnitude'},
                     projection='natural earth',
                     hover_name=titulos)
fig.show()









# path = Path('eq_data/eq_data_30_day_m1.geojson')
# conteudo_arquivo = path.read_text(encoding='utf-8')
# conteudo_em_json = json.loads(conteudo_arquivo)

# todos_dicionarios = conteudo_em_json["features"]
# print(len(todos_dicionarios))

# mags, lons, lats, titulos = [], [], [], []

# for dicionario in todos_dicionarios:
#     mags.append(dicionario['properties']['mag'])
#     lons.append(dicionario['geometry']['coordinates'][0])
#     lats.append(dicionario['geometry']['coordinates'][1])
#     titulos.append(dicionario['properties']['title'])
    


# fig = px.scatter_geo(lat=lats, lon=lons, size=mags, title='Terremotos Global',
#                      color=mags,
#                      color_continuous_scale='Viridis',
#                      labels={'color': 'Magnitude'},
#                      projection='natural earth',
#                      hover_name=titulos)
# fig.show()






# path = Path('eq_data/eq_data_30_day_m1.geojson')
# conteudo_arquivo = path.read_text(encoding='utf-8')
# conteudo_em_json = json.loads(conteudo_arquivo)

# todos_dicionarios = conteudo_em_json["features"]
# print(len(todos_dicionarios))

# mags, lons, lats = [], [], []

# for dicionario in todos_dicionarios:
#     mag = dicionario['properties']['mag']
#     lon = dicionario['geometry']['coordinates'][0]
#     lat = dicionario['geometry']['coordinates'][1]
#     mags.append(mag)
#     lons.append(lon)
#     lats.append(lat)


# fig = px.scatter_geo(lat=lats, lon=lons, size=mags, title='Terremotos Global',
#                      color=mags,
#                      color_continuous_scale='Viridis',
#                      labels={'color': 'Magnitude'},
#                      projection='natural earth')
# fig.show()



# path = Path('eq_data/eq_data_1_day_m1.geojson')
# conteudo_arquivo = path.read_text(encoding='utf-8')
# conteudo_em_json = json.loads(conteudo_arquivo)

# todos_dicionarios = conteudo_em_json["features"]
# print(len(todos_dicionarios))

# mags, lons, lats = [], [], []

# for dicionario in todos_dicionarios:
#     mag = dicionario['properties']['mag']
#     lon = dicionario['geometry']['coordinates'][0]
#     lat = dicionario['geometry']['coordinates'][1]
#     mags.append(mag)
#     lons.append(lon)
#     lats.append(lat)

# print(mags[:5])
# print(lons[:5])
# print(lats[:5])

# path = Path('eq_data/eq_data_1_day_m1.geojson')
# contents = path.read_text(encoding='utf-8')
# conteudo = json.loads(contents)

# path = Path('eq_data/readable_eq_data.geojson')
# readle_contents = json.dumps(conteudo, indent=4)
# path.write_text(readle_contents)