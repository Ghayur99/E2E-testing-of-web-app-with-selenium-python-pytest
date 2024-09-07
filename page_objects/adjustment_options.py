"""Adjustment options screen object are define here"""
from page_objects.common_objects import CommonObjects


class AdjustmentOptions(CommonObjects):
    adjustment_option_xpath = {
        "saveButton": "//body/div[@id='__nuxt']/div[@id='__layout']/div[@id='inspire']/div[1]/main[1]/div[1]/div[1]"
                      "/div[2]/div[1]/div[1]/button[1]",
        "resetButton": "//body/div[@id='__nuxt']/div[@id='__layout']/div[@id='inspire']/div[1]/main[1]/div[1]/div[1]"
                       "/div[2]/div[1]/div[1]/button[2]",
        "transferOverRemittance": "//body/div[@id='__nuxt']/div[@id='__layout']/div[@id='inspire']/div[1]/main[1]/div"
                                  "[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[14]/div[1]/div[1]/div[1]/div[1]"
                                  "/div[1]/div[2]/div[1]/i[1]",
        "listCheckBoxOfTransferRemittance": "//div[@tabindex = '-1']//*[@class = 'v-simple-checkbox']/i",
        "toastMessage": "//div[@class='toast-body']",
        "closeToast": "//button[contains(text(),'×')]"

    }
