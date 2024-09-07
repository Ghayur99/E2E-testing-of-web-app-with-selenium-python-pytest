import os

USER_EMAIL = "haroon@websential.ca"
USER_PASSWORD = "123456789a"
SUPER_USER_EMAIL = "haroon@technologyelement.com"
SUPER_USER_PASSWORD = "123456789a"
CLIENT_XPATH = "//tbody/tr[1]/td[3]/div[1]"
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHROME_DRIVER_PATH = BASE_DIR+"/static/chromedriver"

# this is for windows user
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# CHROME_DRIVER_PATH = BASE_DIR+"\\static\\chromedriver.exe"
