from behave import *

from utils.email_verification import get_confirmation_code_from_email
from pages.identity_verification_page import IdentityVerificationPage

use_step_matcher("re")


@then("I should be on the Identity Verification page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    page = IdentityVerificationPage(context)
    page.verify_page_opened()


@then("Verify submit button is (enabled|disabled)")
def step_impl(context, condition):
    """
    :type context: behave.runner.Context
    :param condition: expected button state (enabled or disabled)
    """
    page = IdentityVerificationPage(context)
    page.verify_submit_btn_enabled(True if condition == "enabled" else False)


@when("I click Submit button")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    page = IdentityVerificationPage(context)
    page.click_submit_btn()


@when("I enter verification code")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    page = IdentityVerificationPage(context)
    verification_code = get_confirmation_code_from_email()
    page.enter_verification_code(verification_code)


@then("Verification code field should be displayed")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    page = IdentityVerificationPage(context)
    page.wait_for_verification_code_field()
