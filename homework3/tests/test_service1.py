"""
School: OTUS "QA Automation"
Task 3: Files's code 'service1.py' coverage by automated tests (API - https://dog.ceo/dog-api/)
Author: Anton Borisov
"""

import pytest

from homework3.service1 import get_random_img_all
from homework3.service1 import get_multiple_img_all
from homework3.service1 import get_random_img_subbreed
from homework3.service1 import get_random_img_breed
from homework3.service1 import get_multiple_img_breed


# Тест на проверку получения одной случайной картинки собаки
def test_random_img_all():
    result = get_random_img_all()
    assert 'message' in result, "Expects message element presence in json list!"
    assert 'status' in result, "Expects status element presence in json list!"
    assert result['status'] == 'success', "Expects status 'success' get in json list!"
    assert '.jpg' or '.jpeg' in result['message'], "Expects '.jpg' ending presence in 'message' string!"


# Тест на проверку получения нескольких (трех) случайных картинок
def test_multiple_img():
    result = get_multiple_img_all()
    assert 'message' in result, "Expects message element presence in json list!"
    assert 'status' in result, "Expects status element presence in json list!"
    assert len(result['message']) == 3, "Expects 3 elements presence in json list by key 'message'!"
    assert result['status'] == 'success', "Expects status 'success' get in json list!"


# Тест на проверку получения одной случайной картинки из подпороды собак
def test_random_img_subbreed(breed='english'):
    result = get_random_img_subbreed(breed)
    assert 'message' in result, "Expects message element presence in json list!"
    assert 'status' in result, "Expects status element presence in json list!"
    assert result['status'] == 'success', "Expects status 'success' get in json list!"
    assert '.jpg' or '.jpeg' in result['message'], "Expects '.jpg' ending presence in 'message' string!"


# Параметризированный тест на проверку получения одной случайной картинки по определенной породе собаки
@pytest.mark.parametrize(
    "breed", [
        "hound",
        "briard",
        "boxer",
        "clumber",
        "pitbull"
    ]
)
def test_random_breed(breed):
    result = get_random_img_breed(breed)
    assert 'message' in result, "Expects message element presence in json list!"
    assert 'status' in result, "Expects status element presence in json list!"
    assert result['status'] == 'success', "Expects status 'success' got in json list!"
    assert '.jpg' or '.jpeg' in result['message'], "Expects '.jpg' ending presence in strings by key 'message'!"


# Параметризированный тест на проверку получения нескольких случайных картинок по определенной породе собаки
@pytest.mark.parametrize(
    "breed", [
        "hound",
        "dingo",
        "lhasa",
        "saluki",
        "shiba"
    ]
)
def test_multiple_image_breed(breed):
    result = get_multiple_img_breed(breed)
    assert 'message' in result, "Expects message element presence in json list!"
    assert 'status' in result, "Expects status element presence in json list!"
    assert len(result['message']) == 3, "Expects 3 elements presence in json list by key 'message'!"
    assert result['status'] == 'success', "Expects status 'success' get in json list!"
