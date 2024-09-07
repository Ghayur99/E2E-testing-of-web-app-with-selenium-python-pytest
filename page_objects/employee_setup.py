
from page_objects.common_objects import CommonObjects

class EmployeeSetup(CommonObjects):
    """This class contains webElements of employee setup page"""
    employee_xpaths = {"addEmployee": "//span[contains(text(),'Add Employee')]",
                       "firstName": "//input[@id='id_name1']",
                       "lastName": "//input[@id='id_name2']",
                       "initials": "//input[@id='id_initials']",
                       "dOB": "//input[@id='id_dob']",
                       "employeeCode": "//input[@id='id_external_id']",
                       "sin": "//input[@id='id_sin']",
                       "type": "//input[@id='id_employee_type']",
                       "status": "//input[@id='id_status']",
                       "nextBtn": "//button[contains(text(),'Next Step')]",
                       "address": "//input[@id='id_address']",
                       "city": "//input[@id='id_city']",
                       "postCode": "//input[@id='id_post_code']",
                       "province": "//input[@id='id_province_id']",
                       "country": "//input[@id='id_country']",
                       "email": "//input[@id='id_email']",
                       "phoneHome": "//input[@id='id_phone_number']",
                       "homeExt": "//input[@id='id_ext']",
                       "phonePersonal": "//input[@id='id_phone_number2']",
                       "personalExt": "//input[@id='id_ext2']",
                       "nex1Btn": "//button[contains(text(),'Next Step')]",
                       "poe": "//input[@id='id_province_of_employment_id']",
                       "cppExempt": "//label[contains(text(),'CPP/QPP Exempt')]",
                       "eiExempt": "//label[contains(text(),'EI Exempt')]",
                       "ppipExempt": "//label[contains(text(),'PPIP Exempt')]",
                       "employmentCode": "//input[@id='id_employment_code']",
                       "payPeriod": "//input[@id='id_pay_period_id']",
                       "ReducedEi": "//input[@id='id_reduced_ei']",
                       "saveBtn": "//button[contains(text(),'Save')]",
                       "toastMessage": "//div[@class='toast-body']",
                       "closeToast": "//button[contains(text(),'×')]",
                       "employee_list": "//div[contains(text(),'Haroon Hassan')]",
                       "basicInfoLbl": "//div[contains(text(),'Enter basic information (Employee)')]",
                       "dobAlert": "//span[contains(text(),'Date of birth must be at least 10 years back.')]",
                       "incorrectSinAlert": "//span[contains(text(),'Social Insurance No. is incorrect')]",
                       "incorrectPostCode": "//span[contains(text(),'This value is incorrect')]",
                       "invalidEmail": "//span[contains(text(),'This field must only contain valid email')]",
                       "profileBtn": "//header/div[1]/button[4]/span[1]/i[1]",
                       "logout": "//a[contains(text(),'Logout')]",
                       "firstWizard": "//div[contains(text(),'2')]",
                       "basicInfo": "//div[contains(text(),'Enter basic information (Employee)')]",
                       "addressTitle": "//div[contains(text(),'Enter Address (Employee)')]",
                       "thirdWizard": "//div[contains(text(),'3')]",
                       "filingTitle": "//div[contains(text(),'Enter tax filing attributes (Employee)')]",
                       "fNameReq": "//body/div[@id='__nuxt']/div[@id='__layout']/div[@id='inspire']/"
                                            "div[1]/main[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/"
                                            "div[1]/div[1]/span[1]/form[1]/div[1]/span[1]/div[2]/div[2]/div[1]"
                                            "/div[1]/span[1]/span[1]",
                       "lNameReq": "//body/div[@id='__nuxt']/div[@id='__layout']/div[@id='inspire']/div[1]/main[1]"
                                   "/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/span[1]/form[1]"
                                   "/div[1]/span[1]/div[2]/div[2]/div[2]/div[1]/span[1]/span[1]",
                       "addressReq": "//body/div[@id='__nuxt']/div[@id='__layout']/div[@id='inspire']/div[1]"
                                     "/main[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]"
                                     "/span[1]/form[1]/div[2]/span[1]/div[2]/div[2]/div[1]/div[1]/span[1]/span[1]",
                       "cityReq": "//body/div[@id='__nuxt']/div[@id='__layout']/div[@id='inspire']/div[1]"
                                  "/main[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]"
                                  "/span[1]/form[1]/div[2]/span[1]/div[2]/div[2]/div[2]/div[1]/span[1]/span[1]",
                       "postcodeReq": "//body/div[@id='__nuxt']/div[@id='__layout']/div[@id='inspire']/div[1]"
                                      "/main[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]"
                                      "/span[1]/form[1]/div[2]/span[1]/div[2]/div[2]/div[3]/div[1]/span[1]/span[1]",
                       "provinceReq": "//body/div[@id='__nuxt']/div[@id='__layout']/div[@id='inspire']/div[1]"
                                      "/main[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]"
                                      "/span[1]/form[1]/div[2]/span[1]/div[2]/div[2]/div[4]/div[1]/span[1]/span[1]",
                       "emailReq": "//body/div[@id='__nuxt']/div[@id='__layout']/div[@id='inspire']/div[1]/main[1]"
                                   "/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/span[1]/form[1]"
                                   "/div[2]/span[1]/div[2]/div[2]/div[6]/div[1]/span[1]/span[1]",
                       "filingTxt": "//div[contains(text(),'Enter tax filing attributes (Employee)')]",
                       "poeReq": "//span[contains(text(),'This field is required')]"
                       }

