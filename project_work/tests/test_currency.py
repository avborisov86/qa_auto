"""
School: OTUS "QA Automation"
Project work: "Changing currency" coverage by automated tests (http://127.0.0.1:8081)

Tests
1. Проверка: элемент "меню для изменения валюты" существует на странице
2. Проверка: появление меню для изменения валюты по нажатию на кнопку
3. Проверка: переключение валюты на Евро (EUR)
4. Проверка: переключение валюты на Фунты (GBP)
5. Проверка: переключение валюты на Доллары (USD)
6. Проверка: поочередная смена значений валюты
7. Проверка: после переключения валюты на Фунты (GBP) измененяется валюта на кнопке "корзина"
8. Проверка: после переключения валюты на Евро (EUR) измененяется валюта на кнопке "корзина"
9. Проверка: после переключения валюты на Доллары (USD) измененяется валюта на кнопке "корзина"
10. Проверка: после переключения валюты на Фунты (GBP) измененяется валюта у любого из товаров на главной странице

11. Проверка: после переключения валюты на Евро (EUR) измененяется валюта у любого из товаров на главной странице
12. Проверка: после переключения валюты на Доллары (USD) измененяется валюта у любого из товаров на главной странице
13. Проверка: после переключения валюты на Фунты (GBP) измененяется валюта у любого из товаров на странице категории
с товарами
14. Проверка: после переключения валюты на Евро (EUR) измененяется валюта у любого из товаров на странице категории
с товарами
15. Проверка: после переключения валюты на Доллары (USD) измененяется валюта у любого из товаров на странице категории
с товарами

Author: Anton Borisov
"""

import pytest
import allure
import time
from project_work.page_objects.HeaderCurrency import HeaderCurrency as Currency
from project_work.page_objects.TestData import TestDataHeader
from project_work.page_objects.MainPage import MainPage


@pytest.mark.webtest
@allure.title("Проверка: элемент 'кнопка для изменения валюты' существует на всех страницах магазина")
@allure.feature("Добавление функионала изменения валюты в магазине")
@allure.story("Элемент 'кнопка для изменения валюты' отображается на всех страницах магазина в хеадере")
@allure.description(""" 
    На главной странице ИМ http://127.0.0.1:8081/ находим и проверяем присутствие элемента 'кнопка для изменения 
    валюты'  
""")
@allure.severity(allure.severity_level.CRITICAL)
@allure.issue("123", name="Элемент 'кнопка для изменения валюты' существует на всех страницах")
def test1_change_currency_elem_exists(browser, local_base_url):
    main_page = Currency(browser, local_base_url)
    main_page.go_to_site()
    assert main_page.verify_element_presence(
        Currency.CURRENCY_BTN), "Currency form must be visible on the page."


@allure.title("Проверка: появление меню для изменения валюты по нажатию на кнопку")
@allure.feature("Добавление функионала изменения валюты в магазине")
@allure.story("Пользователь может открыть меню с валютами")
@allure.description("""
    На главной странице ИМ http://127.0.0.1:8081/ нажимаем на кнопку (с валютами) и проверяем появился ли новый класс 
    у элемента и появляется ли меню с выбором валюты
""")
@allure.severity(allure.severity_level.CRITICAL)
def test2_change_currency_dropdown_appears(browser, local_base_url):
    main_page = Currency(browser, local_base_url)
    main_page.go_to_site()
    main_page.simple_click(Currency.CURRENCY_BTN)
    errors = []
    if not main_page.element_has_open_class(Currency.CURRENCY_DROPDOWN_GROUP):
        errors.append("1.Currency group of elements has no 'open' class. Check drop down menu appears.")
    if not main_page.get_property(Currency.CURRENCY_DROPDOWN_GROUP,
                                  "className") == TestDataHeader.CURRENCY_GROUP_CLASS_NAME_VALUE:
        errors.append("2.Check if element ClassName == 'btn-group open'")
    assert not errors, "Errors exist:\n{}".format("\n".join(errors))


@allure.title("Проверка: переключение валюты на Евро (EUR)")
@allure.feature("Добавление функионала изменения валюты в магазине")
@allure.story("Пользователь может изменить валюту покупки на Евро")
@allure.description("""
    На главной странице ИМ http://127.0.0.1:8081/ изменяем валюту на Евро и проверяем изменился ли знак валюты в 
    главном окне изменения валюты 
""")
@allure.severity(allure.severity_level.TRIVIAL)
@allure.issue("182", name="Отсутствует возможность измененить валюту на Евро")
def test3_change_currency_to_eur(browser, local_base_url):
    main_page = Currency(browser, local_base_url)
    main_page.go_to_site()
    main_page.change_currency_to('EUR')
    assert TestDataHeader.EURO_SIGN == main_page.get_property(Currency.CURRENCY_SIGN,
                                                              'innerHTML'), "Currency sign must be '€'."


@allure.title("Проверка: переключение валюты на Фунты (GBP)")
@allure.feature("Добавление функионала изменения валюты в магазине")
@allure.story("Пользователь может изменить валюту покупки на Фунты")
@allure.description("""
    На главной странице ИМ http://127.0.0.1:8081/ изменяем валюту на Фунты и проверяем изменился ли знак валюты в 
    главном окне изменения валюты 
""")
@allure.severity(allure.severity_level.MINOR)
def test4_change_currency_to_gbp(browser, local_base_url):
    main_page = Currency(browser, local_base_url)
    main_page.go_to_site()
    main_page.change_currency_to('GBP')
    assert TestDataHeader.GBP_SIGN == main_page.get_property(Currency.CURRENCY_SIGN,
                                                             'innerHTML'), "Currency sign must be '£'."


@allure.title("Проверка: переключение валюты на Доллары (USD)")
@allure.feature("Добавление функионала изменения валюты в магазине")
@allure.story("Пользователь может изменить валюту покупки на Доллары")
@allure.description("""
    На главной странице ИМ http://127.0.0.1:8081/ изменяем валюту на Доллары и проверяем изменился ли знак валюты в 
    главном окне изменения валюты 
""")
@allure.severity(allure.severity_level.MINOR)
def test5_change_currency_to_usd(browser, local_base_url):
    main_page = Currency(browser, local_base_url)
    main_page.go_to_site()
    main_page.change_currency_to('USD')
    assert TestDataHeader.USD_SIGN == main_page.get_property(Currency.CURRENCY_SIGN,
                                                             'innerHTML'), "Currency sign must be '$'."


@allure.title("Проверка: поочередная смена значений валюты")
@allure.feature("Добавление функионала изменения валюты в магазине")
@allure.story("Пользователь может поочередно выбрать разные валюты оплаты")
@allure.description("""
    На главной странице ИМ http://127.0.0.1:8081/ нажимаем на кнопку, поочередно выбираем каждую валюту и заканчиваем 
    на Евро. Проверяем у последнего элемента (Евро) корректность отображаемого знака валюты.
""")
@allure.severity(allure.severity_level.NORMAL)
def test6_user_change_currency_one_by_one(browser, local_base_url):
    main_page = Currency(browser, local_base_url)
    main_page.go_to_site()
    main_page.simple_click(Currency.CURRENCY_BTN)
    main_page.move_and_click(Currency.GBP_BTN, 1)
    main_page.simple_click(Currency.CURRENCY_BTN)
    main_page.move_and_click(Currency.USD_BTN, 1)
    main_page.simple_click(Currency.CURRENCY_BTN)
    main_page.move_and_click(Currency.EURO_BTN, 1)
    assert TestDataHeader.EURO_SIGN == main_page.get_property(Currency.CURRENCY_SIGN,
                                                              'innerHTML'), "Currency sign must be '€'."


@allure.title("Проверка: после переключения валюты на Фунты (GBP) измененяется валюта на кнопке 'корзина'")
@allure.feature("Добавление функионала изменения валюты в магазине")
@allure.story("После изменения валюты оплаты на главной странице в корзине изменяется валюта оплаты")
@allure.description("""
    На главной странице ИМ http://127.0.0.1:8081/ изменяем валюту на Фунты (GBP) и проверяем, что на кнопке 'корзина' 
    валюта оплаты изменилась на Фунты.
""")
@allure.severity(allure.severity_level.CRITICAL)
def test7_changing_currency_to_gbp_on_cart_button(browser, local_base_url):
    main_page = Currency(browser, local_base_url)
    main_page.go_to_site()
    main_page.change_currency_to("USD")
    main_page.change_currency_to("GBP")
    assert TestDataHeader.GBP_SIGN in main_page.get_property(MainPage.CART_TOTAL_INFO, "textContent")


@allure.title("Проверка: после переключения валюты на Евро (EUR) измененяется валюта на кнопке 'корзина'")
@allure.feature("Добавление функионала изменения валюты в магазине")
@allure.story("После изменения валюты оплаты на главной странице в корзине изменяется валюта оплаты")
@allure.description("""
    На главной странице ИМ http://127.0.0.1:8081/ изменяем валюту на Евро (EUR) и проверяем, что на кнопке 'корзина' 
    валюта оплаты изменилась на Евро.
""")
@allure.severity(allure.severity_level.CRITICAL)
def test8_changing_currency_to_eur_on_cart_button(browser, local_base_url):
    main_page = Currency(browser, local_base_url)
    main_page.go_to_site()
    main_page.change_currency_to("USD")
    main_page.change_currency_to("EUR")
    assert TestDataHeader.EURO_SIGN in main_page.get_property(MainPage.CART_TOTAL_INFO, "textContent")


@allure.title("Проверка: после переключения валюты на Доллары (USD) измененяется валюта на кнопке 'корзина'")
@allure.feature("Добавление функионала изменения валюты в магазине")
@allure.story("После изменения валюты оплаты на главной странице в корзине изменяется валюта оплаты")
@allure.description("""
    На главной странице ИМ http://127.0.0.1:8081/ изменяем валюту на Доллары (USD) и проверяем, что на кнопке 'корзина' 
    валюта оплаты изменилась на Евро.
""")
@allure.severity(allure.severity_level.CRITICAL)
def test9_changing_currency_to_usd_on_cart_button(browser, local_base_url):
    main_page = Currency(browser, local_base_url)
    main_page.go_to_site()
    main_page.change_currency_to("GBP")
    main_page.change_currency_to("USD")
    assert TestDataHeader.USD_SIGN in main_page.get_property(MainPage.CART_TOTAL_INFO, "textContent")


@allure.title(
    "Проверка: после переключения валюты на Фунты (GBP) измененяется валюта у любого из товаров на главной странице")
@allure.feature("Добавление функионала изменения валюты в магазине")
@allure.story(
    "После изменения валюты оплаты на главной странице изменяется валюта оплаты у любого из товаров на главной странице")
@allure.description("""
    На главной странице ИМ http://127.0.0.1:8081/ изменяем валюту на Фунты (GBP) и проверяем, что у любого товара на 
    главной странице из раздела 'Featured' изменилась валюта оплаты.
""")
@allure.severity(allure.severity_level.CRITICAL)
def test10_changing_currency_to_gbp_on_any_featured_product(browser, local_base_url):
    main_page = Currency(browser, local_base_url)
    main_page.go_to_site()
    main_page.change_currency_to("GBP")
    assert TestDataHeader.GBP_SIGN in main_page.get_property(MainPage.ANY_FEATURED_PROD_PRICE, "innerText")
