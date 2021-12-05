import allure
import logging
import pytest
import os
from selenium import webdriver
from selenium.webdriver.opera.options import Options as OperaOptions
from selenium.webdriver.chrome.service import Service

DRIVERS = os.path.dirname(__file__)

logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s',
                    level=logging.INFO,
                    filename='tests.log')


def pytest_addoption(parser):
    parser.addoption("--maximized", action="store_true", help="Maximize browser windows")
    parser.addoption("--headless", action="store_true", help="Run tests headless")
    parser.addoption("--executor", action="store", default="127.0.0.1:8081",
                     choices=["127.0.0.1:8081", "192.168.1.45:8081", "0.0.0.0:4444"],
                     help="Choose from 127.0.0.1:8081, 192.168.1.45:8081, 0.0.0.0:4444")
    parser.addoption("--browser", action="store", default="chrome",
                     choices=["chrome", "firefox", "opera"])
    parser.addoption("--bversion", action="store", default="94.0",
                     choices=["94.0", "95.0", "92.0", "93.0", "79.0", "80.0"])
    parser.addoption("--vnc", action="store_true", default=False)
    parser.addoption("--logs", action="store_true", default=False)
    parser.addoption("--videos", action="store_true", default=False)
    parser.addoption("--mobile", action="store_true")
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
    parser.addoption("--remote_url", action="store",
                     default="http://0.0.0.0:4444/")


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
def remote_url(request):
    return request.config.getoption("--remote_url")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == 'call' and rep.failed:
        mode = 'a' if os.path.exists('failures') else 'w'
        try:
            with open('failures', mode) as f:
                if 'browser' in item.fixturenames:
                    web_driver = item.funcargs['browser']
                else:
                    print('Fail to take screen-shot')
                    return
            allure.attach(
                web_driver.get_screenshot_as_png(),
                name='screenshot',
                attachment_type=allure.attachment_type.PNG
            )
        except Exception as e:
            print('Fail to take screen-shot: {}'.format(e))


@pytest.fixture
def browser(request):
    _browser = request.config.getoption("--browser")
    executor = request.config.getoption("--executor")
    version = request.config.getoption("--bversion")
    vnc = request.config.getoption("--vnc")
    logs = request.config.getoption("--logs")
    videos = request.config.getoption("--videos")
    mobile = request.config.getoption("--mobile")
    headless = request.config.getoption("--headless")
    maximized = request.config.getoption("--maximized")
    logger = logging.getLogger('BrowserLoger')
    test_name = request.node.name

    logger.info(" ----> Test {} started".format(test_name))

    driver = None
    executor_url = f"http://{executor}/wd/hub"
    ser = Service("/Users/avboris/Develop/drivers/chromedriver")

    if _browser == "chrome":
        options = webdriver.ChromeOptions()
        options.binary_location = "/Applications/Google Chrome 0.app/Contents/MacOS/Google Chrome"
        chrome_driver_binary = f"{DRIVERS}/drivers/chromedriver"
        if headless:
            options.headless = True

        if executor == "127.0.0.1:8081":
            driver = webdriver.Chrome(service=ser, options=options)

        elif executor == "0.0.0.0:4444":
            capabilities = {
                "browserName": _browser,
                "browserVersion": version,
                "screenResolution": "1280x1024",
                "name": "Anton Chrome tests",
                "selenoid:options": {
                    "sessionTimeout": "60s",
                    "enableVNC": vnc,
                    "enableVideo": videos,
                    "enableLog": logs
                },
            }

            driver = webdriver.Remote(
                command_executor=executor_url,
                desired_capabilities=capabilities
            )

    elif _browser == "opera":
        options = OperaOptions()
        if headless:
            options.headless = True

        if executor == "127.0.0.1:8081":
            driver = webdriver.Opera(executable_path=f"{DRIVERS}/operadriver_mac64/operadriver", options=options)

        elif executor == "0.0.0.0:4444":
            capabilities = {
                "browserName": _browser,
                "browserVersion": version,
                "screenResolution": "1280x1024",
                "name": "Anton Opera tests",
                "selenoid:options": {
                    "sessionTimeout": "60s",
                    "enableVNC": vnc,
                    "enableVideo": videos,
                    "enableLog": logs
                },
            }

            driver = webdriver.Remote(
                command_executor=executor_url,
                desired_capabilities=capabilities
            )

    elif _browser == "firefox":
        options = webdriver.FirefoxOptions()
        if headless:
            options.headless = True

        if executor == "127.0.0.1:8081":
            driver = webdriver.Firefox(executable_path=f"{DRIVERS}/geckodriver", options=options)

        elif executor == "0.0.0.0:4444":
            capabilities = {
                "browserName": _browser,
                "browserVersion": version,
                "screenResolution": "1280x1024",
                "name": "Anton Firefox tests",
                "selenoid:options": {
                    "sessionTimeout": "60s",
                    "enableVNC": vnc,
                    "enableVideo": videos,
                    "enableLog": logs
                },
            }

            driver = webdriver.Remote(
                command_executor=executor_url,
                desired_capabilities=capabilities
            )

    if maximized:
        driver.maximize_window()

    def final():
        with open('allure-results/environment.properties', 'w') as f:
            f.write(f'Browser={_browser}\n')
            f.write(f'Browser.Version={version}\n')
            f.write(f'Executor={executor}\n')
            f.write(f'Headless={headless}')
        driver.quit()
        logger.info(" ----> Test {} finished".format(test_name))

    request.addfinalizer(final)

    return driver
