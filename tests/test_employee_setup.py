import time
import pytest
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from page_objects.client_list import ClientList
from page_objects.employee_list import EmployeeList
from page_objects.employee_setup import EmployeeSetup
from page_objects.header import Header
from page_objects.login_page import LoginPage
from page_objects.sidebar_menu import SidebarMenu
from utilities.base_class import BaseClass


class TestEmployeeSetup(BaseClass):

    def test_all_fields(self):
        """
        test with all fields
        :return:
        # """
        employee_setup = EmployeeSetup(self.driver)
        employee_elements = employee_setup.employee_xpaths
        self.get_login()

        self.go_to_add_employee()
        self.get_element_presence(employee_elements["firstName"])
        self.get_elements(employee_elements["firstName"]).send_keys("Haroon")
        self.get_elements(employee_elements["lastName"]).send_keys("Hassan")
        self.get_elements(employee_elements["initials"]).send_keys("M")
        self.get_elements(employee_elements["dOB"]).send_keys("Sep 06 1985")
        self.get_elements(employee_elements["employeeCode"]).send_keys("12344")
        self.get_elements(employee_elements["sin"]).send_keys("990-000-010")
        self.get_elements(employee_elements["type"]).send_keys("FullTime Employee")
        self.get_elements(employee_elements["status"]).send_keys("Active")
        self.get_elements(employee_elements["nextBtn"]).click()
        self.get_element_presence(employee_elements["address"])
        self.get_elements(employee_elements["address"]).send_keys("House # 23, Street No. 2")
        self.get_elements(employee_elements["city"]).send_keys("Toronto")
        self.get_elements(employee_elements["postCode"]).send_keys("A5A5A5")
        self.get_elements(employee_elements["province"]).send_keys("Ontario")
        self.get_elements(employee_elements["country"]).send_keys("Canada")
        self.get_elements(employee_elements["email"]).send_keys("haroon@websential.ca")
        self.get_elements(employee_elements["phoneHome"]).send_keys("(123) 456-7890")
        self.get_elements(employee_elements["homeExt"]).send_keys("123")
        self.get_elements(employee_elements["phonePersonal"]).send_keys("(987) 654-3210")
        self.get_elements(employee_elements["personalExt"]).send_keys("458")
        self.get_elements(employee_elements["nex1Btn"]).click()
        self.get_element_presence(employee_elements["poe"])
        self.get_elements(employee_elements["poe"]).send_keys("Ontario")
        self.get_element_presence(employee_elements["employmentCode"])
        self.get_elements(employee_elements["employmentCode"]).send_keys("--")
        self.get_elements(employee_elements["payPeriod"]).send_keys("26-Bi-Weekly")
        self.get_elements(employee_elements["ReducedEi"]).send_keys("No")
        self.get_elements(employee_elements["saveBtn"]).click()
        self.verify_toast_message()

    def test_required_fields(self):
        """
        Test with required fields
        :return:
        """
        employee_setup = EmployeeSetup(self.driver)
        employee_elements = employee_setup.employee_xpaths
        self.get_login()
        self.go_to_add_employee()
        self.get_element_presence(employee_elements["firstName"])
        self.get_elements(employee_elements["firstName"]).send_keys("Tauqeer")
        self.get_elements(employee_elements["lastName"]).send_keys("Afzal")
        self.get_elements(employee_elements["type"]).send_keys("FullTime Employee")
        self.get_elements(employee_elements["status"]).send_keys("Active")
        self.get_elements(employee_elements["nextBtn"]).click()
        self.get_element_presence(employee_elements["address"])
        self.get_elements(employee_elements["address"]).send_keys("House # 12, Street No. 4, Link RD Cavalry Ground")
        self.get_elements(employee_elements["city"]).send_keys("Toronto")
        self.get_elements(employee_elements["postCode"]).send_keys("Q2W3R4")
        self.get_elements(employee_elements["province"]).send_keys("Alberta")
        self.get_elements(employee_elements["country"]).send_keys("USA")
        self.get_elements(employee_elements["email"]).send_keys("tauqeer@websential.ca")
        self.get_elements(employee_elements["nex1Btn"]).click()
        self.get_element_presence(employee_elements["poe"])
        self.get_elements(employee_elements["poe"]).send_keys("Quebec")
        self.get_element_presence(employee_elements["employmentCode"])
        self.get_elements(employee_elements["employmentCode"]).send_keys("--")
        self.get_elements(employee_elements["saveBtn"]).click()
        self.verify_toast_message()

    def test_incorrect_alerts(self):
        """
        test with invalid email
        :return:
        """
        employee_setup = EmployeeSetup(self.driver)
        employee_elements = employee_setup.employee_xpaths
        self.get_login()
        self.go_to_add_employee()
        self.get_element_presence(employee_elements["firstName"])
        self.get_elements(employee_elements["firstName"]).send_keys("Zahid")
        self.get_elements(employee_elements["lastName"]).send_keys("Badar")
        self.get_elements(employee_elements["type"]).send_keys("FullTime Employee")
        self.get_elements(employee_elements["status"]).send_keys("Active")
        self.get_elements(employee_elements["nextBtn"]).click()
        self.get_element_presence(employee_elements["address"])
        self.get_elements(employee_elements["address"]).send_keys("House # 43, Street No. 6")
        self.get_elements(employee_elements["city"]).send_keys("Lahore")
        self.get_elements(employee_elements["postCode"]).send_keys("A5A5A5")
        self.get_elements(employee_elements["province"]).send_keys("British Columbia")
        self.get_elements(employee_elements["country"]).send_keys("Canada")
        self.get_elements(employee_elements["email"]).send_keys("zahid")
        incorrect_email_alert = self.get_elements(employee_elements['invalidEmail']).text
        assert incorrect_email_alert == "This field must only contain valid email", "Alert message dose not appear"
        employee_setup.actions.double_click(self.get_elements(employee_elements["email"])).perform()
        self.get_elements(employee_elements["email"]).send_keys(Keys.BACKSPACE)
        self.get_elements(employee_elements["email"]).send_keys("zahid@websential.ca")
        self.get_elements(employee_elements["nex1Btn"]).click()
        self.get_element_presence(employee_elements["poe"])
        self.get_elements(employee_elements["poe"]).send_keys("British Columbia")
        self.get_element_presence(employee_elements["employmentCode"])
        self.get_elements(employee_elements["employmentCode"]).send_keys("--")
        self.get_elements(employee_elements["payPeriod"]).send_keys("26-Bi-Weekly")
        self.get_elements(employee_elements["ReducedEi"]).send_keys("No")
        self.get_elements(employee_elements["saveBtn"]).click()
        self.verify_toast_message()

    def test_emp_wizards(self):
        """
        Test the wizard of employee
        :return:
        """
        employee_setup = EmployeeSetup(self.driver)
        employee_elements = employee_setup.employee_xpaths
        self.get_login()
        self.go_to_add_employee()
        self.get_element_presence(employee_elements["firstWizard"])
        self.get_elements(employee_elements["firstWizard"]).click()
        time.sleep(3)
        basic_Info = self.get_elements(employee_elements["basicInfo"]).text
        assert basic_Info == "Enter basic information (Employee)", "Address wizard do not clickable"
        self.get_element_presence(employee_elements["fNameReq"])
        f_name = self.get_elements(employee_elements["fNameReq"]).text
        assert f_name == "This field is required", "FName is mandatory"
        l_name = self.get_elements(employee_elements["lNameReq"]).text
        assert l_name == "This field is required", "LName is mandatory"
        self.get_element_presence(employee_elements["firstName"])
        self.get_elements(employee_elements["firstName"]).send_keys("Bilal")
        self.get_elements(employee_elements["lastName"]).send_keys("Khan")
        time.sleep(3)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollLength);")
        self.get_element_presence(employee_elements["firstWizard"])
        self.get_elements(employee_elements["firstWizard"]).click()
        self.get_element_presence("//div[contains(text(),'3')]")
        self.get_elements(employee_elements["thirdWizard"]).click()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollLength);")
        time.sleep(3)
        address = self.get_elements(employee_elements["addressTitle"]).text
        assert address == "Enter Address (Employee)", "Filing wizard do not clickable"
        time.sleep(3)
        address_lbl = self.get_elements(employee_elements["addressReq"]).text
        assert address_lbl == "This field is required", "Address is mandatory"
        self.get_elements(employee_elements["address"]).send_keys("House # 22, Street No. 5, Link RD")
        time.sleep(3)
        city_lbl = self.get_elements(employee_elements["cityReq"]).text
        assert city_lbl == "This field is required", "City is mandatory"
        self.get_elements(employee_elements["city"]).send_keys("Toronto")
        time.sleep(3)
        post_code_lbl = self.get_elements(employee_elements["postcodeReq"]).text
        assert post_code_lbl == "This field is required", "Post Code is mandatory"
        self.get_elements(employee_elements["postCode"]).send_keys("Q2W3R4")
        province_lbl = self.get_elements(employee_elements["provinceReq"]).text
        assert province_lbl == "This field is required", "Province is mandatory"
        self.get_elements(employee_elements["province"]).send_keys("Manitoba")
        self.get_elements(employee_elements["country"]).send_keys("Canada")
        email_lbl = self.get_elements(employee_elements["emailReq"]).text
        assert email_lbl == "This field is required", "Email is mandatory"
        self.get_elements(employee_elements["email"]).send_keys("bilal@websential.ca")
        self.get_elements(employee_elements["nex1Btn"]).click()
        self.get_element_presence(employee_elements["poe"])
        filing_txt = self.get_elements(employee_elements["filingTxt"]).text
        assert filing_txt == "Enter tax filing attributes (Employee)", "User do not on Filing wizard"
        self.get_element_presence(employee_elements["poe"])
        self.get_elements(employee_elements["saveBtn"]).click()
        poe_lbl = self.get_elements(employee_elements["poeReq"]).text
        assert poe_lbl == "This field is required", "POE is mandatory"
        self.get_element_presence(employee_elements["poe"])
        self.get_elements(employee_elements["poe"]).send_keys("Quebec")
        self.get_element_presence(employee_elements["employmentCode"])
        self.get_elements(employee_elements["employmentCode"]).send_keys("--")
        self.get_elements(employee_elements["saveBtn"]).click()
        self.verify_toast_message()

    def test_cpp_exempt(self):
        """
        Test CPP exempt of employee and incorrect sin
        :return:
        """
        employee_setup = EmployeeSetup(self.driver)
        employee_elements = employee_setup.employee_xpaths
        self.get_login()
        self.go_to_add_employee()
        self.get_element_presence(employee_elements["firstName"])
        self.get_elements(employee_elements["firstName"]).send_keys("Exempt")
        self.get_elements(employee_elements["lastName"]).send_keys("CPP")
        self.get_elements(employee_elements["initials"]).send_keys("M")
        self.get_elements(employee_elements["dOB"]).send_keys("Sep 06 1985")
        self.get_elements(employee_elements["employeeCode"]).send_keys("47854AS")
        self.get_elements(employee_elements["sin"]).send_keys("999999")
        incorrect_sin_alert = self.get_elements(employee_elements['incorrectSinAlert']).text
        assert incorrect_sin_alert == "Social Insurance No. is incorrect", "Alert message dose not appear"
        employee_setup.actions.double_click(self.get_elements(employee_elements["sin"])).perform()
        self.get_elements(employee_elements["sin"]).send_keys(Keys.BACKSPACE)
        self.get_elements(employee_elements["sin"]).send_keys("990-000-093")
        self.get_elements(employee_elements["type"]).send_keys("FullTime Employee")
        self.get_elements(employee_elements["status"]).send_keys("Active")
        self.get_elements(employee_elements["nextBtn"]).click()
        self.get_element_presence(employee_elements["address"])
        self.get_elements(employee_elements["address"]).send_keys("House # 76, Street No. 3")
        self.get_elements(employee_elements["city"]).send_keys("Toronto")
        self.get_elements(employee_elements["postCode"]).send_keys("A5A5A5")
        self.get_elements(employee_elements["province"]).send_keys("Manitoba")
        self.get_elements(employee_elements["country"]).send_keys("Canada")
        self.get_elements(employee_elements["email"]).send_keys("haroon@technologyelement.com")
        self.get_elements(employee_elements["phoneHome"]).send_keys("(123) 456-7890")
        self.get_elements(employee_elements["homeExt"]).send_keys("123")
        self.get_elements(employee_elements["phonePersonal"]).send_keys("(987) 654-3210")
        self.get_elements(employee_elements["personalExt"]).send_keys("458")
        self.get_elements(employee_elements["nex1Btn"]).click()
        self.get_element_presence(employee_elements["poe"])
        self.get_elements(employee_elements["poe"]).send_keys("Manitoba")
        self.get_visibility_element(employee_elements["cppExempt"])
        self.get_elements(employee_elements["cppExempt"]).click()
        self.get_element_presence(employee_elements["employmentCode"])
        self.get_elements(employee_elements["employmentCode"]).send_keys("--")
        self.get_elements(employee_elements["payPeriod"]).send_keys("26-Bi-Weekly")
        self.get_elements(employee_elements["ReducedEi"]).send_keys("No")
        self.get_elements(employee_elements["saveBtn"]).click()
        self.verify_toast_message()

    def test_ei_exempt(self):
        """
        Test EI exempt of employee
        :return:
        """
        employee_setup = EmployeeSetup(self.driver)
        employee_elements = employee_setup.employee_xpaths
        self.get_login()
        self.go_to_add_employee()
        self.get_element_presence(employee_elements["firstName"])
        self.get_elements(employee_elements["firstName"]).send_keys("EI")
        self.get_elements(employee_elements["lastName"]).send_keys("Exempt")
        self.get_elements(employee_elements["initials"]).send_keys("M")
        self.get_elements(employee_elements["dOB"]).send_keys("Sep 06 1985")
        self.get_elements(employee_elements["employeeCode"]).send_keys("891504")
        self.get_elements(employee_elements["sin"]).send_keys("990-000-051")
        self.get_elements(employee_elements["type"]).send_keys("FullTime Employee")
        self.get_elements(employee_elements["status"]).send_keys("Active")
        self.get_elements(employee_elements["nextBtn"]).click()
        self.get_element_presence(employee_elements["address"])
        self.get_elements(employee_elements["address"]).send_keys("House # 174A, Garden Block, Garden Town")
        self.get_elements(employee_elements["city"]).send_keys("Lahore")
        self.get_elements(employee_elements["postCode"]).send_keys("S3F5H6")
        self.get_elements(employee_elements["province"]).send_keys("Nunavut")
        self.get_elements(employee_elements["country"]).send_keys("Canada")
        self.get_elements(employee_elements["email"]).send_keys("zahid@technologyelement.com")
        self.get_elements(employee_elements["phoneHome"]).send_keys("(123) 456-7890")
        self.get_elements(employee_elements["homeExt"]).send_keys("123")
        self.get_elements(employee_elements["phonePersonal"]).send_keys("(987) 654-3210")
        self.get_elements(employee_elements["personalExt"]).send_keys("458")
        self.get_elements(employee_elements["nex1Btn"]).click()
        self.get_element_presence(employee_elements["poe"])
        self.get_elements(employee_elements["poe"]).send_keys("Nunavut")
        self.get_visibility_element(employee_elements["eiExempt"])
        self.get_elements(employee_elements["eiExempt"]).click()
        self.get_element_presence(employee_elements["employmentCode"])
        self.get_elements(employee_elements["employmentCode"]).send_keys("--")
        self.get_elements(employee_elements["payPeriod"]).send_keys("26-Bi-Weekly")
        self.get_elements(employee_elements["ReducedEi"]).send_keys("No")
        self.get_elements(employee_elements["saveBtn"]).click()
        self.verify_toast_message()

    def test_ppip_exempt(self):
        """
        Test ppip exempt of employee
        :return:
        """
        employee_setup = EmployeeSetup(self.driver)
        employee_elements = employee_setup.employee_xpaths
        self.get_login()
        self.go_to_add_employee()
        self.get_element_presence(employee_elements["firstName"])
        self.get_elements(employee_elements["firstName"]).send_keys("PPIP")
        self.get_elements(employee_elements["lastName"]).send_keys("Exempt")
        self.get_elements(employee_elements["initials"]).send_keys("M")
        self.get_elements(employee_elements["dOB"]).send_keys("Sep 06 1985")
        self.get_elements(employee_elements["employeeCode"]).send_keys("96310")
        self.get_elements(employee_elements["sin"]).send_keys("990-000-036")
        self.get_elements(employee_elements["type"]).send_keys("FullTime Employee")
        self.get_elements(employee_elements["status"]).send_keys("Active")
        self.get_elements(employee_elements["nextBtn"]).click()
        self.get_element_presence(employee_elements["address"])
        self.get_elements(employee_elements["address"]).send_keys("House # 23, Street No. 2")
        self.get_elements(employee_elements["city"]).send_keys("Toronto")
        self.get_elements(employee_elements["postCode"]).send_keys("A5A5A5")
        self.get_elements(employee_elements["province"]).send_keys("New Brunswick")
        self.get_elements(employee_elements["country"]).send_keys("Canada")
        self.get_elements(employee_elements["email"]).send_keys("tauqeer@technologyelement.com")
        self.get_elements(employee_elements["phoneHome"]).send_keys("(123) 456-7890")
        self.get_elements(employee_elements["homeExt"]).send_keys("123")
        self.get_elements(employee_elements["phonePersonal"]).send_keys("(987) 654-3210")
        self.get_elements(employee_elements["personalExt"]).send_keys("4154")
        self.get_elements(employee_elements["nex1Btn"]).click()
        self.get_element_presence(employee_elements["poe"])
        self.get_elements(employee_elements["poe"]).send_keys("Quebec")
        self.get_visibility_element(employee_elements["ppipExempt"])
        self.get_elements(employee_elements["ppipExempt"]).click()
        self.get_element_presence(employee_elements["employmentCode"])
        self.get_elements(employee_elements["employmentCode"]).send_keys("--")
        self.get_elements(employee_elements["payPeriod"]).send_keys("26-Bi-Weekly")
        self.get_elements(employee_elements["ReducedEi"]).send_keys("No")
        self.get_elements(employee_elements["saveBtn"]).click()
        self.verify_toast_message()

    def test_cpp_ei_exempt(self):
        """
        Test CPP and EI exempt of employee
        :return:
        """
        employee_setup = EmployeeSetup(self.driver)
        employee_elements = employee_setup.employee_xpaths
        self.get_login()
        self.go_to_add_employee()
        self.get_element_presence(employee_elements["firstName"])
        self.get_elements(employee_elements["firstName"]).send_keys("Exempt CPP EI")
        self.get_elements(employee_elements["lastName"]).send_keys("Employee")
        self.get_elements(employee_elements["initials"]).send_keys("M")
        self.get_elements(employee_elements["dOB"]).send_keys("Sep 06 1985")
        self.get_elements(employee_elements["employeeCode"]).send_keys("96547")
        self.get_elements(employee_elements["sin"]).send_keys("122-131-238")
        self.get_elements(employee_elements["type"]).send_keys("FullTime Employee")
        self.get_elements(employee_elements["status"]).send_keys("Active")
        self.get_elements(employee_elements["nextBtn"]).click()
        self.get_element_presence(employee_elements["address"])
        self.get_elements(employee_elements["address"]).send_keys("House # 23, Street No. 2")
        self.get_elements(employee_elements["city"]).send_keys("Toronto")
        self.get_elements(employee_elements["postCode"]).send_keys("A5A5A5")
        self.get_elements(employee_elements["province"]).send_keys("Alberta")
        self.get_elements(employee_elements["country"]).send_keys("Canada")
        self.get_elements(employee_elements["email"]).send_keys("haroon@websential.ca")
        self.get_elements(employee_elements["phoneHome"]).send_keys("(123) 456-7890")
        self.get_elements(employee_elements["homeExt"]).send_keys("123")
        self.get_elements(employee_elements["phonePersonal"]).send_keys("(987) 654-7845")
        self.get_elements(employee_elements["personalExt"]).send_keys("8523")
        self.get_elements(employee_elements["nex1Btn"]).click()
        self.get_element_presence(employee_elements["poe"])
        self.get_elements(employee_elements["poe"]).send_keys("Ontario")
        self.get_visibility_element(employee_elements["cppExempt"])
        self.get_elements(employee_elements["cppExempt"]).click()
        self.get_visibility_element(employee_elements["eiExempt"])
        self.get_elements(employee_elements["eiExempt"]).click()
        self.get_element_presence(employee_elements["employmentCode"])
        self.get_elements(employee_elements["employmentCode"]).send_keys("--")
        self.get_elements(employee_elements["payPeriod"]).send_keys("26-Bi-Weekly")
        self.get_elements(employee_elements["ReducedEi"]).send_keys("No")
        self.get_elements(employee_elements["saveBtn"]).click()
        self.verify_toast_message()

    def test_french_characters(self):
        """
        Test with french characters of employee
        :return:
        """
        employee_setup = EmployeeSetup(self.driver)
        employee_elements = employee_setup.employee_xpaths
        self.get_login()
        self.go_to_add_employee()
        self.get_element_presence(employee_elements["firstName"])
        self.get_elements(employee_elements["firstName"]).send_keys("àâæçé")
        self.get_elements(employee_elements["lastName"]).send_keys("èêëïîô")
        self.get_elements(employee_elements["initials"]).send_keys("M")
        self.get_elements(employee_elements["dOB"]).send_keys("Sep 06 1985")
        self.get_elements(employee_elements["employeeCode"]).send_keys("12344")
        self.get_elements(employee_elements["sin"]).send_keys("121-212-104")
        self.get_elements(employee_elements["type"]).send_keys("FullTime Employee")
        self.get_elements(employee_elements["status"]).send_keys("Active")
        self.get_elements(employee_elements["nextBtn"]).click()
        self.get_element_presence(employee_elements["address"])
        self.get_elements(employee_elements["address"]).send_keys("Hoùse # 23, Streüt No. 2")
        self.get_elements(employee_elements["city"]).send_keys("Toronto")
        self.get_elements(employee_elements["postCode"]).send_keys("A5A5A5")
        self.get_elements(employee_elements["province"]).send_keys("Yukon")
        self.get_elements(employee_elements["country"]).send_keys("Canada")
        self.get_elements(employee_elements["email"]).send_keys("haroon@websential.ca")
        self.get_elements(employee_elements["phoneHome"]).send_keys("(123) 456-7890")
        self.get_elements(employee_elements["homeExt"]).send_keys("123")
        self.get_elements(employee_elements["phonePersonal"]).send_keys("(987) 654-3210")
        self.get_elements(employee_elements["personalExt"]).send_keys("458")
        self.get_elements(employee_elements["nex1Btn"]).click()
        self.get_element_presence(employee_elements["poe"])
        self.get_elements(employee_elements["poe"]).send_keys("Yukon")
        self.get_visibility_element(employee_elements["cppExempt"])
        self.get_elements(employee_elements["cppExempt"]).click()
        self.get_visibility_element(employee_elements["eiExempt"])
        self.get_elements(employee_elements["eiExempt"]).click()
        self.get_element_presence(employee_elements["employmentCode"])
        self.get_elements(employee_elements["employmentCode"]).send_keys("--")
        self.get_elements(employee_elements["payPeriod"]).send_keys("26-Bi-Weekly")
        self.get_elements(employee_elements["ReducedEi"]).send_keys("No")
        self.get_elements(employee_elements["saveBtn"]).click()
        self.verify_toast_message()

    def test_employee_del_all(self):
        """
        To test the deletion of employee
        :return:
        """
        employee_list = EmployeeList(self.driver)
        employee_list_elements = employee_list.employee_list_xpath
        log = self.test_logging()
        self.get_login()
        self.navigate_sidebar_menu(main_menu="peopleMenu", sub_menu_type="employeeMenu", expand_parent=False)

        try:
            time.sleep(3)
            self.get_element_click_able(employee_list_elements["headerListCheckBox"])
            self.get_elements(employee_list_elements["headerListCheckBox"]).click()
            self.get_element_click_able(employee_list_elements["deleteBtn"])
            self.get_elements(employee_list_elements["deleteBtn"]).click()
            self.get_element_click_able(employee_list_elements["OKBtn"])
            self.get_elements(employee_list_elements["OKBtn"]).click()
            self.verify_toast_message('delete')
        except NoSuchElementException:
            log.info("There is no employee in list")
