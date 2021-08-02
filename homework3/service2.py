"""
School: OTUS "QA Automation"
Task 3: Getting test data from API - https://www.openbrewerydb.org/
Author: Anton Borisov
"""

import requests


# Функция для получения списка пивоварен по наименованию города
def get_brewery_city(brew_city):
    result = requests.get(f"https://api.openbrewerydb.org/breweries?by_city={brew_city}").json()
    return result
    # return result[randint(0, len(result))]['city']


# Функция для получения списка пивоварен по их типу
def get_brewery_type(brew_type):
    result = requests.get(f"https://api.openbrewerydb.org/breweries?by_type={brew_type}").json()
    return result


# Функция для получения списка пивоварен по количеству элементов на странице
def get_brewery_quantity(elem_page):
    result = requests.get(f"https://api.openbrewerydb.org/breweries?per_page={elem_page}").json()
    return result


# Функция для получения данных конкретной пивоварни по ее 'id'
def get_brewery_by_id(brew_id):
    result = requests.get(f"https://api.openbrewerydb.org/breweries/{brew_id}").json()
    return result


# Функция для получения данных конкретной пивоварни по ее 'postal_code'
def get_brewery_by_postal_code(brew_postal):
    result = requests.get(f"https://api.openbrewerydb.org/breweries?by_postal={brew_postal}").json()
    return result
    # return result[0]['postal_code']
