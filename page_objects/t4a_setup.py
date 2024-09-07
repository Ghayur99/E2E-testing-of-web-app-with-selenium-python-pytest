"""T4A setup objects are define here"""

from page_objects.common_objects import CommonObjects


class T4aSetup(CommonObjects):
    """This class contains webElements of T4A setup """

    t4a_x_paths = {
        "loadVendor": "//input[@id='id_load_vendor']", "loadSlip": "//input[@id='id_load_slip']",
        "reflectInMasterData": "//input[@id='id_reflect_master_data']",
        "personalRadioButton": "//*[contains(@class, 'v-radio theme')][1]/div",
        "businessRadioButton": "//*[contains(@class, 'v-radio theme')][2]/div",
        "saveButton": "//*[contains(text(),'Save')]", "resetButton": "//*[contains(text(),'Reset')]",
        "deleteButton": "//*[contains(text(),'Delete')]",
        "firstName": "//input[@id='id_first_name']",
        "initials": "//input[@id='id_initials']",
        "lastName": "//input[@id='id_last_name']",
        "sin": "//input[@id='id_emp_sin']",
        "businessName": "//input[@id='id_business_name']",
        "businessNumber": "//input[@id='id_business_number']",
        "address": "//input[@id='id_address']", "city": "//input[@id='id_city']",
        "postCode": "//input[@id='id_post_code']", "province": "//input[@id='id_province']",
        "country": "//input[@id='id_country']",
        "email": "//input[@id='id_email']", "slipType": "//input[@id='id_slip_type']",
        "status": "//input[@id='id_slip_status']",
        "PensionOrSuperannuation": "//input[@id='id_box_016']",
        "Lump-Sum Payments": "//input[@id='id_box_018_1']",
        "Lump-Sum Payments (Other)": "//input[@id='id_box_018_2']",
        "Self-Employed Commissions": "//input[@id='id_box_020']",
        "Income Tax Deducted": "//input[@id='id_box_022']",
        "Annuities": "//input[@id='id_box_024_1']",
        "Annuities (Other)": "//input[@id='id_box_024_2']",
        "Fees": "//input[@id='id_box_048']",
        "AddMore": "//span[contains(text(),'Add More')]",
        "OtherInfo0": "//input[@id='id_other_info_code_0']",
        "amount0": "//input[@id='id_other_info_amount_0']",
        "OtherInfo1": "//input[@id='id_other_info_code_1']",
        "amount1": "//input[@id='id_other_info_amount_1']",
        "OtherInfo2": "//input[@id='id_other_info_code_2']",
        "amount2": "//input[@id='id_other_info_amount_2']",
        "OtherInfo3": "//input[@id='id_other_info_code_3']",
        "amount3": "//input[@id='id_other_info_amount_3']",
        "OtherInfo4": "//input[@id='id_other_info_code_4']",
        "amount4": "//input[@id='id_other_info_amount_4']",
        "OtherInfo5": "//input[@id='id_other_info_code_5']",
        "amount5": "//input[@id='id_other_info_amount_5']",
        "OtherInfo6": "//input[@id='id_other_info_code_6']",
        "amount6": "//input[@id='id_other_info_amount_6']",
        "OtherInfo7": "//input[@id='id_other_info_code_7']",
        "amount7": "//input[@id='id_other_info_amount_7']",
        "OtherInfo8": "//input[@id='id_other_info_code_8']",
        "amount8": "//input[@id='id_other_info_amount_8']",
        "OtherInfo9": "//input[@id='id_other_info_code_9']",
        "amount9": "//input[@id='id_other_info_amount_9']",
        "OtherInfo10": "//input[@id='id_other_info_code_10']",
        "amount10": "//input[@id='id_other_info_amount_10']",
        "OtherInfo11": "//input[@id='id_other_info_code_11']",
        "amount11": "//input[@id='id_other_info_amount_11']",
        "toastMessage": "//div[@class='toast-body']",
        "closeToast": "//button[contains(text(),'×')]"
    }
    t4a_alerts_xpaths = {
        "reflectInMasterDataRequired":"//body[1]/div[2]/div[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[2]/span[1]"
                                      "/form[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/span[1]/span[1]",
        "sinRequired": "//body/div[@id='__nuxt']/div[@id='__layout']/div[@id='inspire']/div[1]/main[1]/div[1]/div[1]/"
                       "div[2]/span[1]/form[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[6]/div[1]/div[2]/span[1]/span[1]",
        "firstNameRequired": "//body/div[@id='__nuxt']/div[@id='__layout']/div[@id='inspire']/div[1]/main[1]/div[1]/"
                             "div[1]/div[2]/span[1]/form[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[3]/div[1]/div[2]/"
                             "span[1]/span[1]",
        "lastNameRequired": "//body/div[@id='__nuxt']/div[@id='__layout']/div[@id='inspire']/div[1]/main[1]/div[1]/"
                            "div[1]/div[2]/span[1]/form[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[5]/div[1]/div[2]/"
                            "span[1]/span[1]",
        "businessNameRequired": "//body/div[@id='__nuxt']/div[@id='__layout']/div[@id='inspire']/div[1]/main[1]/div[1]/"
                                "div[1]/div[2]/span[1]/form[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[7]/div[1]/div[2]"
                                "/span[1]/span[1]",
        "businessNumberRequired": "//body/div[@id='__nuxt']/div[@id='__layout']/div[@id='inspire']/div[1]/main[1]/"
                                  "div[1]/div[1]/div[2]/span[1]/form[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[8]/div"
                                  "[1]/div[2]/span[1]/span[1]",
        "addressRequired": "//body/div[@id='__nuxt']/div[@id='__layout']/div[@id='inspire']/div[1]/main[1]/div[1]/div"
                           "[1]/div[2]/span[1]/form[1]/div[2]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[2]/span[1]"
                           "/span[1]",
        "cityRequired": "//body/div[@id='__nuxt']/div[@id='__layout']/div[@id='inspire']/div[1]/main[1]/div[1]/div[1]/"
                        "div[2]/span[1]/form[1]/div[2]/div[1]/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]/span[1]/span[1]",
        "postCodeRequired": "//body/div[@id='__nuxt']/div[@id='__layout']/div[@id='inspire']/div[1]/main[1]/div"
                            "[1]/div[1]/div[2]/span[1]/form[1]/div[2]/div[1]/div[2]/div[2]/div[2]/div[4]/div[1]"
                            "/div[2]/span[1]/span[1]",
        "provinceRequired": "//body/div[@id='__nuxt']/div[@id='__layout']/div[@id='inspire']/div[1]/main[1]/div[1]/div"
                            "[1]/div[2]/span[1]/form[1]/div[2]/div[1]/div[2]/div[2]/div[2]/div[3]/div[1]/div[2]/span[1]"
                            "/span[1]",
        "otherInfoValueRequiredAlert": "//body/div[@id='__nuxt']/div[@id='__layout']/div[@id='inspire']/div[1]/main[1]/"
                                       "div[1]/div[1]/div[2]/span[1]/form[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[10]"
                                       "/div[1]/div[2]/div[1]/div[1]/div[3]/span[1]/span[1]",
        "emailAlert": "//span[contains(text(),'This field must only contain valid email')]",
        "sinIncorrectAlert": "//span[contains(text(),'Social Insurance is incorrect')]",
        "businessNumberIncorrectAlert": "//span[contains(text(),'Business Number is incorrect')]",
        "postCodeIncorrectAlert": "//span[contains(text(),'This value is incorrect')]"

    }
