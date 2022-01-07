from selenium.webdriver.common.by import By
from .BasePage import BasePage


# Класс с локаторами элементов страницы Поиска
class SearchGroup(BasePage):
    # Элемент - группа 'Search input + button'
    SEARCH_GROUP = (By.CSS_SELECTOR, "#search")
    # Элемент - input для ввода текстовой информации
    SEARCH_INPUT = (By.CSS_SELECTOR, "input[name=search]")
    # Элемент - кнопка поиск (с иконкой 'лупа')
    SEARCH_BTN = (By.CSS_SELECTOR, "button[class='btn btn-default btn-lg']")
