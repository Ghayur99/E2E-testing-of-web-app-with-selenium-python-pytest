from page_objects.common_objects import CommonObjects


class FilingResourceList(CommonObjects):
    """This class contains webElements of filing resource list page"""
    X_paths = {
        "createButton": "//body/div[@id='__nuxt']/div[@id='__layout']/div[@id='inspire']/div[1]/main[1]/div[1]/div[1]"
                        "/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/a[1]",
        "selectAllCheckBox": "//tr[1]/th[1]/div/i",
        "deleteAllButton": "//*[@id='inspire']/div/main/div/div/div[2]/div/div/div/div[1]/div[2]/div/button/i",
        "toastMessage": "//div[@class='toast-body']",
        "closeToast": "//button[contains(text(),'×')]",
        "confirmDeleteAll": "//button[contains(text(),'OK')]"
    }