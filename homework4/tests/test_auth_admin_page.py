"""
School: OTUS "QA Automation"
Task 4: Page https://demo.opencart.com/admin/ coverage by 5 automated tests
Author: Anton Borisov
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from homework4.page_objects.selectors import authAdminPageSelectors

import time

# Тест на проверку видимости элемента "заголовок формы аутентификации" на странице входа в админку
def test_form_title_visibility(browser, url_auth):
    # Идем на 'https://demo.opencart.com' и затем в админку
    browser.get(url_auth)
    # Записываем в переменную информацию об ожидаемом на странице элементе
    element = WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".panel-title")))
    time.sleep(10)
    # Проверяем соответствие найденного на странцие и ожидаемого элемента
    assert browser.find_element(
        *authAdminPageSelectors.AUTH_FORM_TITLE) == element, "Needs form title 'element' to be found on the page!"


# Тест на проверку видимости элемента "поле ввода логина" на странице входа в админку
def test_login_input_visibility(browser, url_auth):
    # Идем на 'https://demo.opencart.com' и затем в админку
    browser.get(url_auth)
    # Записываем в переменную информацию об ожидаемом на странице элементе
    element = WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#input-username")))
    # Проверяем соответствие найденного на странцие и ожидаемого элемента
    assert browser.find_element(
        *authAdminPageSelectors.LOGIN_INPUT) == element, "Needs login input 'element' to be found on the page!"


# Тест на проверку видимости элемента "поле ввода пароля" на странице входа в админку
def test_password_input_visibility(browser, url_auth):
    # Идем на 'https://demo.opencart.com' и затем в админку
    browser.get(url_auth)
    # Записываем в переменную информацию об ожидаемом на странице элементе
    element = WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#input-password")))
    # Проверяем соответствие найденного на странцие и ожидаемого элемента
    assert browser.find_element(
        *authAdminPageSelectors.PASS_INPUT) == element, "Needs password input 'element' to be found on the page!"


# Тест на проверку видимости элемента "ссылка Забыли пароль" на странице входа в админку
def test_forgot_password_visibility(browser, url_auth):
    # Идем на 'https://demo.opencart.com' и затем в админку
    browser.get(url_auth)
    # Записываем в переменную информацию об ожидаемом на странице элементе
    element = WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".help-block")))
    # Проверяем соответствие найденного на странцие и ожидаемого элемента
    assert browser.find_element(
        *authAdminPageSelectors.FORGOT_PASS_BTN) == element, "Needs forgot password 'element' to be found on the page!"


# Тест на проверку видимости элемента "кнопка Войти" на странице входа в админку
def test_login_btn_visibility(browser, url_auth):
    # Идем на 'https://demo.opencart.com' и затем в админку
    browser.get(url_auth)
    # Записываем в переменную информацию об ожидаемом на странице элементе
    element = WebDriverWait(browser, 1).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "button[type=submit]")))
    # Проверяем соответствие найденного на странцие и ожидаемого элемента
    assert browser.find_element(
        *authAdminPageSelectors.LOGIN_BTN) == element, "Needs login button 'element' to be found on the page!"
