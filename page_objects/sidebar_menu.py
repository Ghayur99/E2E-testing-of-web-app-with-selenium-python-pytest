"""sidebar objects are define here"""

from page_objects.common_objects import CommonObjects


class SidebarMenu(CommonObjects):
    menu_xpaths = {"peopleMenu": "//div[contains(text(),'People')]",
                   "employeeMenu": "//body/div[@id='__nuxt']/div[@id='__layout']/div[@id='inspire']/div[1]/div[2]"
                                   "/div[1]/nav[1]/div[1]/div[2]/div[2]/div[2]/a[1]/div[1]",
                   "vendorMenu": "//body/div[@id='__nuxt']/div[@id='__layout']/div[@id='inspire']/div[1]/div[2]/div[1]"
                                 "/nav[1]/div[1]/div[2]/div[2]/div[2]/a[2]/div[1]",
                   "filingResourceMenu": "//body/div[@id='__nuxt']/div[@id='__layout']/div[@id='inspire']/div[1]/div"
                                         "[2]/div[1]/nav[1]/div[1]/div[2]/div[2]/div[2]/a[3]/div[1]",
                   "complianceMenu": "//div[contains(text(),'Compliance')]",
                   "t4Menu": "//body/div[@id='__nuxt']/div[@id='__layout']/"
                             "div[@id='inspire']/div[1]/div[2]/div[1]/nav[1]"
                             "/div[1]/div[2]/div[5]/div[2]/div[1]/div[1]/div[2]",
                   "t4Setup": "//body/div[@id='__nuxt']/div[@id='__layout']/div[@id='inspire']"
                              "/div[1]/div[2]/div[1]/nav[1]/div[1]/div[2]/div[5]/div[2]/div[1]"
                              "/div[2]/a[2]/div[1]/div[1]",
                   "t4List": "//body/div[@id='__nuxt']/div[@id='__layout']/div[@id='inspire']"
                             "/div[1]/div[2]/div[1]/nav[1]/div[1]/div[2]/div[5]/div[2]/div[1]"
                             "/div[2]/a[1]/div[1]/div[1]",
                   "rl1Menu": "//body/div[@id='__nuxt']/div[@id='__layout']/div[@id='inspire']/div[1]"
                              "/div[2]/div[1]/nav[1]/div[1]/div[2]/div[5]/div[2]/div[3]/div[1]/div[2]/div[1]",
                   "rl1List": "//body/div[@id='__nuxt']/div[@id='__layout']/div[@id='inspire']/div[1]"
                              "/div[2]/div[1]/nav[1]/div[1]/div[2]/div[5]/div[2]/div[3]/div[2]/a[1]/div[1]/div[1]",
                   "rl1Setup": "//body/div[@id='__nuxt']/div[@id='__layout']/div[@id='inspire']/div[1]/div[2]"
                               "/div[1]/nav[1]/div[1]/div[2]/div[5]/div[2]/div[3]/div[2]/a[2]/div[1]/div[1]",
                   "t4Summary": "//body/div[@id='__nuxt']/div[@id='__layout']/div[@id='inspire']/div[1]/div[2]/div[1]"
                                "/nav[1]/div[1]/div[2]/div[5]/div[2]/div[1]/div[2]/a[3]/div[1]/div[1]",
                   "adjustmentMenu": "//div[contains(text(),'Adjustment')]",
                   "adjustments": "//div[contains(text(),'Adjustments')]",
                   "adjustmentOptions": "//body/div[@id='__nuxt']/div[@id='__layout']/div[@id='inspire']"
                                        "/div[1]/div[2]/div[1]/nav[1]/div[1]/div[2]/div[3]/div[2]/a[1]/div[1]",
                       # "//div[contains(text(),'Options')]"
                       #         "/div[1]/nav[1]/div[1]/div[2]/div[5]/div[2]/div[3]/div[2]/a[2]/div[1]/div[1]",
                   "t4aSummary": "//body/div[@id='__nuxt']/div[@id='__layout']/div[@id='inspire']/div[1]"
                                  "/div[2]/div[1]/nav[1]/div[1]/div[2]/div[5]/div[2]/div[2]/div[2]/a[3]/div[1]",
                   "t4aMenu": "//body/div[@id='__nuxt']/div[@id='__layout']/div[@id='inspire']/div[1]"
                               "/div[2]/div[1]/nav[1]/div[1]/div[2]/div[5]/div[2]/div[2]/div[1]/div[2]/div[1]"

                   }




