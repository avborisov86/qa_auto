import books
import users

if __name__ == '__main__':

    # Читаем данные из файла 'csv' и сохраняем в переменную 'books_list'
    books_list = books.read_books(books.csv_file)

    # Читаем данные из файла 'json' и сохраняем в переменную 'users_list'
    users_list = users.read_users(users.json_file)

    # Перебираем все книги в списке и распределяем поровну между всеми студентами (кому-то досталось больше на одну)
    while len(books_list) > 0:
        for user in users_list:
            if len(books_list) == 0:
                break
            else:
                user.books.append(books_list.pop(0))

    # Делаем encoding данных в формат json и записываем в новый файл result.json
    users.write_users(users_list, users.result_json_file)
