import allure
import logging
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import common


class BasePage:

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        self.logger = logging.getLogger(type(self).__name__)

    @allure.step("Looking for the unique element {locator} on the page")
    def find_element(self, locator: tuple, time=10):
        self.logger.info("Finding element {}".format(locator))
        try:
            return WebDriverWait(self.browser, time).until(EC.visibility_of_element_located(locator),
                                                           message=f"Can't find element by locator {locator}")
        except TimeoutException:
            raise AssertionError(f"Can't find element by locator {locator}")
        # except common.exceptions.NoSuchElementException:
        #     allure.attach(
        #         name=self.browser.session_id,
        #         body=self.browser.get_screenshot_as_png(),
        #         attachment_type=allure.attachment_type.PNG
        #     )
        #     raise AssertionError(f"Element {locator} not found on the page!")

    @allure.step("Looking for same elements on the page")
    def find_elements(self, locator: tuple, time=10):
        self.logger.info("Finding elements {}".format(locator))
        return WebDriverWait(self.browser, time).until(EC.visibility_of_all_elements_located(locator),
                                                       message=f"Can't find elements by locator {locator}")

    @allure.step("Verifying if the element {locator} is on the page and visible")
    def verify_element_presence(self, locator: tuple, time=10):
        self.logger.info("Verifying element {} presence".format(locator))
        try:
            return WebDriverWait(self.browser, time).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            raise AssertionError(f"Can't find element by locator {locator}")

    @allure.step("Going to page")
    def go_to_site(self):
        self.logger.info("Moving to url {}".format(self.url))
        return self.browser.get(self.url)

    @allure.step("Getting property of the element")
    def get_property(self, locator: tuple, prop: str):
        elem_property = self.find_element(locator).get_property(prop)
        self.logger.info("Getting property '{}' of element {}".format(prop, locator))
        return elem_property

    @allure.step("Getting quantity of elements")
    def get_quantity(self, locator: tuple):
        quantity = len(self.find_elements(locator))
        self.logger.info("Getting quantity of elements {}".format(locator))
        return quantity

    @allure.step("Clicking the element (without mouse moving)")
    def simple_click(self, locator: tuple):
        self.find_element(locator).click()
        self.logger.info("Clicking element (without mouse moving) {}".format(locator))

    @allure.step("Moving the mouse to the element and clicking it")
    def move_and_click(self, locator: tuple, time=0.5):
        ActionChains(self.browser).pause(time).move_to_element(self.find_element(locator)).pause(time).click().perform()
        self.logger.info("Moving the mouse to the element {} and clicking".format(locator))

    @allure.step("Getting the page title")
    def get_page_title(self):
        self.logger.info("Getting page {} title".format(self.url))
        return self.browser.title

    @allure.step("Approving the allert message")
    def alert_accept(self):
        self.logger.info("Accepting alert {}".format(self.browser.switch_to.alert))
        self.browser.switch_to.alert.accept()

    @allure.step("Denying the allert message")
    def alert_dismiss(self):
        self.logger.info("Denying alert {}".format(self.browser.switch_to.alert))
        self.browser.switch_to.alert.dismiss()

    @allure.step("Entering data to element")
    def enter_data(self, locator: tuple, value: str):
        entered_value = self.find_element(locator, 2).send_keys(value)
        self.logger.info("Entering value '{}' to element {}".format(value, locator))
        return entered_value

    @allure.step("Checking css property")
    def get_css_property(self, locator: tuple, value: str):
        css_property = self.find_element(locator).value_of_css_property(value)
        self.logger.info("Getting css property '{}'".format(value))
        return css_property
