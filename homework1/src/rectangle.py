"""
School: OTUS "QA Automation"
Task 1: describe class 'rectangle' and its attributes / работа с фигурой - прямоугольник
Author: Anton Borisov
"""

from homework1.src.figure import Figure


class Rectangle(Figure):
    name = 'rectangle'
    area = 0
    perimeter = 0

    x: int
    y: int

    # Создаем конструктор прямоугольника
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.area = self.get_area()
        self.perimeter = self.get_perimeter()

    # Вычисляем площадь прямоугольника
    def get_area(self):
        return self.x * self.y

    # Вычисляем периметр прямоугольника
    def get_perimeter(self):
        return 2 * (self.x + self.y)

    # К площади прямоугольника добавляем площадь другой фигуры
    def add_area(self, other_figure):
        if not isinstance(other_figure, Figure):
            raise ValueError('Object is not class of Figure')
        return self.area + other_figure.area
