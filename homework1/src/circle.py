"""
School: OTUS "QA Automation"
Task 1: describe class 'circle' and its attributes / работа с фигурой - круг
Author: Anton Borisov
"""

from homework1.src.figure import Figure
import math


class Circle(Figure):
    name = 'circle'
    area = 0
    perimeter = 0
    pi = math.pi

    pi: float
    r: int

    # Создаем конструктор круга
    def __init__(self, x, pi):
        self.pi = pi
        self.x = x
        self.area = self.get_area()
        self.perimeter = self.get_perimeter()


    # Вычисляем площадь круга
    def get_area(self):
        return self.pi * (self.x * self.x)

    # Вычисляем площадь круга
    def get_perimeter(self):
        return self.pi * self.x * 2

    # К площади круга добавляем площадь другой фигуры
    def add_area(self, other_figure):
        if not isinstance(other_figure, Figure):
            raise ValueError('Object is not class of Figure')
        return self.area + other_figure.area
