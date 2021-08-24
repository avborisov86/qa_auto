from selenium.webdriver.common.by import By


# Класс с локаторами элементов Продуктовой страницы
class ProductPageLocators:
    # Элемент со всеми изображениями товара
    THUMBS_ELEM = (By.CSS_SELECTOR, ".thumbnails")
    # Элемент - количество изображений товара
    THUMBS_QTY = (By.CSS_SELECTOR, ".thumbnail")
    # Элемент - название товара
    PROD_TITLE = (By.CSS_SELECTOR, "div.btn-group + h1")
    # Элемент - поле для ввода количества товара
    QTY_INPUT = (By.CSS_SELECTOR, "input[name=quantity]")
    # Элемент - кнопка "положить в корзину"
    CART_BTN = (By.CSS_SELECTOR, "#button-cart")
