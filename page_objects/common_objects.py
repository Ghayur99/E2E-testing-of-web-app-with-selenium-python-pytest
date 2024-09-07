from selenium.webdriver import ActionChains


class CommonObjects:
    global_xpath = {
        "toastMessage": "//div[@class='toast-body']",
        "closeToast": "//button[contains(text(),'×')]",
    }

    def __init__(self, driver):
        self.driver = driver
        self.actions = ActionChains(driver)
