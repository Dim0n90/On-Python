import matplotlib.pyplot as plt

from pract_diagram4_randomwalk import RandomWalk

while True:
    """Создаем случайное блуждание"""
    rw = RandomWalk(1000)
    rw.fill_walk()  # вызываем ф-цию

    plt.style.use('ggplot')
    fig, ax = plt.subplots(figsize=(10,6), dpi=128) # размер рисунка-кортеж (15, 9)
    points_numbers = range(rw.num_points) # генерируем последовательность чисел, которая = точкам блуждания
    ax.plot(rw.x_values, rw.y_values, linewidth=1)  # передаем значения Х и У, EDGECOLORS - избавляет от черного контура точек
    """Выделяем первую и последнюю точки"""
    ax.scatter(0, 0, c='green', edgecolors='none', s=50) # ПЕРВАЯ ТОЧКА
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='yellow', edgecolors='none', s=50)
    """Скрываем оси координат"""
    ax.get_xaxis().set_visible(False) # Видимости осей делаем FALSE
    ax.get_yaxis().set_visible(False)

    plt.show()

    try_again = input("Do you want to try again (y/n)? :")
    if try_again == 'n':
        break