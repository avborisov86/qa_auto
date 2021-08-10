"""
School: OTUS "QA Automation"
Task 4: Page https://demo.opencart.com coverage by 5 automated tests
Author: Anton Borisov
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from homework4.page_objects.selectors import mainPageSelectors


# Тест на проверку видимости элемента "слайдер" на главной странице
def test_slider_visibility(browser, url_base):
    # Идем на 'https://demo.opencart.com'
    browser.get(url_base)
    # Записываем в переменную информацию об ожидаемом на странице элементе
    element = WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#slideshow0")))
    # Проверяем соответствие найденного на странцие и ожидаемого элемента
    assert browser.find_element(
        *mainPageSelectors.MAIN_SLIDER) == element, "Needs slider 'element' to be found on the page!"


# Тест на проверку видимости элемента "корзина" на главной странице
def test_cart_visibility(browser, url_base):
    # Идем на 'https://demo.opencart.com'
    browser.get(url_base)
    # Записываем в переменную информацию об ожидаемом на странице элементе
    element = WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#cart")))
    # Проверяем соответствие найденного на странцие и ожидаемого элемента
    assert browser.find_element(*mainPageSelectors.CART) == element, "Needs cart 'element' to be found on the page!"


# Тест на проверку видимости элемента "поиск" на главной странице
def test_search_visibility(browser, url_base):
    # Идем на 'https://demo.opencart.com'
    browser.get(url_base)
    # Записываем в переменную информацию об ожидаемом на странице элементе
    element = WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#search")))
    # Проверяем соответствие найденного на странцие и ожидаемого элемента
    assert browser.find_element(
        *mainPageSelectors.SEARCH) == element, "Needs search 'element' to be found one the page!"


# Тест на проверку видимости элемента "карусель логотипов" на главной странице
def test_logo_swiper_visibility(browser, url_base):
    # Идем на 'https://demo.opencart.com'
    browser.get(url_base)
    # Записываем в переменную информацию об ожидаемом на странице элементе
    element = WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#carousel0")))
    # Проверяем соответствие найденного на странцие и ожидаемого элемента
    assert browser.find_element(
        *mainPageSelectors.LOGO_CAROUSEL) == element, "Needs logo carousel 'element' to be found one the page!"


# Тест на проверку видимости 4 продуктовых карточек на главной странице
def test_products_visibility(browser, url_base):
    # Идем на 'https://demo.opencart.com'
    browser.get(url_base)
    # Записываем в переменную информацию об ожидаемом на странице элементе
    elements = WebDriverWait(browser, 1).until(
        EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".product-layout")))
    # Проверяем соответствие найденного на странцие и ожидаемого элемента
    assert len(elements) == 4, "Needs 4 products cards 'element' to be found one the page!"
