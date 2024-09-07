"""T4A slip test cases"""
import time
import pytest
from selenium.common.exceptions import NoSuchElementException
from test_data.credentials import Credentials
from test_data.t4a_data import DataT4a
from utilities.base_class import BaseClass
from page_objects.dashboard import Dashboard
from page_objects.header import Header
from page_objects.t4a_list import T4aList
from page_objects.t4a_setup import T4aSetup


class TestT4aSetup(BaseClass):
    """
    This is the class in which all the T4A setup test cases are defined in methods
    """

    def test_all_fields_filled(self):
        """
        In this test case we are testing the T4A slip foam with all fields filled
        :return:
        """
        t4a_setup = T4aSetup(self.driver)
        t4a_list = T4aList(self.driver)
        t4a_data = DataT4a
        t4a_elements = t4a_setup.t4a_x_paths
        t4a_list_elements = t4a_list.t4a_list_xpaths
        test_case_data = t4a_data.test_case1
        self.get_login()
        self.go_to_create_t4a()
        self.get_element_presence(t4a_elements['loadVendor'])
        for key, value in t4a_elements.items():

            if key not in ["loadVendor", "AddMore", "country", "loadSlip", "saveButton", "toastMessage", "closeToast"] \
                    and "Button" not in key:
                if key == 'province':
                    time.sleep(3)
                try:

                        self.get_elements(value).send_keys(test_case_data[key])
                except NoSuchElementException:
                    print("Element not found")

        self.get_elements(t4a_elements['saveButton']).click()
        self.verify_toast_message()

    def test_required_fields(self):
        """
        Test the required fields according to the payeeType
        :return:
        """
        t4a_setup = T4aSetup(self.driver)
        t4a_list = T4aList(self.driver)
        t4a_elements = t4a_setup.t4a_x_paths
        t4a_alerts = t4a_setup.t4a_alerts_xpaths
        t4a_list_elements = t4a_list.t4a_list_xpaths
        self.get_login()
        self.go_to_create_t4a()
        self.get_element_presence(t4a_elements['loadVendor'], 10)
        self.get_elements(t4a_elements['OtherInfo0']).send_keys("014")
        self.get_elements(t4a_elements['saveButton']).click()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollLength);")
        # self.get_element_presence(t4a_alerts["reflectInMasterDataRequired"], 10)
        # reflectInMasterDataAlert = t4aSetup.get_elements(t4a_alerts["reflectInMasterDataRequired"]).text
        # assert reflectInMasterDataAlert == "This field is required", "reflect in master data field is not required"
        first_name_alert = self.get_elements(t4a_alerts['firstNameRequired']).text
        assert first_name_alert == "This field is required"
        last_name_alert = self.get_elements(t4a_alerts['lastNameRequired']).text
        assert last_name_alert == "This field is required"
        sin_alert = self.get_elements(t4a_alerts['sinRequired']).text
        assert sin_alert == "This field is required"
        address_alert = self.get_elements(t4a_alerts['addressRequired']).text
        assert address_alert == "This field is required"
        city_alert = self.get_elements(t4a_alerts['cityRequired']).text
        assert city_alert == "This field is required"
        province_alert = self.get_elements(t4a_alerts['provinceRequired']).text
        assert province_alert == "This field is required"
        postcode_alert = self.get_elements(t4a_alerts['postCodeRequired']).text
        assert postcode_alert == "This field is required"
        other_code_value_alert = self.get_elements(t4a_alerts['otherInfoValueRequiredAlert']).text
        assert other_code_value_alert == "This field is required"
        self.get_elements(t4a_elements['businessRadioButton']).click()
        business_name_alert = self.get_elements(t4a_alerts['businessNameRequired']).text
        assert business_name_alert == "This field is required"
        business_number_alert = self.get_elements(t4a_alerts['businessNumberRequired']).text
        assert business_number_alert == "This field is required"

    def test_incorrect_fields_alert(self):
        """
        Testing the incorrect sin,business,postCode and email alert
        :return:
        """
        t4a_setup = T4aSetup(self.driver)
        t4a_list = T4aList(self.driver)
        t4a_elements = t4a_setup.t4a_x_paths
        t4a_alerts = t4a_setup.t4a_alerts_xpaths
        t4a_list_elements = t4a_list.t4a_list_xpaths
        self.get_login()
        self.go_to_create_t4a()
        self.get_element_presence(t4a_elements['loadVendor'], 10)
        self.get_elements(t4a_elements['sin']).send_keys("000")
        incorrect_sin = self.get_elements(t4a_alerts["sinIncorrectAlert"]).text
        assert incorrect_sin == "Social Insurance is incorrect"
        self.get_elements(t4a_elements['businessNumber']).send_keys("123")
        incorrect_business_number = self.get_elements(t4a_alerts["businessNumberIncorrectAlert"]).text
        assert incorrect_business_number == "Business Number is incorrect"
        self.get_elements(t4a_elements['email']).send_keys("Ghayur")
        incorrect_email = self.get_elements(t4a_alerts["emailAlert"]).text
        assert incorrect_email == "This field must only contain valid email"
        self.get_elements(t4a_elements['postCode']).send_keys("k9")
        incorrect_post_code = self.get_elements(t4a_alerts["postCodeIncorrectAlert"]).text
        assert incorrect_post_code == "This value is incorrect"

    @pytest.mark.skip
    def test_masking_unmasking(self):
        """Testing the masking and unmasking functionality"""
        g_credentials = Credentials.users_credentials
        dashboard_obj = Dashboard(self.driver)
        header_setup = Header(self.driver)
        t4a_setup = T4aSetup(self.driver)
        t4a_list = T4aList(self.driver)
        t4a_data = DataT4a
        header_elements = header_setup.Xpaths
        t4a_elements = t4a_setup.t4a_x_paths
        t4a_list_elements = t4a_list.t4a_list_xpaths
        dashboard_elements = dashboard_obj.dashboard_X_paths
        test_case_data = t4a_data.test_case2
        self.get_login()
        self.go_to_create_t4a()
        self.get_element_presence(t4a_elements['loadVendor'])

        for key, value in t4a_elements.items():
            if key not in ["loadVendor", "AddMore", "country", "loadSlip", "saveButton", "toastMessage", "closeToast"] \
                    and "Button" not in key:
                try:
                    self.get_elements(value).send_keys(test_case_data[key])
                except NoSuchElementException:
                    print("otherInfo element not found")
        self.get_elements(t4a_elements['saveButton']).click()
        self.get_element_presence(t4a_elements['toastMessage'], 10)
        self.driver.back()
        self.get_element_click_able(t4a_list_elements['testMask'], 10)
        self.get_elements(t4a_list_elements['testMask']).click()
        self.get_element_presence(t4a_elements['loadSlip'], 10)
        self.get_elements(t4a_elements['loadSlip']).send_keys("Com")
        checkMasking = self.get_elements(header_elements['maskButton']).text
        if checkMasking == "Unmask":
            sin_masked = self.get_elements(t4a_elements["sin"]).get_attribute("value")
            assert "**" in sin_masked, "sin number is not masked"
            email_masked = self.get_elements(t4a_elements["email"]).get_attribute("value")
            assert "**" in email_masked, "email  is not masked"
        else:
            self.get_elements(header_elements['maskButton']).click()
            sin_masked = self.get_elements(t4a_elements['sin']).get_attribute("value")
            assert "**" in sin_masked, "sin number is not masked"
            email_masked = self.get_elements(t4a_elements["email"]).get_attribute("value")
            assert "**" in email_masked, "email  is not masked"
        self.get_elements(t4a_elements["reflectInMasterData"]).send_keys("Yes")
        self.get_elements(t4a_elements["saveButton"]).click()
        self.get_element_presence(t4a_elements["toastMessage"], 10)
        self.get_elements(t4a_elements["closeToast"]).click()
        self.get_elements(header_elements['maskButton']).click()
        self.get_element_presence(header_elements['unmaskPassword'], 10)
        self.get_elements(header_elements['unmaskPassword']).send_keys(g_credentials['password'])
        self.get_elements(header_elements['verifyButton']).click()
        time.sleep(2)
        email_unmasked = self.get_elements(t4a_elements["email"]).get_attribute("value")
        assert "Ghayur@technologyelement.com" == email_unmasked, "email  is not unmasked"
        sin_masked = self.get_elements(t4a_elements["sin"]).get_attribute("value")
        assert "000-000-000" == sin_masked, "sin number is not unmasked"