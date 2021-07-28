"""
School: OTUS "QA Automation"
Task 3: Getting test data from  API - https://dog.ceo/dog-api/
Author: Anton Borisov
"""

import requests


# Функция для отправки запроса на получение одной случайной картинки собаки
def get_random_img_all():
    result = requests.get("https://dog.ceo/api/breeds/image/random").json()
    return result


# Функция для отправки запроса на получение нескольких (трех) случайных картинок собак
def get_multiple_img_all():
    result = requests.get("https://dog.ceo/api/breeds/image/random/3").json()
    return result


# Функция для отправки запроса на получение одной случайной картинки из подпороды собак
def get_random_img_subbreed(breed):
    result = requests.get(f"https://dog.ceo/api/breed/hound/{breed}/images/random").json()
    return result


# Функция для отправки запроса на получение одной случайной картинки собаки по ее породе
def get_random_img_breed(breed):
    result = requests.get(f"https://dog.ceo/api/breed/{breed}/images/random").json()
    return result


# Функция для отправки запроса на получение нескольких случайных картинок собак по их породе
def get_multiple_img_breed(breed):
    result = requests.get(f"https://dog.ceo/api/breed/{breed}/images/random/3").json()
    return result
