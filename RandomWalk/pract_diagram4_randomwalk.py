from random import choice

class RandomWalk:
    """Класс, который генерирует случайное блуждание"""
    def __init__(self, num_points=5000):  
        """Атрибуты блуждания"""
        self.num_points = num_points
        self.x_values = [0]  # два списка
        self.y_values = [0]  # блуждания начинаются с 0

    def get_step(self):

        x_direction = choice([1, -1])  # ф-ция CHOICE - "выбрать" 
        x_distance = choice([0, 1, 2, 3, 4, 5, 6])
        x_step = x_direction * x_distance

        y_direction = choice([1, -1])
        y_distance = choice([0, 1, 2, 3, 4, 5, 6])
        y_step = y_direction * y_distance

        x = self.x_values[-1] + x_step  # расчитываем новые позиции
        y = self.y_values[-1] + y_step

        self.x_values.append(x)
        self.y_values.append(y)

    
    def fill_walk(self): 
        """Вычисляем все точки блуждания""" 
        while len(self.x_values) < self.num_points: # делаем цикл, который будет работать до набора правильного кол-ва точек
            
            x_step = self.get_step()
            y_step = self.get_step()

            if x_step == 0 and y_step == 0: # убираем шаги, которые никуда не движутся
                continue


    