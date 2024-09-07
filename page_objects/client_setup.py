from page_objects.common_objects import CommonObjects

class ClientSetup(CommonObjects):
    client_setup_xpaths = {"registration": "//input[@id='id_registration_number']",
                           "legalName": "//input[@id='id_client_name']",
                           "operatingName": "//input[@id='id_operating_name']",
                           "createDate": "//input[@id='id_creation_date']",
                           "employees": "//input[@id='id_employee']",
                           "accManager": "//input[@id='id_account_owner']",
                           "bsnNo": "//input[@id='id_business_number']",
                           "reiNo": "//input[@id='id_reduced_ei_business_number']",
                           "accCode": "//input[@id='id_access_code']",
                           "nxtButton": "//button[contains(text(),'Next Step')]",
                           "address": "//input[@id='id_address']",
                           "city": "//input[@id='id_city']",
                           "province": "//input[@id='id_province']",
                           "opeProv": "//*[contains(@class, 'v-autocomplete')]",
                           "country": "//input[@id='id_country']",
                           "postCode": "//input[@id='id_postal_code']",
                           "email": "//input[@id='id_email']",
                           "phoneHome": "//input[@id='id_phone_no']",
                           "extHome": "//input[@id='id_ext']",
                           "phonePer": "//input[@id='id_phone2']",
                           "extPer": "//input[@id='id_ext2']",
                           "fax": "//input[@id='id_fax']",
                           "website": "//input[@id='id_url']",
                           "saveButton": "//button[contains(text(),'Save')]"
                           }



