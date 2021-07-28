"""
School: OTUS "QA Automation"
Task 3: Files's code 'service3.py' coverage by automated tests (API - https://jsonplaceholder.typicode.com/)
Author: Anton Borisov
"""

import pytest
from random import randint

from homework3.service3 import get_posts_all
from homework3.service3 import get_comments_all
from homework3.service3 import get_photos_all
from homework3.service3 import get_post_by_id
from homework3.service3 import get_comments_by_postid


# Тест на получение 100 постов в формате json (допом проверка наличия полей в случаейных элементах по ключам)
def test_posts_all():
    result = get_posts_all()
    rand_post = result[randint(0, len(result) - 1)]
    assert 'body' in rand_post, "Expects 'body' key presence in random element of json!"
    assert 'userId' in rand_post, "Expects 'userId' key presence in random element of json!"
    assert 'title' in rand_post, "Expects 'title' key presence in random element of json!"
    assert 'id' in rand_post, "Expects 'id' key presence in random element of json!"
    assert len(result) == 100, "Expects 100 posts presence in json!"


# Тест на получение 500 комментариев в формате json (допом проверка наличия полей в случаейных элементах по ключам)
def test_comments_all():
    result = get_comments_all()
    rand_comment = result[randint(0, len(result) - 1)]
    assert 'body' in rand_comment, "Expects 'body' key presence in random element of json!"
    assert 'email' in rand_comment, "Expects 'email' key presence in random element of json!"
    assert 'id' in rand_comment, "Expects 'id' key presence in random element of json!"
    assert 'name' in rand_comment, "Expects 'name' key presence in random element of json!"
    assert 'postId' in rand_comment, "Expects 'postId' key presence in random element of json!"
    assert len(result) == 500, "Expects 500 comments presence in json!"


# Тест на получение 5000 фото в формате json (допом проверка наличия полей в случаейных элементах по ключам)
def test_photos_all():
    result = get_photos_all()
    rand_photo = result[randint(0, len(result) - 1)]
    assert 'albumId' in rand_photo, "Expects 'albumId' key presence in random element of json!"
    assert 'id' in rand_photo, "Expects 'id' key presence in random element of json!"
    assert 'thumbnailUrl' in rand_photo, "Expects 'thumbnailUrl' key presence in random element of json!"
    assert 'title' in rand_photo, "Expects 'title' key presence in random element of json!"
    assert 'url' in rand_photo, "Expects 'url' key presence in random element of json!"
    assert len(result) == 5000, "Expects 5000 photos presence in json!"


# Параметризированный тест на получение поста по его id в формате json
# (допом проверка наличия полей в получаемом элементе)
@pytest.mark.parametrize(
    "brew_id", [
        "2",
        "12",
        "23",
        "56",
        "78",
        "99"
    ]
)
def test_post_by_id(brew_id):
    result = get_post_by_id(brew_id)
    assert len(result) == 4, "Expects dict in json consists of 4 elements!"
    assert 'body' in result, "Expects 'body' key presence in json!"
    assert 'id' in result, "Expects 'id' key presence in random element of json!"
    assert 'title' in result, "Expects 'title' key presence in random element of json!"
    assert 'userId' in result, "Expects 'userId' key presence in random element of json!"


# Параметризированный тест на получение комментариев по его post_id в формате json
# (допом проверка наличия полей в получаемом элементе)
@pytest.mark.parametrize(
    "post_id", [
        "6",
        "11",
        "19",
        "34",
        "42",
        "72"
    ]
)
def test_comments_by_id(post_id):
    result = get_comments_by_postid(post_id)
    rand_post = result[randint(0, len(result) - 1)]
    assert 'body' in rand_post, "Expects 'body' key presence in random element of json!"
    assert 'email' in rand_post, "Expects 'email' key presence in random element of json!"
    assert 'id' in rand_post, "Expects 'id' key presence in random element of json!"
    assert 'name' in rand_post, "Expects 'name' key presence in random element of json!"
    assert 'postId' in rand_post, "Expects 'postId' key presence in random element of json!"
    assert len(result) == 5, "Expects 5 elements presence in json!"
