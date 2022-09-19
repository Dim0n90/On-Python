import requests

from plotly.graph_objs import Bar
from plotly import offline

"""Сделать вызов через API и сохранить ответ"""
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
#headers = {'Accept': 'application/vnd.githab.v3+json'}
r = requests.get(url)
print(f"Status code: {r.status_code}")

"""Сохраняем ответ API в переменную"""
response_dict = r.json()  # API возвращает инфу в формате JSON, поэтому ковертируем в словарь
print(f"Total repositories: {response_dict['total_count']}") # Общее кол-во репов

"""Информация в репозиториях"""
repos_dicts = response_dict['items'] # это словарь, который содержит инфу про одно отдельное хранилище
print(f"Repositories returned: {len(repos_dicts)}") # про сколько репов есть инфа

repos_names, stars = [], []
for details_repos in repos_dicts: # смотрим данные про каждый реп
    repos_names.append(details_repos['name'])
    stars.append(details_repos['stargazers_count'])

"""Делаем визуализацию"""
data = [{'type': 'bar',
        'x': repos_names, 'y': stars,
        'marker': {'color': 'rgb(60, 100, 150)',
                   'line': {'width': 1.5, 'color': 'rgb(150, 25, 25)'}},
        'opacity': 0.6}]
my_layout = {'title': 'Most - Starred Python Projects on GitHub',
            'titlefont': {'size': 28}, # ШРИФТ
            'xaxis': {'title': 'Repository','titlefont': {'size': 24}, 'tickfont': {'size':14}},
            'yaxis': {'title': 'Stars', 'titlefont': {'size': 24}, 'tickfont': {'size':14}}}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='stars_python.html')
