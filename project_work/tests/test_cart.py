"""
School: OTUS "QA Automation"
Project work: "Cart" coverage by automated tests (http://127.0.0.1:8081)

Tests:
1. Проверка: элемент 'корзина' присутствует на странице
2. Проверка: до момента добавления товара корзина пустая
3. Проверка: возможность добавления одного товара в корзину + клиенту отображается информационное сообщение о
добавлении товара
4. Проверка: возможность добавления нескольких товаров в корзину

5. Проверка: после добавления товара в корзину в информационном сообщении о добавлении товара клиенту отображается
правильное название добавленного товара
6. Проверка: есть возможность закрыть информационное сообщение (alert) после добавления товара в корзину
7. Проверка: после добавления товара в корзину во всплывающем меню корзины правильно отображается название
добавленного товара
8. Проверка: после добавления товара в корзину из всплывающего меню корзины есть возможность перейти на страницу
корзины (Shopping Cart) через кнопку 'View Cart' + проверка правильности добавления товара (название товара)
9. Проверка: после добавления товара в корзину из Header есть возможность перейти на страницу
корзины (Shopping Cart) через кнопку 'Shopping Cart' + проверка правильности добавления товара (название товара)
10. Проверка: после добавления товара в корзину из всплывающего меню корзины есть возможность перейти по ссылке
на страницу добавленного товара и просмотреть его
11. Проверка: после добавления товара в корзину со страницы корзины 'Shopping Cart' есть возможность перейти по ссылке
на страницу добавленного товара и просмотреть его
12. Проверка: после добавления товара в корзину со страницы корзины 'Shopping Cart' есть возможность изменить
количество добавленного товара и пересчитать общую сумму
13. Проверка: после добавления товара в корзину со страницы корзины 'Shopping Cart' есть возможность продолжить
совершать покупки через кнопку "Continue Shopping"
14. Проверка: товар удаляется из корзины через всплывающее меню корзины + проверка, что страница 'Shopping Cart'
тоже пустая
15. Проверка: товар удаляется из корзины через основную страницу корзины 'Shopping Cart' + проверка, что всплывающее
 меню корзины становится пустым (пока test4)

Author: Anton Borisov
"""

import pytest
import allure
import time
from project_work.page_objects.ShoppingCart import Cart
from project_work.page_objects.TestData import TestDataCart


@pytest.mark.webtest
@allure.title("Проверка: элемент 'корзина' присутствует на странице")
@allure.feature("Реализация функционала 'корзины' в интернет-магазине")
@allure.story("Элемент 'корзина' отображается на всех страницах магазина рядом со строкой поиска")
@allure.description(""" 
    На главной странице ИМ http://127.0.0.1:8081/ находим и проверяем отображение элемента 'корзина'
""")
@allure.severity(allure.severity_level.BLOCKER)
@allure.issue("005", name="Элемент 'корзина' не оторажается на странице интернет-магазина")
def test1_cart_button_exists(browser, local_base_url):
    main_page = Cart(browser, local_base_url)
    main_page.go_to_site()
    assert main_page.verify_element_presence(Cart.CART_BTN), "Cart button doesn't exist on the main page"


@allure.title("Проверка: до момента добавления товара корзина пустая")
@allure.feature("Реализация функционала 'корзины' в интернет-магазине")
@allure.story("До добавления товара корзина пустая")
@allure.description(""" 
    На главной странице ИМ http://127.0.0.1:8081/ находим корзину и проверяем отображение 
    в ней сообщения 'Your shopping cart is empty!'
""")
@allure.severity(allure.severity_level.CRITICAL)
def test2_cart_is_empty(browser, local_base_url):
    main_page = Cart(browser, local_base_url)
    main_page.go_to_site()
    main_page.simple_click(Cart.CART_BTN)
    cart_empty_value = main_page.get_property(Cart.CART_EMPTY_NOTE, "innerHTML")
    assert cart_empty_value == TestDataCart.CART_EMPTY_NOTE, "Cart empty info note must be 'Your shopping cart is empty'"


@allure.title("Проверка: возможность добавления одного товара в корзину + клиенту отображается информационное "
              "сообщение о добавлении товара")
@allure.feature("Реализация функционала 'корзины' в интернет-магазине")
@allure.story("Есть возможность добавить товар в корзину")
@allure.description(""" 
    На главной странице ИМ http://127.0.0.1:8081/ открываем каталог mp3 плееров, добавляем первый mp3 плеер и 
    проверяем добавление данного товара в корзину (дополнительно проверяем, что пользователю отображается 
    информационное сообщение о добавленном в корзину товаре)'
""")
@allure.severity(allure.severity_level.CRITICAL)
def test3_one_product_add_to_cart(browser, local_base_url):
    main_page = Cart(browser, local_base_url)
    main_page.go_to_site()
    main_page.show_all_mp3()
    main_page.simple_click(Cart.FIRST_MP3_PRODUCT)
    main_page.simple_click(Cart.CART_BTN)
    errors = []
    if not main_page.verify_element_presence(Cart.ADD_ALERT):
        errors.append("Alert notification about added product is absent")
    if not main_page.verify_element_presence(Cart.CART_PROD_LINK):
        errors.append("Product link is absent in the cart")
    assert not errors, "Errors exist:\n{}".format("\n".join(errors))


@allure.title("Проверка: возможность добавления нескольких товаров в корзину")
@allure.feature("Реализация функционала 'корзины' в интернет-магазине")
@allure.story("Есть возможность добавить несколько товаров в корзину")
@allure.description(""" 
    На главной странице ИМ http://127.0.0.1:8081/ открываем каталог mp3 плееров, добавляем несколько mp3 плееров и 
    проверяем добавление разных товаров в корзину (дополнительно проверяем, что пользователю отображаются 
    информационные сообщения о добавленных в корзину товарах)'
""")
@allure.severity(allure.severity_level.CRITICAL)
def test4_some_products_add_to_cart(browser, local_base_url):
    main_page = Cart(browser, local_base_url)
    main_page.go_to_site()
    main_page.show_all_mp3()
    main_page.simple_click(Cart.FIRST_MP3_PRODUCT)
    main_page.simple_click(Cart.SECOND_MP3_PRODUCT)
    main_page.simple_click(Cart.THIRD_MP3_PRODUCT)
    main_page.simple_click(Cart.CART_BTN)
    time.sleep(10)
    assert main_page.get_quantity(Cart.CART_PROD_ROWS_ADDED) == 3, "Number of added products must be 3"


@allure.title("Проверка: товар удаляется из корзины через всплывающее меню корзины + проверка, что страница "
              "'Shopping Cart' тоже пустая")
@allure.feature("Реализация функционала 'корзины' в интернет-магазине")
@allure.story("Есть возможность удалить товар из корзины через вспдывающее меню корзины")
@allure.description(""" 
    На главной странице ИМ http://127.0.0.1:8081/ после добавления произвольного товара в корзину открываем 
    всплывающее меню корзины и удаляем товар
    """)
@allure.severity(allure.severity_level.CRITICAL)
def test14_product_del_from_cart(browser, local_base_url):
    main_page = Cart(browser, local_base_url)
    main_page.go_to_site()
    main_page.show_all_mp3()
    main_page.simple_click(Cart.FIRST_MP3_PRODUCT)
    main_page.simple_click(Cart.CART_BTN)
    main_page.simple_click(Cart.CART_DEL_PROD)
    main_page.simple_click(Cart.CART_BTN)
    cart_empty_value = main_page.get_property(Cart.CART_EMPTY_NOTE, "innerHTML")
    main_page.simple_click(Cart.SHOPPING_CART_BTN)
    time.sleep(4)
    errors = []
    if not cart_empty_value == TestDataCart.CART_EMPTY_NOTE:
        errors.append("Cart empty info note must be 'Your shopping cart is empty'")
    if not main_page.get_property(Cart.SHOPPING_CART_EMPTY_NOTE, "innerHTML") == TestDataCart.CART_EMPTY_NOTE:
        errors.append("Cart empty info note must be 'Your shopping cart is empty'")
    assert not errors, "Errors exist:\n{}".format("\n".join(errors))
