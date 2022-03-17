from behave import *

from pages.upload_device_page import UploadDevicePage

use_step_matcher("re")


@then("I should be on the Upload Device page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    page = UploadDevicePage(context)
    page.verify_page_opened()
