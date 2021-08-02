"""
School: OTUS "QA Automation"
Task 3: Getting test data from API - https://jsonplaceholder.typicode.com/
Author: Anton Borisov
"""

import requests


# Функция, которая получает 100 постов в формате json
def get_posts_all():
    result = requests.get("https://jsonplaceholder.typicode.com/posts").json()
    return result


# Функция, которая получает 500 комментариев в формате json
def get_comments_all():
    result = requests.get("https://jsonplaceholder.typicode.com/comments").json()
    return result


# Функция, которая получает 5000 фото в формате json
def get_photos_all():
    result = requests.get("https://jsonplaceholder.typicode.com/photos").json()
    return result


# Функция, которая получает пост по его id в формате json
def get_post_by_id(brew_id):
    result = requests.get(f"https://jsonplaceholder.typicode.com/posts/{brew_id}").json()
    return result


# Функция, которая получает комментарии по id поста в формате json
def get_comments_by_postid(post_id):
    result = requests.get(f"https://jsonplaceholder.typicode.com/comments?postId={post_id}").json()
    return result
