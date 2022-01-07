"""
School: OTUS "QA Automation"
Project work: "Search group" coverage by automated tests (http://127.0.0.1:8081)

Tests:
1. Проверка: строка поиска (search input) + кнопка поиск с иконкой (button) присутствуют на странице
2.

Проверка: строка поиска работает + поисковый запрос передается на страницу поиска после нажатия кнопки
3.

Author: Anton Borisov
"""

import allure
import time
from project_work.page_objects.MainPage import MainPage
from project_work.page_objects.TestData import TestDataMainPage
from project_work.page_objects.TestData import TestDataSearchPage
from project_work.page_objects.SearchGroup import SearchGroup


@allure.title("Проверка: строка поиска (search input) + кнопка поиск с иконкой (button) присутствуют на странице")
@allure.description
def test1_search_input_exists(browser, local_base_url):
    main_page = MainPage(browser, local_base_url)
    main_page.go_to_site()
    assert main_page.verify_element_presence(SearchGroup.SEARCH_GROUP)


@allure.title("Проверка: строка поиска работает + поисковый запрос передается на страницу поиска после нажатия кнопки")
@allure.description
def test2_search_input_works(browser, local_base_url):
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