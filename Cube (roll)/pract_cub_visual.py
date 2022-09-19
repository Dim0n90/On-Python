from plotly.graph_objs import Bar, Layout
from plotly import offline 

from pract_cube import Cube

# создаем два кубика Д8 
cube_1 = Cube()
cube_2 = Cube()
cube_3 = Cube()

# делаем несколько бросаний и сохраняем
results = []
for roll_numb in range(1000): # симуляция 1000 бросков
    result = cube_1.roll() + cube_2.roll() + cube_3.roll() 
    results.append(result)

frequencies = []  # в пустой список будем сохранять результаты кол-ва выпадений
max_result = cube_1.num_sides + cube_2.num_sides + cube_3.num_sides
for value in range(3, max_result+1):
    frequency = results.count(value) #считаем сколько раз каждое значение попадается в RESULTS
    frequencies.append(frequency) # помещаем в пустой список
# делаем визуализацию, гистограмму
x_values = list(range(3, max_result+1)) # сюда сохраняем столбики с результатами от 1 до числа греней
data = [Bar(x=x_values, y=frequencies)] # класс BAR - набор данных для диаграммы, ему нужны Х и У
                                        # класс через [] поскольку может быть много эл-ов
                                        # Plotly не принимает рез-ты RANGE, поэтому через список LIST
x_axis_config = {'title': 'Result', 'dtick': 1} # ключ DTICK - контролирует ширину разметки оси Х
y_axis_config = {'title': 'Repeats of Results'}
my_layout = Layout(title='Results of rolling three cube D6 dies 1000 times',
        xaxis=x_axis_config, yaxis=y_axis_config)
# OFFLINE.PLOT принимает как праметр словарь с обьектами данных, компановку/построенеие и имя файла 
offline.plot({'data': data, 'layout': my_layout}, filename='roll_thrice_d6.html')