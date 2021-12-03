import allure
from selenium.webdriver.common.by import By
from .BasePage import BasePage


class Header(BasePage):
    # Кнопка открытия выпадающего меню для выбора валют
    CURRENCY_BTN = (By.CSS_SELECTOR, '#form-currency > div > button')
    # Группа элементов с выбором значений разных валют
    CURRENCY_DROPDOWN_GROUP = (By.CSS_SELECTOR, '#form-currency > div')
    # Кнопка переключения валюты на Евро
    EURO_BTN = (By.CSS_SELECTOR, 'button[name=EUR]')
    # Кнопка переключения валюты на Фунты
    GBP_BTN = (By.CSS_SELECTOR, 'button[name=GBP]')
    # Кнопка переключения валюты на Доллары
    USD_BTN = (By.CSS_SELECTOR, 'button[name=USD]')
    # Знак отображения разных валют
    CURRENCY_SIGN = (By.CSS_SELECTOR, '#form-currency > div > button > strong')
    # Кнопка "My Account" в топ меню
    MY_ACCOUNT_BTN = (By.CSS_SELECTOR, '#top-links > ul > li:nth-child(2)')
    # Кнопка Register в "My Account"
    REGISTER_BTN = (By.CSS_SELECTOR, '#top-links > ul > li:nth-child(2) > ul > li')

    @allure.step("Changing currency to chosen value")
    def change_currency_to(self, value: str):
        self.simple_click(self.CURRENCY_BTN)
        if value == "EUR":
            self.simple_click(self.EURO_BTN)
        elif value == "GBP":
            self.simple_click(self.GBP_BTN)
        elif value == "USD":
            self.simple_click(self.USD_BTN)

    @allure.step("Checking 'open' class exists with element")
    def element_has_open_class(self, locator: tuple):
        if 'open' in self.get_property(locator, "className"):
            self.logger.info("Checking 'open' class exists with element {}".format(locator))
            return True
