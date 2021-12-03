"""
School: OTUS "QA Automation"
Project work: Main page http://127.0.0.1:8081 coverage by automated tests
Tests:

1. Проверка: строка поиска работает + поисковый запрос передается на страницу поиска после нажатия кнопки
2. Проверка: до добавления товара корзина - пустая
3. Проверка: товар добавляется в корзину + появляется информирование клиента о добавлении товара в корзину
4. Проверка: товар удаляется из корзины
5.

Author: Anton Borisov
"""

import allure
import time
from project_work.page_objects.MainPage import MainPage
from project_work.page_objects.TestData import TestDataMainPage
from project_work.page_objects.TestData import TestDataSearchPage
from project_work.page_objects.SearchPage import SearchPage


@allure.title("Проверка: строка поиска работает + поисковый запрос передается на страницу поиска после нажатия кнопки")
@allure.description
def test1_search_input_works(browser, local_base_url):
    main_page = MainPage(browser, local_base_url)
    main_page.go_to_site()
    main_page.enter_data(main_page.SEARCH_INPUT, "any query")
    main_page.simple_click(main_page.SEARCH_BTN)
    errors = []
    if not main_page.get_property(SearchPage.SEARCH_INPUT, "value") == TestDataSearchPage.SEARCH_INPUT_VALUE:
        errors.append(f"Input value equals to \"{TestDataSearchPage.SEARCH_INPUT_VALUE}\"!")
    if not main_page.get_page_title() == TestDataMainPage.SEARCH_PAGE_TITLE:
        errors.append(f"Page title equals to \"{TestDataMainPage.SEARCH_PAGE_TITLE}\"!")
    assert not errors, "Errors exist:\n{}".format("\n".join(errors))


@allure.title("Проверка: до добавления товара корзина - пустая")
@allure.description
def test2_cart_is_empty(browser, local_base_url):
    main_page = MainPage(browser, local_base_url)
    main_page.go_to_site()
    main_page.simple_click(MainPage.CART_BTN)
    cart_empty_value = main_page.get_property(MainPage.CART_EMPTY_NOTE, "innerHTML")
    assert cart_empty_value == TestDataMainPage.CART_EMPTY_NOTE, "Cart note equals to 'Your shopping cart is empty'!"


@allure.title("Проверка: товар добавляется в корзину + появляется информирование клиента о добавлении товара в корзину")
@allure.description
def test3_product_add_to_cart(browser, local_base_url):
    main_page = MainPage(browser, local_base_url)
    main_page.go_to_site()
    main_page.show_all_mp3()
    main_page.simple_click(MainPage.FIRST_MP3_PRODUCT)
    main_page.simple_click(MainPage.CART_BTN)
    errors = []
    if not main_page.verify_element_presence(MainPage.ADD_ALERT):
        errors.append("Alert notification about added product is absent!")
    if not main_page.verify_element_presence(MainPage.CART_PROD_LINK):
        errors.append("Product link is absent in the cart!")
    assert not errors, "Errors exist:\n{}".format("\n".join(errors))


@allure.title("Проверка: товар удаляется из корзины")
@allure.description
def test4_product_del_from_cart(browser, local_base_url):
    main_page = MainPage(browser, local_base_url)
    main_page.go_to_site()
    main_page.show_all_mp3()
    main_page.simple_click(MainPage.FIRST_MP3_PRODUCT)
    main_page.simple_click(MainPage.CART_BTN)
    main_page.simple_click(MainPage.CART_DEL_PROD)
    main_page.simple_click(MainPage.CART_BTN)
    cart_empty_value = main_page.get_property(MainPage.CART_EMPTY_NOTE, "innerHTML")
    assert cart_empty_value == TestDataMainPage.CART_EMPTY_NOTE, "Cart note equals to 'Your shopping cart is empty'!"
