"""
School: OTUS "QA Automation"
Task 1: describe class 'triangle' and its attributes / работа с фигурой - треугольник
Author: Anton Borisov
"""

from homework1.src.figure import Figure


class Triangle(Figure):
    name = 'triangle'
    area = 0
    perimeter = 0

    x: int
    y: int
    z: int
    h: int

    # Создаем конструктор треугольника
    def __init__(self, x, y, z, h):
        self.x = x
        self.y = y
        self.z = z
        self.h = h
        self.area = self.get_area()
        self.perimeter = self.get_perimeter()

    # Вычисляем площадь треугольника
    def get_area(self):
        return self.x * self.h / 2

    # Вычисляем периметр треугольника
    def get_perimeter(self):
        return self.x + self.y + self.z

    # К площади трегуольника добавляем площадь другой фигуры
    def add_area(self, other_figure):
        if not isinstance(other_figure, Figure):
            raise ValueError('Object is not class of of Figure')
        return self.area + other_figure.area
