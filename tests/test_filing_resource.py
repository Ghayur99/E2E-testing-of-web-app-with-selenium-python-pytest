"""Filing Resource test cases"""
import time
import pytest as pytest
from page_objects.filing_resource_list import FilingResourceList
from page_objects.filing_resource_setup import FilingResourceSetup
from test_data.filing_resource_data import FilingResourceData
from utilities.form_entity_class import FormEntity


class TestFilingResourceSetup(FormEntity):
    """
    This is the class in which Filing Resource setup and list test cases are defined in methods
    """
    def test_create_filing_resource_all_fields(self):
        """TC-1
        In this test case we are testing filing resources with all fields
        :return:
        """
        filing_resource_list = FilingResourceList(self.driver)
        filing_resource_list_elements = filing_resource_list.X_paths
        filing_resource_setup = FilingResourceSetup(self.driver)
        x_paths = filing_resource_setup.X_paths
        dropdown_xpaths = FilingResourceSetup.drop_down_xpath
        expected_dict = FilingResourceData.all_fields_exp_data
        self.get_login()
        self.navigate_sidebar_menu(main_menu="peopleMenu", sub_menu_type="filingResourceMenu", expand_parent=False)
        self.get_element_click_able(filing_resource_list_elements["createButton"])
        self.get_elements(filing_resource_list_elements["createButton"]).click()
        self.fill_form_and_save(FilingResourceData.all_fields_data, FilingResourceSetup.X_paths)
        self.verify_toast_message()
        self.unmask_data()
        self.navigate_sidebar_menu(main_menu="peopleMenu", sub_menu_type="filingResourceMenu", expand_parent=False)
        self.get_element_click_able(filing_resource_list_elements["allFRList"])
        fr_list = self.get_elements_in_list(filing_resource_list_elements["allFRList"])
        fr = "Haroon"
        self.click_on_any_element_in_list(fr_list, fr)
        self.get_element_presence(x_paths["effectiveFrom"])
        # Updating the drop down xpath so we can read the selected option in them
        ignored_fields_list = ["saveBtn", "resetBtn", "roleField", "issuerchkbox", "transmitterchkbox", "contactchkbox"]
        drop_down_fields_list = ["contactPerson", "Issuer", "transmitter", "effectiveFrom", "rl1Type", "province"]
        """Comparing the t4a with expected data dict"""
        self.read_data(expected_dict, x_paths, dropdown_xpaths, ignored_fields_list, drop_down_fields_list)

    def test_incorrect_alerts(self):
        """TC-7, TC-8, TC-9, TC-10
        In this test case we are testing validation of SIN, CRA TransmitterNo, RQ TransmitterNo and email
        :return:
        """
        filing_resource_list = FilingResourceList(self.driver)
        filing_resource_list_elements = filing_resource_list.X_paths
        filing_resource_setup = FilingResourceSetup(self.driver)
        x_paths = filing_resource_setup.X_paths
        self.get_login()
        self.navigate_sidebar_menu(main_menu="peopleMenu", sub_menu_type="filingResourceMenu", expand_parent=False)
        self.get_element_click_able(filing_resource_list_elements["createButton"])
        self.get_elements(filing_resource_list_elements["createButton"]).click()
        self.get_element_click_able(x_paths["roleField"])
        self.get_elements(x_paths['roleField']).click()
        self.get_element_click_able(x_paths["issuerchkbox"])
        self.get_elements(x_paths['issuerchkbox']).click()
        self.get_elements(x_paths['transmitterchkbox']).click()
        self.get_elements(x_paths["ownerSin1"]).send_keys("777")
        owner_sin1_alert = self.get_elements(x_paths['ownerSin1IncorrectAlert']).text
        assert owner_sin1_alert == "Owner SIN 1 is incorrect"
        self.get_elements(x_paths["ownerSin2"]).send_keys("433")
        owner_sin2_alert = self.get_elements(x_paths['ownerSin2IncorrectAlert']).text
        assert owner_sin2_alert == "Owner SIN 2 is incorrect"
        self.get_elements(x_paths["craTransmitterNo"]).send_keys("433")
        cra_alert = self.get_elements(x_paths['craTransmitterIncorrectAlert']).text
        assert cra_alert == "This value is incorrect"
        self.get_elements(x_paths["rqTransmitterNo"]).send_keys("433")
        rq_alert = self.get_elements(x_paths['rqTransmitterIncorrectAlert']).text
        assert rq_alert == "This value is incorrect"
        self.get_elements(x_paths["email"]).send_keys("433")
        email_alert = self.get_elements(x_paths['emailIncorrectAlert']).text
        assert email_alert == "This field must only contain valid email"

    def test_mandatory_fields(self):
        """TC-2
        In this test case we are testing filing resources with mandatory fields
        :return:
        """
        filing_resource_list = FilingResourceList(self.driver)
        filing_resource_list_elements = filing_resource_list.X_paths
        filing_resource_setup = FilingResourceSetup(self.driver)
        x_paths = filing_resource_setup.X_paths
        dropdown_xpaths = FilingResourceSetup.drop_down_xpath
        expected_dict = FilingResourceData.req_fields_exp_data
        self.get_login()
        self.navigate_sidebar_menu(main_menu="peopleMenu", sub_menu_type="filingResourceMenu", expand_parent=False)
        self.get_element_click_able(filing_resource_list_elements["createButton"])
        self.get_elements(filing_resource_list_elements["createButton"]).click()
        self.get_element_click_able(x_paths["roleField"])
        self.get_elements(x_paths['roleField']).click()
        self.get_element_click_able(x_paths["issuerchkbox"])
        self.get_elements(x_paths['issuerchkbox']).click()
        self.get_elements(x_paths['transmitterchkbox']).click()
        self.check_required_fields(FilingResourceSetup.X_paths, FilingResourceData.req_fields_data,
                                   FilingResourceSetup.req_field_list, wizard_tabs=1)
        self.verify_toast_message()
        self.unmask_data()
        self.navigate_sidebar_menu(main_menu="peopleMenu", sub_menu_type="filingResourceMenu", expand_parent=False)
        self.get_element_click_able(filing_resource_list_elements["allFRList"])
        fr_list = self.get_elements_in_list(filing_resource_list_elements["allFRList"])
        fr = "Ghayur"
        self.click_on_any_element_in_list(fr_list, fr)
        self.get_element_presence(x_paths["effectiveFrom"])
        # Updating the drop down xpath so we can read the selected option in them
        ignored_fields_list = ["saveBtn", "resetBtn", "roleField", "issuerchkbox", "transmitterchkbox", "ext1",
                               "ownerSin2", "rqTransmitterNo", "rl1Type", "contactchkbox"]
        drop_down_fields_list = ["contactPerson", "Issuer", "transmitter", "effectiveFrom", "rl1Type", "province"]
        """Comparing the t4a with expected data dict"""
        self.read_data(expected_dict, x_paths, dropdown_xpaths, ignored_fields_list, drop_down_fields_list)

    def test_create_filing_resource_contact(self):
        """TC-3
        In this test case we are testing filing resource only contact person
        :return:
        """
        filing_resource_list = FilingResourceList(self.driver)
        filing_resource_list_elements = filing_resource_list.X_paths
        filing_resource_setup = FilingResourceSetup(self.driver)
        x_paths = filing_resource_setup.X_paths
        dropdown_xpaths = FilingResourceSetup.drop_down_xpath
        expected_dict = FilingResourceData.contact_person_exp_data
        self.get_login()
        self.navigate_sidebar_menu(main_menu="peopleMenu", sub_menu_type="filingResourceMenu", expand_parent=False)
        self.get_element_click_able(filing_resource_list_elements["createButton"])
        self.get_elements(filing_resource_list_elements["createButton"]).click()
        self.get_element_presence(x_paths['effectiveFrom'])
        self.get_elements(x_paths['effectiveFrom']).send_keys("2020")
        self.get_elements(x_paths["name"]).send_keys("Contact")
        self.get_elements(x_paths["phone1"]).send_keys("(124) 579-9625")
        self.get_elements(x_paths["ext1"]).send_keys("853")
        self.get_elements(x_paths["saveBtn"]).click()
        self.verify_toast_message()
        self.navigate_sidebar_menu(main_menu="peopleMenu", sub_menu_type="filingResourceMenu", expand_parent=False)
        self.get_element_click_able(filing_resource_list_elements["allFRList"])
        fr_list = self.get_elements_in_list(filing_resource_list_elements["allFRList"])
        fr = "Contact"
        self.click_on_any_element_in_list(fr_list, fr)
        self.get_element_presence(x_paths["effectiveFrom"])
        # Updating the drop down xpath so we can read the selected option in them
        ignored_fields_list = ["saveBtn", "resetBtn", "roleField", "issuerchkbox", "transmitterchkbox", "Issuer",
                               "transmitter", "ownerSin1", "ownerSin2", "craTransmitterNo", "rqTransmitterNo",
                               "rl1Type", "address", "city", "province", "postCode", "contactName", "email", "country",
                               "contactchkbox"]
        drop_down_fields_list = ["contactPerson", "Issuer", "transmitter", "effectiveFrom", "rl1Type", "province"]
        self.read_data(expected_dict, x_paths, dropdown_xpaths, ignored_fields_list, drop_down_fields_list)

    def test_contact_mandatory_fields(self):
        """TC-15
        In this test case we are testing filing resource contact person mandatory fields
        :return:
        """
        filing_resource_list = FilingResourceList(self.driver)
        filing_resource_list_elements = filing_resource_list.X_paths
        filing_resource_setup = FilingResourceSetup(self.driver)
        x_paths = filing_resource_setup.X_paths
        self.get_login()
        self.navigate_sidebar_menu(main_menu="peopleMenu", sub_menu_type="filingResourceMenu", expand_parent=False)
        self.get_element_click_able(filing_resource_list_elements["createButton"])
        self.get_elements(filing_resource_list_elements["createButton"]).click()
        self.get_element_click_able(x_paths["effectiveFrom"])
        self.get_elements(x_paths["saveBtn"]).click()
        effective_alert = self.get_elements(x_paths['effectiveFromAlert']).text
        assert effective_alert == "This field is required"
        name_alert = self.get_elements(x_paths['nameAlert']).text
        assert name_alert == "This field is required"
        phone_alert = self.get_elements(x_paths['phone1Alert']).text
        assert phone_alert == "This field is required"

    def test_create_filing_resource_issuer(self):
        """TC-4
        In this test case we are testing filing resources with issuer fields
        :return:
        """
        filing_resource_list = FilingResourceList(self.driver)
        filing_resource_list_elements = filing_resource_list.X_paths
        filing_resource_setup = FilingResourceSetup(self.driver)
        x_paths = filing_resource_setup.X_paths
        dropdown_xpaths = FilingResourceSetup.drop_down_xpath
        expected_dict = FilingResourceData.issuer_exp_data
        self.get_login()
        self.navigate_sidebar_menu(main_menu="peopleMenu", sub_menu_type="filingResourceMenu", expand_parent=False)
        self.get_element_click_able(filing_resource_list_elements["createButton"])
        self.get_elements(filing_resource_list_elements["createButton"]).click()
        self.get_element_click_able(x_paths["roleField"])
        self.get_elements(x_paths['roleField']).click()
        self.get_element_click_able(x_paths["contactchkbox"])
        self.get_elements(x_paths["contactchkbox"]).click()
        self.get_elements(x_paths["issuerchkbox"]).click()
        self.get_element_presence(x_paths['effectiveFrom'])
        self.get_elements(x_paths['effectiveFrom']).send_keys("2020")
        self.get_elements(x_paths["name"]).send_keys("Issuer")
        self.get_elements(x_paths["phone1"]).send_keys("(458) 951-2310")
        self.get_elements(x_paths["ext1"]).send_keys("532")
        self.get_elements(x_paths["ownerSin1"]).send_keys("990-000-010")
        self.get_elements(x_paths["ownerSin2"]).send_keys("990-000-051")
        self.get_elements(x_paths["saveBtn"]).click()
        self.verify_toast_message()
        self.unmask_data()
        self.navigate_sidebar_menu(main_menu="peopleMenu", sub_menu_type="filingResourceMenu", expand_parent=False)
        self.get_element_click_able(filing_resource_list_elements["allFRList"])
        fr_list = self.get_elements_in_list(filing_resource_list_elements["allFRList"])
        fr = "Issuer"
        self.click_on_any_element_in_list(fr_list, fr)
        self.get_element_presence(x_paths["effectiveFrom"])
        # Updating the drop down xpath so we can read the selected option in them
        ignored_fields_list = ["saveBtn", "resetBtn", "roleField", "issuerchkbox", "transmitterchkbox", "contactchkbox",
                               "transmitter", "craTransmitterNo", "rqTransmitterNo", "contactPerson",
                               "rl1Type", "address", "city", "province", "postCode", "contactName", "email", "country"]
        drop_down_fields_list = ["contactPerson", "Issuer", "transmitter", "effectiveFrom", "rl1Type", "province"]
        self.read_data(expected_dict, x_paths, dropdown_xpaths, ignored_fields_list, drop_down_fields_list)

    def test_issuer_mandatory_fields(self):
        """TC-16
        In this test case we are testing filing resources issuer mandatory fields
        :return:
        """
        filing_resource_list = FilingResourceList(self.driver)
        filing_resource_list_elements = filing_resource_list.X_paths
        filing_resource_setup = FilingResourceSetup(self.driver)
        x_paths = filing_resource_setup.X_paths
        self.get_login()
        self.navigate_sidebar_menu(main_menu="peopleMenu", sub_menu_type="filingResourceMenu", expand_parent=False)
        self.get_element_click_able(filing_resource_list_elements["createButton"])
        self.get_elements(filing_resource_list_elements["createButton"]).click()
        self.get_element_click_able(x_paths["roleField"])
        self.get_elements(x_paths['roleField']).click()
        self.get_element_click_able(x_paths["contactchkbox"])
        self.get_elements(x_paths["contactchkbox"]).click()
        self.get_elements(x_paths["issuerchkbox"]).click()
        self.get_element_click_able(x_paths["effectiveFrom"])
        self.get_elements(x_paths["saveBtn"]).click()
        effective_alert = self.get_elements(x_paths['effectiveFromAlert']).text
        assert effective_alert == "This field is required"
        name_alert = self.get_elements(x_paths['nameAlert']).text
        assert name_alert == "This field is required"
        phone_alert = self.get_elements(x_paths['phone1Alert']).text
        assert phone_alert == "This field is required"
        sin_alert = self.get_elements(x_paths['ownerSin1Alert']).text
        assert sin_alert == "This field is required"

    def test_create_filing_resource_french_chars(self):
        """TC-11
        In this test case we are testing filing resources with french characters in all fields
        :return:
        """
        filing_resource_list = FilingResourceList(self.driver)
        filing_resource_list_elements = filing_resource_list.X_paths
        filing_resource_setup = FilingResourceSetup(self.driver)
        x_paths = filing_resource_setup.X_paths
        dropdown_xpaths = FilingResourceSetup.drop_down_xpath
        expected_dict = FilingResourceData.french_chars_exp_data
        self.get_login()
        self.navigate_sidebar_menu(main_menu="peopleMenu", sub_menu_type="filingResourceMenu", expand_parent=False)
        self.get_element_click_able(filing_resource_list_elements["createButton"])
        self.get_elements(filing_resource_list_elements["createButton"]).click()
        self.fill_form_and_save(FilingResourceData.french_chars_data, FilingResourceSetup.X_paths)
        self.verify_toast_message()
        self.unmask_data()
        self.navigate_sidebar_menu(main_menu="peopleMenu", sub_menu_type="filingResourceMenu", expand_parent=False)
        self.get_element_click_able(filing_resource_list_elements["allFRList"])
        fr_list = self.get_elements_in_list(filing_resource_list_elements["allFRList"])
        fr = "Bîlàl"
        self.click_on_any_element_in_list(fr_list, fr)
        self.get_element_presence(x_paths["effectiveFrom"])
        # Updating the drop down xpath so we can read the selected option in them
        ignored_fields_list = ["saveBtn", "resetBtn", "roleField", "issuerchkbox", "transmitterchkbox", "contactchkbox"]
        drop_down_fields_list = ["contactPerson", "Issuer", "transmitter", "effectiveFrom", "rl1Type", "province"]
        """Comparing the t4a with expected data dict"""
        self.read_data(expected_dict, x_paths, dropdown_xpaths, ignored_fields_list, drop_down_fields_list)

    def test_delete_filing_resource(self):
        """TC-13
        In this test case we are testing filing resources with only one record
        :return:
        """
        filing_resource_list = FilingResourceList(self.driver)
        filing_resource_list_elements = filing_resource_list.X_paths
        filing_resource_setup = FilingResourceSetup(self.driver)
        x_paths = filing_resource_setup.X_paths
        self.get_login()
        self.navigate_sidebar_menu(main_menu="peopleMenu", sub_menu_type="filingResourceMenu", expand_parent=False)
        self.get_element_click_able(filing_resource_list_elements["createButton"])
        self.get_elements(filing_resource_list_elements["createButton"]).click()
        self.fill_form_and_save(FilingResourceData.delete_data, FilingResourceSetup.X_paths)
        self.verify_toast_message()
        self.navigate_sidebar_menu(main_menu="peopleMenu", sub_menu_type="filingResourceMenu", expand_parent=False)
        self.get_element_presence(filing_resource_list_elements['deleteList'])
        self.get_elements(filing_resource_list_elements['deleteList']).click()
        self.get_element_click_able(filing_resource_list_elements['confirmDeleteAll'])
        self.get_elements(filing_resource_list_elements['confirmDeleteAll']).click()
        self.verify_toast_message('delete')

    def test_update_filing_resource(self):
        """TC-14
        In this test case we are updating existing filing resources with all fields
        :return:
        """
        filing_resource_list = FilingResourceList(self.driver)
        filing_resource_list_elements = filing_resource_list.X_paths
        filing_resource_setup = FilingResourceSetup(self.driver)
        x_paths = filing_resource_setup.X_paths
        dropdown_xpaths = FilingResourceSetup.drop_down_xpath
        expected_dict = FilingResourceData.after_update_exp_data
        self.get_login()
        self.navigate_sidebar_menu(main_menu="peopleMenu", sub_menu_type="filingResourceMenu", expand_parent=False)
        self.get_element_click_able(filing_resource_list_elements["createButton"])
        self.get_elements(filing_resource_list_elements["createButton"]).click()
        self.fill_form_and_save(FilingResourceData.before_update_data, FilingResourceSetup.X_paths)
        self.verify_toast_message()
        self.unmask_data()
        self.navigate_sidebar_menu(main_menu="peopleMenu", sub_menu_type="filingResourceMenu", expand_parent=False)
        self.get_element_click_able(filing_resource_list_elements["allFRList"])
        fr_list = self.get_elements_in_list(filing_resource_list_elements["allFRList"])
        fr = "Zahid"
        self.click_on_any_element_in_list(fr_list, fr)
        self.get_text_presence_in_element_value(x_paths['name'], "Zahid")
        self.update_info_of_any_form(FilingResourceData.after_update_data, FilingResourceSetup.X_paths,
                                     FilingResourceSetup.setup_drop_down_list)
        self.verify_toast_message('update')
        self.navigate_sidebar_menu(main_menu="peopleMenu", sub_menu_type="filingResourceMenu", expand_parent=False)
        self.get_element_click_able(filing_resource_list_elements["allFRList"])
        fr_list = self.get_elements_in_list(filing_resource_list_elements["allFRList"])
        fr = "Tauqeer"
        self.click_on_any_element_in_list(fr_list, fr)
        self.get_text_presence_in_element_value(x_paths['name'], "Tauqeer")
        # Updating the drop down xpath so we can read the selected option in them
        ignored_fields_list = ["saveBtn", "resetBtn", "roleField", "issuerchkbox", "transmitterchkbox", "contactchkbox"]
        drop_down_fields_list = ["contactPerson", "Issuer", "transmitter", "effectiveFrom", "rl1Type", "province"]
        """Comparing the t4a with expected data dict"""
        self.read_data(expected_dict, x_paths, dropdown_xpaths, ignored_fields_list, drop_down_fields_list)

    def test_delete_all(self):
        """
        In this test case we are testing delete all filing resources
        :return:
        """
        filing_resource_list = FilingResourceList(self.driver)
        filing_resource_list_elements = filing_resource_list.X_paths
        filing_resource_setup = FilingResourceSetup(self.driver)
        x_paths = filing_resource_setup.X_paths
        self.get_login()
        self.navigate_sidebar_menu(main_menu="peopleMenu", sub_menu_type="filingResourceMenu", expand_parent=False)
        time.sleep(2)
        self.get_element_click_able(filing_resource_list_elements['selectAllCheckBox'])
        self.get_elements(filing_resource_list_elements['selectAllCheckBox']).click()
        self.get_element_click_able(filing_resource_list_elements['deleteAllButton'])
        self.get_elements(filing_resource_list_elements['deleteAllButton']).click()
        self.get_element_click_able(filing_resource_list_elements['confirmDeleteAll'])
        self.get_elements(filing_resource_list_elements['confirmDeleteAll']).click()
        self.verify_toast_message('delete')
