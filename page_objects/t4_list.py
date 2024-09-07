from page_objects.common_objects import CommonObjects

class T4List(CommonObjects):
    t4_list_xpaths = {
        "editButton": "//tbody/tr[1]/td[12]/div[1]/button[1]",
        "noOfRowsOnPage": "//div[@class= 'v-data-footer__pagination']",
        "t4ListDeleteButtons": "//tbody/tr/td/div[1]/button[2]",
        "deleteButton": "//body/div[@id='__nuxt']/div[@id='__layout']/div[@id='inspire']/div[1]/main[1]/"
                        "div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/button[1]",
        "headerListCheckBox": "//thead/tr[1]/th[1]/div[1]/i[1]",

        "noOfRowsOnPage": "//div[@class= 'v-data-footer__pagination']"

    }
