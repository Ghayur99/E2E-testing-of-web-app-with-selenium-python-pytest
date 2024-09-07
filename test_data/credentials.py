"""
In this class login credentials are stored
"""
from settings.development import USER_EMAIL, USER_PASSWORD, SUPER_USER_EMAIL, SUPER_USER_PASSWORD


class Credentials:

    users_credentials = {
        "loginEmail": USER_EMAIL, "password": USER_PASSWORD,
        "SUPER_USER_EMAIL": SUPER_USER_EMAIL, "SUPER_USER_PASSWORD": SUPER_USER_PASSWORD
    }