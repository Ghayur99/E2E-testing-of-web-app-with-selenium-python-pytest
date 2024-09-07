"""Test cases for login page"""
import time
import pytest
from selenium.webdriver.common.keys import Keys
from test_data.credentials import Credentials
from utilities.base_class import BaseClass
from page_objects.login_page import LoginPage


class TestLoginPage(BaseClass):

    """This is the class in which all the login test cases are defined in methods"""

    def test_wrong_email(self):
        """ In this test case we are checking login with invalid email address
        :param
        :return:
        """
        log = self.test_logging()
        login = LoginPage(self.driver)
        login_elements = login.login_xpaths
        self.get_elements(login_elements['email']).send_keys("Ghayur")
        self.get_visibility_element(login_elements['invalidEmailAlert'])
        emailAlert = self.get_elements(login_elements['invalidEmailAlert']).text
        assert "This field must only contain valid email" in emailAlert, "In valid Email Alert dose not appear"
        self.get_elements(login_elements['passwordField']).send_keys("ghayurbutt12")
        self.get_elements(login_elements['signInButton']).click()
        currentUrl = self.get_current_url()
        log.info("Current page URL is " + currentUrl)
        assert"https://app.taxslips.com/#/login" in currentUrl

    def test_wrong_password(self):

        """Login with the wrong Password
        :param 
        :return:
        """
        self.driver.refresh()
        log = self.test_logging()
        login = LoginPage(self.driver)
        login_elements = login.login_xpaths
        self.get_elements(login_elements['email']).send_keys("ghayur@technologyelement.com")
        login.actions.click(self.get_elements(login_elements['passwordField'])).perform()
        self.get_elements(login_elements['passwordField']).send_keys("ghayur")
        self.get_elements(login_elements['signInButton']).click()
        self.get_element_presence("//div[@class='toast-body']", 10)
        alert_text = self.get_elements(login_elements['toastMessage']).text
        log.info("Alert appears: " + alert_text)
        assert "Login attempt fail. Invalid email or password" == alert_text, "Alert message dose not appear"

    def test_with_unregistered_email(self):
        """Login with the wrong Email
        :param
        :return:
        """
        self.driver.refresh()
        log = self.test_logging()
        login = LoginPage(self.driver)
        login_elements = login.login_xpaths
        self.get_elements(login_elements['email']).send_keys("ghayur@webssential.ca")
        login.actions.click(self.get_elements(login_elements['passwordField'])).perform()
        self.get_elements(login_elements['passwordField']).send_keys("12345678Aa")
        self.get_elements(login_elements['signInButton']).click()
        self.get_element_presence("//div[@class='toast-body']", 10)
        alert_text = self.get_elements(login_elements['toastMessage']).text
        log.info("Alert appears: " + alert_text)
        assert "Login attempt fail. Invalid email or password" == alert_text, "Toast alert message dose not appear"

    def test_admin_login_credentials(self):
        """
        Login with correct email and password, and it's an admin role account
        :param:
        :return:
        """
        self.driver.refresh()
        login = LoginPage(self.driver)
        user_credentials = Credentials.users_credentials
        login_elements = login.login_xpaths
        self.get_elements(login_elements['email']).send_keys(user_credentials['loginEmail'])
        self.get_elements(login_elements['passwordField']).send_keys(user_credentials['password'])
        self.get_elements(login_elements['signInButton']).click()
        self.get_element_presence("//span[contains(text(),'Add Client')]", 10)
        current_url = self.get_current_url()
        assert "https://app.taxslips.com/#/accounts/clients/list/" == current_url, "Client list screen dose not " \
                                                                                  "appear after login"

    def test_superUser_login_credentials(self):
        """
        Login with correct email and password, and it's an superuser role account
        :param :
        :return:
        """
        log = self.test_logging()
        user_credentials = Credentials.users_credentials
        login = LoginPage(self.driver)
        login_elements = login.login_xpaths
        self.driver.get("https://app.taxslips.com/#/login")
        self.get_element_presence("//span[contains(text(),'Logout')]", 10)
        self.get_elements(login_elements['logout']).click()
        self.get_text_prasence("Create an Account", 10)
        self.get_elements(login_elements['email']).send_keys(user_credentials['SUPER_USER_EMAIL'])
        self.get_elements(login_elements['passwordField']).send_keys(user_credentials['SUPER_USER_PASSWORD'])
        self.get_elements(login_elements['signInButton']).click()
        self.get_element_presence("//div[contains(text(),'Accountants')]", 10)
        current_url = self.get_current_url()
        log.info("Current page URL is " + current_url)
        assert "https://app.taxslips.com/#/accounts/global/search/" == current_url, "Global search screen dose not " \
                                                                                   "appear after login"

    def test_forgot_password(self):
        """
        Checking forgot password link
        :return:
        """
        log = self.test_logging()
        login = LoginPage(self.driver)
        login_elements = login.login_xpaths
        self.driver.get("https://app.taxslips.com/#/login")
        self.get_element_presence("//span[contains(text(),'Logout')]", 10)
        self.get_elements(login_elements['logout']).click()
        self.get_text_prasence("Forgot Password?", 10)
        self.get_elements(login_elements['forgotPassword']).click()
        time.sleep(1)
        current_url = self.get_current_url()
        log.info("Current page URL is " + current_url)
        assert "https://app.taxslips.com/#/forgotpassword" == current_url, "Forgot password link is not working"

    def test_create_an_account(self):
        """
        Checking Create an account link
        :return:
        """
        login = LoginPage(self.driver)
        login_elements = login.login_xpaths
        self.driver.get("https://app.taxslips.com/#/login")
        self.get_text_prasence("Create an Account", 10)
        self.get_elements(login_elements['createAccount']).click()
        self.get_element_presence("//h1[contains(text(),'Coming Soon')]", 10)
        current_url = self.get_current_url()
        assert "https://app.taxslips.com/#/comingsoon" == current_url, "Create an account link is not working"

    def test_required_fields(self):
        """
        Test case to test the required fields
        :return:
        """
        login = LoginPage(self.driver)
        login_elements = login.login_xpaths
        self.driver.get("https://app.taxslips.com/#/login")
        self.get_text_prasence("Create an Account", 10)
        self.get_elements(login_elements['signInButton']).click()
        self.get_elements(login_elements['signInButton']).click()
        self.get_text_prasence_in_element(login_elements['emailRequiredAlert'], "This")
        email_alert = self.get_elements(login_elements['emailRequiredAlert']).text
        self.get_elements(login_elements['email']).send_keys("Ghayurtest@gmail.com")
        self.get_elements(login_elements['signInButton']).click()
        self.get_elements(login_elements['signInButton']).click()
        self.get_text_prasence_in_element(login_elements['passwordRequiredAlert'], "This")
        password_alert = self.get_elements(login_elements['passwordRequiredAlert']).text
        current_url = self.get_current_url()
        assert current_url == "https://app.taxslips.com/#/login"
        assert email_alert == "This field is required", "Email do not have required field alert"
        assert password_alert == "This field is required", "Password do not have required field alert"

    def test_enter_key(self):
        """
        To test that user will login if user press enter key after providing correct credentials
        :return:
        """
        log = self.test_logging()
        g_credentials = Credentials.users_credentials
        login = LoginPage(self.driver)
        login_elements = login.login_xpaths
        self.driver.refresh()
        self.get_elements(login_elements['email']).send_keys(g_credentials['loginEmail'])
        self.get_elements(login_elements['passwordField']).send_keys(g_credentials['password'])
        self.get_elements(login_elements['passwordField']).send_keys(Keys.ENTER)
        self.get_element_presence("//span[contains(text(),'Add Client')]", 10)
        current_url = self.get_current_url()
        log.info("Current page URL is " + current_url)
        assert "https://app.taxslips.com/#/accounts/clients/list/" == current_url, "Client list screen dose not " \
                                                                                   "appear after login"
