"""
Header elements are define here
"""
from page_objects.common_objects import CommonObjects

class Header(CommonObjects):
    """This class contains webElements of header  """
    Xpaths = {"accountOptions": "//header/div[1]/button[4]/span[1]",
              "Logout": "//a[contains(text(),'Logout')]",
              "fillingResource": "//a[contains(text(),'Filing Resources')]",
              "maskButton": "//*[contains(@class, 'mask_unmask')]",
              "unmaskPassword": "//input[@placeholder = 'Enter Password']",
              "verifyButton": "//button[contains(text(),'Verify')]"
              }
