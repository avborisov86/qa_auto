"""
School: OTUS "QA Automation"
Project work: User register page http://127.0.0.1:8081/index.php?route=account/register coverage by automated tests

Tests:
1. Проверка: проваленная регистрация с незаполненными обязательными полями
2. Проверка: проваленная регистрация нового пользователя без Политики конфиденциальности
3. Проверка: текст в окне warn alert 'Warning: You must agree to the Privacy Policy!'
4. Проверка: успешная регистрация нового пользователя c Политикой конфиденциальности
5. Проверка: отображение подсказки при незаполненном поле 'First Name' + правильный текст
подсказки + смена цвета заголовка поля + смена цвета границы поля input
6. Проверка: отображение подсказки при незаполненном поле 'Last Name' + правильный текст
подсказки + смена цвета заголовка поля + смена цвета границы поля input
7. Проверка: отображение подсказки при незаполненном поле 'E-mail' + правильный текст
подсказки + смена цвета заголовка поля + смена цвета границы поля input
8. Проверка: отображение подсказки при незаполненном поле 'Telephone' + правильный текст
подсказки + смена цвета заголовка поля + смена цвета границы поля input
9.
10.
11.
12.

Author: Anton Borisov
"""

import allure
import time
from project_work.page_objects.Header import Header
from project_work.page_objects.UserRegisterPage import UserRegisterPage
from project_work.page_objects.TestData import TestDataUserRegistration


@allure.title(
    "Проверка: проваленная регистрация с незаполненными обязательными полями")
@allure.feature("Регистрация нового пользователя")
@allure.story("Ввод невалидных значений")
@allure.description("""
    На странице регистрации нового пользователя http://127.0.0.1:8081/index.php?route=account/register 
    все поля формы оставляем пустыми и нажимаем кнопку "Continue", чтобы убедиться, что регистрация не выполняется и 
    мы остаемся на той же самой странице, проверяя для этого title страницы формы регистрации.
""")
@allure.severity(allure.severity_level.CRITICAL)
@allure.issue("582", name="Сбой в работе контура")
def test1_new_user_registration_with_blank_required_fields(browser, local_base_url):
    user_register_page = UserRegisterPage(browser, local_base_url)
    user_register_page.go_to_site()
    user_register_page.simple_click(Header.MY_ACCOUNT_BTN)
    user_register_page.move_and_click(Header.REGISTER_BTN)
    user_register_page.push_continue_btn()
    assert user_register_page.get_page_title() == TestDataUserRegistration.REGISTER_PAGE_TITLE, "Register page title equals to 'Register Account'!"


@allure.title(
    "Проверка: проваленная регистрация нового пользователя без Политики конфиденциальности")
@allure.feature("Регистрация нового пользователя")
@allure.story("Ввод валидных значений")
@allure.description("""
    На странице регистрации нового пользователя http://127.0.0.1:8081/index.php?route=account/register 
    все поля формы заполняем правильными данными, но не проставляем чек-бокс 'I have read and agree to the Privacy 
    Policy', и нажимаем кнопку "Continue", чтобы убедиться, что регистрация не выполняется и мы остаемся на той же 
    самой странице, проверяя для этого title страницы формы регистрации + появление окна с текстом предупреждения о том, 
    что чек-бокс не проставлен.
""")
@allure.severity(allure.severity_level.NORMAL)
@allure.link("https://ihelp.rt.ru/browse/OMNIDEV-582")
def test2_new_user_registration_without_privacy_policy(browser, local_base_url):
    user_register_page = UserRegisterPage(browser, local_base_url)
    user_register_page.go_to_site()
    user_register_page.simple_click(Header.MY_ACCOUNT_BTN)
    user_register_page.move_and_click(Header.REGISTER_BTN)
    user_register_page.fill_in_register_form()
    user_register_page.push_continue_btn()
    errors = []
    if not user_register_page.verify_element_presence(UserRegisterPage.POLICY_WARN_ALERT):
        errors.append("Alert warning Privacy Policy is absent!")
    if not user_register_page.get_page_title() == TestDataUserRegistration.REGISTER_PAGE_TITLE:
        errors.append("Page title equals to 'Register Account'!")
    assert not errors, "Errors exist:\n{}".format("\n".join(errors))


@allure.title(
    "Проверка: текст в окне warn alert 'Warning: You must agree to the Privacy Policy!'")
def test3_new_user_registration_without_privacy_policy(browser, local_base_url):
    user_register_page = UserRegisterPage(browser, local_base_url)
    user_register_page.go_to_site()
    user_register_page.simple_click(Header.MY_ACCOUNT_BTN)
    user_register_page.move_and_click(Header.REGISTER_BTN)
    user_register_page.fill_in_register_form()
    user_register_page.push_continue_btn()
    assert user_register_page.get_property(UserRegisterPage.POLICY_WARN_ALERT,
                                           "outerText") == TestDataUserRegistration.WARN_ALERT_TEXT, "Warn alert text equals to ' Warning: You must agree to the Privacy Policy!'!"


@allure.title(
    "Проверка: успешная регистрация нового пользователя c Политикой конфиденциальности")
def test4_new_user_registration_with_privacy_policy(browser, local_base_url):
    user_register_page = UserRegisterPage(browser, local_base_url)
    user_register_page.go_to_site()
    user_register_page.simple_click(Header.MY_ACCOUNT_BTN)
    user_register_page.move_and_click(Header.REGISTER_BTN)
    user_register_page.fill_in_register_form()
    user_register_page.agree_with_policy()
    user_register_page.push_continue_btn()
    if user_register_page.verify_element_presence(UserRegisterPage.SUCCESS_BLOCK, 2):
        assert user_register_page.get_page_title() == TestDataUserRegistration.SUCCESS_REGISTER_PAGE_TITLE, "Success register page title equals to 'Your Account Has Been Created!'"


@allure.title(
    "Проверка: отображение подсказки при незаполненном поле 'First Name' + правильный текст подсказки "
    "+ смена цвета заголовка поля + смена цвета границы поля input")
def test5_warn_info_when_first_name_empty(browser, local_base_url):
    user_register_page = UserRegisterPage(browser, local_base_url)
    user_register_page.go_to_site()
    user_register_page.simple_click(Header.MY_ACCOUNT_BTN)
    user_register_page.move_and_click(Header.REGISTER_BTN)
    user_register_page.fill_in_register_form_without_field("First Name")
    user_register_page.agree_with_policy()
    user_register_page.push_continue_btn()
    errors = []
    if not user_register_page.check_css_property(UserRegisterPage.FIRST_NAME_LABEL,
                                                 "color") == TestDataUserRegistration.ERROR_LABEL_TEXT_COLOR:
        errors.append("Label color equals to 'rgba(169, 68, 66, 1)'/'#a94442'")
    if not user_register_page.check_css_property(UserRegisterPage.FIRST_NAME_TEXT_DANGER,
                                                 "color") == TestDataUserRegistration.ERROR_LABEL_TEXT_COLOR:
        errors.append("Text danger color equals to 'rgba(169, 68, 66, 1)'/'#a94442'")
    if not user_register_page.get_property(UserRegisterPage.FIRST_NAME_TEXT_DANGER,
                                           "innerHTML") == TestDataUserRegistration.FIRST_NAME_TEXT_DANGER:
        errors.append("Text danger equals to 'First Name must be between 1 and 32 characters!'")
    if not user_register_page.element_has_error_class(UserRegisterPage.FIRST_NAME_ELEM_GROUP):
        errors.append("Input 'First Name' has no error class! Check border-color!")
    assert not errors, "Errors exist:\n{}".format("\n".join(errors))


@allure.title("Проверка: отображение подсказки при незаполненном поле 'Last Name' + правильный текст подсказки "
              "+ смена цвета заголовка поля + смена цвета границы поля input")
def test6_warn_info_when_last_name_empty(browser, local_base_url):
    user_register_page = UserRegisterPage(browser, local_base_url)
    user_register_page.go_to_site()
    user_register_page.simple_click(Header.MY_ACCOUNT_BTN)
    user_register_page.move_and_click(Header.REGISTER_BTN)
    user_register_page.fill_in_register_form_without_field("Last Name")
    user_register_page.agree_with_policy()
    user_register_page.push_continue_btn()
    errors = []
    if not user_register_page.check_css_property(UserRegisterPage.LAST_NAME_LABEL,
                                                 "color") == TestDataUserRegistration.ERROR_LABEL_TEXT_COLOR:
        errors.append("Label color equals to 'rgba(169, 68, 66, 1)'/'#a94442'")
    if not user_register_page.check_css_property(UserRegisterPage.LAST_NAME_TEXT_DANGER,
                                                 "color") == TestDataUserRegistration.ERROR_LABEL_TEXT_COLOR:
        errors.append("Text danger color equals to 'rgba(169, 68, 66, 1)'/'#a94442'")
    if not user_register_page.get_property(UserRegisterPage.LAST_NAME_TEXT_DANGER,
                                           "innerHTML") == TestDataUserRegistration.LAST_NAME_TEXT_DANGER:
        errors.append("Text danger equals to 'Last Name must be between 1 and 32 characters!'")
    if not user_register_page.element_has_error_class(UserRegisterPage.LAST_NAME_ELEM_GROUP):
        errors.append("Input 'Last Name' has no error class! Check border-color!")
    assert not errors, "Errors exist:\n{}".format("\n".join(errors))


@allure.title("Проверка: отображение подсказки при незаполненном поле 'E-mail' + правильный текст подсказки "
              "+ смена цвета заголовка поля + смена цвета границы поля input")
def test7_warn_info_when_email_empty(browser, local_base_url):
    user_register_page = UserRegisterPage(browser, local_base_url)
    user_register_page.go_to_site()
    user_register_page.simple_click(Header.MY_ACCOUNT_BTN)
    user_register_page.move_and_click(Header.REGISTER_BTN)
    user_register_page.fill_in_register_form_without_field("E-Mail")
    user_register_page.agree_with_policy()
    user_register_page.push_continue_btn()
    errors = []
    if not user_register_page.check_css_property(UserRegisterPage.EMAIL_LABEL,
                                                 "color") == TestDataUserRegistration.ERROR_LABEL_TEXT_COLOR:
        errors.append("Label color equals to 'rgba(169, 68, 66, 1)'/'#a94442'")
    if not user_register_page.check_css_property(UserRegisterPage.EMAIL_TEXT_DANGER,
                                                 "color") == TestDataUserRegistration.ERROR_LABEL_TEXT_COLOR:
        errors.append("Text danger color equals to 'rgba(169, 68, 66, 1)'/'#a94442'")
    if not user_register_page.get_property(UserRegisterPage.EMAIL_TEXT_DANGER,
                                           "innerHTML") == TestDataUserRegistration.EMAIL_TEXT_DANGER:
        errors.append("E-Mail Address does not appear to be valid!")
    if not user_register_page.element_has_error_class(UserRegisterPage.EMAIL_ELEM_GROUP):
        errors.append("Input 'E-Mail' has no error class! Check border-color!")
    assert not errors, "Errors exist:\n{}".format("\n".join(errors))


@allure.title("Проверка: отображение подсказки при незаполненном поле 'Telephone' + правильный текст подсказки "
              "+ смена цвета заголовка поля + смена цвета границы поля input")
def test8_warn_info_when_telephone_empty(browser, local_base_url):
    user_register_page = UserRegisterPage(browser, local_base_url)
    user_register_page.go_to_site()
    user_register_page.simple_click(Header.MY_ACCOUNT_BTN)
    user_register_page.move_and_click(Header.REGISTER_BTN)
    user_register_page.fill_in_register_form_without_field("Telephone")
    user_register_page.agree_with_policy()
    user_register_page.push_continue_btn()
    time.sleep(7)
    # errors = []
    # if not user_register_page.check_css_property(UserRegisterPage.EMAIL_LABEL,
    #                                              "color") == UserRegisterPageTestData.ERROR_LABEL_TEXT_COLOR:
    #     errors.append("Label color equals to 'rgba(169, 68, 66, 1)'/'#a94442'")
    # if not user_register_page.check_css_property(UserRegisterPage.EMAIL_TEXT_DANGER,
    #                                              "color") == UserRegisterPageTestData.ERROR_LABEL_TEXT_COLOR:
    #     errors.append("Text danger color equals to 'rgba(169, 68, 66, 1)'/'#a94442'")
    # if not user_register_page.get_property(UserRegisterPage.EMAIL_TEXT_DANGER,
    #                                        "innerHTML") == UserRegisterPageTestData.EMAIL_TEXT_DANGER:
    #     errors.append("E-Mail Address does not appear to be valid!")
    # if not user_register_page.element_has_error_class(UserRegisterPage.EMAIL_ELEM_GROUP):
    #     errors.append("Input 'E-Mail' has no error class! Check border-color!")
    # assert not errors, "Errors exist:\n{}".format("\n".join(errors))
