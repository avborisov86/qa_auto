"""
School: OTUS "QA Automation"
Task 4: Making selectors classes of elements at different pages
Author: Anton Borisov
"""

from selenium.webdriver.common.by import By


class mainPageSelectors:
    # Элемент - главный слайдер
    MAIN_SLIDER = (By.CSS_SELECTOR, "#slideshow0")
    # Элемент - корзина
    CART = (By.CSS_SELECTOR, "#cart")
    # Элемент - поиск
    SEARCH = (By.CSS_SELECTOR, "#search")
    # Элемент - карусель логотипов под карточками с товарами
    LOGO_CAROUSEL = (By.CSS_SELECTOR, "#carousel0")
    # Элемент - все элементы товаров на странице
    PRODUCTS = (By.CSS_SELECTOR, ".product-layout")


class catalogPageSelectors:
    # Элемент - боковое меню
    ASIDE_MENU = (By.CSS_SELECTOR, "#column-left")
    # Элемент - баннер под боковым меню
    BANNER = (By.CSS_SELECTOR, "#banner0")
    # Элемент - кнопка для переключения режима отображения в построчный
    LIST_VIEW_BTN = (By.CSS_SELECTOR, "#list-view")
    # Элемент - кнопка для переключения режима отображения в сетку
    GRID_VIEW_BTN = (By.CSS_SELECTOR, "#grid-view")
    # Элемент - все элементы товаров на странице
    PRODUCTS = (By.CSS_SELECTOR, ".product-layout")


class productPageSelectors:
    # Элемент со всеми изображениями товара
    THUMB_ELEM = (By.CSS_SELECTOR, ".thumbnails")
    # Элемент - количество изображений товара
    THUMB_QTY = (By.CSS_SELECTOR, ".thumbnail")
    # Элемент - название товара
    PROD_TITLE = (By.CSS_SELECTOR, "div.btn-group + h1")
    # Элемент - поле для ввода количества товара
    QTY_INPUT = (By.CSS_SELECTOR, "input[name = \"quantity\"]")
    # Элемент - кнопка "положить в корзину"
    CART_BTN = (By.CSS_SELECTOR, "#button-cart")


class authAdminPageSelectors:
    # Элемент - заголовок формы аутентификации
    AUTH_FORM_TITLE = (By.CSS_SELECTOR, ".panel-title")
    # Элемент - поле ввода логина
    LOGIN_INPUT = (By.CSS_SELECTOR, "#input-username")
    # Элемент - поле ввода пароля
    PASS_INPUT = (By.CSS_SELECTOR, "#input-password")
    # Элемент - ссылка Забыли пароль?
    FORGOT_PASS_BTN = (By.CSS_SELECTOR, ".help-block")
    # Элемент - кнопка Войти
    LOGIN_BTN = (By.CSS_SELECTOR, "button[type=submit]")
