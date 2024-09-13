"""Test cases for vendor setup"""
import time

import pytest
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

from test_data.credentials import Credentials
from utilities.base_class import BaseClass
from page_objects.login_page import LoginPage
from page_objects.client_list import ClientList
from page_objects.header import Header
from page_objects.sidebar_menu import SidebarMenu
from page_objects.vendor_list import VendorList
from page_objects.vendor_setup import VendorSetup


class TestVendorSetup(BaseClass):
    """
    This is the class in which all the vendor setup test cases are defined in methods
    """

    def test_required_fields_info_screen(self):
        """
        Testing the required fields on the bases of the vendor type and there alert messages
        :return:
        """
        vendor_list = VendorList(self.driver)
        vendor_setup = VendorSetup(self.driver)
        vendor_elements = vendor_setup.x_paths
        vendorList_elements = vendor_list.vendor_list_Xpaths
        self.get_login()
        self.go_to_add_vendor()
        self.get_element_presence(vendor_elements["infoScreenLabel"])
        self.get_elements(vendor_elements["personalRatioButton"]).click()
        self.get_elements(vendor_elements["nextStep"]).click()
        self.get_element_presence(vendor_elements["sinAlert"])
        sin_alert = self.get_elements(vendor_elements["sinAlert"]).text
        first_name_alert = self.get_elements(vendor_elements["firstNameAlert"]).text
        last_name_alert = self.get_elements(vendor_elements["lastNameAlert"]).text
        assert sin_alert == "This field is required", "Sin field is not required"
        assert first_name_alert == "This field is required", "firstName field is not required"
        assert last_name_alert == "This field is required", "lastName field is not required"
        self.driver.execute_script("window.scrollTo(0, document.body.scrollLength);")
        self.get_elements(vendor_elements["businessRatioButton"]).click()
        self.get_elements(vendor_elements["nextStep"]).click()
        business_name_alert = self.get_elements(vendor_elements["businessNameAlert"]).text
        business_no_alert = self.get_elements(vendor_elements["businessNoAlert"]).text
        assert business_name_alert == "This field is required", "Sin field is not required"
        assert business_no_alert == "This field is required", "firstName field is not required"

    def test_incorrect_alert(self):
        """
        Testing the incorrect sin,business,postCode and email alert
        :return:
        """
        vendor_list = VendorList(self.driver)
        vendor_setup = VendorSetup(self.driver)
        vendor_elements = vendor_setup.x_paths
        vendorList_elements = vendor_list.vendor_list_Xpaths
        self.get_login()
        self.go_to_add_vendor()
        self.get_element_presence(vendor_elements["firstName"])
        self.get_elements(vendor_elements["sin"]).send_keys("99999999")
        incorrect_sin_Alert = self.get_elements(vendor_elements['incorrectSinAlert']).text
        assert incorrect_sin_Alert == "Social Insurance No. is incorrect", "Alert message dose not appear"
        self.get_elements(vendor_elements["businessNumber"]).send_keys("12121212121")
        incorrect_business_no_Alert = self.get_elements(vendor_elements['incorrectBusinessNoAlert']).text
        assert incorrect_business_no_Alert == "Business No. is incorrect", "Alert message dose not appear"
        vendor_setup.actions.double_click(self.get_elements(vendor_elements["sin"])).perform()
        self.get_elements(vendor_elements["sin"]).send_keys(Keys.BACKSPACE)
        vendor_setup.actions.double_click(self.get_elements(vendor_elements["businessNumber"])).perform()
        self.get_elements(vendor_elements["businessNumber"]).send_keys(Keys.BACKSPACE)
        self.get_elements(vendor_elements["businessNumber"]).send_keys("121212120RP0000")
        self.get_elements(vendor_elements["businessName"]).send_keys("Test name")
        self.get_elements(vendor_elements["nextStep"]).click()
        self.get_element_presence(vendor_elements["addressScreenLabel"])
        self.get_elements(vendor_elements["postCode"]).send_keys("J9l99")
        self.get_elements(vendor_elements["email"]).send_keys("ghayurbutt")
        self.get_elements(vendor_elements["save"]).click()
        incorrect_post_code_Alert = self.get_elements(vendor_elements['incorrectPostCodeAlert']).text
        assert incorrect_post_code_Alert == "This value is incorrect", "Alert message dose not appear"
        incorrect_email_Alert = self.get_elements(vendor_elements['incorrectEmailAlert']).text
        assert incorrect_email_Alert == "This field must only contain valid email", "Alert message dose not appear"

    def test_required_fields_address_screen(self):
        """
        Testing the required fields on the address wizard screen
        :return:
        """
        vendor_list = VendorList(self.driver)
        vendor_setup = VendorSetup(self.driver)
        vendor_elements = vendor_setup.x_paths
        vendorList_elements = vendor_list.vendor_list_Xpaths
        self.get_login()
        self.go_to_add_vendor()
        self.get_element_presence(vendor_elements["businessName"])
        self.get_elements(vendor_elements["businessName"]).send_keys("Zahid Bader")
        self.get_elements(vendor_elements["businessNumber"]).send_keys("121212120RP0000")
        self.driver.execute_script("window.scrollTo(0, document.body.scrollLength);")
        self.get_elements(vendor_elements["vendorAddressWizard"]).click()
        self.get_element_presence(vendor_elements["addressScreenLabel"])
        self.get_elements(vendor_elements["save"]).click()
        address_alert = self.get_elements(vendor_elements["addressAlert"]).text
        city_alert = self.get_elements(vendor_elements["cityAlert"]).text
        post_code_required_alert = self.get_elements(vendor_elements["postCodeRequiredAlert"]).text
        email_required_alert = self.get_elements(vendor_elements["emailRequiredAlert"]).text
        province_alert = self.get_elements(vendor_elements["provinceAlert"]).text
        assert address_alert == "This field is required", "address field is not required"
        assert city_alert == "This field is required", "city field is not required"
        assert post_code_required_alert == "This field is required", "post_code field is not required"
        assert email_required_alert == "This field is required", "email field is not required"
        assert province_alert == "This field is required", "province field is not required"

    def test_wizard_switching(self):
        """
        Testing the wizard switching option with required data filled it should switch the screen
        :return:
        """
        side_menu = SidebarMenu(self.driver)
        vendor_list = VendorList(self.driver)
        vendor_setup = VendorSetup(self.driver)
        vendor_elements = vendor_setup.x_paths
        vendorList_elements = vendor_list.vendor_list_Xpaths
        sidebar_elements = side_menu.menu_xpaths
        self.get_login()
        self.go_to_add_vendor()
        self.get_element_presence(vendor_elements["infoScreenLabel"])
        self.get_elements(vendor_elements["businessName"]).send_keys("GhayurButt")
        self.get_elements(vendor_elements["businessNumber"]).send_keys("121212120RP0000")
        self.driver.execute_script("window.scrollTo(0, document.body.scrollLength);")
        self.get_elements(vendor_elements["vendorAddressWizard"]).click()
        self.get_element_presence(vendor_elements["addressScreenLabel"])
        address_screen_label = self.get_elements(vendor_elements["addressScreenLabel"]).text
        assert address_screen_label == "Enter Address (Vendor)", "Wizard is not working"
        self.get_elements(vendor_elements["address"]).send_keys("test Address")
        self.get_elements(vendor_elements["city"]).send_keys("lahore")
        self.get_elements(vendor_elements["postCode"]).send_keys("H8H8H8")
        self.get_elements(vendor_elements["province"]).send_keys("ab")
        self.get_elements(vendor_elements["country"]).send_keys("ca")
        self.get_elements(vendor_elements["email"]).send_keys("Ghayurbutt11@gmail.com")
        self.get_elements(vendor_elements["vendorInfoWizard"]).click()
        self.get_element_presence(vendor_elements["infoScreenLabel"])
        info_screen_label = self.get_elements(vendor_elements["infoScreenLabel"]).text
        assert info_screen_label == "Enter basic information (Vendor)", "Wizard is not working"

    def test_wizard_switching_with_no_data(self):
        """
        Testing the wizard switching option with no data filled it should not switch to the address screen but it can
        switch to vendor info screen if required fields are not filled
        :return:
        """
        vendor_list = VendorList(self.driver)
        vendor_setup = VendorSetup(self.driver)
        vendor_elements = vendor_setup.x_paths
        vendorList_elements = vendor_list.vendor_list_Xpaths
        self.get_login()
        self.go_to_add_vendor()
        self.get_element_presence(vendor_elements["infoScreenLabel"])
        self.driver.execute_script("window.scrollTo(0, document.body.scrollLength);")
        self.get_elements(vendor_elements["vendorAddressWizard"]).click()
        info_screen_label = self.get_elements(vendor_elements["infoScreenLabel"]).text
        assert info_screen_label == "Enter basic information (Vendor)", "Wizard is switching the screen without " \
                                                                        "required fields filed"
        business_no_alert = self.get_elements(vendor_elements["businessNoAlert"]).text
        business_name_alert = self.get_elements(vendor_elements["businessNameAlert"]).text
        assert business_name_alert == "This field is required", "Sin field is not required"
        assert business_no_alert == "This field is required", "firstName field is not required"
        self.get_elements(vendor_elements["businessName"]).send_keys("GhayurButt")
        self.get_elements(vendor_elements["businessNumber"]).send_keys("121212120RP0000")
        self.driver.execute_script("window.scrollTo(0, document.body.scrollLength);")
        self.get_elements(vendor_elements["vendorAddressWizard"]).click()
        self.get_element_presence(vendor_elements["addressScreenLabel"])
        address_screen_label = self.get_elements(vendor_elements["addressScreenLabel"]).text
        assert address_screen_label == "Enter Address (Vendor)", "Wizard is not working "
        self.get_elements(vendor_elements["vendorInfoWizard"]).click()
        self.get_element_presence(vendor_elements["infoScreenLabel"])
        info_screen_label = self.get_elements(vendor_elements["infoScreenLabel"]).text
        assert info_screen_label == "Enter basic information (Vendor)", "Wizard is not working"

    def test_creating_business_vendor(self):
        """
        Creating business vendor with only required fields filled
        :return:
        """
        vendor_list = VendorList(self.driver)
        vendor_setup = VendorSetup(self.driver)
        vendor_elements = vendor_setup.x_paths
        vendorList_elements = vendor_list.vendor_list_Xpaths
        self.get_login()
        self.go_to_add_vendor()
        self.get_element_presence(vendor_elements["infoScreenLabel"])
        self.get_elements(vendor_elements["businessName"]).send_keys("GhayurButt")
        self.get_elements(vendor_elements["businessNumber"]).send_keys("121212120RP0000")
        self.get_elements(vendor_elements["nextStep"]).click()
        self.get_element_presence(vendor_elements["addressScreenLabel"])
        self.get_elements(vendor_elements["address"]).send_keys("test Address")
        self.get_elements(vendor_elements["city"]).send_keys("lahore")
        self.get_elements(vendor_elements["postCode"]).send_keys("H8H8H8")
        self.get_elements(vendor_elements["province"]).send_keys("ab")
        self.get_elements(vendor_elements["country"]).send_keys("ca")
        self.get_elements(vendor_elements["email"]).send_keys("Ghayurbutt11@gmail.com")
        self.get_elements(vendor_elements["save"]).click()
        self.verify_toast_message()

    def test_creating_personal_vendor(self):
        """
        Creating personal vendor with only required fields filled
        :return:
        """
        vendor_list = VendorList(self.driver)
        vendor_setup = VendorSetup(self.driver)
        vendor_elements = vendor_setup.x_paths
        vendorList_elements = vendor_list.vendor_list_Xpaths
        self.get_login()
        self.go_to_add_vendor()
        self.get_element_presence(vendor_elements["infoScreenLabel"])
        self.get_elements(vendor_elements["personalRatioButton"]).click()
        self.get_elements(vendor_elements["sin"]).send_keys("000-000-000")
        self.get_elements(vendor_elements["firstName"]).send_keys("Zahid")
        self.get_elements(vendor_elements["lastName"]).send_keys("bader")
        self.get_elements(vendor_elements["nextStep"]).click()
        self.get_element_presence(vendor_elements["addressScreenLabel"])
        self.get_elements(vendor_elements["address"]).send_keys("test Address")
        self.get_elements(vendor_elements["city"]).send_keys("lahore")
        self.get_elements(vendor_elements["postCode"]).send_keys("H8H8H8")
        self.get_elements(vendor_elements["province"]).send_keys("ab")
        self.get_elements(vendor_elements["country"]).send_keys("ca")
        self.get_elements(vendor_elements["email"]).send_keys("Ghayurbutt11@gmail.com")
        self.get_elements(vendor_elements["save"]).click()
        self.verify_toast_message()

    def test_creating_vendor_with_all_field_filled(self):
        """
        Creating vendor with all the fields filled
        :return:
        """
        side_menu = SidebarMenu(self.driver)
        vendor_list = VendorList(self.driver)
        vendor_setup = VendorSetup(self.driver)
        vendor_elements = vendor_setup.x_paths
        vendorList_elements = vendor_list.vendor_list_Xpaths
        sidebar_elements = side_menu.menu_xpaths
        self.get_login()
        self.go_to_add_vendor()
        self.get_text_prasence_in_element(vendor_elements["infoScreenLabel"], "Enter")
        # self.get_elements(vendor_elements["personalRatioButton"]).click()
        self.get_elements(vendor_elements["sin"]).send_keys("000-000-000")
        self.get_elements(vendor_elements["firstName"]).send_keys("Zahid")
        self.get_elements(vendor_elements["lastName"]).send_keys("bader")
        self.get_elements(vendor_elements["initials"]).send_keys("m")
        self.get_elements(vendor_elements["businessName"]).send_keys("GhayurButt")
        self.get_elements(vendor_elements["businessNumber"]).send_keys("121212120RP0000")
        self.get_elements(vendor_elements["nextStep"]).click()
        self.get_element_presence(vendor_elements["addressScreenLabel"], 10)
        self.get_elements(vendor_elements["address"]).send_keys("test Address")
        self.get_elements(vendor_elements["city"]).send_keys("lahore")
        self.get_elements(vendor_elements["postCode"]).send_keys("H8H8H8")
        self.get_elements(vendor_elements["province"]).send_keys("ab")
        self.get_elements(vendor_elements["country"]).send_keys("ca")
        self.get_elements(vendor_elements["email"]).send_keys("Ghayurbutt11@gmail.com")
        self.get_elements(vendor_elements["phone1"]).send_keys("1234567890")
        self.get_elements(vendor_elements["ext1"]).send_keys("456")
        self.get_elements(vendor_elements["phone2"]).send_keys("1234562586")
        self.get_elements(vendor_elements["ext2"]).send_keys("0308")
        self.get_elements(vendor_elements["save"]).click()
        self.verify_toast_message()

    @pytest.mark.skip
    def test_masking_unmasking(self):
        """
        Testing the masking and unmasking on vendor setup
        :return:
        """
        g_credentials = Credentials.users_credentials
        side_menu = SidebarMenu(self.driver)
        vendor_list = VendorList(self.driver)
        vendor_setup = VendorSetup(self.driver)
        header_setup = Header(self.driver)
        header_elements = header_setup.Xpaths
        vendor_elements = vendor_setup.x_paths
        vendorList_elements = vendor_list.vendor_list_Xpaths
        sidebar_elements = side_menu.menu_xpaths
        self.get_login()
        self.go_to_add_vendor()
        self.get_element_presence(vendor_elements["infoScreenLabel"], 10)
        self.get_elements(vendor_elements["sin"]).send_keys("000-000-000")
        self.get_elements(vendor_elements["businessName"]).send_keys("MaskTest")
        self.get_elements(vendor_elements["businessNumber"]).send_keys("121212120RP0000")
        self.get_elements(vendor_elements["nextStep"]).click()
        self.get_element_presence(vendor_elements["addressScreenLabel"], 10)
        self.get_elements(vendor_elements["address"]).send_keys("test Address")
        self.get_elements(vendor_elements["city"]).send_keys("lahore")
        self.get_elements(vendor_elements["postCode"]).send_keys("H8H8H8")
        self.get_elements(vendor_elements["province"]).send_keys("ab")
        self.get_elements(vendor_elements["country"]).send_keys("ca")
        self.get_elements(vendor_elements["email"]).send_keys("Ghayurbutt11@gmail.com")
        self.get_elements(vendor_elements["save"]).click()
        self.get_element_presence(vendor_elements["ToastMessage"], 10)
        self.driver.back()
        self.get_element_presence(vendorList_elements['testMask'], 10)
        self.get_elements(vendorList_elements['testMask']).click()
        self.get_element_presence(vendor_elements['sin'], 10)
        checkMasking = self.get_elements(header_elements['maskButton']).text
        if checkMasking == "Unmask":
            sin_masked = self.get_elements(vendor_elements["sin"]).get_attribute("value")
            assert "**" in sin_masked, "sin number is not masked"
        else:
            self.get_elements(header_elements['maskButton']).click()
            sin_masked = self.get_elements(vendor_elements['sin']).get_attribute("value")
            assert "**" in sin_masked, "sin number is not masked"
        self.get_elements(vendor_elements["nextStep"]).click()
        self.get_element_presence(vendor_elements["addressScreenLabel"], 10)
        email_masked = self.get_elements(vendor_elements["email"]).get_attribute("value")
        assert "**" in email_masked, "email  is not masked"
        self.get_elements(vendor_elements["save"]).click()
        self.get_element_presence(vendor_elements["ToastMessage"], 10)
        self.get_elements(vendor_elements["closeToast"]).click()
        self.get_elements(header_elements['maskButton']).click()
        self.get_element_presence(header_elements['unmaskPassword'], 10)
        self.get_elements(header_elements['unmaskPassword']).send_keys(g_credentials['password'])
        self.get_elements(header_elements['verifyButton']).click()
        time.sleep(2)
        email_unmasked = self.get_elements(vendor_elements["email"]).get_attribute("value")
        assert "Ghayurbutt11@gmail.com" == email_unmasked, "email  is not unmasked"
        self.get_elements(vendor_elements["previous"]).click()
        self.get_element_presence(vendor_elements["infoScreenLabel"], 10)
        sin_masked = self.get_elements(vendor_elements["sin"]).get_attribute("value")
        assert "000-000-000" == sin_masked, "sin number is not unmasked"

    def test_delete_all_vendors(self):
        """
        Deleting all the vendors that are created in previous test cases so that they will not fail the tests when they
        run again
        :return:
        """
        log = self.test_logging()
        vendor_list = VendorList(self.driver)
        vendorList_elements = vendor_list.vendor_list_Xpaths
        self.get_login()
        self.navigate_sidebar_menu(main_menu="peopleMenu", sub_menu_type="vendorMenu", expand_parent=False)
        self.get_element_click_able(vendorList_elements['addVendor'])
        try:
            self.get_elements(vendorList_elements["firstVendor"])
            self.get_elements(vendorList_elements["selectAllVendors"]).click()
            self.get_element_presence(vendorList_elements["deleteAllButton"])
            self.get_elements(vendorList_elements["deleteAllButton"]).click()
            self.get_element_click_able(vendorList_elements["confirmDeleteAll"])
            self.get_elements(vendorList_elements["confirmDeleteAll"]).click()

            self.verify_toast_message('delete')
            log.info("Record is been deleted")
        except NoSuchElementException:
            print("There is no vendor in the list")
            log.info("There is no vendor in the list")
