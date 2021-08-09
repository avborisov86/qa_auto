# qa_hw1
Наименование удаленного репозитория на Git "qa_hw1"
Каждое домашнее задание хранится в отдельном Package  

**Homework # 1**

_Package "src"_

Заголовок: "Основы ООП (работа с классами) / первые автотесты покрывающие логику работы с геметрическими фигурами"

...
...


**Homework # 2**

_Package "homework2"_

Заголовок: "Парсинг данных из json и csv / выгрузка результата во внешний файл json" 

1. Точка входа для запуска приложения - "main.py"

2. Логика для парсинга данных из файла "books.csv" и сохранения их в нужном формате для Python расположена в файле "books.py"
   read_books() - открывает на чтение файл 'csv' и возвращает список с данными из файла в нужной структуре
   
3. Логика для парсинга данных из файла "users.json", сохранение данных в нужном формате для Python и дальнейшая запись в файл расположена в файле "users.py"
   read_users() - читает файл 'json' и возвращает список с данными из файла
   encode_data() - чтение данных из полученного списка объектов и представление в формате json
   write_users() - encoding отфильтрованных данных и создание нового файла json для записи данных в него
   

**Homework # 3**

_Package "homework3"_

Заголовок: "Тестирование API сервисов"

1. Вся логика отправки запросов на API сервисы расположена в файлах (возвращается json формат данных):

service1.py - "https://dog.ceo/dog-api/"
   
   'get_random_img_all()' - не принимает на вход никаких аргументов и возвращает одну картинку любой собаки любой породы
   'get_multiple_img_all()' - не принимает на вход никаких аргументов и возвращает несколько (три) картинок любых собак
   'get_random_img_subbreed(breed)' - принимает на вход параметр ('breed' - порода собаки) и возвращает одну 
   случайную картинку из подпороды собак _(функция используется для параметризированных тестов)_
   'get_random_img_breed(breed)' - принимает на вход параметр ('breed' - порода собаки) и возвращает одну
   случайную картинку собаки по ее попроде _(функция используется для параметризированных тестов)_
   'get_multiple_img_breed(breed)' - принимает на вход параметр ('breed' - порода собаки) и возвращает нескольких 
   случайных картинок собак по их породе _(функция используется для параметризированных тестов)_
   
service2.py - "https://www.openbrewerydb.org/"
   
   'get_brewery_city(brew_city)' - принимает на вход параметр ('brew_city' - город пивоварни) и возвращает список 
   пивоарен по наименованию города _(функция используется для параметризированных тестов)_
   'get_brewery_type(brew_type)' - принимает на вход параметр ('brew_type' - тип пивоварни) и возвращает список 
   пивоарен по их типу _(функция используется для параметризированных тестов)_
   'get_brewery_quantity(elem_page)' - принимает на вход параметр ('elem_page' - количество элементов на странице) 
   и возвращает заданное количество элементов на странице _(функция используется для параметризированных тестов)_
   'get_brewery_by_id(brew_id)' - принимает на вход параметр ('brew_id' - id пивоварни) и возвращает одну 
   пивоарню по ее id _(функция используется для параметризированных тестов)_
   'get_brewery_by_postal_code(brew_postal)' - принимает на вход параметр ('brew_postal' - почтовый индекс пивоварни) 
   и возвращает одну пивоварню по ее почтовому коду _(функция используется для параметризированных тестов)_

service3.py - "https://jsonplaceholder.typicode.com/"
      
   'get_posts_all()' - не принимает на вход никаких аргументов и возвращает все посты
   'get_comments_all()' - не принимает на вход никаких аргументов и возвращает все комментарии
   'get_photos_all()' - не принимает на вход никаких аргументов и возвращает все фотографии
   'get_post_by_id(brew_id)' - принимает на вход параметр ('brew_id' - id пивоварни) и возвращает одну пивоварню 
   по ее id _(функция используется для параметризированных тестов)_
   'get_comments_by_postid(post_id)' - принимает на вход параметр ('post_id' - postid пивоварни) и возвращает одну пивоварню 
   по ее postid _(функция используется для параметризированных тестов)_

2. Все тесты для полученных данных от API сервисов расположены в файлах:

test_service1.py - "https://dog.ceo/dog-api/"

   'test_random_img_all()' - тестовая функция, использующая функцию 'get_random_img_all()' для получения данных 
   1. проверяет наличие 'message' в ответе
   2. проверяет наличие 'status' в ответе
   3. проверяет статус ответа на 'success'
   4. проверяет наличие картинки в ответе
   
   'test_multiple_img()' - тестовая функция, использующая функцию 'get_random_img_all()' для получения данных   
   1. проверяет наличие 'message' в ответе
   2. проверяет наличие 'status' в ответе
   3. проверяет количество полученных элементов = 3(три)
   4. проверяет статус ответа на 'success'

   'test_random_img_subbreed(breed='english')' - тестовая функция, использующая функцию 'get_random_img_subbreed(breed)' 
   для получения данных
   1. проверяет наличие 'message' в ответе
   2. проверяет наличие 'status' в ответе
   3. проверяет статус ответа на 'success'
   4. проверяет наличие окнчания '.jpg'/'.jpeg' в строке элемента 'message'

   'test_random_breed(breed)' - тестовая функция, использующая функцию 'get_random_img_breed(breed)' 
   для получения данных / _используется параметризация входных параметров_
   1. проверяет наличие 'message' в ответе
   2. проверяет наличие 'status' в ответе
   3. проверяет статус ответа на 'success'
   4. проверяет наличие окнчания '.jpg'/'.jpeg' в строке элемента 'message'      

   'test_multiple_image_breed(breed)' - тестовая функция, использующая функцию 'get_multiple_img_breed(breed)' 
   для получения данных / _используется параметризация входных параметров_
   1. проверяет наличие 'message' в ответе
   2. проверяет наличие 'status' в ответе
   3. проверяет статус ответа на 'success'
   4. проверяет количество полученных элементов = 3(три)

test_service2.py - "https://www.openbrewerydb.org/"
   
   'test_brewery_city(brew_city)' - тестовая функция, использующая функцию 'get_brewery_city(brew_city)' 
   для получения данных / _используется параметризация входных параметров_
   1. проверяет наличие элемента 'city' в случайном элементе ответа
   2. проверяет соответствие названия города, отправляемого в запросе и получаемого в ответе

   test_brewery_type(brew_type) - тестовая функция, использующая функцию 'get_brewery_type(brew_type)' 
   для получения данных / _используется параметризация входных параметров_
   1. проверяет наличие элемента 'brewery_type' в случайном элементе ответа
   2. проверяет соответствие типа пивоварни, отправляемого в запросе и получаемого в ответе

   'test_brewery_quantity(elem_page)' - тестовая функция, использующая функцию 'get_brewery_quantity(elem_page)' 
   для получения данных / _используется параметризация входных параметров_
   1. проверяет соовтетствие количества полученных элементов ответа и отправленных в запросе

   'test_brewery_by_id(brew_id)' - тестовая функция, использующая функцию 'get_brewery_by_id(brew_id)' 
   для получения данных / _используется параметризация входных параметров_
   1. проверяет наличие элемента 'id' полученном элементе ответа
   2. проверяет соответствие 'id' пивоварни, отправляемого в запросе и получаемого в ответе

   'test_brewery_by_postal_code(brew_postal)' - тестовая функция, использующая функцию 'get_brewery_by_postal_code(brew_postal)' 
   для получения данных / _используется параметризация входных параметров_
   1. проверяет наличие элемента 'postal_code' полученном элементе ответа
   2. проверяет соответствие 'postal_code' пивоварни, отправляемого в запросе и получаемого в ответе

test_service3.py - "https://jsonplaceholder.typicode.com/"

   'test_posts_all()' - тестовая функция, использующая функцию 'get_posts_all()' для получения данных
   1. проверяет наличие 'body' в ответе
   2. проверяет наличие 'userId' в ответе
   3. проверяет наличие 'title' в ответе
   4. проверяет наличие 'id' в ответе
   5. проверяет количество получаемых в ответе элементов = 100 (сто)

   'test_comments_all()' - тестовая функция, использующая функцию 'get_comments_all()' для получения данных
   1. проверяет наличие 'body' в ответе
   2. проверяет наличие 'email' в ответе
   3. проверяет наличие 'id' в ответе
   4. проверяет наличие 'name' в ответе
   5. проверяет наличие 'postId' в ответе
   5. проверяет количество получаемых в ответе элементов = 500 (пятьсот)

   'test_photos_all()' - тестовая функция, использующая функцию 'get_photos_all()' для получения данных
   1. проверяет наличие 'albumId' в ответе
   2. проверяет наличие 'id' в ответе
   3. проверяет наличие 'thumbnailUrl' в ответе
   4. проверяет наличие 'title' в ответе
   5. проверяет наличие 'url' в ответе
   6. проверяет количество получаемых в ответе элементов = 5000 (пять тысяч)

   'test_post_by_id(brew_id)' - тестовая функция, использующая функцию 'get_brewery_quantity(elem_page)' 
   для получения данных / _используется параметризация входных параметров_
   1. проверяет наличие 'body' в ответе
   2. проверяет наличие 'id' в ответе
   3. проверяет наличие 'title' в ответе
   4. проверяет наличие 'userId' в ответе
   5. проверяет количество получаемых в ответе элементов = 4 (четыре)

   'test_comments_by_id(post_id)' - тестовая функция, использующая функцию 'get_comments_by_postid(post_id)' 
   для получения данных / _используется параметризация входных параметров_
   1. проверяет наличие 'body' в ответе
   2. проверяет наличие 'email' в ответе
   3. проверяет наличие 'id' в ответе
   4. проверяет наличие 'name' в ответе
   5. проверяет наличие 'postId' в ответе
   6. проверяет количество получаемых в ответе элементов = 5 (пять)



**Homework # 4**

_Package "homework4"_

Заголовок: "Настройка окружения Selenium, явные ожидания элементов, UI тесты на проверку наличия элемента на странице."

1. Все селекторы для поиска элементов расположены в репозитории page_objects/selectors.py
   
   class class mainPageSelectors описывает селекторы элементов главной страницы сайта https://demo.opencart.com   
   class catalogPageSelectors описывает селекторы элементов главной страницы сайта https://demo.opencart.com/index.php?route=product/category&path=18
   class productPageSelectors описывает селекторы элементов главной страницы сайта https://demo.opencart.com/index.php?route=product/product&path=18&product_id=44   
   class authAdminPageSelectors описывает селекторы элементов главной страницы сайта https://demo.opencart.com/admin/ 
   
2. Все исполняемые тесты расположены в репозитории tests
   
   test_main_page.py - тесты элементов главной страницы
   
   'test_slider_visibility(browser, url_base)' - тестовая функция, проверяющая видимость элемента "слайдер" на главной странице
   'test_cart_visibility(browser, url_base)' - тестовая функция, проверяющая видимость элемента "корзина" на главной странице
   'test_search_visibility(browser, url_base)' - тестовая функция, проверяющая видимость элемента "поиск" на главной странице
   'test_logo_swiper_visibility(browser, url_base)' - тестовая функция, проверяющая видимость элемента "карусель логотипов" на главной странице
   'test_products_visibility(browser, url_base)' - тестовая функция, проверяющая видимость 4х продуктовых карточек на главной странице
   
   test_catalog_page.py - тесты элементов страницы каталога

   'test_aside_menu_visibility(browser, url_cat)' - тестовая функция, проверяющая видимость элемента "боковое меню" на странице каталога
   'test_banner_visibility(browser, url_cat)' - тестовая функция, проверяющая видимость элемента "баннер" на странице каталога
   'test_list_btn_visibility(browser, url_cat)' - тестовая функция, проверяющая видимость элемента "кнопка вывода - list" на странице каталога
   'test_grid_btn_visibility(browser, url_cat)' - тестовая функция, проверяющая видимость элемента "кнопка вывода - grid" на странице каталога
   'test_products_visibility(browser, url_cat)' - тестовая функция, проверяющая видимость 5 продуктовых карточек на странице каталога с товарами
   
   test_product_page.py - тесты элементов страницы продукта

   'test_thumbnail_visibility(browser, url_prod)' - тестовая функция, проверяющая видимость элемента "все изображения товара в одном блоке" на странице товара 
   'test_thumbnails_qty_visibility(browser, url_prod)' - тестовая функция, проверяющая видимость 4х элементов "изображения товара" на странице товара 
   'test_product_title_visibility(browser, url_prod)' - тестовая функция, проверяющая видимость элемента "название товара" на странице товара
   'test_quantity_input_visibility(browser, url_prod)' - тестовая функция, проверяющая видимость элемента "поле для ввода количества товаров" на странице товара
   'test_cart_btn_visibility(browser, url_prod)' - тестовая функция, проверяющая видимость элемента "кнопка положить в корзину" на странице товара
   
   test_auth_admin_page.py - тесты элементов страницы входа в админку

   'test_form_title_visibility(browser, url_auth)' - тестовая функция, проверяющая видимость элемента "заголовок формы аутентификации" на странице входа в админку 
   'test_login_input_visibility(browser, url_auth)' - тестовая функция, проверяющая видимость элемента "поле ввода логина" на странице входа в админку
   'test_password_input_visibility(browser, url_auth)' - тестовая функция, проверяющая видимость элемента "поле ввода пароля" на странице входа в админку
   'test_forgot_password_visibility(browser, url_auth)' - тестовая функция, проверяющая видимость элемента "ссылка Забыли пароль" на странице входа в админку
   'test_login_btn_visibility(browser, url_auth)' - тестовая функция, проверяющая видимость элемента "кнопка Войти" на странице входа в админку
   
   

