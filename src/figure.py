"""
School: OTUS "QA Automation"
Task: describe class 'figure' and its attributes
Author: Anton Borisov
"""

from abc import ABC, abstractmethod


class Figure(ABC):
    name: str
    area: int
    perimeter: int

    # Вычисляем площадь
    @abstractmethod
    def get_area(self):
        pass

    # Вычисляем периметр
    @abstractmethod
    def get_perimeter(self):
        pass

    # Cуммируем площади фигур
    @abstractmethod
    def add_area(self, other_figure):
        pass
