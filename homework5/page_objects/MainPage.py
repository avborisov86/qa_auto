from selenium.webdriver.common.by import By


# Класс с локаторами элементов Главной страницы
class MainPageLocators:
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
