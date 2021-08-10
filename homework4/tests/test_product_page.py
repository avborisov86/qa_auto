"""
School: OTUS "QA Automation"
Task 4: Page https://demo.opencart.com/index.php?route=product/product&path=18&product_id=44 coverage by 5 automated tests
Author: Anton Borisov
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from homework4.page_objects.selectors import productPageSelectors


# Тест на проверку видимости элемента "все изображения товара в одном блоке" на странице товара
def test_thumbnail_visibility(browser, url_prod):
    # Идем на 'https://demo.opencart.com' в раздел с выбранным товаром
    browser.get(url_prod)
    # Записываем в переменную информацию об ожидаемом на странице элементе
    element = WebDriverWait(browser, 1).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".thumbnails")))
    # Проверяем соответствие найденного на странцие и ожидаемого элемента
    assert browser.find_element(
        *productPageSelectors.THUMB_ELEM) == element, "Needs main thumbnail 'element' to be found on the page!"


# Тест на проверку видимости 4х элементов "изображения товара" на странице товара
def test_thumbnails_qty_visibility(browser, url_prod):
    # Идем на 'https://demo.opencart.com' в раздел с выбранным товаром
    browser.get(url_prod)
    # Записываем в переменную информацию об ожидаемом на странице элементе
    element = WebDriverWait(browser, 1).until(
        EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".thumbnail")))
    # Проверяем соответствие найденного на странцие и ожидаемого элемента
    assert len(element) == 4, "Needs 4 thumbnails 'element' to be found on the page!"


# Тест на проверку видимости элемента "название товара" на странице товара
def test_product_title_visibility(browser, url_prod):
    # Идем на 'https://demo.opencart.com' в раздел с выбранным товаром
    browser.get(url_prod)
    # Записываем в переменную информацию об ожидаемом на странице элементе
    element = WebDriverWait(browser, 1).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "div.btn-group + h1")))
    # Проверяем соответствие найденного на странцие и ожидаемого элемента
    assert browser.find_element(
        *productPageSelectors.PROD_TITLE) == element, "Needs product title 'element' to be found on the page!"


# Тест на проверку видимости элемента "поле для ввода количества товаров" на странице товара
def test_quantity_input_visibility(browser, url_prod):
    # Идем на 'https://demo.opencart.com' в раздел с выбранным товаром
    browser.get(url_prod)
    # Записываем в переменную информацию об ожидаемом на странице элементе
    element = WebDriverWait(browser, 1).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name = \"quantity\"]")))
    # Проверяем соответствие найденного на странцие и ожидаемого элемента
    assert browser.find_element(
        *productPageSelectors.QTY_INPUT) == element, "Needs quantity of goods input 'element' to be found on the page!"


# Тест на проверку видимости элемента "кнопка положить в корзину" на странице товара
def test_cart_btn_visibility(browser, url_prod):
    # Идем на 'https://demo.opencart.com' в раздел с выбранным товаром
    browser.get(url_prod)
    # Записываем в переменную информацию об ожидаемом на странице элементе
    element = WebDriverWait(browser, 1).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#button-cart")))
    # Проверяем соответствие найденного на странцие и ожидаемого элемента
    assert browser.find_element(
        *productPageSelectors.CART_BTN) == element, "Needs cart button 'element' to be found on the page!"
