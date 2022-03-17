from behave.model_core import Status
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from datetime import datetime
import time
import os
import sys

from constants import Constants
from properties import Properties

"""
    behave -D user_email=codechallengeadc@gmail.com -D user_password=P@ssword1234 -D country=US -D language=en_US
"""


def before_all(context):
    context.base_url = "https://www.libreview.com/"


def before_scenario(context, scenario):
    print("\nUser data:", context.config.userdata)
    # behave -D browser=chrome
    if context.config.userdata[Properties.BROWSER] == "true" or \
            context.config.userdata[Properties.BROWSER] == "chrome":  # if 'browser' parameter is declared without value
        context.browser = webdriver.Chrome()
    elif context.config.userdata[Properties.BROWSER] == "firefox":
        context.browser = webdriver.Firefox()
    elif context.config.userdata[Properties.BROWSER] == "safari":
        context.browser = webdriver.Safari()
    elif context.config.userdata[Properties.BROWSER] == "ie":
        context.browser = webdriver.Ie()
    elif context.config.userdata[Properties.BROWSER] == "opera":
        context.browser = webdriver.Opera()
    elif context.config.userdata[Properties.BROWSER] == "phantomjs":
        context.browser = webdriver.PhantomJS()
    else:
        print(f"'{context.config.userdata[Properties.BROWSER]}' browser is not supported.")

    context.browser.set_window_size(1024, 768)
    context.browser.implicitly_wait(Constants.IMPLICIT_TIMEOUT)
    context.browser.set_page_load_timeout(Constants.LONG_TIMEOUT)


def after_scenario(context, scenario):
    if scenario.status == Status.failed:
        if not os.path.exists("failed_scenarios_screenshots"):
            os.makedirs("failed_scenarios_screenshots")
        os.chdir("failed_scenarios_screenshots")
        context.browser.save_screenshot(scenario.name + "_failed.png")

    context.browser.delete_all_cookies()
    context.browser.quit()
