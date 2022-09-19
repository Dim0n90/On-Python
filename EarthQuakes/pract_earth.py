import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = 'eq_new.json'
with open(filename, encoding="utf-8") as f:
    all_data = json.load(f) 

all_dicts = all_data['features'] 
name_table = all_data['metadata']['title'] # запись имени в таблицу


magnitudes = [all_dict['properties']['mag'] for all_dict in all_dicts]
longitude = [all_dict['geometry']['coordinates'][0] for all_dict in all_dicts]
latitude = [all_dict['geometry']['coordinates'][1] for all_dict in all_dicts]
description_text = [all_dict['properties']['title'] for all_dict in all_dicts]
"""Землетресения на карте"""
#data = [Scattergeo(lon=longitude, lat=latitude)] # точечная диаграмма гео-данных на карте
data = [{'type': 'scattergeo', 
        'lon': longitude, 
        'lat': latitude,
        'text': description_text,
        'marker': {'size': [5*magnitude for magnitude in magnitudes],
                    'color': magnitudes, 'colorscale': 'Blackbody',
                    'reversescale': True, 'colorbar': {'title': 'Magnitude'}
                    }}] 
            
my_layout = Layout(title=name_table)

fig = {'data': data, 'layout': my_layout}  
offline.plot(fig, filename='global_earthquakes_new.html') 
#print(magnitudes[:10]) # первые 10 магнитуд
#print(longitude[:5])  # первые 5 ширина и долгота
#print(latitude[:5])
print(len(all_dicts)) # кол-во землетресений

    
