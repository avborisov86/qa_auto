import allure
from selenium.webdriver.common.by import By
from .BasePage import BasePage


class HeaderCurrency(BasePage):
    # Форма с элементами для изменения валюты на страницы
    CURRENCY_FORM = (By.CSS_SELECTOR, '#form-currency')
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
