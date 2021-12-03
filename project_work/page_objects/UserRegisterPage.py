import allure
import random
import string
import names
from selenium.webdriver.common.by import By
from .BasePage import BasePage
from .TestData import TestDataUserRegistration


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
    # Элемент - warn alert об обязательности заполнения Privacy Policy
    POLICY_WARN_ALERT = (By.CSS_SELECTOR, "div[class='alert alert-danger alert-dismissible']")
    # Элемент - label (заголовок) поля 'First Name'
    FIRST_NAME_LABEL = (By.CSS_SELECTOR, "#account > div:nth-child(3) > label")
    # Элемент - текст text danger при незаполненном поле 'First Name'
    FIRST_NAME_TEXT_DANGER = (By.CSS_SELECTOR, "#account > div:nth-child(3) > div > div")
    # Элемент - группа элементов 'First Name'
    FIRST_NAME_ELEM_GROUP = (By.CSS_SELECTOR, "#account > div:nth-child(3)")
    # Элемент - label (заголовок) поля 'Last Name'
    LAST_NAME_LABEL = (By.CSS_SELECTOR, "#account > div:nth-child(4) > label")
    # Элемент - текст text danger при незаполненном поле 'Last Name'
    LAST_NAME_TEXT_DANGER = (By.CSS_SELECTOR, "#account > div:nth-child(4) > div > div")
    # Элемент - группа элементов 'Last Name'
    LAST_NAME_ELEM_GROUP = (By.CSS_SELECTOR, "#account > div:nth-child(4)")
    # Элемент - label (заголовок) поля 'E-Mail'
    EMAIL_LABEL = (By.CSS_SELECTOR, "#account > div:nth-child(5) > label")
    # Элемент - текст text danger при незаполненном поле 'E-Mail'
    EMAIL_TEXT_DANGER = (By.CSS_SELECTOR, "#account > div:nth-child(5) > div > div")
    # Элемент - группа элементов 'E-Mail'
    EMAIL_ELEM_GROUP = (By.CSS_SELECTOR, "#account > div:nth-child(5)")

    @allure.step("Entering data into chosen input")
    def fill_in_input(self, value: str):
        if value == 'First Name':
            first_name = names.get_first_name()
            element = self.find_element(UserRegisterPage.FIRST_NAME_INPUT)
            element.send_keys(first_name)
            self.logger.info(
                "Filling in input '{}' with value '{}'".format(value, first_name))
        elif value == "Last Name":
            last_name = names.get_last_name()
            element = self.find_element(UserRegisterPage.LAST_NAME_INPUT)
            element.send_keys(last_name)
            self.logger.info(
                "Filling in input '{}' with value '{}'".format(value, last_name))
        elif value == "E-Mail":
            e_mail_generated_part = str(random.randint(1, 1000)) + "_" + random.choice(string.ascii_letters).lower()
            element = self.find_element(UserRegisterPage.EMAIL_INPUT)
            element.send_keys(TestDataUserRegistration.EMAIL_PART + e_mail_generated_part + "@gmail.com")
            self.logger.info("Filling in input '{}' with value '{}'".format(value,
                                                                        TestDataUserRegistration.EMAIL_PART + e_mail_generated_part + "@gmail.com"))
        elif value == "Telephone":
            element = self.find_element(UserRegisterPage.TELEPHONE_INPUT)
            element.send_keys(TestDataUserRegistration.PHONE_NUMBER)
            self.logger.info(
                "Filling in input '{}' with value '{}'".format(value, TestDataUserRegistration.PHONE_NUMBER))
        elif value == "Password":
            element = self.find_element(UserRegisterPage.PASS_INPUT)
            element.send_keys(TestDataUserRegistration.PASS_DATA)
            self.logger.info(
                "Filling in input '{}' with value '{}'".format(value, TestDataUserRegistration.PASS_DATA))
        elif value == "Password Confirm":
            element = self.find_element(UserRegisterPage.CONFIRM_PASS_INPUT)
            element.send_keys(TestDataUserRegistration.PASS_CONFIRM_DATA)
            self.logger.info(
                "Filling in input '{}' with value '{}'".format(value, TestDataUserRegistration.PASS_CONFIRM_DATA))

    @allure.step("Entering all data into inputs of the new user registration form")
    def fill_in_register_form(self):
        self.fill_in_input('First Name')
        self.fill_in_input('Last Name')
        self.fill_in_input('E-Mail')
        self.fill_in_input('Telephone')
        self.fill_in_input('Password')
        self.fill_in_input('Password Confirm')

    @allure.step("Entering data into registration form without one field")
    def fill_in_register_form_without_field(self, value: str):
        if value == "First Name":
            self.fill_in_register_form()
            self.find_element(UserRegisterPage.FIRST_NAME_INPUT).clear()
            self.logger.info("Filling the form without element '{}'".format(value))
        elif value == "Last Name":
            self.fill_in_register_form()
            self.find_element(UserRegisterPage.LAST_NAME_INPUT).clear()
            self.logger.info("Filling the form without element '{}'".format(value))
        elif value == "E-Mail":
            self.fill_in_register_form()
            self.find_element(UserRegisterPage.EMAIL_INPUT).clear()
            self.logger.info("Filling the form without element '{}'".format(value))
        elif value == "Telephone":
            self.fill_in_register_form()
            self.find_element(UserRegisterPage.TELEPHONE_INPUT).clear()
            self.logger.info("Filling the form without element '{}'".format(value))
        elif value == "Password":
            self.fill_in_register_form()
            self.find_element(UserRegisterPage.PASS_INPUT).clear()
            self.logger.info("Filling the form without element '{}'".format(value))
        elif value == "Password Confirm":
            self.fill_in_register_form()
            self.find_element(UserRegisterPage.CONFIRM_PASS_INPUT).clear()
            self.logger.info("Filling the form without element '{}'".format(value))

    @allure.step("Agreeing with policy agreement")
    def agree_with_policy(self):
        self.simple_click(self.AGREE_POLICY_BOX)

    @allure.step("Pushing continue button")
    def push_continue_btn(self):
        self.simple_click(self.CONTINUE_BTN)

    @allure.step("Checking 'has-error' class exists with element")
    def element_has_error_class(self, locator: tuple):
        if 'has-error' in self.get_property(locator, "className"):
            self.logger.info("Checking 'has-error' class exists with element {}".format(locator))
            return True
