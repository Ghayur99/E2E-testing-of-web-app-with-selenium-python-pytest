"""Users screen test cases"""
import time

import pytest
from selenium.webdriver import ActionChains
from page_objects.client_list import ClientList
from page_objects.users import InviteUsers
from test_data.users_data import InviteUsersData
from utilities.form_entity_class import FormEntity


class TestInviteUsersSetup(FormEntity):
    """
    This is the class in which all invite user test cases are defined in methods
    """
    def test_all_fields(self):
        """ TC-1, TC-6
        In this test case we are testing with all fields and Assigning the client to the user which is already
         registered with tax slip
        :return:
        """
        self.get_login()
        self.go_to_invite_user()
        self.fill_form_and_save(InviteUsersData.all_fields_data, InviteUsers.users_xpath)
        self.verify_toast_message("client_invitation")

    def test_assign_client_which_is_not_register(self):
        """ TC-5
        Assigning the client to the user which is not registered with tax slip
        :return:
        """
        self.get_login()
        self.go_to_invite_user()
        self.fill_form_and_save(InviteUsersData.assign_client_which_is_not_register_data, InviteUsers.users_xpath)
        self.verify_toast_message("client_invitation")

    def test_required_fields(self):
        """TC-2
        In this test case we are testing mandatory fields
        :return:
        """
        user_setup = InviteUsers(self.driver)
        user_elements = user_setup.users_xpath
        self.get_login()
        self.go_to_invite_user()
        self.get_element_presence(user_elements["saveBtn"])
        self.get_elements(user_elements["saveBtn"]).click()
        first_name_alert = self.get_elements(user_elements['firstNameAlert']).text
        assert first_name_alert == "This field is required"
        last_name_alert = self.get_elements(user_elements['lastNameAlert']).text
        assert last_name_alert == "This field is required"
        email_alert = self.get_elements(user_elements['emailAlert']).text
        assert email_alert == "This field is required"
        role_alert = self.get_elements(user_elements['rolesDropDownAlert']).text
        assert role_alert == "This field is required"
        time_profile_alert = self.get_elements(user_elements['timeProfileDropDownAlert']).text
        assert time_profile_alert == "This field is required"

    def test_email_validation(self):
        """ TC-4
        In this test case we are testing validation of email
        :return:
        """
        invite_user_setup = InviteUsers(self.driver)
        x_paths = invite_user_setup.users_xpath
        self.get_login()
        self.go_to_invite_user()
        self.get_element_presence(x_paths["email"])
        self.get_elements(x_paths["email"]).send_keys("777")
        email_alert = self.get_elements(x_paths['emailIncorrectAlert']).text
        assert email_alert == "This field must only contain valid email"

    def test_verify_client_toast(self):
        self.get_login_client_setup()
        self.go_to_invite_user_via_client_list()
        self.fill_form_and_save(InviteUsersData.verify_client_toast_data, InviteUsers.users_xpath)
        self.verify_toast_message("client_invite_user")

    def test_client_level_user(self):
        """ TC-9
        To verify that client appears on Invite user screen if user open the invite user screen in the client level
        :return:
        """
        client_list = ClientList(self.driver)
        client_list_elements = client_list.client_xpaths
        user_setup = InviteUsers(self.driver)
        user_elements = user_setup.user_read_data
        self.get_login_client_setup()
        time.sleep(4)
        self.get_element_click_able(client_list_elements["allClientList"])
        client_list = self.get_elements_in_list(client_list_elements["allClientList"])
        client = "Test Delete Client (Corporation)"
        self.click_on_any_element_in_list(client_list, client)
        self.go_to_invite_user()
        self.get_element_presence(user_elements["clientNameLabel"])
        client_name = self.get_elements(user_elements['clientNameLabel']).text
        assert client_name == "Test Delete Client"

    @pytest.mark.skip
    # Reset button functionality is not working
    def test_reset_button_functionality(self):
        """ TC-11
        To verify the reset button functionality
        :return:
        """
        user_setup = InviteUsers(self.driver)
        user_elements = user_setup.users_xpath
        dropdown_xpaths = InviteUsers.drop_down_xpath
        expected_dict = InviteUsersData.reset_fields_exp_data
        self.get_login()
        self.go_to_invite_user()
        self.fill_form_and_save(InviteUsersData.reset_fields_data, InviteUsers.users_xpath)
        # Updating the drop down xpath so we can read the selected option in them
        ignored_fields_list = ["saveBtn", ]
        drop_down_fields_list = ["adminChkbox", "adminProfileChkbox"]
        """Comparing the t4a with expected data dict"""
        self.read_data(expected_dict, user_elements, dropdown_xpaths, ignored_fields_list, drop_down_fields_list)

    def test_client_list_level_users(self):
        """ TC-10
        To verify that existing clients on client list screen with clients appear on invite user screen
        (user will open 'Invite user' screen via client list screen)
        :return:
        """
        company_client_list = []
        invite_user_clients = []
        client_list = ClientList(self.driver)
        client_list_elements = client_list.client_xpaths
        user_setup = InviteUsers(self.driver)
        user_elements = user_setup.user_read_data
        self.get_login_client_setup()
        time.sleep(4)
        # client names on client list
        element_list = self.get_elements_in_list(client_list_elements["allClientList"])
        for element in element_list:
            element_name = element.text
            company_client_list.append(element_name)
        self.go_to_invite_user_via_client_list()
        time.sleep(2)
        # client names on invite user
        clients_list = self.get_elements_in_list(user_elements["allUserList"])
        for clients in clients_list:
            client_name = clients.text
            invite_user_clients.append(client_name)
        # invite_user_clients.append("ABC")
        company_client_list.sort()
        invite_user_clients.sort()
        if company_client_list == invite_user_clients:
            return "Equals"
        else:
            pytest.fail("The Client does not match")

    def test_multi_assign_user_from_client_list(self):
        """ TC-8
        To verify that user invite multiple clients through client list screen
        :return:
        """
        user_setup = InviteUsers(self.driver)
        user_elements = user_setup.user_read_data
        self.get_login_client_setup()
        self.go_to_invite_user_via_client_list()
        self.get_element_presence(user_elements["firstName"])
        self.get_elements(user_elements["firstName"]).send_keys("Ghayur")
        self.get_elements(user_elements["lastName"]).send_keys("Butt")
        self.get_elements(user_elements["email"]).send_keys("Ghayur@websential.ca")
        self.get_element_presence(user_elements["firstClientChkbox"])
        self.get_elements(user_elements["firstClientChkbox"]).click()
        self.get_element_click_able(user_elements["rolesDropDown"])
        self.get_elements(user_elements["rolesDropDown"]).click()
        self.get_element_click_able(user_elements["adminChkbox"])
        self.get_elements(user_elements["adminChkbox"]).click()
        self.get_element_click_able(user_elements["timeProfileDropDown"])
        self.get_elements(user_elements["timeProfileDropDown"]).click()
        self.get_element_click_able(user_elements["adminProfileChkbox"])
        self.get_elements(user_elements["adminProfileChkbox"]).click()
        self.get_elements(user_elements["secondClientChkbox"]).click()
        self.get_element_click_able(user_elements["secondRolesDropDown"])
        self.get_elements(user_elements["secondRolesDropDown"]).click()
        time.sleep(3)
        user_setup.actions = ActionChains(self.driver)
        user_setup.actions.click(self.get_elements(user_elements["thirdRoleChkbox"])).perform()
        # self.get_element_click_able(user_elements["thirdRoleChkbox"])
        # self.get_elements(user_elements["thirdRoleChkbox"]).click()
        self.get_element_click_able(user_elements["secondTimeProfileDropDown"])
        self.get_elements(user_elements["secondTimeProfileDropDown"]).click()
        self.get_element_click_able(user_elements["secondTimeProfile"])
        self.get_elements(user_elements["secondTimeProfile"]).click()
        self.get_elements(user_elements["thirdClientChkbox"]).click()
        self.get_element_click_able(user_elements["thirdRolesDropDown"])
        self.get_elements(user_elements["thirdRolesDropDown"]).click()
        self.get_element_click_able(user_elements["fourthRoleChkbox"])
        self.get_elements(user_elements["fourthRoleChkbox"]).click()
        self.get_element_click_able(user_elements["thirdTimeProfileDropDown"])
        self.get_elements(user_elements["thirdTimeProfileDropDown"]).click()
        self.get_element_click_able(user_elements["secondTimeProfile"])
        self.get_elements(user_elements["secondTimeProfile"]).click()
        self.get_elements(user_elements["saveBtn"]).click()
