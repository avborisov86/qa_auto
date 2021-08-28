# Класс с данными элементов Главной страницы для проверки
class MainPageTestData:
    # id главного слайдера
    MAIN_SLIDER_ID = "slideshow0"
    # id корзины
    CART_ID = "cart"
    # id строки поиска
    SEARCH_ID = "search"
    # id карусели логотипов под карточками товаров
    LOGO_CAROUSEL_ID = "carousel0"
    # Количество карточек товара
    PRODUCT_CLASS_QTY = 4


# Класс с данными элементов Хедера
class HeaderTestData:
    # Значок валюты Евро
    EURO_SIGN_CHECK = '€'
    # Значение name у валюты Фунт
    GBP_SIGN_CHECK = '£'
    # Значение name у валюты Доллар
    USD_SIGN_CHECK = '$'


# Класс с данными элементов Продуктовой страницы
class ProductPageTestData:
    # Значение класса элемента со всеми изображениями товара
    THUMBS_ELEM_CLASS = 'thumbnails'
    # Количество изображений товара
    THUMBS_QTY = 4
    # Значение из заголовка h1
    PROD_TITLE_VALUE = 'MacBook Air'
    # Имя из поля ввода количества товара
    QTY_INPUT_NAME = 'quantity'
    # id кнопки "положить в козину"
    CART_BTN_ID = "button-cart"


# Класс с данными элементов страницы Каталога
class CatalogPageTestData:
    # id бокового меню
    ASIDE_MENU_ID = 'column-left'
    # id баннера
    BANNER_ID = 'banner0'
    # id кнопки для переключения режима отображения в построчный
    LIST_VIEW_BTN_ID = 'list-view'
    # id кнопки для переключения режима отображения в сетку
    GRID_VIEW_BTN_ID = 'grid-view'
    # Количество товаров на странице
    ALL_PRODUCTS_QTY = 5


# Класс с данными элементов страницы Регистрации пользователя
class UserRegisterPageTestData:
    # Данные для ввода First Name
    FIRST_NAME_DATA = 'Anton'
    # Данные для ввода Last Name
    LAST_NAME_DATA = 'Borisov'
    # Данные для ввода E-Mail
    EMAIL_DATA = 'automation'
    # Данные для ввода Telephone
    TELEPHONE_DATA = '89278956767'
    # Данные для ввода Password
    PASS_DATA = 'qwerty987'
    # Данные для ввода Password Confirm
    PASS_CONFIRM_DATA = 'qwerty987'
    # Название страницы с упешной регистрацией
    SUCCESS_REGISTER_PAGE_TITLE = 'Your Account Has Been Created!'


# Класс с данными элементов страницы Аутентификации
class AuthPageTestData:
    # Логин входа в админку
    USER_LOGIN = 'user'
    # Пароль входа в админку
    USER_PASS = 'bitnami'
    # Значение из заголовка формы h1
    AUTH_FORM_TITLE_CHECK = ' Please enter your login details.'
    # Значение id поля ввода логина
    LOGIN_INPUT_ID = 'input-username'
    # Значение id поля ввода пароля
    PASS_INPUT_ID = 'input-password'
    # Текст ссылки в поле "Забыли пароль"
    FORGOT_PASS_TEXT = 'Forgotten Password'
    # Тип кнопки отправки формы аутентификации
    LOGIN_BTN_TYPE = 'submit'


# Класс с данными элементов страницы Админки (каталог/продукты)
class AdminCatalogProductsPageTestData:
    # Текст элемента после удаления всех продуктов в каталоге
    NO_RESULTS_TEXT = 'No results!'
    # Данные для поля ввода "Product name"
    PROD_NAME_DATA = 'New product'
    # Данные для поля ввода "Meta tag title"
    META_TAG_TITLE_DATA = 'New product'
    # Данные для поля ввода "Model"
    MODEL_DATA = 'New model'
