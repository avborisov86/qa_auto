"""
School: OTUS "QA Automation"
First task: покрытие автотестами кода из файлов circle.py, rectangle.py, square.py, triangle.py
Author: Anton Borisov
"""
from homework1.src.figure import Figure
from homework1.src.square import Square
from homework1.src import Triangle
from homework1.src.rectangle import Rectangle
from homework1.src.circle import Circle

import pytest
import random
import math


# Проверяем запрет на создание экземпляров базового класса
def test_base_figure():
    with pytest.raises(TypeError):
        ekz = Figure()


# Проверяем корректность имени квадрата
def test_square_name():
    square = Square(5)
    assert square.name == 'square', "Имя square.name должно быть равно 'square'!"


# Проверяем, что задалась сторона квадрата
def test_square_side():
    square = Square(15)
    assert square.x == 15, "Сторона квадрата задана неверно!"


# Проверяем вычисление площади квадрата
def test_square_area():
    square = Square(10)
    assert square.area == square.x * square.x, "Площадь квадрата рассчитана неверно!"


# Проверяем вычисление периметра квадрата
def test_square_perimeter():
    square = Square(10)
    assert square.perimeter == square.x * 4, "Периметр квадрата рассчитан неверно!"


# Проверяем корректность имени треугольника
def test_triangle_name():
    triangle = Triangle(1, 2, 3, 4)
    assert triangle.name == 'triangle', "Имя triangle.name должно быть равно 'triangle'!"


# Проверяем, что задалась сторона треугольника X
def test_triangle_xside():
    x = random.randint(1, 6)
    triangle = Triangle(x, 4, 7, 10)
    assert triangle.x == x, "Сторона X треугольника задана неверно!"


# Проверяем, что задалась сторона треугольника Y
def test_triangle_yside():
    y = random.randint(10, 20)
    triangle = Triangle(2, y, 7, 10)
    assert triangle.y == y, "Сторона Y треугольника задана неверно!"


# Проверяем, что задалась сторона треугольника Z
def test_triangle_zside():
    z = random.randint(5, 10)
    triangle = Triangle(2, 8, z, 10)
    assert triangle.z == z, "Сторона Z треугольника задана неверно!"


# Проверяем, что задалась высота треугольника H
def test_triangle_height():
    h = random.randint(0, 125)
    triangle = Triangle(2, 8, 9, h)
    assert triangle.h == h, "Высота H треугольника задана неверно!"


# Проверяем вычисление площади треугольника
def test_triangle_area():
    triangle = Triangle(3, 4, 5, 8)
    assert triangle.area == triangle.x * triangle.h / 2, "Площадь треугольника задана неверно!"


# Проверяем вычисление периметра треугольника
def test_triangle_perimeter():
    triangle = Triangle(3, 4, 5, 8)
    assert triangle.perimeter == triangle.x + triangle.y + triangle.z, "Периметр треугольника задан неверно!"


# Проверяем корректность имени прямоугольника
def test_rectangle_name():
    rectangle = Rectangle(1, 6)
    assert rectangle.name == 'rectangle', "Имя rectangle.name должно быть равно 'rectangle'!"


# Проверяем, что задалась сторона прямоугольника X
def test_rectangle_xside():
    x = random.randint(10, 56)
    rectangle = Rectangle(x, 34)
    assert rectangle.x == x, "Сторона X прямоугольника задана неверно!"


# Проверяем, что задалась сторона прямоугольника Y
def test_rectangle_yside():
    y = random.randint(24, 123)
    rectangle = Rectangle(25, y)
    assert rectangle.y == y, "Сторона Y прямоугольника задана неверно!"


# Проверяем вычисление площади прямоугольника
def test_rectangle_area():
    rectangle = Rectangle(13, 45)
    assert rectangle.area == rectangle.x * rectangle.y, "Площадь прямоугольника задана неверно!"


# Проверяем вычисление периметра прямоугольника
def test_rectangle_perimeter():
    rectangle = Rectangle(56, 178)
    assert rectangle.perimeter == (rectangle.x + rectangle.y) * 2, "Периметр прямоугольника задана неверно!"


# Проверяем корректность имени круга
def test_circle_name():
    circle = Circle(6, math.pi)
    assert circle.name == 'circle', "Имя circle.name должно быть равно 'circle'!"


# Проверяем, что задался радиус круга
def test_circle_xside():
    circle = Circle(10, math.pi)
    assert circle.x == 10, "Радиус круга задан неверно!"


# Проверяем вычисление площади круга
def test_circle_area():
    circle = Circle(23, math.pi)
    assert circle.area == 23 * 23 * math.pi, "Площадь круга задана неверно!"


# Проверяем вычисление периметра круга
def test_perimeter_circle():
    circle = Circle(16, math.pi)
    assert circle.perimeter == circle.x * 2 * math.pi, "Периметр круга задан неверно!"


# Проверяем добавление к площади трегольника площад другой фигуры (круга)
def test_rectangle_add_area_triangle():
    triangle = Triangle(4, 9, 1, 4)
    circle = Circle(34, math.pi)
    summ = triangle.add_area(circle)
    assert summ == triangle.area + circle.area, "Сумма площадей треугольника и круга рассчитана неверно!"


# Проверяем добавление к площади квадрата площади другой фигуры (прямоугольника)
def test_rectangle_add_area_square():
    square = Square(23)
    rectangle = Rectangle(4, 56)
    summ = square.add_area(rectangle)
    assert summ == square.area + rectangle.area, "Сумма площадей квадрата и прямоугольника рассчитана неверно!"


# Проверяем добавление к площади прямоугольника площади другой фигуры (круга)
def test_rectangle_add_area_circle():
    circle = Circle(12, math.pi)
    rectangle = Rectangle(10, 20)
    summ = circle.add_area(rectangle)
    assert summ == circle.area + rectangle.area, "Сумма площадей круга и прямоугольника рассчитана неверно!"