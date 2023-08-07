import requests
import json
import plotly.express as px

url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"

headers = {"Aceppt": "application/vnd.github.v3+json"}
requisicao = requests.get(url, headers=headers)
print(f"Resposta Servidor: {requisicao.status_code}")

resposta_dicionarios = requisicao.json()

respo_dicionarios =resposta_dicionarios['items']
repo_links, repo_stars, descricao = [], [], []

for respo_dicionario in respo_dicionarios:
    repo_nome = respo_dicionario['name']
    repo_url = respo_dicionario['html_url']
    repo_link = f"<a hrf='{repo_url}'>{repo_nome}</a>"
    repo_links.append(repo_link)
    repo_stars.append(respo_dicionario['stargazers_count'])
    owner = respo_dicionario['owner']['login']
    descri = respo_dicionario['description']
    descricao_texto = f"{owner}<br />{descri}"
    descricao.append(descricao_texto)

titulo = "Projetos Em Python no GitHub Com Mais Estrelas"
labels = {"x": "Repositorios", "y": "Estrelas"}
fig = px.bar(x=repo_links, y=repo_stars, title=titulo, labels=labels, hover_name=descricao)
fig.update_layout(title_font_size=28, xaxis_title_font_size=20, yaxis_title_font_size=20)
fig.update_traces(marker_color='SteelBlue', marker_opacity=0.6)

fig.show()


# url = "https://api.github.com/search/repositories"
# url += "?q=language:python+sort:stars+stars:>10000"

# headers = {"Aceppt": "application/vnd.github.v3+json"}
# requisicao = requests.get(url, headers=headers)
# print(f"Resposta Servidor: {requisicao.status_code}")

# resposta_dicionarios = requisicao.json()

# respo_dicionarios =resposta_dicionarios['items']
# repo_links, repo_stars, descricao = [], [], []

# for respo_dicionario in respo_dicionarios:
#     repo_nome = respo_dicionario['name']
#     repo_url = respo_dicionario['html_url']
#     repo_link = f"<a hrf='{repo_url}'>{repo_nome}</a>"
#     repo_links.append(repo_link)
#     repo_stars.append(respo_dicionario['stargazers_count'])
#     owner = respo_dicionario['owner']['login']
#     descri = respo_dicionario['description']
#     descricao_texto = f"{owner}<br />{descri}"
#     descricao.append(descricao_texto)

# titulo = "Projetos Em Python no GitHub Com Mais Estrelas"
# labels = {"x": "Repositorios", "y": "Estrelas"}
# fig = px.bar(x=repo_links, y=repo_stars, title=titulo, labels=labels, hover_name=descricao)
# fig.update_layout(title_font_size=28, xaxis_title_font_size=20, yaxis_title_font_size=20)

# fig.show()


# url = "https://api.github.com/search/repositories"
# url += "?q=language:python+sort:stars+stars:>10000"

# headers = {"Aceppt": "application/vnd.github.v3+json"}
# requisicao = requests.get(url, headers=headers)
# print(f"Resposta Servidor: {requisicao.status_code}")

# resposta_dicionarios = requisicao.json()

# respo_dicionarios =resposta_dicionarios['items']
# repo_nome, repo_stars, descricao = [], [], []

# for respo_dicionario in respo_dicionarios:
#     repo_nome.append(respo_dicionario['name'])
#     repo_stars.append(respo_dicionario['stargazers_count'])
#     owner = respo_dicionario['owner']['login']
#     descri = respo_dicionario['description']
#     descricao_texto = f"{owner}<br />{descri}"
#     descricao.append(descricao_texto)

# titulo = "Projetos Em Python no GitHub Com Mais Estrelas"
# labels = {"x": "Repositorios", "y": "Estrelas"}
# fig = px.bar(x=repo_nome, y=repo_stars, title=titulo, labels=labels, hover_name=descricao)
# fig.update_layout(title_font_size=28, xaxis_title_font_size=20, yaxis_title_font_size=20)

# fig.show()


