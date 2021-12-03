import allure
from selenium.webdriver.common.by import By
from .BasePage import BasePage


# Класс с локаторами элементов Главной страницы
class MainPage(BasePage):
    # Элемент - поиск (input + button search)
    SEARCH_GROUP = (By.CSS_SELECTOR, "#search")
    # Элемент - input для ввода текстовой информации
    SEARCH_INPUT = (By.CSS_SELECTOR, "input[name=search]")
    # Элемент - кнопка поиск
    SEARCH_BTN = (By.CSS_SELECTOR, "button[class='btn btn-default btn-lg']")
    # Элемент - кнопка корзины
    CART_BTN = (By.CSS_SELECTOR, "button[class='btn btn-inverse btn-block btn-lg dropdown-toggle']")
    # Элемент - заголовок всплывающего уведомления о том, что корзина пуста
    CART_EMPTY_NOTE = (By.CSS_SELECTOR, "#cart > ul > li > p")
    # Элемент - кнопка меню MP3 players
    MP3_MENU_BTN = (By.CSS_SELECTOR,
                    "#menu > div[class='collapse navbar-collapse navbar-ex1-collapse'] > ul > li:nth-child(8)")
    # Элемент - внутренняя кнопка меню MP3 players "Show all MP3 players"
    SHOW_ALL_MP3 = (By.CSS_SELECTOR,
                    "#menu > div[class='collapse navbar-collapse navbar-ex1-collapse'] > ul > li:nth-child(8) > div > a")
    # Элемент - произвольный товар MP3
    FIRST_MP3_PRODUCT = (By.CSS_SELECTOR,
                         "#content > div:nth-child(8) > div:nth-child(1) > div > div:nth-child(2) > div[class='button-group'] > button")
    # Элемент - информационный alert о добавлении товара в корзину
    ADD_ALERT = (By.CSS_SELECTOR, "div[class='alert alert-success alert-dismissible']")
    # Элемент - всплывающее меню с добавленным товаром
    CART_PROD_LINK = (By.CSS_SELECTOR, "#cart > ul > li > table > tbody > tr > td:nth-child(2) > a")
    # Элемент - кнопка "удалить товар" во всплывающем меню корзины
    CART_DEL_PROD = (By.CSS_SELECTOR, "#cart > ul > li > table > tbody > tr > td:nth-child(5) > button")

    # cart > ul > li:nth-child(1) > table > tbody > tr > td:nth-child(5) > button

    @allure.step("Opening all mp3 products page through main menu")
    def show_all_mp3(self):
        self.simple_click(self.MP3_MENU_BTN)
        self.move_and_click(self.SHOW_ALL_MP3)
