import allure
from selenium.webdriver.common.by import By
from homework5.page_objects.BasePage import BasePage


# Класс с локаторами элементов Хедера
class Header(BasePage):
    # Кнопка открытия выпадающего меню для выбора валют
    CURRENCY_BTN = (By.CSS_SELECTOR, '#form-currency > div > button')
    # Кнопка переключения валюты на Евро
    EURO = (By.CSS_SELECTOR, 'button[name=EUR]')
    # Кнопка переключения валюты на Фунты
    GBP = (By.CSS_SELECTOR, 'button[name=GBP]')
    # Кнопка переключения валюты на Доллары
    USD = (By.CSS_SELECTOR, 'button[name=USD]')
    # Знак отображения разных валют
    CURRENCY_SIGN = (By.CSS_SELECTOR, '#form-currency > div > button > strong')

    @allure.step("Changing currency to chosen value")
    def change_currency_to(self, value: str):
        self.find_element(self.CURRENCY_BTN, 2).click()
        if value == "EUR":
            self.find_element(self.EURO, 2).click()
        elif value == "GBP":
            self.find_element(self.GBP, 2).click()
        elif value == "USD":
            self.find_element(self.USD, 2).click()
