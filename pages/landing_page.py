from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LandingPage(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context)

    __email_field_locator = (By.ID, "loginForm-email-input")
    __password_field_locator = (By.ID, "loginForm-password-input")
    __log_in_btn_locator = (By.ID, "loginForm-submit-button")

    def open(self):
        self.visit()

    def login(self, email: str, password: str):
        self.find_element(self.__email_field_locator).send_keys(email)
        self.find_element(self.__password_field_locator).send_keys(password)
        self.click_element(self.__log_in_btn_locator)

    def verify_page_opened(self):
        self.wait_for_url(self.context.base_url)
