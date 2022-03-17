from datetime import datetime
import os

from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from properties import Properties


class IdentityVerificationPage(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context)
        self.url_extension = "auth/finishlogin"

    __page_title_locator = (By.ID, "wizardTitle-text")
    __verification_code_field_locator = (By.ID, "twoFactor-step2-code-input")
    __submit_btn_locator = (By.CSS_SELECTOR, "button[type='submit']")

    def verify_page_opened(self):
        self.wait_until_displayed(self.__page_title_locator)
        self.wait_for_url(self.context.base_url + self.url_extension)

    def click_submit_btn(self):
        self.click_element(self.__submit_btn_locator)
        os.environ[Properties.VERIF_CODE_REQUEST_TIME] = str(datetime.utcnow())

    def enter_verification_code(self, value):
        self.enter_text(value, self.__verification_code_field_locator)

    def verify_submit_btn_enabled(self, is_enabled: bool):
        self.verify_element_enabled(self.__submit_btn_locator, is_enabled)

    def wait_for_verification_code_field(self):
        self.wait_until_displayed(self.__verification_code_field_locator)
