"""
vendor setup objects are define here
"""
from page_objects.common_objects import CommonObjects

class VendorSetup(CommonObjects):
    """This class contains webElements of vendor list """

    x_paths = {"personalRatioButton": "//*[contains(@class, 'v-radio theme')][1]/div",
               "businessRatioButton": "//*[contains(@class, 'v-radio theme')][2]/div",
               "sin": "//input[@id='id_sin']", "firstName": "//input[@id='id_name1']",
               "lastName": "//input[@id='id_name2']", "initials": "//input[@id='id_initials']",
               "status": "//body/div[@id='__nuxt']/div[@id='__layout']/div[@id='inspire']/div[1]/main[1]/div[1]/div[1]"
                         "/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/span[1]/form[1]/div[1]/span[1]/div[2]"
                         "/div[2]/div[6]/div[1]/span[1]/div[1]/div[1]/div[1]/div[1]/div[1]",
               "businessName": "//input[@id='id_business_name']", "businessNumber": "//input[@id='id_business_number']",
               "nextStep": "//button[contains(text(),'Next Step')]", "address": "//input[@id='id_address']",
               "city": "//input[@id='id_city']", "postCode": "//input[@id='id_post_code']",
               "province": "//input[@id='id_province_id']", "country": "//input[@id='id_country']",
               "email": "//input[@id='id_email']", "phone1": "//input[@id='id_phone_number']",
               "ext1": "//input[@id='id_ext']", "phone2": "//input[@id='id_phone_number2']",
               "ext2": "//input[@id='id_ext2']", "previous": "//button[contains(text(),'Previous')]",
               "save": "//button[contains(text(),'Save')]", "vendorInfoWizard": "//div[contains(text(),'1')]",
               "vendorAddressWizard": "//div[contains(text(),'2')]",
               "addressScreenLabel": "//div[contains(text(),'Enter Address (Vendor)')]",
               "infoScreenLabel": "//div[contains(text(),'Enter basic information (Vendor)')]",
               "incorrectSinAlert": "//span[contains(text(),'Social Insurance No. is incorrect')]",
               "incorrectBusinessNoAlert": "//span[contains(text(),'Business No. is incorrect')]",
               "incorrectPostCodeAlert": "//span[contains(text(),'This value is incorrect')]",
               "incorrectEmailAlert": "//span[contains(text(),'This field must only contain valid email')]",
               "sinAlert": "//body/div[@id='__nuxt']/div[@id='__layout']/div[@id='inspire']/div[1]/main[1]/div[1]"
                           "/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/span[1]/form[1]/div[1]/span[1]/"
                           "div[2]/div[2]/div[2]/div[1]/span[1]/span[1]",
               "firstNameAlert": "//body/div[@id='__nuxt']/div[@id='__layout']/div[@id='inspire']/div[1]/main[1]/div[1]"
                                 "/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/span[1]/form[1]/div[1]"
                                 "/span[1]/div[2]/div[2]/div[3]/div[1]/span[1]/span[1]",
               "lastNameAlert": "//body/div[@id='__nuxt']/div[@id='__layout']/div[@id='inspire']/div[1]/main[1]/div[1]"
                               "/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/span[1]/form[1]/div[1]/span[1]"
                               "/div[2]/div[2]/div[4]/div[1]/span[1]/span[1]",
               "businessNameAlert": "//body/div[@id='__nuxt']/div[@id='__layout']/div[@id='inspire']/div[1]/main[1]"
                                    "/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/span[1]/form[1]"
                                    "/div[1]/span[1]/div[2]/div[2]/div[7]/div[1]/span[1]/span[1]",
               "businessNoAlert": "//body/div[@id='__nuxt']/div[@id='__layout']/div[@id='inspire']/div[1]/main[1]"
                                  "/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/span[1]/form[1]"
                                  "/div[1]/span[1]/div[2]/div[2]/div[7]/div[1]/span[1]/span[1]",
               "addressAlert": "//body/div[@id='__nuxt']/div[@id='__layout']/div[@id='inspire']/div[1]/main[1]/div[1]"
                               "/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/span[1]/form[1]/div[2]/span[1]"
                               "/div[2]/div[2]/div[1]/div[1]/span[1]/span[1]",
               "cityAlert": "//body/div[@id='__nuxt']/div[@id='__layout']/div[@id='inspire']/div[1]/main[1]/div[1]"
                            "/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/span[1]/form[1]/div[2]/span[1]"
                            "/div[2]/div[2]/div[2]/div[1]/span[1]/span[1]",
               "postCodeRequiredAlert": "//body/div[@id='__nuxt']/div[@id='__layout']/div[@id='inspire']/div[1]/main[1]"
                                        "/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/span[1]"
                                        "/form[1]/div[2]/span[1]/div[2]/div[2]/div[3]/div[1]/span[1]/span[1]",
               "provinceAlert": "//body/div[@id='__nuxt']/div[@id='__layout']/div[@id='inspire']/div[1]/main[1]/div[1]"
                                "/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/span[1]/form[1]/div[2]"
                                "/span[1]/div[2]/div[2]/div[4]/div[1]/span[1]/span[1]",
               "emailRequiredAlert": "//body/div[@id='__nuxt']/div[@id='__layout']/div[@id='inspire']/div[1]/main[1]"
                                     "/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/span[1]/form[1]"
                                     "/div[2]/span[1]/div[2]/div[2]/div[6]/div[1]/span[1]/span[1]",
               "emailValidationAlert": "//span[contains(text(),'This field must only contain valid email')]",
               "ToastMessage": "//div[@class='toast-body']",
               "closeToast": "//button[contains(text(),'×')]"}
