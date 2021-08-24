from selenium.webdriver.common.by import By


# Класс с локаторами элементов страницы Каталога
class CatalogPageLocators:
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
