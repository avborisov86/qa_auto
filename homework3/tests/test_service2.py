"""
School: OTUS "QA Automation"
Task 3: Files's code 'service2.py' coverage by automated tests (API - https://www.openbrewerydb.org/)
Author: Anton Borisov
"""

import pytest
from random import randint

from homework3.service2 import get_brewery_city
from homework3.service2 import get_brewery_type
from homework3.service2 import get_brewery_quantity
from homework3.service2 import get_brewery_by_id
from homework3.service2 import get_brewery_by_postal_code


# Параметризированный тест на проверку города пивоварни
@pytest.mark.parametrize(
    "brew_city", [
        "new_york",
        "san_diego",
        "dallas",
        "boston",
        "chicago",
    ]
)
def test_brewery_city(brew_city):
    result = get_brewery_city(brew_city)
    rand_brew = result[randint(0, len(result) - 1)]['city']
    assert 'city' in result[randint(0, len(result) - 1)], "Expects 'city' in a random element of json!"
    assert rand_brew.lower().replace(" ", "_") == brew_city, "Expects brewery city name equals to city name from url!"


# Параметризированный тест на проверку типа пивоварни
@pytest.mark.parametrize(
    "brew_type", [
        "micro",
        "regional",
        "closed",
        "brewpub",
        "large",
    ]
)
def test_brewery_type(brew_type):
    result = get_brewery_type(brew_type)
    rand_brew = result[randint(0, len(result) - 1)]['brewery_type']
    assert 'brewery_type' in result[randint(0, len(result) - 1)], "Expects 'brewery type' in a random element of json!"
    assert rand_brew == brew_type, "Expects brewery type (from json) equals to type name from url!"


# Параметризированный тест на проверку количества выводимых на странице пивоварен
@pytest.mark.parametrize(
    "elem_page", [
        "20",
        "25",
        "30",
        "40",
        "50",
    ]
)
def test_brewery_quantity(elem_page):
    result = get_brewery_quantity(elem_page)
    assert len(
        result).__str__() == elem_page, "Expects quantity of breweries (from json) equals to quantity of breweries from url!"


# Тест на проверку 'id' пивоварни (сравнение в ответе и запросе)
@pytest.mark.parametrize(
    "brew_id", [
        "9094",
        "14677",
        "12773",
        "14417",
        "14347",
    ]
)
def test_brewery_by_id(brew_id):
    result = get_brewery_by_id(brew_id)
    assert result['id'].__str__() == brew_id, "Expects brewery's 'id' (from json) equals to brewery's 'id' from url!"
    assert 'id' in result, "Expects 'id' in returned element of json!"


# Тест на проверку 'postal_code' пивоварни (сравнение в ответе и запросе)
@pytest.mark.parametrize(
    "brew_postal", [
        "23662-0000",
        "19123",
        "49203-4908",
        "24141-1403",
        "78163-4156",
    ]
)
def test_brewery_by_postal_code(brew_postal):
    result = get_brewery_by_postal_code(brew_postal)
    assert result[0][
               'postal_code'] == brew_postal, "Expects brewery's 'postal_code' equals to 'postal_code' from url!"
    assert 'postal_code' in result[0], "Expects 'postal_code' in returned element of json!"
