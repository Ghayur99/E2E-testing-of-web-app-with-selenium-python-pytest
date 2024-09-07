"""ForgotPassword page objects are define here"""

from page_objects.common_objects import CommonObjects

class ForgotPassword(CommonObjects):
    """This class contains webElements of ForgotPassword page """
    forgot_password_xpaths = {
        "emailField": "//input[@id='id_email']", "emailFieldAlert": "//*[contains(@class, 'v-input')]//*[contains"
                                                                    "(@class, 'v-messages__message')]",
        "submitButton": "//button[@type='submit']", "cancelButton": "//span[contains(text(),'Cancel')]",
        "loginButton": "//span[@class= 'v-btn__content']", "emailSent": "//p[contains(text(),'Email Sent')]",
        "toastMessage": "//div[@class='toast-body']"
    }
