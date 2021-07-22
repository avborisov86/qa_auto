"""
School: OTUS "QA Automation"
Task 2: Reading from json files and filter / Writing result json file
Author: Anton Borisov
"""

import json
from json import JSONEncoder

# Задаем путь к файлу 'json' для чтения
json_file = '../homework2/users.json'
# Задаем путь к файлу 'json' для записи
result_json_file = '../homework2/result.json'


# Объявляем класс User с данными для задания структуры, соответствующей структуре результирующего файла
# (делается для того, чтобы выводить в список только нужные имена полей и данных (в исходнике много ненужных данных))
class User:
    name: str
    gender: str
    address: str
    age: str
    books: list

    # Объявляем конструктор класса
    def __init__(self, name, gender, address, age, **kwargs):
        self.name = name
        self.gender = gender
        self.address = address
        self.age = age
        self.books = []

    # Объявляем метод класса для вывода данных в соответствии с заданной строковой структурой
    def __str__(self):
        return "User: name is %s, gender is %s, address is %s, age is %s, books: %s" % (
            self.name, self.gender, self.address, self.age, self.books)


# Функция, которая открывает на чтение файл 'json' и возвращает список с данными из файла
def read_users(read_filename):
    with open(read_filename, 'r', encoding='utf-8') as file:
        users = []
        users_obj = json.load(file)
        for user in users_obj:
            users.append(User(**user))
        return users


# Объявляем класс для чтения данных из полученного объекта
class MyEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


# Функция для чтения данных из полученного списка объектов (представление данных в формате json)
def encode_data(data):
    result = json.dumps(data, cls=MyEncoder)
    return result


# Функция, которая делает encoding отфильтрованных данных и создает новый файл json для записи данных в него
def write_users(data, write_filename):
    data = json.dumps(data, cls=MyEncoder)
    data = json.loads(data)
    with open(write_filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)
