import pytest
from selenium import webdriver
import os
from selenium.webdriver.opera.options import Options as OperaOptions

DRIVERS = os.path.expanduser("/Users/avboris/Develop/drivers")


def pytest_addoption(parser):
    parser.addoption("--maximized", action="store_true", help="Maximize browser windows")
    parser.addoption("--headless", action="store_true", help="Run tests headless")
    parser.addoption("--browser", action="store", default="chrome", choices=["chrome", "opera", "firefox", "safari"])
    parser.addoption("--base_url", action="store", default="https://demo.opencart.com")
    parser.addoption("--cat_url", action="store",
                     default="https://demo.opencart.com/index.php?route=product/category&path=18")
    parser.addoption("--prod_url", action="store",
                     default="https://demo.opencart.com/index.php?route=product/product&path=18&product_id=44")
    parser.addoption("--auth_url", action="store",
                     default="https://demo.opencart.com/admin/")
    parser.addoption("--local_base_url", action="store", default="http://127.0.0.1:8081/")
    parser.addoption("--local_admin_url", action="store", default="http://127.0.0.1:8081/admin/")
    parser.addoption("--local_register_url", action="store",
                     default="http://127.0.0.1:8081/index.php?route=account/register")


@pytest.fixture
def base_url(request):
    return request.config.getoption("--base_url")


@pytest.fixture
def cat_url(request):
    return request.config.getoption("--cat_url")


@pytest.fixture
def prod_url(request):
    return request.config.getoption("--prod_url")


@pytest.fixture
def auth_url(request):
    return request.config.getoption("--auth_url")


@pytest.fixture
def local_base_url(request):
    return request.config.getoption("--local_base_url")


@pytest.fixture
def local_admin_url(request):
    return request.config.getoption("--local_admin_url")


@pytest.fixture
def local_register_url(request):
    return request.config.getoption("--local_register_url")


@pytest.fixture
def browser(request):
    _browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    maximized = request.config.getoption("--maximized")

    driver = None

    if _browser == "chrome":
        options = webdriver.ChromeOptions()
        options.binary_location = "/Applications/Google Chrome 0.app/Contents/MacOS/Google Chrome"
        chrome_driver_binary = "/Users/avboris/Develop/drivers/chromedriver"
        if headless:
            options.headless = True
        driver = webdriver.Chrome(chrome_driver_binary, options=options)

    elif _browser == "opera":
        options = OperaOptions()
        if headless:
            options.headless = True
        driver = webdriver.Opera(executable_path=f"{DRIVERS}/operadriver_mac64/operadriver", options=options)

    elif _browser == "firefox":
        options = webdriver.FirefoxOptions()
        if headless:
            options.headless = True
        driver = webdriver.Firefox(executable_path=f"{DRIVERS}/geckodriver", options=options)

    elif _browser == "safari":
        driver = webdriver.Safari(executable_path="/usr/bin/safaridriver")

    if maximized:
        driver.maximize_window()

    def final():
        driver.quit()

    request.addfinalizer(final)

    return driver
