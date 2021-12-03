"""
School: OTUS "QA Automation"
Task 1: describe class 'square' and its attributes / работа с фигурой - квадрат
Author: Anton Borisov
"""

from homework1.src.figure import Figure


class Square(Figure):
    name = 'square'
    area = 0
    perimeter = 0

    x: int

    # Создаем конструктор квадрата
    def __init__(self, x):
        self.x = x
        self.area = self.get_area()
        self.perimeter = self.get_perimeter()

    # Вычисляем площадь квадрата
    def get_area(self):
        return self.x * self.x

    # Вычисляем периметр квадрата
    def get_perimeter(self):
        return self.x * 4

    # К площади квадрата добавляем площадь другой фигуры
    def add_area(self, other_figure):
        if not isinstance(other_figure, Figure):
            raise ValueError('Object is not class of Figure')
        return self.area + other_figure.area
