import homework2

if __name__ == '__main__':

    # Читаем данные из файла 'csv' и сохраняем в переменную 'books_list'
    books_list = homework2.read_books(homework2.csv_file)

    # Читаем данные из файла 'json' и сохраняем в переменную 'users_list'
    users_list = homework2.read_users(homework2.json_file)

    # Перебираем все книги в списке и распределяем поровну между всеми студентами (кому-то досталось больше на одну)
    while len(books_list) > 0:
        for user in users_list:
            if len(books_list) == 0:
                break
            else:
                user.books.append(books_list.pop(0))

    # Делаем encoding данных в формат json и записываем в новый файл result.json
    homework2.write_users(users_list, homework2.result_json_file)
