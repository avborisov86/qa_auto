"""
School: OTUS "QA Automation"
Project work: User register page http://127.0.0.1:8081 coverage by automated tests

Tests:
1. Проверка: переключение валюты на Евро (EUR)
2. Проверка: переключение валюты на Фунты (GBP)
3. Проверка: переключение валюты на Доллары (USD)
4. Проверка: появление меню для изменения валюты по нажатию на кнопку
5. Проверка: поочередная смена значений валюты

Author: Anton Borisov
"""

import allure
import time
from project_work.page_objects.Header import Header
from project_work.page_objects.TestData import TestDataHeader


@allure.title("Проверка: переключение валюты на Евро (EUR)")
def test1_change_currency_to_eur(browser, local_base_url):
    main_page = Header(browser, local_base_url)
    main_page.go_to_site()
    main_page.change_currency_to('EUR')
    assert TestDataHeader.EURO_SIGN == main_page.get_property(Header.CURRENCY_SIGN,
                                                              'innerHTML'), "Currency sign equals to '€'!"
    print(main_page.get_property(Header.CURRENCY_SIGN, 'innerHTML'))


@allure.title("Проверка: переключение валюты на Фунты (GBP)")
def test2_change_currency_to_gbp(browser, local_base_url):
    main_page = Header(browser, local_base_url)
    main_page.go_to_site()
    main_page.change_currency_to('GBP')
    assert TestDataHeader.GBP_SIGN == main_page.get_property(Header.CURRENCY_SIGN,
                                                             'innerHTML'), "Currency sign equals to '£'!"


@allure.title("Проверка: переключение валюты на Доллары (USD)")
def test3_change_currency_to_usd(browser, local_base_url):
    main_page = Header(browser, local_base_url)
    main_page.go_to_site()
    main_page.change_currency_to('USD')
    assert TestDataHeader.USD_SIGN == main_page.get_property(Header.CURRENCY_SIGN,
                                                             'innerHTML'), "Currency sign equals to '$'!"


@allure.title("Проверка: появление меню для изменения валюты по нажатию на кнопку")
def test4_change_currency_dropdown_appears(browser, local_base_url):
    main_page = Header(browser, local_base_url)
    main_page.go_to_site()
    main_page.simple_click(Header.CURRENCY_BTN)
    errors = []
    if not main_page.element_has_open_class(Header.CURRENCY_DROPDOWN_GROUP):
        errors.append("Currency element's group has no 'open' class! Check drop down menu appears!")
    if not main_page.get_property(Header.CURRENCY_DROPDOWN_GROUP,
                                  "className") == TestDataHeader.CURRENCY_GROUP_CLASS_NAME_VALUE:
        errors.append("ClassName value equals to 'btn-group open'!")
    assert not errors, "Errors exist:\n{}".format("\n".join(errors))


@allure.title("Проверка: поочередная смена значений валюты")
def test5_user_change_currency_one_by_one(browser, local_base_url):
    main_page = Header(browser, local_base_url)
    main_page.go_to_site()
    main_page.simple_click(Header.CURRENCY_BTN)
    main_page.move_and_click(Header.GBP_BTN, 1)
    main_page.simple_click(Header.CURRENCY_BTN)
    main_page.move_and_click(Header.USD_BTN, 1)
    main_page.simple_click(Header.CURRENCY_BTN)
    main_page.move_and_click(Header.EURO_BTN, 1)
    assert TestDataHeader.EURO_SIGN == main_page.get_property(Header.CURRENCY_SIGN,
                                                              'innerHTML'), "Currency sign equals to '€'!"
