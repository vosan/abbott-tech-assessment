from typing import Tuple

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webdriver import WebElement, WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from constants import Constants
from utils.helpers import normalize_url


class BasePage:
    def __init__(self, context):
        self.context = context
        self.browser: WebDriver = context.browser

    def find_element(self, locator: Tuple[str, str]) -> WebElement:
        """
        :param locator: a tuple pair of By value and locator value. Example: (By.ID, "someId")
        :return: a web element that matches the specified locator
        """
        (by, locator) = locator
        return self.browser.find_element(by, locator)

    def click_element(self, locator: Tuple[str, str]):
        """
        Performs click on a specified element. Implicit_wait will be applied if element was not found
        :param locator: a tuple pair of By value and locator value. Example: (By.ID, "someId")
        """
        self.wait_until_displayed(locator)
        self.find_element(locator).click()

    def enter_text(self, value, locator):
        """
        type_text: enters value in text field
        :param value: value that you want to add in text field
        :param locator: locator of text field
        """
        element = self.find_element(locator)
        element.clear()
        element.send_keys(value)

    def wait_until_displayed(self, locator: Tuple[str, str], timeout=Constants.MEDIUM_TIMEOUT):
        """
        Wait until the specified element is visible
        :param locator: a tuple pair of By value and locator value. Example: (By.ID, "someId")
        :param timeout: seconds
        """
        self.browser.implicitly_wait(0)  # disable implicit wait as with WebDriverWait it results in longer wait time

        try:
            WebDriverWait(self.browser, timeout).until(
                ec.visibility_of_element_located(locator))  # wait until element is visible
        except TimeoutException:
            raise TimeoutException(f"Could not find element: {locator} within: {timeout} seconds timeout.")

        self.browser.implicitly_wait(Constants.IMPLICIT_TIMEOUT)  # re-enable implicit wait

    def wait_until_gone(self, locator: Tuple[str, str], timeout=Constants.MEDIUM_TIMEOUT):
        """
        Wait until the specified element is not present on the DOM
        :param locator: a tuple pair of By value and locator value. Example: (By.ID, "someId")
        :param timeout: seconds
        """
        self.browser.implicitly_wait(0)  # disable implicit wait as with WebDriverWait it results in longer wait time

        try:
            WebDriverWait(self.browser, timeout).until_not(
                ec.presence_of_element_located(locator))  # wait until element is gone
        except TimeoutException:
            raise TimeoutException(f"Element: {locator} was not gone within {timeout} seconds.")

        self.browser.implicitly_wait(Constants.IMPLICIT_TIMEOUT)  # re-enable implicit wait

    def wait_for_url(self, expected_url: str, timeout=Constants.MEDIUM_TIMEOUT):
        """
        Wait until the expected URL is detected
        :param expected_url: full URL (base url + subdir)
        :param timeout: seconds
        """
        try:
            WebDriverWait(self.browser, timeout).until(
                lambda browser: normalize_url(browser.current_url) == normalize_url(expected_url)
            )
        except TimeoutException:
            raise TimeoutException(f"Couldn't verify the expected URL: {expected_url} within {timeout} seconds")

    def verify_element_enabled(self, locator, is_clickable):
        result = self.find_element(locator).is_enabled()
        if is_clickable:
            assert result, f"Expected element {locator} to be enabled."
        else:
            assert not result, f"Expected element {locator} to be disabled."

    def visit(self, url_subdirectory=""):
        """
        Open the specified URL in the browser
        :param url_subdirectory: subdirectory to be added to the main URL. Example: "/subdirectory/"
        """
        self.browser.get(normalize_url(self.context.base_url + url_subdirectory))
