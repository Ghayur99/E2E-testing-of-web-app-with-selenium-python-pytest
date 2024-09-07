"""vendor list objects are define here"""
from page_objects.common_objects import CommonObjects

class VendorList(CommonObjects):
    """This class contains webElements of vendor list """

    vendor_list_Xpaths = {"addVendor": "//span[contains(text(),'Add Vendor')]",
                          "testMask": "//div[contains(text(),'MaskTest')]",
                          "rowsPerPage": "//input[@aria-label= 'Rows per page:']",
                          "selectAllVendors": "//thead/tr[1]/th[1]/div[1]/i[1]",
                          "deleteAllButton": "//*[contains(@class, 'no_bg')]",
                          "confirmDeleteAll": "//button[contains(text(),'OK')]",
                          "ToastMessage": "//div[@class='toast-body']",
                          "closeToast": "//button[contains(text(),'×')]",
                          "firstVendor": "//tbody/tr[1]/td[2]"
                          }
