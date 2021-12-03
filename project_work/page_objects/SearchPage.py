from selenium.webdriver.common.by import By
from .BasePage import BasePage

# Класс с локаторами элементов страницы Поиска
class SearchPage(BasePage):
    # Элемент - кнопка поиск
    SEARCH_BTN = (By.CSS_SELECTOR, "#button3-search")
    # Элемент - кнопка поиск
    SEARCH_INPUT = (By.CSS_SELECTOR, "#input-search")
