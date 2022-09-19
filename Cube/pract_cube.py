from random import randint

class Cube:
    """Один кубик"""
    def __init__(self, num_sides=6):

        self.num_sides = num_sides

    def roll(self):
        """Случайное значение от 1 до 6"""
        return randint(1, self.num_sides)