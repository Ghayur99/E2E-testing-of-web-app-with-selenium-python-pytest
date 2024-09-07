"""Login page objects are define here"""

from page_objects.common_objects import CommonObjects


class LoginPage(CommonObjects):
    """This class contains webElements of login page """

    login_xpaths = {"email": "//input[@id='id_email']",
                    "passwordField": "//input[@id='id_password']",
                    "forgotPassword": "//a[contains(text(), 'Forgot Password?')]",
                    "signInButton": "//button[@type='submit']",
                    "hidePasswordButton": "//button[@type='button']",
                    "invalidEmailAlert": "//div[contains(text(),'This field must only contain valid email')]",
                    "emailRequiredAlert": "//body/div[@id='__nuxt']/div[@id='__layout']/div[@id='inspire']/div[1]"
                                          "/main[1]/div[1]/div[1]/div[2]/div[1]/div[1]/span[1]/form[1]/span[1]/div[1]"
                                          "/div[1]/div[2]/div[1]/div[1]/div[1]",
                    "passwordRequiredAlert": "//*[contains(@class, 'password')]//*[contains(@class, "
                                             "'v-messages__message')]",
                    "toastMessage": "//div[@class='toast-body']",
                    "logout": "//span[contains(text(),'Logout')]",
                    "createAccount": "//a[contains(text(),'Create an Account')]"
                    }
