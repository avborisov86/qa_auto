from selenium.webdriver.common.by import By
from homework5.page_objects.BasePage import BasePage
from homework5.page_objects.TestData import UserRegisterPageTestData
import random
import string


# Класс с локаторами элементов Хедера
class UserRegisterPage(BasePage):
    # Поле ввода First Name
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, '#input-firstname')
    # Поле ввода Last Name
    LAST_NAME_INPUT = (By.CSS_SELECTOR, '#input-lastname')
    # Поле ввода Email
    EMAIL_INPUT = (By.CSS_SELECTOR, '#input-email')
    # Поле ввода Telephone
    TELEPHONE_INPUT = (By.CSS_SELECTOR, '#input-telephone')
    # Поле ввода Password
    PASS_INPUT = (By.CSS_SELECTOR, '#input-password')
    # Поле ввода подтверждения Password
    CONFIRM_PASS_INPUT = (By.CSS_SELECTOR, '#input-confirm')
    # Чек-бокс подтверждения прочтения соглашения
    AGREE_POLICY_BOX = (By.CSS_SELECTOR, "input[name=agree")
    # Кнопка "Продолжить регистрацию"
    CONTINUE_BTN = (By.CSS_SELECTOR, "input[value=Continue")
    # Блок с информацией об успешной регистрации
    SUCCESS_BLOCK = (By.CSS_SELECTOR, "#common-success")

    def enter_data(self, value: str):
        if value == 'First Name':
            element = self.find_element(UserRegisterPage.FIRST_NAME_INPUT)
            element.send_keys(UserRegisterPageTestData.FIRST_NAME_DATA)
        elif value == "Last Name":
            element = self.find_element(UserRegisterPage.LAST_NAME_INPUT)
            element.send_keys(UserRegisterPageTestData.LAST_NAME_DATA)
        elif value == "E-Mail":
            element = self.find_element(UserRegisterPage.EMAIL_INPUT)
            element.send_keys(UserRegisterPageTestData.EMAIL_DATA + str(random.randint(1, 1000)) + "_" + random.choice(
                string.ascii_letters) + "@gmail.com")
        elif value == "Telephone":
            element = self.find_element(UserRegisterPage.TELEPHONE_INPUT)
            element.send_keys(UserRegisterPageTestData.TELEPHONE_DATA)
        elif value == "Password":
            element = self.find_element(UserRegisterPage.PASS_INPUT)
            element.send_keys(UserRegisterPageTestData.PASS_DATA)
        elif value == "Password Confirm":
            element = self.find_element(UserRegisterPage.CONFIRM_PASS_INPUT)
            element.send_keys(UserRegisterPageTestData.PASS_CONFIRM_DATA)

    def fill_in_register_form(self):
        self.enter_data('First Name')
        self.enter_data('Last Name')
        self.enter_data('E-Mail')
        self.enter_data('Telephone')
        self.enter_data('Password')
        self.enter_data('Password Confirm')

    def agree_with_policy(self):
        self.simple_click(self.AGREE_POLICY_BOX)

    def push_continue_btn(self):
        self.simple_click(self.CONTINUE_BTN)
