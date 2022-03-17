from behave import *

from pages.choose_country_language_page import ChooseCountryLanguagePage

use_step_matcher("re")


@given("Choose country and language page is opened")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    page = ChooseCountryLanguagePage(context)
    page.open()


@when("I submit country and language")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    page = ChooseCountryLanguagePage(context)
    page.set_country("US")
    page.set_language("en-US")
    page.click_submit_btn()
