from page_objects.common_objects import CommonObjects

class EmployeeList(CommonObjects):
    
    """This class contains webElements of employee list page"""

    employee_list_xpath={"headerListCheckBox": "//thead/tr[1]/th[1]/div[1]/i[1]",
                         "deleteBtn": "//body/div[@id='__nuxt']/div[@id='__layout']/div[@id='inspire']/div[1]/main[1]/"
                                      "div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/button[1]",
                         "OKBtn": "//button[contains(text(),'OK')]",
                         "toastMessage": "//div[@class='toast-body']",
                         "closeToast": "//button[contains(text(),'×')]",
                         "confirmPopup": "//div[@id='__BVID__296___BV_modal_content_']",
                         "activeFilter": "//span[contains(text(),'Filter')]",
                         "selectAll": "//small[contains(text(),'All')]",
                         "editBtn": "//tbody/tr[2]/td[11]/div[1]/button[1]",
                         "basicInfoTxt": "//div[contains(text(),'Enter basic information (Employee)')]",
                         "addressWizard": "//div[contains(text(),'2')]",
                         "addressTitle": "//div[contains(text(),'Enter Address (Employee)')]",
                         "secondWizard": "//div[contains(text(),'3')]",
                         "filingTitle": "//div[contains(text(),'Enter tax filing attributes (Employee)')]",
                         "moreActions": "//span[contains(text(),'More actions')]",
                         "mergeEmployee": "//body/div[@id='__nuxt']/div[@id='__layout']/div[@id='inspire']"
                                          "/div[1]/main[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]"
                                          "/div[1]/div[2]/div[1]/ul[1]/li[1]/a[1]/small[1]",
                         "unMergeEmployee": "//small[contains(text(),'Un-Merge Employee')]",
                         "ignoredEmployee": "//small[contains(text(),'Ignored Employee')]",
                         "noOfRowsOnPage": "//div[@class= 'v-data-footer__pagination']",
                         "allCheckBoxesOfEmployees": "//tbody/tr/td[1]/div/i",
                         "empListDeleteButtons": "//tbody/tr/td/div[1]/button[2]"

                         }

