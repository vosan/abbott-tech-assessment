from pages.base_page import BasePage


class UploadDevicePage(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context)
        self.url_extension = "meter"

    def verify_page_opened(self):
        self.wait_for_url(self.context.base_url + self.url_extension)
