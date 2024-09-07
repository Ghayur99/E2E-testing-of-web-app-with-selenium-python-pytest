"""Client screen test cases"""
import time
import pytest as pytest
from page_objects.client_list import ClientList
from page_objects.client_profile import ClientProfile
from page_objects.client_setup import ClientSetup
from page_objects.employee_setup import EmployeeSetup
from page_objects.header import Header
from test_data.client_setup_data import ClientSetupData
from test_data.employee_data import EmployeeData
from utilities.form_entity_class import FormEntity


class TestClientSetup(FormEntity):
    """
    This is the class in which all Client Setup setup test cases are defined in methods
    """
    def test_all_fields(self):
        """ TC-1
        Creating client setup with all fields and verify records
        :return:
        """
        client_list = ClientList(self.driver)
        client_list_elements = client_list.client_xpaths
        x_paths = ClientSetup.client_setup_xpath
        dropdown_xpaths = ClientSetup.drop_down_xpath
        expected_dict = ClientSetupData.all_fields_exp_data
        self.get_login_client_setup()
        self.add_client()
        self.get_element_presence(x_paths['createDate'])
        dob = x_paths['createDate']
        self.select_date(dob, "2021")
        self.fill_form_and_save(ClientSetupData.all_fields_data, ClientSetup.client_setup_xpath)
        self.verify_toast_message()
        self.navigate_sidebar_menu(menu_type='homeMenu', sub_menu_type='clientList', expand_compliance=False)
        self.unmask_data()
        time.sleep(3)
        self.get_element_click_able(client_list_elements["allClientList"])
        list_of_name = self.get_elements_in_list(client_list_elements['allClientList'])
        client_name = "Test Client (Inc)"
        self.edit_any_client_in_list(list_of_name, client_name)
        # Updating the drop down xpath so we can read the selected option in them
        ignored_fields_list = ["saveBtn", "opeProv", "abchkbox", "bcchkbox", "mbchkbox", "nbchkbox", "nlchkbox",
                               "ntchkbox", "nschkbox", "nuchkbox", "onchkbox", "pechkbox", "qcchkbox", "skchkbox",
                               "ykchkbox", "abCrossBtn", "bcCrossBtn", "mbCrossBtn", "nbCrossBtn", "nlCrossBtn",
                               "ntCrossBtn", "nsCrossBtn", "nuCrossBtn", "onCrossBtn", "peCrossBtn", "qcCrossBtn",
                               "skCrossBtn", "ykCrossBtn" "address_wizard"]
        drop_down_fields_list = ["employees", "province", "ab", "bc", "mb", "nb", "nl", "nt", "ns", "nu", "on", "pe",
                                 "qc", "sk", "yk"]
        """Comparing the t4a with expected data dict"""
        self.read_data(expected_dict, x_paths, dropdown_xpaths, ignored_fields_list, drop_down_fields_list)

    def test_mandatory_fields(self):
        """ TC-2
        Creating client setup with mandatory fields
        :return:
        """
        x_paths = ClientSetup.client_setup_xpath
        self.get_login_client_setup()
        self.add_client()
        self.get_element_click_able(x_paths['nextBtn1'])
        self.get_elements(x_paths['nextBtn1']).click()
        name_alert = self.get_elements(x_paths['legalNameAlert']).text
        assert name_alert == "This field is required"
        emp_alert = self.get_elements(x_paths['employeesAlert']).text
        assert emp_alert == "This field is required"
        am_alert = self.get_elements(x_paths['accManagerAlert']).text
        assert am_alert == "This field is required"
        bn_alert = self.get_elements(x_paths['bsnNoAlert']).text
        assert bn_alert == "This field is required"
        self.get_elements(x_paths['legalName']).send_keys("Test required fields")
        self.get_elements(x_paths['employees']).send_keys("1-10")
        self.get_elements(x_paths['accManager']).send_keys("Zahid")
        self.get_elements(x_paths['bsnNo']).send_keys("121212120RP5010")
        self.get_elements(x_paths['nextBtn1']).click()
        self.get_element_click_able(x_paths['saveBtn'])
        self.get_elements(x_paths['saveBtn']).click()
        address_alert = self.get_elements(x_paths['addressAlert']).text
        assert address_alert == "This field is required"
        city_alert = self.get_elements(x_paths['cityAlert']).text
        assert city_alert == "This field is required"
        province_alert = self.get_elements(x_paths['provinceAlert']).text
        assert province_alert == "This field is required"
        ope_alert = self.get_elements(x_paths['opeProvAlert']).text
        assert ope_alert == "This field is required"
        post_code_alert = self.get_elements(x_paths['postCodeAlert']).text
        assert post_code_alert == "This field is required"
        email_alert = self.get_elements(x_paths['emailAlert']).text
        assert email_alert == "This field is required"

    def test_wizards_with_empty_fields(self):
        """ TC-3
        Creating client setup wizards without filing any field
        :return:
        """
        x_paths = ClientSetup.client_setup_xpath
        self.get_login_client_setup()
        self.add_client()
        self.get_element_click_able(x_paths['address_wizard'])
        self.get_elements(x_paths['address_wizard']).click()

    def test_wizards_with_filling_fields(self):
        """ TC-4
        Creating client setup wizards with filing mandatory fields
        :return:
        """
        x_paths = ClientSetup.client_setup_xpath
        self.get_login_client_setup()
        self.add_client()
        self.get_element_click_able(x_paths['address_wizard'])
        self.get_elements(x_paths['address_wizard']).click()
        name_alert = self.get_elements(x_paths['legalNameAlert']).text
        assert name_alert == "This field is required"
        emp_alert = self.get_elements(x_paths['employeesAlert']).text
        assert emp_alert == "This field is required"
        am_alert = self.get_elements(x_paths['accManagerAlert']).text
        assert am_alert == "This field is required"
        bn_alert = self.get_elements(x_paths['bsnNoAlert']).text
        assert bn_alert == "This field is required"
        self.get_elements(x_paths['legalName']).send_keys("Test required fields")
        self.get_elements(x_paths['employees']).send_keys("1-10")
        self.get_elements(x_paths['accManager']).send_keys("Zahid")
        self.get_elements(x_paths['bsnNo']).send_keys("121212120RP5010")
        self.get_elements(x_paths['address_wizard']).click()
        self.get_element_click_able(x_paths['saveBtn'])
        self.get_elements(x_paths['saveBtn']).click()
        address_alert = self.get_elements(x_paths['addressAlert']).text
        assert address_alert == "This field is required"

    def test_duplication_client(self):
        """ TC-6
        Duplication of client with same name
        :return:
        """
        self.get_login_client_setup()
        self.add_client()
        self.fill_form_and_save(ClientSetupData.duplication_data, ClientSetup.client_setup_xpath)
        self.verify_toast_message()
        self.navigate_sidebar_menu(menu_type='homeMenu', sub_menu_type='clientList', expand_compliance=False)
        self.add_client()
        self.fill_form_and_save(ClientSetupData.duplication_data, ClientSetup.client_setup_xpath)
        self.verify_toast_message("duplication")

    def test_special_characters(self):
        """ TC-8, TC-11
        Creating client setup with special chars, verify that records and delete single record from client list
        :return:
        """
        client_list = ClientList(self.driver)
        client_list_elements = client_list.client_xpaths
        x_paths = ClientSetup.client_setup_xpath
        dropdown_xpaths = ClientSetup.drop_down_xpath
        expected_dict = ClientSetupData.special_chars_exp_data
        self.get_login_client_setup()
        self.add_client()
        self.get_element_presence(x_paths['createDate'])
        dob = x_paths['createDate']
        self.select_date(dob, "2021")
        self.fill_form_and_save(ClientSetupData.special_chars_data, ClientSetup.client_setup_xpath)
        self.verify_toast_message()
        self.navigate_sidebar_menu(menu_type='homeMenu', sub_menu_type='clientList', expand_compliance=False)
        self.unmask_data()
        time.sleep(3)
        self.get_element_click_able(client_list_elements["allClientList"])
        list_of_name = self.get_elements_in_list(client_list_elements['allClientList'])
        client_name = "$pecial & ch@rs (#)"
        self.edit_any_client_in_list(list_of_name, client_name)
        # Updating the drop down xpath so we can read the selected option in them
        ignored_fields_list = ["saveBtn", "opeProv", "Abchkbox", "bcchkbox", "mbchkbox", "nbchkbox", "nlchkbox",
                               "ntchkbox", "nschkbox", "nuchkbox", "onchkbox", "pechkbox", "qcchkbox", "skchkbox",
                               "ykchkbox", "abCrossBtn", "bcCrossBtn", "mbCrossBtn", "nbCrossBtn", "nlCrossBtn",
                               "ntCrossBtn", "nsCrossBtn", "nuCrossBtn", "onCrossBtn", "peCrossBtn", "qcCrossBtn",
                               "skCrossBtn", "ykCrossBtn" "address_wizard"]
        drop_down_fields_list = ["employees", "province", "ab", "bc", "mb", "nb", "nl", "nt", "ns", "nu", "on", "pe",
                                 "qc", "sk", "yk"]
        """Comparing the t4a with expected data dict"""
        self.read_data(expected_dict, x_paths, dropdown_xpaths, ignored_fields_list, drop_down_fields_list)
        self.navigate_sidebar_menu(menu_type='homeMenu', sub_menu_type='clientList', expand_compliance=False)
        time.sleep(3)
        self.get_element_click_able(client_list_elements["allClientList"])
        list_of_name = self.get_elements_in_list(client_list_elements['allClientList'])
        client_name = "$pecial & ch@rs (#)"
        self.delete_any_record_in_list(list_of_name, client_name)
        # self.get_element_click_able(client_list_elements["listCheckBox"])
        # self.get_elements(client_list_elements["listCheckBox"]).click()
        # self.get_element_click_able(client_list_elements["listDeleteBtn"])
        # self.get_elements(client_list_elements["listDeleteBtn"]).click()
        self.get_element_click_able(client_list_elements["confirmBtnOk"])
        self.get_elements(client_list_elements["confirmBtnOk"]).click()
        self.verify_toast_message('delete')

    def test_french_characters(self):
        """ TC-7
        Creating client setup with french characters
        :return:
        """
        client_list = ClientList(self.driver)
        client_list_elements = client_list.client_xpaths
        x_paths = ClientSetup.client_setup_xpath
        dropdown_xpaths = ClientSetup.drop_down_xpath
        expected_dict = ClientSetupData.french_chars_exp_data
        self.get_login_client_setup()
        self.add_client()
        self.get_element_presence(x_paths['createDate'])
        dob = x_paths['createDate']
        self.select_date(dob, "2021")
        self.fill_form_and_save(ClientSetupData.french_chars_data, ClientSetup.client_setup_xpath)
        self.verify_toast_message()
        self.navigate_sidebar_menu(menu_type='homeMenu', sub_menu_type='clientList', expand_compliance=False)
        self.unmask_data()
        time.sleep(3)
        self.get_element_click_able(client_list_elements["allClientList"])
        list_of_client_name = self.get_elements_in_list(client_list_elements['allClientList'])
        client_name = "Frénçh chars dâta (înc)"
        self.edit_any_client_in_list(list_of_client_name, client_name)
        # Updating the drop down xpath so we can read the selected option in them
        ignored_fields_list = ["saveBtn", "opeProv", "Abchkbox", "bcchkbox", "mbchkbox", "nbchkbox", "nlchkbox",
                               "ntchkbox", "nschkbox", "nuchkbox", "onchkbox", "pechkbox", "qcchkbox", "skchkbox",
                               "ykchkbox", "abCrossBtn", "bcCrossBtn", "mbCrossBtn", "nbCrossBtn", "nlCrossBtn",
                               "ntCrossBtn", "nsCrossBtn", "nuCrossBtn", "onCrossBtn", "peCrossBtn", "qcCrossBtn",
                               "skCrossBtn", "ykCrossBtn" "address_wizard"]
        drop_down_fields_list = ["employees", "province", "ab", "bc", "mb", "nb", "nl", "nt", "ns", "nu", "on", "pe",
                                 "qc", "sk", "yk"]
        """Comparing the t4a with expected data dict"""
        self.read_data(expected_dict, x_paths, dropdown_xpaths, ignored_fields_list, drop_down_fields_list)

    def test_business_number_validation(self):
        """ TC-10
        Verify the business number validation
        :return:
        """
        x_paths = ClientSetup.client_setup_xpath
        self.get_login_client_setup()
        self.add_client()
        self.get_element_presence(x_paths['bsnNo'])
        self.get_elements(x_paths['bsnNo']).send_keys("4444444")
        business_no_alert = self.get_elements(x_paths['bsnNoIncorrectAlert']).text
        assert business_no_alert == "Business no is incorrect"
        self.get_elements(x_paths['reiNo']).send_keys("3333333")
        business_no_alert = self.get_elements(x_paths['reiNoIncorrectAlert']).text
        assert business_no_alert == "Reduce El Account no is incorrect"

    def test_email_validation(self):
        """ TC-9
        Verify the email validation
        :return:
        """
        x_paths = ClientSetup.client_setup_xpath
        self.get_login_client_setup()
        self.add_client()
        self.get_element_presence(x_paths['legalName'])
        self.get_elements(x_paths['legalName']).send_keys("Test Email")
        self.get_elements(x_paths['employees']).send_keys("1-10")
        self.get_elements(x_paths['accManager']).send_keys("Test")
        self.get_elements(x_paths['bsnNo']).send_keys("121212120RP0000")
        self.get_elements(x_paths['nextBtn1']).click()
        self.get_element_presence(x_paths['email'])
        self.get_elements(x_paths['email']).send_keys("3333333")
        email_alert = self.get_elements(x_paths['emailIncorrectAlert']).text
        assert email_alert == "This field must only contain valid email"

    def test_delete_client_has_any_data(self):
        """ TC-12
        Verify the delete functionality if client has any data
        :return:
        """
        client_list = ClientList(self.driver)
        client_list_elements = client_list.client_xpaths
        self.get_login_client_setup()
        self.add_client()
        self.fill_form_and_save(ClientSetupData.delete_client_data, ClientSetup.client_setup_xpath)
        self.verify_toast_message()
        self.navigate_sidebar_menu(menu_type='homeMenu', sub_menu_type='clientList', expand_compliance=False)
        time.sleep(4)
        self.get_element_click_able(client_list_elements["allClientList"])
        client_list = self.get_elements_in_list(client_list_elements["allClientList"])
        client = "Test Delete Client (Corporation)"
        self.click_on_any_element_in_list(client_list, client)
        self.go_to_add_employee()
        self.fill_form_and_save(EmployeeData.all_fields_test_data, EmployeeSetup.emp_form_xpath,
                                before_submit_action=True, before_action_element=EmployeeSetup.fillingLbl,
                                save_btn=EmployeeSetup.saveBtn)
        self.verify_toast_message()
        self.navigate_sidebar_menu(menu_type='homeMenu', sub_menu_type='clientList', expand_compliance=False)
        time.sleep(3)
        self.get_element_click_able(client_list_elements["allClientList"])
        list_of_name = self.get_elements_in_list(client_list_elements['allClientList'])
        client_name = "Test Delete Client (Corporation)"
        self.delete_any_record_in_list(list_of_name, client_name)
        self.get_element_click_able(client_list_elements["confirmBtnOk"])
        self.get_elements(client_list_elements["confirmBtnOk"]).click()
        self.verify_toast_message('client_delete')

    def test_update_client_from_setup(self):
        """ TC-13
        Verify the edit record from client setup
        :return:
        """
        # TODO: This test will be failed, there is bug in that case
        client_list = ClientList(self.driver)
        client_list_elements = client_list.client_xpaths
        x_paths = ClientSetup.client_setup_xpath
        dropdown_xpaths = ClientSetup.drop_down_xpath
        expected_dict = ClientSetupData.after_update_exp_data
        self.get_login_client_setup()
        self.add_client()
        self.get_element_presence(x_paths['createDate'])
        dob = x_paths['createDate']
        self.select_date(dob, "2021")
        self.fill_form_and_save(ClientSetupData.before_update_data, ClientSetup.client_setup_xpath)
        self.verify_toast_message()
        self.navigate_sidebar_menu(menu_type='homeMenu', sub_menu_type='clientList', expand_compliance=False)
        self.unmask_data()
        time.sleep(3)
        self.get_element_click_able(client_list_elements["allClientList"])
        list_of_name = self.get_elements_in_list(client_list_elements['allClientList'])
        client_name = "Client before update (Inc)"
        self.edit_any_client_in_list(list_of_name, client_name)
        self.update_info_of_any_form(ClientSetupData.after_update_data, ClientSetup.client_setup_xpath,
                                     ClientSetup.setup_drop_down_list)
        self.verify_toast_message("update")
        self.navigate_sidebar_menu(menu_type='homeMenu', sub_menu_type='clientList', expand_compliance=False)
        time.sleep(8)
        self.get_element_click_able(client_list_elements["allClientList"])
        list_of_name = self.get_elements_in_list(client_list_elements['allClientList'])
        client_name = "After update (Corporation)"
        self.edit_any_client_in_list(list_of_name, client_name)
        # Updating the drop down xpath so we can read the selected option in them
        ignored_fields_list = ["saveBtn", "opeProv", "abchkbox", "bcchkbox", "mbchkbox", "nbchkbox", "nlchkbox",
                               "ntchkbox", "nschkbox", "nuchkbox", "onchkbox", "pechkbox", "qcchkbox", "skchkbox",
                               "ykchkbox", "abCrossBtn", "bcCrossBtn", "mbCrossBtn", "nbCrossBtn", "nlCrossBtn",
                               "ntCrossBtn", "nsCrossBtn", "nuCrossBtn", "onCrossBtn", "peCrossBtn", "qcCrossBtn",
                               "skCrossBtn", "ykCrossBtn" "address_wizard", "bc", "mb", "nb", "nl", "nt", "ns", "nu",
                               "on", "pe", "qc", "sk", "yk", ]
        drop_down_fields_list = ["employees", "province", "ab", "bc", "mb", "nb", "nl", "nt", "ns", "nu", "on", "pe",
                                 "qc", "sk", "yk"]
        """Comparing the t4a with expected data dict"""
        self.read_data(expected_dict, x_paths, dropdown_xpaths, ignored_fields_list, drop_down_fields_list)

    def test_verify_client_from_my_profile(self):
        """ TC-14, TC-15
        Verify the record from my profile screen, update that record, verify from client setup screen
        :return:
        """
        # TODO: This test will be failed, there is bug in that case
        client_list = ClientList(self.driver)
        client_list_elements = client_list.client_xpaths
        header_setup = Header(self.driver)
        header_elements = header_setup.Xpaths
        client_profile = ClientProfile(self.driver)
        profile_elements = client_profile.x_paths
        x_paths_profile = ClientProfile.x_paths
        dropdown_xpaths_profile = ClientProfile.drop_down_xpath
        expected_dict_profile = ClientSetupData.my_profile_exp_data
        x_paths_client = ClientSetup.client_setup_xpath
        dropdown_xpaths_client = ClientSetup.drop_down_xpath
        expected_dict_client = ClientSetupData.after_update_on_client_exp_data
        self.get_login_client_setup()
        self.add_client()
        self.get_element_presence(x_paths_client['createDate'])
        dob = x_paths_client['createDate']
        self.select_date(dob, "2021")
        self.fill_form_and_save(ClientSetupData.my_profile_data, ClientSetup.client_setup_xpath)
        self.verify_toast_message()
        self.navigate_sidebar_menu(menu_type='homeMenu', sub_menu_type='clientList', expand_compliance=False)
        time.sleep(4)
        self.get_element_click_able(client_list_elements["allClientList"])
        client_list = self.get_elements_in_list(client_list_elements["allClientList"])
        client = "Client Profile (LTD)"
        self.click_on_any_element_in_list(client_list, client)
        self.get_element_click_able(header_elements["accountOptions"])
        self.get_elements(header_elements["accountOptions"]).click()
        self.get_element_click_able(header_elements["profile"])
        self.get_elements(header_elements["profile"]).click()
        time.sleep(3)
        self.unmask_data()
        time.sleep(3)
        self.get_element_presence(profile_elements["registrationNo"])
        # Updating the drop down xpath so we can read the selected option in them
        ignored_fields_list = ["saveBtn", "opeProv", "abchkbox", "listOfPoes", "abCrossBtn", "bcCrossBtn",
                               "mbCrossBtn", "nbCrossBtn", "nlCrossBtn", "ntCrossBtn", "nsCrossBtn", "nuCrossBtn",
                               "onCrossBtn", "peCrossBtn", "qcCrossBtn", "skCrossBtn", "ykCrossBtn"]
        drop_down_fields_list = ["employees", "province", "ab", "bc", "mb", "nb", "nl", "nt", "ns", "nu", "on", "pe",
                                 "qc", "sk", "yk"]
        """Comparing with expected data dict"""
        self.read_data(expected_dict_profile, x_paths_profile, dropdown_xpaths_profile, ignored_fields_list,
                       drop_down_fields_list)
        time.sleep(4)
        # update my profile screen
        self.get_element_presence(x_paths_profile['creationDate'])
        dob = x_paths_profile['creationDate']
        self.select_date(dob, "2021")
        self.update_info_of_any_form(ClientSetupData.update_my_profile_data, ClientProfile.x_paths,
                                     ClientProfile.setup_drop_down_list)
        self.verify_toast_message("update")
        self.navigate_sidebar_menu(menu_type='homeMenu', sub_menu_type='clientList', expand_compliance=False)
        time.sleep(6)
        self.get_element_click_able(client_list_elements["allClientList"])
        list_of_name = self.get_elements_in_list(client_list_elements['allClientList'])
        client_name = "Updated Client Profile (PVT LTD)"
        self.edit_any_client_in_list(list_of_name, client_name)
        # read data from client setup screen
        self.get_element_presence(x_paths_client["registrationNo"])
        # Updating the drop down xpath so we can read the selected option in them
        ignored_fields_list = ["saveBtn", "opeProv", "abchkbox", "bcchkbox", "mbchkbox", "nbchkbox", "nlchkbox",
                               "ntchkbox", "nschkbox", "nuchkbox", "onchkbox", "pechkbox", "qcchkbox", "skchkbox",
                               "ykchkbox", "abCrossBtn", "bcCrossBtn", "mbCrossBtn", "nbCrossBtn", "nlCrossBtn",
                               "ntCrossBtn", "nsCrossBtn", "nuCrossBtn", "onCrossBtn", "peCrossBtn", "qcCrossBtn",
                               "skCrossBtn", "ykCrossBtn" "address_wizard"]
        drop_down_fields_list = ["employees", "province", "ab", "bc", "mb", "nb", "nl", "nt", "ns", "nu", "on", "pe",
                                 "qc", "sk", "yk"]
        """Comparing with expected data dict"""
        self.read_data(expected_dict_client, x_paths_client, dropdown_xpaths_client, ignored_fields_list,
                       drop_down_fields_list)
