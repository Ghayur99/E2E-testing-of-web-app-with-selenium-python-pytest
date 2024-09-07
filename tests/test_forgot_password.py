"""Test cases for forgotPassword page"""
import time

import pytest

from utilities.base_class import BaseClass
from page_objects.login_page import LoginPage
from page_objects.forgot_password import ForgotPassword


class TestForgotPassword(BaseClass):

    """This is the class in which all the login test cases are defined in methods"""

    def test_wrong_email_alert(self):
        """ In this test case we are checking invalid email alert
        :return: Pass or fail
        """
        log = self.test_logging()
        forgot = ForgotPassword(self.driver)
        login = LoginPage(self.driver)
        login_elements = login.login_xpaths
        forgot_elements = forgot.forgot_password_xpaths
        self.get_elements(login_elements['forgotPassword']).click()
        self.get_element_presence("//p[contains(text(),'Forgot Password')]", 10)
        email = "TestEmail123.com"
        log.info("Email is =" + email)
        self.get_elements(forgot_elements['emailField']).send_keys(email)
        self.get_text_prasence_in_element(forgot_elements['emailFieldAlert'], "This field must only contain valid email")
        email_alert = self.get_elements(forgot_elements['emailFieldAlert']).text
        log.info("Error Alert message is " + str(email_alert))
        self.get_text_prasence_in_element(forgot_elements['emailFieldAlert'], "This field must only contain valid email")
        assert "This field must only contain valid email" == email_alert, "In valid Email Alert dose not appear"

    def test_cancel_button(self):
        """
        Testing the cancel button functionality
        :return:
        """
        forgot = ForgotPassword(self.driver)
        forgot_elements = forgot.forgot_password_xpaths
        self.get_elements(forgot_elements['cancelButton']).click()
        email_field_value = self.get_elements(forgot_elements['emailField']).get_attribute("value")
        assert "" == email_field_value, "cancel button is not working"

    def test_required_field_alert(self):
        """
        In this test case we are checking required field alerts
        :return:
        """
        log = self.test_logging()
        forgot = ForgotPassword(self.driver)
        forgot_elements = forgot.forgot_password_xpaths
        forgot.actions.double_click(self.get_elements(forgot_elements['submitButton'])).perform()
        self.get_text_prasence_in_element(forgot_elements['emailFieldAlert'], "This field")
        alert = self.get_elements(forgot_elements['emailFieldAlert']).text
        log.info("The required field alert is: " + alert)
        assert "This field is required" == alert, "required field alert message dose not appear"

    def test_toast_alert_message(self):
        """
        Testing the toast alert message by providing the email which is not registered with taxSlips.com
        :return:
        """
        log = self.test_logging()
        forgot = ForgotPassword(self.driver)
        forgot_elements = forgot.forgot_password_xpaths
        email = "ghayur@websential.ca"
        log.info("Email is =" + email)
        self.get_elements(forgot_elements['emailField']).send_keys(email)
        self.get_elements(forgot_elements['submitButton']).click()
        self.get_text_prasence_in_element("//div[@class='toast-body']", "Email does not exist")
        toast_message = self.get_elements(forgot_elements['toastMessage']).text
        log.info("Toast message is:" + toast_message)
        assert "Email does not exist" == toast_message

    def test_forgot_password_with_correct_emil(self):
        """
        Checking the forgot password with the correct and registered email
        After submitting with correct email, it will check the success toast message
        This method will test if user will land on the page https://app.taxslips.com/#/register/forgetcompleted
        And on this page user will click on login button and land on login page

        :return:
        """
        log = self.test_logging()
        forgot = ForgotPassword(self.driver)
        forgot_elements = forgot.forgot_password_xpaths
        self.driver.refresh()
        email = "ghayur@technologyelement.com"
        log.info("Email is =" + email)
        self.get_elements(forgot_elements['emailField']).send_keys(email)
        self.get_elements(forgot_elements['submitButton']).click()
        self.get_text_prasence_in_element(forgot_elements["toastMessage"], "Success")
        toast_message = self.get_elements(forgot_elements['toastMessage']).text
        assert "Success" in toast_message, "toast_message dose not appear"
        self.get_element_presence("//p[contains(text(),'Email Sent')]", 10)
        self.get_elements(forgot_elements['loginButton']).click()
        self.get_element_presence("//a[contains(text(),'Create an Account')]", 10)
        current_url = self.get_current_url()
        assert "https://app.taxslips.com/#/login" == current_url
