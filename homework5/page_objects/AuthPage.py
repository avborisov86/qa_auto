from selenium.webdriver.common.by import By
from homework5.page_objects.BasePage import BasePage


class AuthPage(BasePage):
    # Элемент - заголовок формы аутентификации
    AUTH_FORM_TITLE = (By.CSS_SELECTOR, ".panel-title")
    # Элемент - поле ввода логина
    USERNAME_INPUT = (By.CSS_SELECTOR, "#input-username")
    # Элемент - поле ввода пароля
    PASS_INPUT = (By.CSS_SELECTOR, "#input-password")
    # Элемент - ссылка Забыли пароль?
    FORGOT_PASS_BTN = (By.CSS_SELECTOR, ".help-block")
    # Элемент - кнопка Войти
    LOGIN_BTN = (By.CSS_SELECTOR, "button[type=submit]")
    # Имя пользователя
    USERNAME_DATA = 'user'
    # Пароль пользователя
    PASSWORD_DATA = 'bitnami'

    def enter_login(self):
        self.find_element(self.USERNAME_INPUT, 2).send_keys(self.USERNAME_DATA)

    def enter_password(self):
        self.find_element(self.PASS_INPUT, 2).send_keys(self.PASSWORD_DATA)

    def push_login_btn(self):
        self.move_and_click(self.LOGIN_BTN)

    def enter_admin_page(self):
        self.find_element(self.USERNAME_INPUT, 2).send_keys(self.USERNAME_DATA)
        self.find_element(self.PASS_INPUT, 2).send_keys(self.PASSWORD_DATA)
        self.move_and_click(self.LOGIN_BTN)
