from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def find_element(self, locator: tuple, time=10):
        return WebDriverWait(self.browser, time).until(EC.visibility_of_element_located((locator)),
                                                       message=f"Can't find element by locator {locator}")

    def find_elements(self, locator: tuple, time=10):
        return WebDriverWait(self.browser, time).until(EC.visibility_of_all_elements_located(locator),
                                                       message=f"Can't find elements by locator {locator}")

    def verify_element_presence(self, locator: tuple, time=10):
        try:
            return WebDriverWait(self.browser, time).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            raise AssertionError(f"Can't find element by locator {locator}")

    def go_to_site(self):
        return self.browser.get(self.url)

    def get_property(self, element: object, prop: str):
        return element.get_property(prop)

    def get_quantity(self, locator: tuple):
        return len(self.find_elements(locator, 2))

    def simple_click(self, locator: tuple):
        self.find_element(locator).click()

    def move_and_click(self, locator: tuple):
        element = self.find_element(locator)
        ActionChains(self.browser).pause(0.3).move_to_element(element).pause(0.3).click().perform()

    def get_page_title(self):
        return self.browser.title

    def alert_accept(self):
        self.browser.switch_to_alert().accept()

    def alert_dismiss(self):
        self.browser.switch_to_alert().dismiss()

    def enter_data(self, locator: tuple, value: str):
        self.find_element(locator, 2).send_keys(value)
