"""
confTest file is used to define fixtures
"""

import pytest
from selenium import webdriver

from settings.development import CHROME_DRIVER_PATH

driver = None


def pytest_addoption(parser):  # To add the different command line options to your framework
    """
    Function to select the webDriver on run time
    :param parser:
    :return:
    """
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    """
    To setup the browser for the test cases to run
    :param request: Default parameter
    :return:
    """
    # option = webdriver.ChromeOptions()
    # option.add_argument('headless')
    global driver
    browser_name = request.config.getoption("browser_name")     # Setting up the option of commandline
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path="d:\\geckodriver.exe")
    elif browser_name == "IE":
        print("IE driver")
    driver.get("https://app.taxslips.com/#/login")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()

