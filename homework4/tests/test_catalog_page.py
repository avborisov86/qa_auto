"""
School: OTUS "QA Automation"
Task 4: Page https://demo.opencart.com/index.php?route=product/category&path=18 coverage by 5 automated tests
Author: Anton Borisov
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from homework4.page_objects.selectors import catalogPageSelectors


# Тест на проверку видимости элемента "боковое меню" на странице каталога
def test_aside_menu_visibility(browser, url_cat):
    # Идем на 'https://demo.opencart.com' в раздел каталога с товарами
    browser.get(url_cat)
    # Записываем в переменную информацию об ожидаемом на странице элементе
    element = WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#column-left")))
    # Проверяем соответствие найденного на странцие и ожидаемого элемента
    assert browser.find_element(
        *catalogPageSelectors.ASIDE_MENU) == element, "Needs aside menu 'element' to be found on the page!"


# Тест на проверку видимости элемента "баннер" на странице каталога
def test_banner_visibility(browser, url_cat):
    # Идем на 'https://demo.opencart.com' в раздел каталога с товарами
    browser.get(url_cat)
    # Записываем в переменную информацию об ожидаемом на странице элементе
    element = WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#banner0")))
    # Проверяем соответствие найденного на странцие и ожидаемого элемента
    assert browser.find_element(
        *catalogPageSelectors.BANNER) == element, "Needs banner 'element' to be found on the page!"


# Тест на проверку видимости элемента "кнопка вывода - list" на странице каталога
def test_list_btn_visibility(browser, url_cat):
    # Идем на 'https://demo.opencart.com' в раздел каталога с товарами
    browser.get(url_cat)
    # Записываем в переменную информацию об ожидаемом на странице элементе
    element = WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#list-view")))
    # Проверяем соответствие найденного на странцие и ожидаемого элемента
    assert browser.find_element(
        *catalogPageSelectors.LIST_VIEW_BTN) == element, "Needs list button 'element' to be found on the page!"


# Тест на проверку видимости элемента "кнопка вывода - grid" на странице каталога
def test_grid_btn_visibility(browser, url_cat):
    # Идем на 'https://demo.opencart.com' в раздел каталога с товарами
    browser.get(url_cat)
    # Записываем в переменную информацию об ожидаемом на странице элементе
    element = WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#grid-view")))
    # Проверяем соответствие найденного на странцие и ожидаемого элемента
    assert browser.find_element(
        *catalogPageSelectors.GRID_VIEW_BTN) == element, "Needs grid button 'element' to be found on the page!"


# Тест на проверку видимости 5 продуктовых карточек на странице каталога с товарами
def test_products_visibility(browser, url_cat):
    # Идем на 'https://demo.opencart.com'
    browser.get(url_cat)
    # Записываем в переменную информацию об ожидаемом на странице элементе
    elements = WebDriverWait(browser, 1).until(
        EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".product-layout")))
    # Проверяем соответствие найденного на странцие и ожидаемого элемента
    assert len(elements) == 5, "Needs 5 product cards 'element' to be found one the page!"
