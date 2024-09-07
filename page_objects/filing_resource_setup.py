from page_objects.common_objects import CommonObjects


class FilingResourceSetup(CommonObjects):
    """This class contains webElements of filing resource setup page"""
    X_paths = {
        "saveButton": "//body/div[@id='__nuxt']/div[@id='__layout']/div[@id='inspire']/div[1]/main[1]/div[1]/div[1]"
                      "/div[2]/div[1]/div[1]/span[1]/form[1]/div[1]/div[1]/button[1]",
        "resetButton": "//body/div[@id='__nuxt']/div[@id='__layout']/div[@id='inspire']/div[1]/main[1]/div[1]"
                       "/div[1]/div[2]/div[1]/div[1]/span[1]/form[1]/div[1]/div[1]/button[2]",
        "roleField": "//body/div[@id='__nuxt']/div[@id='__layout']/div[@id='inspire']/div[1]/main[1]/div[1]/div[1]/"
                     "div[2]/div[1]/div[1]/span[1]/form[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/span[1]/div[1]"
                     "/div[1]/div[1]/div[1]/div[1]",
        "issuerCheckBox": "//body/div[@id='__nuxt']/div[@id='__layout']/div[@id='inspire']/div[2]/div[1]/div[2]/div[1]"
                          "/div[1]/i[1]",
        "transmitterCheckBox": "//body/div[@id='__nuxt']/div[@id='__layout']/div[@id='inspire']/div[2]/div[1]/div[3]"
                               "/div[1]/div[1]/i[1]",
        "roleFieldDropdown": "//body/div[@id='__nuxt']/div[@id='__layout']/div[@id='inspire']/div[2]",
        "name": "//*[@id='inspire']/div/main/div/div/div[2]/div/div/span/form/div[2]/div/div/div/div[4]/div[2]/span/div"
                "/div/div/div/input",
        "effectiveFrom": "//*[@id='inspire']/div[1]/main/div/div/div[2]/div/div/span/form/div[2]/div/div/div/div[3]/"
                         "div[2]/span/div/div/div/div[1]/div[1]/input",
        "phone1": "//*[@id='__nuxt']/div[@id='__layout']/div[@id='inspire']/div[1]/main[1]/div[1]/div[1]/div[2]/div[1]"
                  "/div[1]/span[1]/form[1]/div[2]/div[1]/div[1]/div[1]/div[5]/div[2]/span[1]/div[1]/div[1]/div[1]"
                  "/div[1]/input",
        "ext1": "//*[@id='inspire']/div[1]/main/div/div/div[2]/div/div/span/form/div[2]/div/div/div/div[5]/div[4]/div/"
                "div/div/div/input",
        "ownerSin1": "//*[@id='inspire']/div[1]/main/div/div/div[2]/div/div/span/form/div[2]/div/div/div/div[6]/div[2]"
                     "/div[2]/span/div/div/div/div/input",
        "ownerSin2": "//*[@id='inspire']/div[1]/main/div/div/div[2]/div/div/span/form/div[2]/div/div/div/div[6]/div[3]"
                     "/div[2]/span/div/div/div/div/input",
        "craTransmitterNo": "//input[@placeholder = 'MM999999']",
        "rqTransmitterNo": "//input[@placeholder = 'NP999999']",
        "rl1Type": "//*[@id='inspire']/div[1]/main/div/div/div[2]/div/div/span/form/div[2]/div/div/div/div[7]/div[4]"
                   "/div[2]/div/div/div/div[1]/div[1]/input",
        "address": "//*[@id='inspire']/div[1]/main/div/div/div[2]/div/div/span/form/div[2]/div/div/div/div[7]/div[5]/"
                   "div[2]/span/div/div/div/div/input",
        "city": "//*[@id='inspire']/div[1]/main/div/div/div[2]/div/div/span/form/div[2]/div/div/div/div[7]/div[6]/div"
                "[2]/span/div/div/div/div/input",
        "province": "//*[@id='inspire']/div[1]/main/div/div/div[2]/div/div/span/form/div[2]/div/div/div/div[7]/div[7]/"
                    "div[2]/span/div/div/div/div[1]/div[1]/input",
        "country": "//*[@id='inspire']/div[1]/main/div/div/div[2]/div/div/span/form/div[2]/div/div/div/div[7]/div[8]/"
                   "div[2]/span/input",
        "postCode": "//input[@placeholder= 'A9A9A9']",
        "contactName": "//*[@id='inspire']/div[1]/main/div/div/div[2]/div/div/span/form/div[2]/div/div/div/div[7]/div"
                       "[10]/div[2]/span/div/div/div/div/input",
        "email": "//*[@id='inspire']/div[1]/main/div/div/div[2]/div/div/span/form/div[2]/div/div/div/div[7]/div[11]/div"
                 "[2]/span/div/div/div/div/input",
        "toastMessage": "//div[@class='toast-body']",
        "closeToast": "//button[contains(text(),'×')]"

    }