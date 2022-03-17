from behave import *

from pages.landing_page import LandingPage
from properties import Properties

use_step_matcher("re")


@given("Landing page is opened")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    page = LandingPage(context)
    page.open()


@when("I sign in with correct credentials")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    page = LandingPage(context)
    page.login(context.config.userdata[Properties.USER_EMAIL], context.config.userdata[Properties.USER_PASSWORD])


@then("I should be on the Landing Page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    page = LandingPage(context)
    page.verify_page_opened()
