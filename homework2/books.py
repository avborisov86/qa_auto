"""
School: OTUS "QA Automation"
Task 2: Reading from csv files
Author: Anton Borisov
"""

from csv import DictReader

# Задаем путь к файлу 'csv' для чтения
csv_file = '../homework2/books.csv'


# Объявляем класс 'Book' с данными для задания структуры, соответствующей структуре результирующего файла
# (делается для того, чтобы выводить в список только нужные имена полей и данных)
class Book:
    title: str
    author: str
    pages: int
    genre: str

    def __init__(self, title, author, pages, genre):
        self.title = title
        self.author = author
        self.pages = pages
        self.genre = genre

    # Объявляем метод класса для вывода данных в соответствии с заданной строковой структурой
    def __str__(self):
        return "Book: title is %s, author is %s, pages is %s, genre is %s" % (
            self.title, self.author, self.pages, self.genre)


# Функция, которая открывает на чтение файл 'csv' и возвращает список с данными из файла в нужной структуре
def read_books(filename):
    books = []
    # Открываем с помощью менеджера контекста 'csv' файл
    with open(filename, 'r') as file:
        reader = DictReader(file)
        # Создаем итератор полученного из файла объекта
        iterator = iter(reader)
        # Иттерируемся по каждой строке данных, выбирая нужные данные и складывая их по порядку в ряды с нужными ключами
        while True:
            try:
                row = next(iterator)
                books.append(Book(title=row['Title'], author=row['Author'], pages=row['Pages'], genre=row['Genre']))
            except StopIteration:
                break
        return books
