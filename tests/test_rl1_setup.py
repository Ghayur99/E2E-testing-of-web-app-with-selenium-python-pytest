"""Test cases for RL_1 setup screen """
import time
import pytest
from selenium.common.exceptions import NoSuchElementException
from test_data.credentials import Credentials
from test_data.rl1_data import DataRl1
from utilities.base_class import BaseClass
from page_objects.dashboard import Dashboard
from page_objects.header import Header
from page_objects.rl1_list import Rl1List
from page_objects.rl1_setup import Rl1Setup


class TestRl1Setup(BaseClass):
    """
    This is the class in which all the Rl_1 setup test cases are defined in methods
    """

    # This test case is skipped because of the Bug in Rl-1 setup foam  BugID# #3da29b
    @pytest.mark.skip
    def test_all_fields_filled_rl1(self):
        """
        In this test case we are testing the RL-1 slip foam with all fields filled
        :return:
        """
        dashboard_obj = Dashboard(self.driver)
        rl1_setup = Rl1Setup(self.driver)
        rl1_list = Rl1List(self.driver)
        rl1_data = DataRl1
        rl1_elements = rl1_setup.rl1_x_paths
        rl1_list_elements = rl1_list.rl1_list_xpaths
        dashboard_elements = dashboard_obj.dashboard_X_paths
        test_case_data = rl1_data.testCase1
        self.get_login()
        self.get_element_presence(dashboard_elements['rl1'], 10)
        self.get_elements(dashboard_elements['rl1']).click()
        self.get_element_presence(rl1_list_elements['createSlip'], 10)
        self.get_elements(rl1_list_elements['createSlip']).click()
        self.get_element_presence(rl1_elements['loadEmployee'], 10)

        for key, value in rl1_elements.items():
            if key not in ["loadEmployee", "AddMore", "country", "loadSlip", "saveButton", "toastMessage",
                           "dateOfBirth", "closeToast"] \
                    and "Button" not in key:
                try:
                    self.get_elements(value).send_keys(test_case_data[key])
                except NoSuchElementException:
                    print("Element not found")

        self.get_elements(rl1_elements['saveButton']).click()
        self.verify_toast_message()

    def test_required_fields_rl1(self):
        """
        Test the required fields
        :return:
        """
        dashboard_obj = Dashboard(self.driver)
        rl1_setup = Rl1Setup(self.driver)
        rl1_list = Rl1List(self.driver)
        rl1_elements = rl1_setup.rl1_x_paths
        rl1_list_elements = rl1_list.rl1_list_xpaths
        dashboard_elements = dashboard_obj.dashboard_X_paths
        rl1_alerts = rl1_setup.rl1_alerts_xpaths
        self.get_login()
        self.get_element_presence(dashboard_elements['rl1'], 10)
        self.get_elements(dashboard_elements['rl1']).click()
        self.get_element_presence(rl1_list_elements['createSlip'], 10)
        self.get_elements(rl1_list_elements['createSlip']).click()
        self.get_element_presence(rl1_elements['loadEmployee'], 10)
        self.get_elements(rl1_elements['OtherInfo0']).send_keys("A-1")
        self.get_elements(rl1_elements['saveButton']).click()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollLength);")
        # self.get_element_presence(t4a_alerts["reflectInMasterDataRequired"], 10)
        # reflectInMasterDataAlert = t4aSetup.get_elements(t4a_alerts["reflectInMasterDataRequired"]).text
        # assert reflectInMasterDataAlert == "This field is required", "reflect in master data field is not required"
        first_name_alert = self.get_elements(rl1_alerts['firstNameRequired']).text
        assert first_name_alert == "This field is required"
        last_name_alert = self.get_elements(rl1_alerts['lastNameRequired']).text
        assert last_name_alert == "This field is required"
        address_alert = self.get_elements(rl1_alerts['addressRequired']).text
        assert address_alert == "This field is required"
        city_alert = self.get_elements(rl1_alerts['cityRequired']).text
        assert city_alert == "This field is required"
        province_alert = self.get_elements(rl1_alerts['provinceRequired']).text
        assert province_alert == "This field is required"
        post_code_alert = self.get_elements(rl1_alerts['postCodeRequired']).text
        assert post_code_alert == "This field is required"
        other_code_value_alert = self.get_elements(rl1_alerts['otherInfoValueRequiredAlert']).text
        assert other_code_value_alert == "This field is required"

    def test_incorrect_fields_alert_rl1(self):
        """
        Testing the incorrect sin,business,postCode and email alert
        :return:
        """
        dashboard_obj = Dashboard(self.driver)
        rl1_setup = Rl1Setup(self.driver)
        rl1_list = Rl1List(self.driver)
        rl1_elements = rl1_setup.rl1_x_paths
        rl1_list_elements = rl1_list.rl1_list_xpaths
        dashboard_elements = dashboard_obj.dashboard_X_paths
        rl1_alerts = rl1_setup.rl1_alerts_xpaths
        self.get_login()
        self.get_element_presence(dashboard_elements['rl1'], 10)
        self.get_elements(dashboard_elements['rl1']).click()
        self.get_element_presence(rl1_list_elements['createSlip'], 10)
        self.get_elements(rl1_list_elements['createSlip']).click()
        self.get_element_presence(rl1_elements['loadEmployee'], 10)
        self.get_elements(rl1_elements['sin']).send_keys("000")
        incorrect_sin = self.get_elements(rl1_alerts["sinIncorrectAlert"]).text
        assert incorrect_sin == "Social Insurance is incorrect"
        self.get_elements(rl1_elements['email']).send_keys("Ghayur")
        incorrect_email = self.get_elements(rl1_alerts["emailAlert"]).text
        assert incorrect_email == "This field must only contain valid email"
        # rl1Setup.get_elements(rl1_elements['postCode']).send_keys("k0")
        # self.get_element_presence(rl1_alerts["postCodeIncorrectAlert"], 10)
        # incorrectPostCode = rl1Setup.get_elements(rl1_alerts["postCodeIncorrectAlert"]).text
        # assert incorrectPostCode == "This value is incorrect"

    @pytest.mark.skip
    def test_masking_unmasking_rl1(self):
        """Testing the masking and unmasking functionality"""

        dashboard_obj = Dashboard(self.driver)
        header_setup = Header(self.driver)
        rl1_setup = Rl1Setup(self.driver)
        rl1_list = Rl1List(self.driver)
        rl1_elements = rl1_setup.rl1_x_paths
        rl1_list_elements = rl1_list.rl1_list_xpaths
        header_elements = header_setup.Xpaths
        dashboard_elements = dashboard_obj.dashboard_X_paths
        g_credentials = Credentials.users_credentials
        test_case_data = DataRl1.testCase2
        self.get_login()
        self.get_element_presence(dashboard_elements['rl1'], 10)
        self.get_elements(dashboard_elements['rl1']).click()
        self.get_element_presence(rl1_list_elements['createSlip'], 10)
        self.get_elements(rl1_list_elements['createSlip']).click()
        self.get_element_presence(rl1_elements['loadEmployee'], 10)
        # time.sleep(4)
        # dob = rl1Setup.get_elements(rl1_elements['dateOfBirth'])
        # self.driver.execute_script("arguments[0].value = arguments[1]", dob, '2008-02-06')
        for key, value in rl1_elements.items():
            if key not in ["loadEmployee", "AddMore", "country", "loadSlip", "saveButton", "toastMessage",
                           "dateOfBirth", "closeToast"] \
                    and "Button" not in key:
                try:
                    self.get_elements(value).send_keys(test_case_data[key])
                except NoSuchElementException:
                    print("otherInfo element not found")

        self.get_elements(rl1_elements['saveButton']).click()
        self.get_element_presence(rl1_elements['toastMessage'], 10)
        self.driver.back()
        self.get_element_click_able(rl1_list_elements['testMask'], 10)
        self.get_elements(rl1_list_elements['testMask']).click()
        self.get_element_presence(rl1_elements['loadSlip'], 10)
        self.get_elements(rl1_elements['loadSlip']).send_keys("Com")
        checkMasking = self.get_elements(header_elements['maskButton']).text
        if checkMasking == "Unmask":
            sin_masked = self.get_elements(rl1_elements["sin"]).get_attribute("value")
            assert "**" in sin_masked, "sin number is not masked"
            email_masked = self.get_elements(rl1_elements["email"]).get_attribute("value")
            assert "**" in email_masked, "email  is not masked"
        else:
            self.get_elements(header_elements['maskButton']).click()
            sin_masked = self.get_elements(rl1_elements['sin']).get_attribute("value")
            assert "**" in sin_masked, "sin number is not masked"
            email_masked = self.get_elements(rl1_elements["email"]).get_attribute("value")
            assert "**" in email_masked, "email  is not masked"
        self.get_elements(rl1_elements["reflectInMasterData"]).send_keys("Yes")
        self.get_elements(rl1_elements["saveButton"]).click()
        self.get_element_presence(rl1_elements["toastMessage"], 10)
        self.get_elements(rl1_elements["closeToast"]).click()
        self.get_elements(header_elements['maskButton']).click()
        self.get_element_presence(header_elements['unmaskPassword'], 10)
        self.get_elements(header_elements['unmaskPassword']).send_keys(g_credentials['password'])
        self.get_elements(header_elements['verifyButton']).click()
        time.sleep(2)
        email_unmasked = self.get_elements(rl1_elements["email"]).get_attribute("value")
        assert "Ghayur@technologyelement.com" == email_unmasked, "email  is not unmasked"
        sin_masked = self.get_elements(rl1_elements["sin"]).get_attribute("value")
        assert "000-000-000" == sin_masked, "sin number is not unmasked"
