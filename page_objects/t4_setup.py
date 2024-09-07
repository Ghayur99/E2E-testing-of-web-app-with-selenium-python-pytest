
from page_objects.common_objects import CommonObjects


class T4Setup(CommonObjects):
    """This class contains webElements of t4 setup page"""
    t4_xpaths = {"reflectEmployee": "//input[@id='id_reflect_master_data']",
                 "employeeCode": "//input[@id='id_emp_code']",
                 "sin": "//input[@id='id_emp_sin']",
                 "fName": "//input[@id='id_first_name']",
                 "initials": "//input[@id='id_initials']",
                 "lName": "//input[@id='id_last_name']",
                 "dateOfBirth": "//input[@id='id_date_of_birth']",
                 "address": "//input[@id='id_address']",
                 "city": "//input[@id='id_city']",
                 "province": "//input[@id='id_province']",
                 "postCode": "//input[@id='id_post_code']",
                 "email": "//input[@id='id_email']",
                 "payPeriod": "//input[@id='id_pay_period']",
                 "pensionablePeriod": "//input[@id='id_pensionable_weeks']",
                 "slipType": "//input[@id='id_slip_type']",
                 "poe": "//input[@id='id_poe']",
                 "exemptCpp": "//body/div[@id='__nuxt']/div[@id='__layout']/div[@id='inspire']/div[1]/main[1]/div[1]/"
                              "div[1]/div[2]/span[1]/form[1]/div[2]/div[1]/div[2]/div[3]/div[2]/div[5]/div[1]/div[2]/d"
                              "iv[1]",
                 "exemptEi": "//body/div[@id='__nuxt']/div[@id='__layout']/div"
                        "[@id='inspire']/div[1]/main[1]/div[1]/div[1]/div[2]"
                        "/span[1]/form[1]/div[2]/div[1]/div[2]/div[3]/div[2]"
                        "/div[5]/div[1]/div[2]/div[2]/label[1]",
                 "exemptPpip": "//body/div[@id='__nuxt']/div[@id='__layout']/div[@id='inspire']/div[1]/main[1]/div[1]"
                               "/div[1]/div[2]/span[1]/form[1]/div[2]/div[1]/div[2]/div[3]/div[2]/div[5]/div[1]/div[2]"
                               "/div[3]/label[1]",
                 "employmentCode": "//input[@id='id_employment_code']",
                 "reducedEi": "//input[@id='id_reduced_ei']",
                 "status": "//input[@id='id_slip_status']",
                 "employmentIncome": "//input[@id='id_box_14']",
                 "cppContribution": "//input[@id='id_box_16']",
                 "qppContribution": "//input[@id='id_box_17']",
                 "eiPremiums": "//input[@id='id_box_18']",
                 "rppContribution": "//input[@id='id_box_20']",
                 "incomeTaxDed": "//input[@id='id_box_22']",
                 "eiInsurableCheckbox": "//body/div[@id='__nuxt']/div[@id='__layout']/"
                                        "div[@id='inspire']/div[1]/main[1]/div[1]/div[1]"
                                        "/div[2]/span[1]/form[1]/div[2]/div[1]/div[1]/div[2]"
                                        "/div[2]/div[7]/div[1]/div[1]/label[1]",
                 "cppPensionableCheckbox": "//body/div[@id='__nuxt']/div[@id='__layout']/div"
                                        "[@id='inspire']/div[1]/main[1]/div[1]/div[1]/div[2]"
                                        "/span[1]/form[1]/div[2]/div[1]/div[1]/div[2]/div[2]"
                                        "/div[8]/div[1]/div[1]/label[1]",
                 "unionDues": "//input[@id='id_box_44']",
                 "charitableDonations": "//input[@id='id_box_46']",
                 "registrationNo": "//input[@id='id_box_50']",
                 "pensionAdj": "//input[@id='id_box_52']",
                 "ppipPremiums": "//input[@id='id_box_55']",
                 "ppipInsurableEarning": "//input[@id='id_box_56']",
                 "saveButton": "//body/div[@id='__nuxt']/div[@id='__layout']/div[@id='inspire']"
                               "/div[1]/main[1]/div[1]/div[1]/div[2]/span[1]/form[1]/div[1]/div[1]/span[1]/button[1]",
                 "toastMessage": "//div[@class='toast-body']",
                 "closeToast": "//button[contains(text(),'×')]",
                 "loadEmployee": "//input[@id='id_load_employee']",
                 "resetButton": "//button[contains(text(),'Reset')]",
                 "deleteButton": "//button[contains(text(),'Delete')]",
                 "insurableEarning": "//input[@id='id_box_24']",
                 "pensionableEarning": "//input[@id='id_box_26']",
                 "otherInfoCode0": "//input[@id='id_other_info_code_0']",
                 "otherInfoAmount0": "//input[@id='id_other_info_amount_0']",
                 "otherInfoCode1": "//input[@id='id_other_info_code_1']",
                 "otherInfoAmount1": "//input[@id='id_other_info_amount_1']",
                 "otherInfoCode2": "//input[@id='id_other_info_code_2']",
                 "otherInfoAmount2": "//input[@id='id_other_info_amount_2']",
                 "otherInfoCode3": "//input[@id='id_other_info_code_3']",
                 "otherInfoAmount3": "//input[@id='id_other_info_amount_3']",
                 "otherInfoCode4": "//input[@id='id_other_info_code_4']",
                 "otherInfoAmount4": "//input[@id='id_other_info_amount_4']"

    }
    t4_alerts_xpaths = {
        "incorrectSinAlert": "//span[contains(text(),'Social Insurance is incorrect')]",
        "reflectEmployeeRequired": "//body/div[@id='__nuxt']/div[@id='__layout']"
                                   "/div[@id='inspire']/div[1]/main[1]/div[1]/div[1]"
                                   "/div[2]/span[1]/form[1]/div[2]/div[1]/div[2]/div[1]"
                                   "/div[2]/div[1]/div[1]/div[2]/span[1]/span[1]",
        "fNameRequired": "//body/div[@id='__nuxt']/div[@id='__layout']/div[@id='inspire']"
                         "/div[1]/main[1]/div[1]/div[1]/div[2]/span[1]/form[1]/div[2]/div[1]"
                         "/div[2]/div[1]/div[2]/div[4]/div[1]/div[2]/span[1]/span[1]",
        "lNameRequired": "//body/div[@id='__nuxt']/div[@id='__layout']/div[@id='inspire']"
                         "/div[1]/main[1]/div[1]/div[1]/div[2]/span[1]/form[1]/div[2]/div[1]"
                         "/div[2]/div[1]/div[2]/div[6]/div[1]/div[2]/span[1]/span[1]",
        "addressRequired": "//body/div[@id='__nuxt']/div[@id='__layout']/div[@id='inspire']"
                           "/div[1]/main[1]/div[1]/div[1]/div[2]/span[1]/form[1]/div[2]/div[1]"
                           "/div[2]/div[2]/div[2]/div[1]/div[1]/div[2]/span[1]/span[1]",
        "cityRequired": "//body/div[@id='__nuxt']/div[@id='__layout']/div[@id='inspire']"
                        "/div[1]/main[1]/div[1]/div[1]/div[2]/span[1]/form[1]/div[2]/div[1]"
                        "/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]/span[1]/span[1]",
        "provinceRequired": "//body/div[@id='__nuxt']/div[@id='__layout']/div[@id='inspire']"
                            "/div[1]/main[1]/div[1]/div[1]/div[2]/span[1]/form[1]/div[2]/div[1]"
                            "/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]/span[1]/span[1]",
        "postCodeRequired": "//body/div[@id='__nuxt']/div[@id='__layout']/div[@id='inspire']"
                            "/div[1]/main[1]/div[1]/div[1]/div[2]/span[1]/form[1]/div[2]/div[1]"
                            "/div[2]/div[2]/div[2]/div[4]/div[1]/div[2]/span[1]/span[1]",
        "invalidEmailAlert": "//span[contains(text(),'This field must only contain valid email')]",
        "countryRequired": "//body/div[@id='__nuxt']/div[@id='__layout']/div[@id='inspire']"
                           "/div[1]/main[1]/div[1]/div[1]/div[2]/span[1]/form[1]/div[2]/div[1]"
                           "/div[2]/div[2]/div[2]/div[5]/div[1]/div[2]/span[1]/span[1]",
        "poeRequired": "//body/div[@id='__nuxt']/div[@id='__layout']/div[@id='inspire']"
                       "/div[1]/main[1]/div[1]/div[1]/div[2]/span[1]/form[1]/div[2]/div[1]"
                       "/div[2]/div[3]/div[2]/div[4]/div[1]/div[2]/span[1]/span[1]",
        "otherInfoAmount0Required": "//body/div[@id='__nuxt']/div[@id='__layout']/div[@id='inspire']"
                                    "/div[1]/main[1]/div[1]/div[1]/div[2]/span[1]/form[1]/div[2]/div[1]"
                                    "/div[1]/div[2]/div[2]/div[15]/div[1]/div[2]/div[1]/div[1]"
                                    "/div[3]/span[1]/span[1]",
        "otherInfoAmount1Required": "//body/div[@id='__nuxt']/div[@id='__layout']/div[@id='inspire']"
                                    "/div[1]/main[1]/div[1]/div[1]/div[2]/span[1]/form[1]/div[2]"
                                    "/div[1]/div[1]/div[2]/div[2]/div[15]/div[1]/div[2]/div[2]"
                                    "/div[1]/div[3]/span[1]/span[1]",
        "otherInfoAmount2Required": "//body/div[@id='__nuxt']/div[@id='__layout']/div[@id='inspire']"
                                    "/div[1]/main[1]/div[1]/div[1]/div[2]/span[1]/form[1]/div[2]/div[1]"
                                    "/div[1]/div[2]/div[2]/div[15]/div[1]/div[2]/div[3]/div[1]/div[3]"
                                    "/span[1]/span[1]",
        "otherInfoAmount3Required": "//body/div[@id='__nuxt']/div[@id='__layout']/div[@id='inspire']"
                                    "/div[1]/main[1]/div[1]/div[1]/div[2]/span[1]/form[1]/div[2]/div[1]"
                                    "/div[1]/div[2]/div[2]/div[15]/div[1]/div[2]/div[4]/div[1]/div[3]"
                                    "/span[1]/span[1]",
        "otherInfoAmount4Required": "//body/div[@id='__nuxt']/div[@id='__layout']/div[@id='inspire']"
                                    "/div[1]/main[1]/div[1]/div[1]/div[2]/span[1]/form[1]/div[2]/div[1]"
                                    "/div[1]/div[2]/div[2]/div[15]/div[1]/div[2]/div[5]/div[1]/div[3]"
                                    "/span[1]/span[1]",
    }
    t4_other_info_codes ={
        "otherInfoCode0": "//input[@id='id_other_info_code_0']",
        "otherInfoAmount0": "//input[@id='id_other_info_amount_0']",
        "otherInfoCode1": "//input[@id='id_other_info_code_1']",
        "otherInfoAmount1": "//input[@id='id_other_info_amount_1']",
        "otherInfoCode2": "//input[@id='id_other_info_code_2']",
        "otherInfoAmount2": "//input[@id='id_other_info_amount_2']",
        "otherInfoCode3": "//input[@id='id_other_info_code_3']",
        "otherInfoAmount3": "//input[@id='id_other_info_amount_3']",
        "otherInfoCode4": "//input[@id='id_other_info_code_4']",
        "otherInfoAmount4": "//input[@id='id_other_info_amount_4']",

    }
    drop_down_xpath = {
        "reflectEmployee": "//*[@id='el_Reflect']/div/div/div/div[1]/div[1]/div",
        "province": "//*[@id='el_Province']/div/div/div/div[1]/div[1]/div",
        "payPeriod": "//*[@id='el_PayPeriods']/div/div/div/div[1]/div[1]/div",
        "slipType": "//*[@id='el_SlipType']/div/div/div/div[1]/div[1]/div",
        "poe": "//*[@id='el_poe']/div/div/div/div[1]/div[1]/div",
        "reducedEi": "//*[@id='inspire']/div[1]/main/div/div/div[2]/span/form/div[2]/div/div[2]/div[3]"
                     "/div[2]/div[7]/div/div[2]/div/div/div/div[1]/div[1]/div",
        "status": "//*[@id='el_Status']/div/div/div/div[1]/div[1]/div",
        "employmentCode": "//*[@id='inspire']/div[1]/main/div/div/div[2]/span/form/div[2]/div/div[2]/"
                          "div[3]/div[2]/div[6]/div/div[2]/div/div/div/div[1]/div[1]/div",
        "otherInfoCode0": "//*[@id='inspire']/div/main/div/div/div[2]/span/form/div[2]/div/div[1]/div[2]"
                          "/div[2]/div[15]/div/div[2]/div[1]/div/div[1]/span/div/div/div/div[1]/div[1]/div",
        "otherInfoCode1": "//*[@id='inspire']/div/main/div/div/div[2]/span/form/div[2]/div/div[1]/div[2]/div[2]/"
                          "div[15]/div/div[2]/div[2]/div/div[1]/span/div/div/div/div[1]/div[1]/div",
        "otherInfoCode2": "//*[@id='inspire']/div/main/div/div/div[2]/span/form/div[2]/div/div[1]/div[2]/div[2]/"
                          "div[15]/div/div[2]/div[3]/div/div[1]/span/div/div/div/div[1]/div[1]/div",
        "otherInfoCode3": "//*[@id='inspire']/div/main/div/div/div[2]/span/form/div[2]/div/div[1]/div[2]/div[2]/div"
                          "[15]/div/div[2]/div[4]/div/div[1]/span/div/div/div/div[1]/div[1]/div",
        "otherInfoCode4": "//*[@id='inspire']/div/main/div/div/div[2]/span/form/div[2]/div/div[1]/div[2]/div[2]/div"
                          "[15]/div/div[2]/div[5]/div/div[1]/span/div/div/div/div[1]/div[1]/div",
        "exemptCpp": "//input[@id='id_cpp_qpp_app_exemption']",
        "exemptEi": "//input[@id='id_ei_app_exemption']",
        "exemptPpip": "//input[@id='id_ei_app_exemption']"
    }

