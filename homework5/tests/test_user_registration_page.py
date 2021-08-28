"""
School: OTUS "QA Automation"
Task 5: User registration page http://127.0.0.1:8081/index.php?route=account/register coverage by automated tests
Tests:
1. Проверка успешности регистрации нового пользователя
Author: Anton Borisov
"""

from homework5.page_objects.UserRegisterPage import UserRegisterPage
from homework5.page_objects.TestData import UserRegisterPageTestData


# Тест на проверку успешности регистрации нового пользователя
def test_user_registration(browser, local_register_url):
    user_reg_page = UserRegisterPage(browser, local_register_url)
    user_reg_page.go_to_site()
    user_reg_page.fill_in_register_form()
    user_reg_page.agree_with_policy()
    user_reg_page.push_continue_btn()
    if user_reg_page.verify_element_presence(UserRegisterPage.SUCCESS_BLOCK, 2):
        assert user_reg_page.get_page_title() == UserRegisterPageTestData.SUCCESS_REGISTER_PAGE_TITLE, "Needs page title to be equal to 'Your Account Has Been Created!'"
