# qa_hw1
Наименование удаленного репозитория на Git "qa_hw1"
Каждое домашнее задание хранится в отдельном Package  

**Homework # 1**

_Package "src"_

...
...


**Homework # 2**

_Package "homework2"_

Heading: "Парсинг json + csv" 

1. Точка входа для запуска приложения - "main.py"

2. Логика для парсинга данных из файла "books.csv" и сохранения их в нужном формате для Python расположена в файле "books.py"
   read_books() - открывает на чтение файл 'csv' и возвращает список с данными из файла в нужной структуре
   
3. Логика для парсинга данных из файла "users.json", сохранение данных в нужном формате для Python и дальнейшая запись в файл расположена в файле "users.py"
   read_users() - читает файл 'json' и возвращает список с данными из файла
   encode_data() - чтения данных из полученного списка объектов и представление в формате json
   write_users() - encoding отфильтрованных данных и создание нового файла json для записи данных в него
   