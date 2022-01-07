from selenium.webdriver.common.by import By
from .BasePage import BasePage


class HeaderMyAccount(BasePage):
    # Кнопка "My Account" в топ меню
    MY_ACCOUNT_BTN = (By.CSS_SELECTOR, '#top-links > ul > li:nth-child(2)')
    # Кнопка Register в "My Account"
    REGISTER_BTN = (By.CSS_SELECTOR, '#top-links > ul > li:nth-child(2) > ul > li')
