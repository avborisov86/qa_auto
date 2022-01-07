import allure
import random
from selenium.webdriver.common.by import By
from .BasePage import BasePage


# Класс с локаторами элементов Корзины
class Cart(BasePage):
    # Элемент - кнопка корзины 'Shopping Cart' в хеадере
    SHOPPING_CART_BTN = (By.CSS_SELECTOR, "#top-links > ul > li:nth-child(4) > a")
    # Элемент - кнопка корзины
    CART_BTN = (By.CSS_SELECTOR, "button[class='btn btn-inverse btn-block btn-lg dropdown-toggle']")
    # Элемент - информационный блок на кнопке 'корзина' о валюте и количестве товаров в корзине
    CART_TOTAL_INFO = (By.CSS_SELECTOR, "#cart-total")
    # Элемент - заголовок всплывающего уведомления о том, что корзина пуста
    CART_EMPTY_NOTE = (By.CSS_SELECTOR, "#cart > ul > li > p")
    # Элемент - заголовок уведомления (p элемент) о том, что корзина пуста
    SHOPPING_CART_EMPTY_NOTE = (By.CSS_SELECTOR, "#content > p")
    # Элемент - информационный alert о добавлении товара в корзину
    ADD_ALERT = (By.CSS_SELECTOR, "div[class='alert alert-success alert-dismissible']")
    # Элемент - всплывающее меню с добавленным товаром
    CART_PROD_LINK = (By.CSS_SELECTOR, "#cart > ul > li > table > tbody > tr > td:nth-child(2) > a")
    # Элемент - кнопка "удалить товар" во всплывающем меню корзины
    CART_DEL_PROD = (By.CSS_SELECTOR, "#cart > ul > li > table > tbody > tr > td:nth-child(5) > button")
    # Элемент - любой из продуктов блока 'Featured' на главной странице
    ANY_FEATURED_PROD_PRICE = (
        By.CSS_SELECTOR, f"#content > div.row > div:nth-child({random.randint(1, 4)}) > div > div.caption > p.price")
    # Элемент - 'ADD TO CART' любого из продуктов блока 'Featured' на главной странице
    ADD_TO_CART_BUTTON_FEATURED_PROD = (By.CSS_SELECTOR, "#content > div.row > div > div > div.button-group > button")
    # Элемент - кнопка меню MP3 players
    MP3_MENU_BTN = (By.CSS_SELECTOR,
                    "#menu > div[class='collapse navbar-collapse navbar-ex1-collapse'] > ul > li:nth-child(8)")
    # Элемент - внутренняя кнопка меню MP3 players "Show all MP3 players"
    SHOW_ALL_MP3 = (By.CSS_SELECTOR,
                    "#menu > div[class='collapse navbar-collapse navbar-ex1-collapse'] > ul > li:nth-child(8) > div > a")
    # Элемент - первый продукт MP3 плеер (iPod Classic)
    FIRST_MP3_PRODUCT = (By.CSS_SELECTOR,
                         "#content > div:nth-child(8) > div:nth-child(1) > div > div:nth-child(2) > div[class='button-group'] > button")
    # Элемент - второй продукт MP3 плеер (iPod Nano)
    SECOND_MP3_PRODUCT = (By.CSS_SELECTOR,
                          "#content > div:nth-child(8) > div:nth-child(2) > div > div:nth-child(2) > div[class='button-group'] > button")
    # Элемент - третий продукт MP3 плеер (iPod Shuffle)
    THIRD_MP3_PRODUCT = (By.CSS_SELECTOR,
                          "#content > div:nth-child(8) > div:nth-child(3) > div > div:nth-child(2) > div[class='button-group'] > button")
    # Элемент - ряд (tr) во всплывающем меню корзины (для рассчета количества рядов  добавленными товарами)
    CART_PROD_ROWS_ADDED = (By.CSS_SELECTOR, "#cart > ul > li:nth-child(1) > table > tbody > tr")

    @allure.step("Opening all mp3 products page through main menu")
    def show_all_mp3(self):
        self.simple_click(self.MP3_MENU_BTN)
        self.move_and_click(self.SHOW_ALL_MP3)
