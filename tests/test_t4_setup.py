"""Class has all test case of t4 setup"""
import time
import pytest
from selenium.common.exceptions import NoSuchElementException
from page_objects.login_page import LoginPage
from page_objects.client_list import ClientList
from page_objects.header import Header
from page_objects.sidebar_menu import SidebarMenu
from page_objects.t4_list import T4List
from page_objects.t4_setup import T4Setup
from test_data.t4_data import T4Data
from utilities.base_class import BaseClass


class TestT4Setup(BaseClass):

    def test_all_fields(self):
        """
        test with all fields
        :return:
        """
        t4_setup = T4Setup(self.driver)
        t4_elements = t4_setup.t4_xpaths
        test_case1_data = T4Data.testCase1
        self.get_login()
        self.navigate_sidebar_menu()
        self.get_element_presence(t4_elements["reflectEmployee"])
        for key, value in t4_elements.items():
            if key not in ["loadEmployee", "AddMore", "country", "loadSlip", "saveButton", "toastMessage",
                           "dateOfBirth", "closeToast", "insurableEarning", "ppipInsurableEarning",
                           "ppipPremiums", "pensionableEarning"] \
                    and "Button" not in key and "otherInfoCode" not in key and "Checkbox"\
                    not in key and "exempt" not in key and "pensionablePeriod" not in key\
                    and "otherInfo" not in key:
                try:
                    self.get_elements(value).send_keys(test_case1_data[key])
                except NoSuchElementException:
                    print("otherInfo element not found")
        self.driver.execute_script("window.scrollTo(0, document.body.scrollLength);")
        self.get_element_presence(t4_elements["saveButton"])
        self.get_elements(t4_elements["saveButton"]).click()
        self.verify_toast_message()

    def test_required_fields(self):
        """
        test with required fields
        :return:
        """
        t4_setup = T4Setup(self.driver)
        t4_elements = t4_setup.t4_xpaths
        t4_alert_element = t4_setup.t4_alerts_xpaths
        self.get_login()
        self.navigate_sidebar_menu()
        self.get_element_presence(t4_elements["reflectEmployee"])
        self.get_elements(t4_elements["reflectEmployee"]).send_keys("123")
        self.get_element_presence(t4_elements["saveButton"])
        self.get_elements(t4_elements["saveButton"]).click()
        reflect_emp = self.get_elements(t4_alert_element["reflectEmployeeRequired"]).text
        assert reflect_emp == "This field is required", "Values do not select"
        self.get_elements(t4_elements["fName"]).send_keys("")
        f_name_required = self.get_elements(t4_alert_element["fNameRequired"]).text
        assert f_name_required == "This field is required", "Values do not enter"
        self.get_elements(t4_elements["lName"]).send_keys("")
        l_name_required = self.get_elements(t4_alert_element["lNameRequired"]).text
        assert l_name_required == "This field is required", "Values do not enter"
        self.get_elements(t4_elements["address"]).send_keys("")
        address_required = self.get_elements(t4_alert_element["addressRequired"]).text
        assert address_required == "This field is required", "Values do not enter"
        self.get_elements(t4_elements["city"]).send_keys("")
        city_required = self.get_elements(t4_alert_element["cityRequired"]).text
        assert city_required == "This field is required", "Value do not enter"
        self.get_elements(t4_elements["province"]).send_keys("")
        province_required = self.get_elements(t4_alert_element["provinceRequired"]).text
        assert province_required == "This field is required", "province do not select"
        self.get_elements(t4_elements["postCode"]).send_keys("")
        post_required = self.get_elements(t4_alert_element["postCodeRequired"]).text
        assert post_required == "This field is required", "Value do not enter"
        self.get_elements(t4_elements["poe"]).send_keys("")
        poe_required = self.get_elements(t4_alert_element["poeRequired"]).text
        assert poe_required == "This field is required", "province do not select"
        self.get_visibility_element(t4_elements["employmentIncome"])
        self.get_elements(t4_elements["otherInfoCode0"]).send_keys("30 - Board and lodging")
        self.get_elements(t4_elements["otherInfoCode1"]).send_keys("31 - Special work site")
        self.get_elements(t4_elements["otherInfoCode2"]).send_keys("32 - Travel in a prescribed zone")
        self.get_elements(t4_elements["otherInfoCode3"]).send_keys("33 - Medical travel assistance")
        self.get_elements(t4_elements["otherInfoCode4"]).send_keys("34 - Personal use of "
                                                                   "employer's automobile or motor vehicle")
        self.get_element_presence(t4_elements["saveButton"])
        self.get_elements(t4_elements["saveButton"]).click()
        other_Info_amount_0 = self.get_elements(t4_alert_element["otherInfoAmount0Required"]).text
        assert other_Info_amount_0 == "This field is required", "Values do not enter"
        other_Info_amount_1 = self.get_elements(t4_alert_element["otherInfoAmount1Required"]).text
        assert other_Info_amount_1 == "This field is required", "Values do not enter"
        other_Info_amount_2 = self.get_elements(t4_alert_element["otherInfoAmount2Required"]).text
        assert other_Info_amount_2 == "This field is required", "Values do not enter"
        other_Info_amount_3 = self.get_elements(t4_alert_element["otherInfoAmount3Required"]).text
        assert other_Info_amount_3 == "This field is required", "Values do not enter"
        other_Info_amount_4 = self.get_elements(t4_alert_element["otherInfoAmount4Required"]).text
        assert other_Info_amount_4 == "This field is required", "Values do not enter"
        self.driver.execute_script("window.scrollTo(0, document.body.scrollLength);")
        self.get_element_presence(t4_elements["saveButton"])
        self.get_elements(t4_elements["saveButton"]).click()

    def test_incorrect_fields(self):
        """
        test incorrect sin and invalid email fields
        :return:
        """
        t4_setup = T4Setup(self.driver)
        t4_elements = t4_setup.t4_xpaths
        t4_alert_element = t4_setup.t4_alerts_xpaths
        self.get_login()
        self.navigate_sidebar_menu()
        self.get_element_presence(t4_elements["reflectEmployee"])
        self.get_elements(t4_elements["reflectEmployee"]).send_keys("Yes")
        self.get_elements(t4_elements["sin"]).send_keys("999-000-010")
        incorrect_sin_alert = self.get_elements(t4_alert_element["incorrectSinAlert"]).text
        assert incorrect_sin_alert == "Social Insurance is incorrect", "Please entered correct value"
        self.get_elements(t4_elements["fName"]).send_keys("Haroon")
        self.get_elements(t4_elements["lName"]).send_keys("Hassan")
        self.get_elements(t4_elements["address"]).send_keys("House # 34, Street # 3")
        self.get_elements(t4_elements["city"]).send_keys("Toronto")
        self.get_elements(t4_elements["province"]).send_keys("Ontario")
        self.get_elements(t4_elements["postCode"]).send_keys("A4A4A4")
        self.get_elements(t4_elements["email"]).send_keys("haroon")
        invalid_email_alert = self.get_elements(t4_alert_element["invalidEmailAlert"]).text
        assert invalid_email_alert == "This field must only contain valid email", "Please entered valid value"
        self.get_elements(t4_elements["payPeriod"]).send_keys("26-Bi-Weekly")

    @pytest.mark.skip
    def test_unmasking(self):
        """
        test masking sin and email fields
        :return:
        """
        login_page = LoginPage(self.driver)
        login_elements = login_page.login_xpaths
        header_setup = Header(self.driver)
        header_elements = header_setup.Xpaths
        client_list = ClientList(self.driver)
        client_list_elements = client_list.client_xpaths
        side_menu = SidebarMenu(self.driver)
        menu_element = side_menu.menu_xpaths
        t4_setup = T4Setup(self.driver)
        t4_elements = t4_setup.t4_xpaths
        t4_list = T4List(self.driver)
        t4_list_elements = t4_list.t4_list_xpaths
        self.get_login()
        self.navigate_sidebar_menu(sub_menu_type='t4List')
        self.get_element_click_able(t4_list_elements["editButton"])
        self.get_elements(t4_list_elements["editButton"]).click()
        time.sleep(3)
        self.get_element_presence(t4_elements["sin"])
        checkMasking = self.get_elements(header_elements['maskButton']).text
        if checkMasking == "Unmask":
            sin_masked = self.get_elements(t4_elements["sin"]).get_attribute("value")
            assert "**" in sin_masked, "sin number is not masked"
            email_masked = self.get_elements(t4_elements["email"]).get_attribute("value")
            assert "**" in email_masked, "email  is not masked"
        else:
            self.get_elements(header_elements['maskButton']).click()
            sin_masked = self.get_elements(t4_elements['sin']).get_attribute("value")
            assert "**" in sin_masked, "sin number is not masked"
            email_masked = self.get_elements(t4_elements["email"]).get_attribute("value")
            assert "**" in email_masked, "email  is not masked"
        self.get_elements(t4_elements["reflectEmployee"]).send_keys("Yes")
        self.get_elements(t4_elements["saveButton"]).click()
        self.get_element_presence(t4_elements["toastMessage"])
        self.get_elements(t4_elements["closeToast"]).click()
        self.get_elements(header_elements['maskButton']).click()
        self.get_element_presence(header_elements['unmaskPassword'])
        self.get_elements(header_elements['unmaskPassword']).send_keys("123456789a")
        self.get_elements(header_elements['verifyButton']).click()
        time.sleep(2)
        email_unmasked = self.get_elements(t4_elements["email"]).get_attribute("value")
        assert "haroon@websential.ca" == email_unmasked, "email  is not unmasked"
        sin_masked = self.get_elements(t4_elements["sin"]).get_attribute("value")
        assert "990-000-010" == sin_masked, "sin number is not unmasked"
