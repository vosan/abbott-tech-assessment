import re

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from constants import Constants
from pages.base_page import BasePage


class ChooseCountryLanguagePage(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context)
        self.url_extension = "chooseCountryLanguage"

    __country_drop_down_locator = (By.ID, "country-select")
    __language_drop_down_locator = (By.ID, "language-select")
    __submit_btn_locator = (By.ID, "submit-button")
    __loading_screen_logo_locator = (By.CLASS_NAME, "pg-loading-logo")

    def wait_for_loading_screen_gone(self, timeout=Constants.SHORT_TIMEOUT):
        self.wait_until_gone(self.__loading_screen_logo_locator, timeout)

    def open(self):
        self.visit(self.url_extension)
        self.wait_for_loading_screen_gone()

    def set_country(self, country: str = "US"):
        is_by_value = re.compile("[A-Z]{2}")
        element = self.find_element(self.__country_drop_down_locator)
        select = Select(element)
        if is_by_value.match(country):
            select.select_by_value(country)
        else:
            select.select_by_visible_text(country)
        return self

    def set_language(self, language: str = "en-US"):
        is_by_value = re.compile("[a-z]{2}-[A-Z]{2}")
        element = self.find_element(self.__language_drop_down_locator)
        select = Select(element)
        if is_by_value.match(language):
            select.select_by_value(language)
        else:
            select.select_by_visible_text(language)
        return self

    def click_submit_btn(self):
        self.click_element(self.__submit_btn_locator)
