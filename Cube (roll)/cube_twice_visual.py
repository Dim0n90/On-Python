from plotly.graph_objs import Bar, Layout
from plotly import offline 

from cube1 import Cube

# создаем два кубика Д6 ()() или ()(10)
cube_1 = Cube()
cube_2 = Cube(10)

# делаем несколько бросаний и сохраняем
results = []
for roll_numb in range(10_000):
    result = cube_1.roll() + cube_2.roll()
    results.append(result)

frequencies = [] 
max_result = cube_1.num_sides + cube_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value) 
    frequencies.append(frequency) 
# делаем визуализацию, гистограмму
x_values = list(range(2, max_result+1)) # сюда сохраняем столбики с результатами от 1 до числа греней
data = [Bar(x=x_values, y=frequencies)] # класс BAR - набор данных для диаграммы, ему нужны Х и У
                                        # класс через [] поскольку может быть много эл-ов
                                        # Plotly не принимает рез-ты RANGE, поэтому через список LIST
x_axis_config = {'title': 'Result', 'dtick': 1} # ключ DTICK - контролирует ширину разметки оси Х
y_axis_config = {'title': 'Repeats of Results'}
my_layout = Layout(title='Results of rolling two cube - D6 and D 10 dies 10000 times',
        xaxis=x_axis_config, yaxis=y_axis_config)
# OFFLINE.PLOT принимает как параметр словарь с обьектами данных, компановку/построенеие и имя файла 
offline.plot({'data': data, 'layout': my_layout}, filename='roll_twice_d6_d10.html')

