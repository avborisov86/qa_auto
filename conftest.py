import pytest
from selenium import webdriver
import os
from selenium.webdriver.opera.options import Options as OperaOptions

DRIVERS = os.path.expanduser("/Users/avboris/Develop/drivers")


def pytest_addoption(parser):
    parser.addoption("--maximized", action="store_true", help="Maximize browser windows")
    parser.addoption("--headless", action="store_true", help="Run tests headless")
    parser.addoption("--browser", action="store", default="chrome", choices=["chrome", "opera", "firefox", "safari"])
    parser.addoption("--url_base", action="store", default="https://demo.opencart.com")
    parser.addoption("--url_cat", action="store",
                     default="https://demo.opencart.com/index.php?route=product/category&path=18")
    parser.addoption("--url_prod", action="store",
                     default="https://demo.opencart.com/index.php?route=product/product&path=18&product_id=44")
    parser.addoption("--url_auth", action="store",
                     default="https://demo.opencart.com/admin/")


@pytest.fixture
def url_base(request):
    return request.config.getoption("--url_base")


@pytest.fixture
def url_cat(request):
    return request.config.getoption("--url_cat")


@pytest.fixture
def url_prod(request):
    return request.config.getoption("--url_prod")


@pytest.fixture
def url_auth(request):
    return request.config.getoption("--url_auth")


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
