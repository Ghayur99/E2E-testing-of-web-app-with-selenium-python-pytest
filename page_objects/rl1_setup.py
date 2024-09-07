"""RL-1 setup objects are define here"""
from page_objects.common_objects import CommonObjects


class Rl1Setup(CommonObjects):
    """This class contains webElements of T4A setup """

    rl1_x_paths = {
        "loadEmployee": "//input[@id='id_load_employee']", "loadSlip": "//input[@id='id_load_slip']",
        "reflectInMasterData": "//input[@id='id_reflect_master_data']",
        "saveButton": "//*[contains(text(),'Save')]", "resetButton": "//*[contains(text(),'Reset')]",
        "deleteButton": "//*[contains(text(),'Delete')]",
        "sin": "//input[@id='id_emp_sin']", "firstName": "//input[@id='id_first_name']",
        "lastName": "//input[@id='id_last_name']", "initials": "//input[@id='id_initials']",
        "dateOfBirth": "//input[@id='id_date_of_birth']", "address": "//input[@id='id_address']",
        "city": "//input[@id='id_city']","postCode": "//input[@id='id_post_code']",
        "province": "//input[@id='id_province']", "country": "//input[@id='id_country']",
        "email": "//input[@id='id_email']", "payPeriod": "//input[@id='id_pay_period']",
        "slipType": "//input[@id='id_slip_type']",
        "status": "//input[@id='id_slip_status']",
        "A-Revenus d'emploi": "//input[@id='id_box_a']",
        "B-Cotisation au RRQ": "//input[@id='id_box_b']",
        "C- Cot. à l'assurance emploi": "//input[@id='id_box_c']",
        "D- Cotisation à un RPA": "//input[@id='id_box_d']",
        "E-ImpôtduQuébecretenu": "//input[@id='id_box_e']",
        "E-Impôt du Québec retenu": "//input[@id='id_box_e']",
        "F-Cotisation syndicale": "//input[@id='id_box_f']",
        "G-Salaire admissible au RRQ": "//input[@id='id_box_g']",
        "H-Cotisation au RQAP": "//input[@id='id_box_h']",
        "I-Salaire admissible au RQAP": "//input[@id='id_box_i']",
        "J- Régime privé d'ass. maladie": "//input[@id='id_box_j']",
        "K-Voyages (région éloignée)": "//input[@id='id_box_k']",
        "L-Autres avantages": "//input[@id='id_box_l']",
        "M-Commissions": "//input[@id='id_box_m']",
        "N-Dons de bienfaisance": "//input[@id='id_box_n']",
        "O-Autres revenus": "//input[@id='id_box_o']",
        "P- Régime d’ass. interentreprises": "//input[@id='id_box_p']",
        "Q-Salaires différés": "//input[@id='id_box_q']",
        "R-Revenu « situé» dans une réserve": "//input[@id='id_box_r']",
        "S- Pourboires reçus": "//input[@id='id_box_s']",
        "T-Pourboires attribués": "//input[@id='id_box_t']",
        "U- Retraite progressive": "//input[@id='id_box_u']",
        "V-Nourriture et logement": "//input[@id='id_box_v']",
        "W-Véhicule à moteur": "//input[@id='id_box_w']",
        "Code (Case O)": "//input[@id='id_code']",
        "OtherInfo0": "//input[@id='id_other_info_code_0']",
        "amount0": "//input[@id='id_other_info_amount_0']",
        "OtherInfo1": "//input[@id='id_other_info_code_1']",
        "amount1": "//input[@id='id_other_info_amount_1']",
        "OtherInfo2": "//input[@id='id_other_info_code_2']",
        "amount2": "//input[@id='id_other_info_amount_2']",
        "OtherInfo3": "//input[@id='id_other_info_code_3']",
        "amount3": "//input[@id='id_other_info_amount_3']",
        "toastMessage": "//div[@class='toast-body']",
        "closeToast": "//button[contains(text(),'×')]"
        }

    rl1_alerts_xpaths = {
        "reflectInMasterDataRequired":"//body/div[@id='__nuxt']/div[@id='__layout']/div[@id='inspire']/div[1]/main[1]"
                                      "/div[1]/div[1]/div[2]/span[1]/form[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]"
                                      "/div[1]/div[2]/span[1]/span[1]",

        "firstNameRequired": "//body/div[@id='__nuxt']/div[@id='__layout']/div[@id='inspire']/div[1]/main[1]/div[1]"
                             "/div[1]/div[2]/span[1]/form[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[3]/div[1]/div[2]"
                             "/span[1]/span[1]",
        "lastNameRequired": "//body/div[@id='__nuxt']/div[@id='__layout']/div[@id='inspire']/div[1]/main[1]/div[1]"
                            "/div[1]/div[2]/span[1]/form[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[5]/div[1]/div[2]"
                            "/span[1]/span[1]",
        "addressRequired": "//body/div[@id='__nuxt']/div[@id='__layout']/div[@id='inspire']/div[1]/main[1]/div[1]"
                           "/div[1]/div[2]/span[1]/form[1]/div[2]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[2]"
                           "/span[1]/span[1]",
        "cityRequired": "//body/div[@id='__nuxt']/div[@id='__layout']/div[@id='inspire']/div[1]/main[1]/div[1]/div[1]"
                        "/div[2]/span[1]/form[1]/div[2]/div[1]/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]/span[1]"
                        "/span[1]",
        "postCodeRequired": "//body/div[@id='__nuxt']/div[@id='__layout']/div[@id='inspire']/div[1]/main[1]/div[1]"
                            "/div[1]/div[2]/span[1]/form[1]/div[2]/div[1]/div[2]/div[2]/div[2]/div[4]/div[1]/div[2]"
                            "/span[1]/span[1]",
        "provinceRequired": "//body/div[@id='__nuxt']/div[@id='__layout']/div[@id='inspire']/div[1]/main[1]/div[1]/"
                            "div[1]/div[2]/span[1]/form[1]/div[2]/div[1]/div[2]/div[2]/div[2]/div[3]/div[1]/div[2]"
                            "/span[1]/span[1]",
        "otherInfoValueRequiredAlert": "//body/div[@id='__nuxt']/div[@id='__layout']/div[@id='inspire']/div[1]/main[1]"
                                       "/div[1]/div[1]/div[2]/span[1]/form[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[2"
                                       "6]/div[1]/div[2]/div[1]/div[1]/div[3]/span[1]/span[1]",
        "emailAlert": "//span[contains(text(),'This field must only contain valid email')]",
        "sinIncorrectAlert": "//span[contains(text(),'Social Insurance is incorrect')]",
        "postCodeIncorrectAlert": "//span[contains(text(),'This value is incorrect')]"

    }
    drop_down_xpath_rl1 = {
        "reflectInMasterData": "//*[@id='el_Reflect']/div/div/div/div[1]/div[1]/div",
        "province": "//*[@id='el_Province']/div/div/div/div[1]/div[1]/div",
        "payPeriod": "//*[@id='el_PayPeriods']/div/div/div/div[1]/div[1]/div",
        "slipType": "//*[@id='el_SlipType']/div/div/div/div[1]/div[1]/div",
        "poe": "//*[@id='el_poe']/div/div/div/div[1]/div[1]/div",
        "status": "//*[@id='el_Status']/div/div/div/div[1]/div[1]/div",
        "Code (Case O)": "//*[@id='inspire']/div/main/div/div/div[2]"
                         "/span/form/div[2]/div/div[1]/div[2]"
                         "/div[2]/div[25]/div/div[2]/div/div/div/div[1]/div[1]/div",
        "OtherInfo0": "//*[@id='inspire']/div/main/div/div/div[2]/span/form/div[2]/div/div[1]"
                      "/div[2]/div[2]/div[26]/div/div[2]/div[1]/div/div[1]/span/div/div/div/div[1]/div[1]/div",
        "OtherInfo1": "//*[@id='inspire']/div/main/div/div/div[2]/span/form/div[2]/div/div[1]"
                      "/div[2]/div[2]/div[26]/div/div[2]/div[2]/div/div[1]/span"
                      "/div/div/div/div[1]/div[1]/div",
        "OtherInfo2": "//*[@id='inspire']/div/main/div/div/div[2]/span/form/div[2]/div/div[1]"
                      "/div[2]/div[2]/div[26]/div/div[2]/div[3]/div/div[1]"
                      "/span/div/div/div/div[1]/div[1]/div",
        "OtherInfo3": "//*[@id='inspire']/div/main/div/div/div[2]/span/form/div[2]/div/div[1]"
                      "/div[2]/div[2]/div[26]/div/div[2]/div[4]/div/div[1]"
                      "/span/div/div/div/div[1]/div[1]/div"
    }




