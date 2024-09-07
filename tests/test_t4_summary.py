import copy
import time

import pytest
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from page_objects.adjustment_options import AdjustmentOptions
from page_objects.adjustments import Adjustments
from page_objects.employee_list import EmployeeList
from page_objects.employee_setup import EmployeeSetup
from page_objects.filing_resource_list import FilingResourceList
from page_objects.filing_resource_setup import FilingResourceSetup
from page_objects.header import Header
from page_objects.sidebar_menu import SidebarMenu
from page_objects.t4_list import T4List
from page_objects.t4_setup import T4Setup
from page_objects.t4_summary import T4Summary
from test_data.credentials import Credentials
from test_data.filing_resource_data import FilingResourceData
from test_data.t4_summary_data import T4SummaryData
from utilities.base_class import BaseClass


class TestT4Summary(BaseClass):
    @pytest.mark.skip
    def test_all_required_fields(self):
        """
        Testing all the required fields on t4 summary screen
        :return:
        """
        side_menu = SidebarMenu(self.driver)
        menu_element = side_menu.menu_xpaths
        t4_setup = T4Setup(self.driver)
        t4Summary = T4Summary(self.driver)
        t4_summary_elements = t4Summary.t4_summary_xpaths
        self.get_login()
        self.get_element_presence(menu_element["complianceMenu"])
        self.get_elements(menu_element['complianceMenu']).click()
        self.get_element_click_able(menu_element['t4Menu'])
        self.get_elements(menu_element['t4Menu']).click()
        self.get_element_presence(menu_element['t4Summary'])
        self.get_elements(menu_element['t4Summary']).click()
        self.get_element_presence(t4_summary_elements["saveButton"])
        self.get_elements(t4_summary_elements["saveButton"]).click()
        self.get_element_presence(t4_summary_elements['transmitterRequiredAlert'])
        tran_alert = self.get_elements(t4_summary_elements['transmitterRequiredAlert']).text
        assert tran_alert == "This field is required"
        self.get_element_presence(t4_summary_elements['issuerRequiredAlert'])
        issu_alert = self.get_elements(t4_summary_elements['issuerRequiredAlert']).text
        assert issu_alert == "This field is required"
        self.get_element_presence(t4_summary_elements['contactPersonRequiredAlert'])
        contact_alert = self.get_elements(t4_summary_elements['contactPersonRequiredAlert']).text
        assert contact_alert == "This field is required"

    def test_creating_filing_resource(self):
        """
        Creating filing resource as it is a pre condition for the next test cases
        :return:
        """
        filing_resource_list = FilingResourceList(self.driver)
        filing_resource_list_elements = filing_resource_list.X_paths
        filing_resource_setup = FilingResourceSetup(self.driver)
        filing_resource_setup_elements = filing_resource_setup.X_paths
        filing_resource_data = FilingResourceData.data1
        self.get_login()
        self.navigate_sidebar_menu(main_menu="peopleMenu", sub_menu_type="filingResourceMenu", expand_parent=False)
        self.get_element_click_able(filing_resource_list_elements["createButton"])
        self.get_elements(filing_resource_list_elements["createButton"]).click()
        self.get_element_click_able(filing_resource_setup_elements['saveButton'])
        self.get_elements(filing_resource_setup_elements['roleField']).click()
        self.get_element_click_able(filing_resource_setup_elements['roleFieldDropdown'])
        self.get_elements(filing_resource_setup_elements['issuerCheckBox']).click()
        self.get_element_click_able(filing_resource_setup_elements['transmitterCheckBox'])
        self.get_elements(filing_resource_setup_elements['transmitterCheckBox']).click()
        self.get_element_click_able(filing_resource_setup_elements['ext1'])
        self.get_elements(filing_resource_setup_elements['ext1']).click()
        self.get_element_presence(filing_resource_setup_elements['effectiveFrom'])
        for key, value in filing_resource_setup_elements.items():
            if "Button" not in key and "CheckBox" not in key and "Checkbox" not in key and "role" not in key \
                    and "Role" not in key \
                    and "country" not in key and "toastMessage" not in key and "closeToast" not in key:
                self.get_elements(value).send_keys(filing_resource_data[key])
        self.get_elements(filing_resource_setup_elements['saveButton']).click()
        self.verify_toast_message()

    def test_summary_values_without_adjustment(self):
        """
        Testing the summary values when slips are not adjusted
        Create the filling resource first manually all named as 'ghayur' before running this test
        :return:
        """
        t4_setup = T4Setup(self.driver)
        t4_elements = t4_setup.t4_xpaths
        slip1_data = T4SummaryData.slip1_data
        slip2_data = T4SummaryData.slip2_data
        t4Summary = T4Summary(self.driver)
        t4_summary_elements = t4Summary.t4_summary_xpaths
        expected_dict = T4SummaryData.expected_dict1
        self.get_login()
        self.navigate_sidebar_menu()
        """Creating the employees for t4 summary data verfication"""
        self.get_element_presence(t4_elements["reflectEmployee"])
        for key, value in t4_elements.items():
            if key not in ["loadEmployee", "AddMore", "country", "loadSlip", "saveButton", "toastMessage",
                           "dateOfBirth", "closeToast", "insurableEarning", "pensionableEarning", "ppipPremiums"] \
                    and "Button" not in key and "CheckBox" not in key and "Checkbox" not in key \
                    and "exempt" not in key and "pensionablePeriod" not in key and "otherInfo" not in key:
                try:
                    self.get_elements(value).send_keys(slip1_data[key])
                except NoSuchElementException:
                    print("otherInfo element not found")

        self.driver.execute_script("window.scrollTo(0, document.body.scrollLength);")
        self.get_element_presence(t4_elements["saveButton"])
        self.get_elements(t4_elements["saveButton"]).click()
        self.verify_toast_message()
        time.sleep(3)
        self.get_elements(t4_elements["resetButton"]).click()
        t4_setup.actions.double_click(self.get_elements(t4_elements["sin"])).perform()
        t4_setup.actions.click(self.get_elements(t4_elements["sin"])).perform()
        self.get_elements(t4_elements["sin"]).send_keys(Keys.BACKSPACE)
        t4_setup.actions.double_click(self.get_elements(t4_elements["email"])).perform()
        t4_setup.actions.click(self.get_elements(t4_elements["email"])).perform()
        self.get_elements(t4_elements["email"]).send_keys(Keys.BACKSPACE)
        self.get_element_presence(t4_elements["reflectEmployee"])
        for key, value in t4_elements.items():
            if key not in ["loadEmployee", "AddMore", "country", "loadSlip", "saveButton", "toastMessage",
                           "dateOfBirth", "closeToast", "insurableEarning", "pensionableEarning"] \
                    and "Button" not in key and "Checkbox" not in key  and "CheckBox" not in key \
                    and "exempt" not in key and "pensionablePeriod" not in key:
                try:
                    self.get_elements(value).send_keys(slip2_data[key])
                except NoSuchElementException:
                    print("otherInfo element not found")
        self.driver.execute_script("window.scrollTo(0, document.body.scrollLength);")
        self.get_element_presence(t4_elements["saveButton"])
        self.get_elements(t4_elements["saveButton"]).click()
        self.verify_toast_message()
        """Verifying the T4 summary data """
        self.navigate_sidebar_menu(sub_menu_type='t4Summary', expand_parent=False, expand_compliance=False)
        time.sleep(2)
        self.get_element_presence(t4_summary_elements["saveButton"])
        # self.get_text_prasence_in_element(t4_summary_elements["addressInfo"], "House#3")
        self.unmask_data()
        time.sleep(2)
        self.get_elements(t4_summary_elements['minusRemittance']).click()
        self.get_elements(t4_summary_elements['transmitter']).send_keys('Gha')
        self.get_elements(t4_summary_elements['xmlType']).send_keys('or')
        self.get_elements(t4_summary_elements['issuer']).send_keys('Gha')
        self.get_elements(t4_summary_elements['contactPerson']).send_keys('Gha')
        self.get_elements(t4_summary_elements['saveButton']).click()
        self.get_text_prasence_in_element(t4_summary_elements['toastTitle'], "Success")
        toast = self.get_elements(t4_summary_elements['toastTitle']).text
        assert "Success" in toast
        self.get_elements(t4_summary_elements['closeToast']).click()

        # Updating the drop down xpaths so we can read the selected option in them
        t4_summary_elements2 = {}
        t4_summary_elements2 = copy.deepcopy(t4_summary_elements)

        t4_summary_elements2.update({
            "transmitter": "//body/div[@id='__nuxt']/div[@id='__layout']/div[@id='inspire']/div[1]/main[1]/div[1]/div"
                           "[1]/di""v[2]/span[1]/form[1]/div[2]/div[1]/div[1]/div[1]/div[25]/div[2]/div[1]/div[2]/span"
                           "[1]/div[1]/div[1]/div[1]/div[1]/div[1]",
            "xmlType": "//body/div[@id='__nuxt']/div[@id='__layout']/div[@id='inspire']/div[1]/main[1]/div[1]/div[1]/"
                       "div[2]/span[1]/form[1]/div[2]/div[1]/div[1]/div[1]/div[25]/div[2]/div[2]/div[2]/span[1]/div[1]"
                       "/div[1]/div[1]/div[1]/div[1]",
            "issuer": "//body/div[@id='__nuxt']/div[@id='__layout']/div[@id='inspire']/div[1]/main[1]/div[1]/div[1]/"
                      "div[2]/span[1]/form[1]/div[2]/div[1]/div[1]/div[1]/div[25]/div[2]/div[4]/div[2]/span[1]/div[1]"
                      "/div[1]/div[1]/div[1]/div[1]",
            "contactPerson": "//body/div[@id='__nuxt']/div[@id='__layout']/div[@id='inspire']/div[1]/main[1]/div[1]/"
                             "div[1]/div[2]/span[1]/form[1]/div[2]/div[1]/div[1]/div[1]/div[25]/div[2]/div[7]/div[3]/"
                             "span[1]/div[1]/div[1]/div[1]/div[1]/div[1]",


        })

        ignored_fields = ["saveButton", "deleteConfirmationButton", "closeToast", "generateXml",
                          "generateXmlDisabled","deleteConfirmationButton",
                          "printButton", "transmitterRequiredAlert", "issuerRequiredAlert",
                          "contactPersonRequiredAlert", "toastTitle", "closeToast", "notes", "toastMessage"]
        drop_down_fields = ["transmitter", "xmlType", "issuer", "contactPerson", "companyName", "addressInfo"]
        # ignored_fields += drop_down_fields
        for element, x_path in t4_summary_elements2.items():
            if element in ignored_fields:
                continue
            if element in drop_down_fields:
                # self.get_element_presence(t4_elements[element])
                field_data = self.get_elements(t4_summary_elements2[element]).text
                assert field_data == expected_dict[element], str(element) + "Value not matched"
            else:
                field_data = self.get_elements(t4_summary_elements2[element]).get_attribute("value")
                assert field_data == expected_dict[element], str(element) + " not matched"

    @pytest.mark.skip
    def test_generate_XML_and_print_validations(self):
        """
        Generate XML and print summary validations, in which we check system should not allow user to print or generate
        XML if data is masked or if there is any Audit Filing and PIER Review errors
        :return:
        """
        t4_setup = T4Setup(self.driver)
        t4Summary = T4Summary(self.driver)
        t4_summary_elements = t4Summary.t4_summary_xpaths
        header_setup = Header(self.driver)
        header_elements = header_setup.Xpaths
        self.get_login()
        self.navigate_sidebar_menu(sub_menu_type='t4Summary')
        time.sleep(2)
        self.get_element_presence(t4_summary_elements["saveButton"])
        self.get_elements(t4_summary_elements['generateXml']).click()
        self.verify_toast_message('unmask_xml')
        time.sleep(2)
        self.get_element_presence(t4_summary_elements['printButton'])
        self.get_elements(t4_summary_elements['printButton']).click()
        self.verify_toast_message('unmask_print')
        time.sleep(2)
        self.unmask_data()
        self.get_text_prasence_in_element(header_elements['maskButton'], "Mask")
        self.get_elements(t4_summary_elements['generateXml']).click()
        time.sleep(2)
        invoice_modal = self.get_elements(t4_summary_elements["invoiceModal"]).text
        assert invoice_modal == "Invoice(s) Due", "Modal is not showing"
        self.get_elements(t4_summary_elements["closeToast"]).click()
        self.get_text_prasence_in_element(t4_summary_elements['toastMessage'], "Please load Audit")
        Audit_toast = self.get_elements(t4_summary_elements['toastMessage']).text
        assert Audit_toast == "Please load Audit in menu and clear all audit items (Audit Filing and PIER Review) " \
                              "to generate documents.", "Unmask validation is not working"
        self.get_elements(t4_summary_elements['closeToast']).click()
        self.get_invisibility_element(t4_summary_elements['toastMessage'])
        time.sleep(2)
        self.get_elements(t4_summary_elements['printButton']).click()
        self.get_text_prasence_in_element(t4_summary_elements['toastMessage'], "Please load Audit")
        Audit_toast2 = self.get_elements(t4_summary_elements['toastMessage']).text
        assert Audit_toast2 == "Please load Audit in menu and clear all audit items (Audit Filing and PIER Review) " \
                               "to generate documents.", "Unmask validation is not working"
        self.get_element_presence(t4_summary_elements['closeToast'])
        self.get_elements(t4_summary_elements['closeToast']).click()

    @pytest.mark.skip
    def test_summary_values_with_adjustment(self):
        """
        Testing the summary values when slips are  adjusted and remittance is transfer
        Create the filling resource first manually all named as 'ghayur' before running this test
        :return:
        """
        side_menu = SidebarMenu(self.driver)
        menu_element = side_menu.menu_xpaths
        header_setup = Header(self.driver)
        adjustments = Adjustments(self.driver)
        adjustments_elements = adjustments.adjustment_xpath
        adjustmentOptions = AdjustmentOptions(self.driver)
        adjustment_options_elements = adjustmentOptions.adjustment_option_xpath
        header_elements = header_setup.Xpaths
        employee_list = EmployeeList(self.driver)
        list_elements = employee_list.employee_list_xpath
        t4_setup = T4Setup(self.driver)
        t4_elements = t4_setup.t4_xpaths
        slip1_data = T4SummaryData.slip1_data
        slip2_data = T4SummaryData.slip2_data
        user_credentials = Credentials.users_credentials
        t4Summary = T4Summary(self.driver)
        t4_summary_elements = t4Summary.t4_summary_xpaths
        expected_dict = T4SummaryData.expected_dict2
        self.get_login()
        self.navigate_sidebar_menu(main_menu="adjustmentMenu", sub_menu_type="adjustmentOptions", expand_parent=False)
        # self.navigate_sidebar_menu(main_menu="adjustmentMenu", sub_menu_type="adjustmentOptions")
        self.get_element_click_able(adjustment_options_elements['transferOverRemittance'])
        self.get_elements(adjustment_options_elements['transferOverRemittance']).click()
        self.get_element_presence(adjustment_options_elements['listCheckBoxOfTransferRemittance'])
        time.sleep(2)
        check_box = self.driver.find_elements_by_xpath(adjustment_options_elements['listCheckBoxOfTransferRemittance'])
        for box in check_box:
            box.click()
        self.get_elements(adjustment_options_elements['saveButton']).click()
        self.get_text_prasence_in_element(adjustment_options_elements['toastMessage'], "Successfully")
        adj_opt_toast_mess = self.get_elements(adjustment_options_elements['toastMessage']).text
        assert "Successfully" in adj_opt_toast_mess
        self.get_element_click_able(menu_element['adjustments'])
        self.get_elements(menu_element['adjustments']).click()
        self.get_element_click_able(adjustments_elements['adjustAllSlips'])
        self.get_elements(adjustments_elements['adjustAllSlips']).click()
        self.get_text_prasence_in_element(adjustments_elements['toastMessage'], "All slips")
        adj_done_mess = self.get_elements(adjustments_elements['toastMessage']).text
        assert adj_done_mess == "All slips have been adjusted"
        self.get_elements(adjustments_elements['closeToast']).click()
        self.get_element_presence(adjustments_elements['transferRemittance'])
        self.get_elements(adjustments_elements['transferRemittance']).click()
        self.get_text_prasence_in_element(adjustments_elements['toastMessage'], "Over-remittance has been")
        tras_remit_toast = self.get_elements(adjustments_elements['toastMessage']).text
        assert "Over-remittance has been transferred" in tras_remit_toast
        self.get_elements(adjustments_elements['closeToast']).click()
        """Verifying the T4 summary data """
        self.navigate_sidebar_menu(sub_menu_type='t4Summary')
        self.get_element_presence(t4_summary_elements["saveButton"])
        self.get_text_prasence_in_element(t4_summary_elements["addressInfo"], "House#3")
        self.get_elements(t4_summary_elements['transmitter']).send_keys('Gha')
        self.get_elements(t4_summary_elements['xmlType']).send_keys('or')
        self.get_elements(t4_summary_elements['issuer']).send_keys('Gha')
        self.get_elements(t4_summary_elements['contactPerson']).send_keys('Gha')
        self.get_elements(t4_summary_elements['saveButton']).click()
        self.get_text_prasence_in_element(t4_summary_elements['toastTitle'] , "Success")
        toast = self.get_elements(t4_summary_elements['toastTitle']).text
        assert "Success" in toast
        self.get_elements(t4_summary_elements['closeToast']).click()
        self.get_element_click_able(header_elements['maskButton'])
        self.get_elements(header_elements['maskButton']).click()
        self.get_element_presence(header_elements['unmaskPassword'])
        self.get_elements(header_elements['unmaskPassword']).send_keys(user_credentials['password'])
        self.get_elements(header_elements['verifyButton']).click()
        time.sleep(2)
        # Updating the drop down xpaths so we can read the selected option in them
        t4_summary_elements2 = {}
        t4_summary_elements2 = copy.deepcopy(t4_summary_elements)

        t4_summary_elements2.update({
            "transmitter": "//body/div[@id='__nuxt']/div[@id='__layout']/div[@id='inspire']/div[1]/main[1]/div[1]/div"
                           "[1]/di""v[2]/span[1]/form[1]/div[2]/div[1]/div[1]/div[1]/div[25]/div[2]/div[1]/div[2]/span"
                           "[1]/div[1]/div[1]/div[1]/div[1]/div[1]",
            "xmlType": "//body/div[@id='__nuxt']/div[@id='__layout']/div[@id='inspire']/div[1]/main[1]/div[1]/div[1]/"
                       "div[2]/span[1]/form[1]/div[2]/div[1]/div[1]/div[1]/div[25]/div[2]/div[2]/div[2]/span[1]/div[1]"
                       "/div[1]/div[1]/div[1]/div[1]",
            "issuer": "//body/div[@id='__nuxt']/div[@id='__layout']/div[@id='inspire']/div[1]/main[1]/div[1]/div[1]/"
                      "div[2]/span[1]/form[1]/div[2]/div[1]/div[1]/div[1]/div[25]/div[2]/div[4]/div[2]/span[1]/div[1]"
                      "/div[1]/div[1]/div[1]/div[1]",
            "contactPerson": "//body/div[@id='__nuxt']/div[@id='__layout']/div[@id='inspire']/div[1]/main[1]/div[1]/"
                             "div[1]/div[2]/span[1]/form[1]/div[2]/div[1]/div[1]/div[1]/div[25]/div[2]/div[7]/div[3]/"
                             "span[1]/div[1]/div[1]/div[1]/div[1]/div[1]",

        })

        ignored_fields = ["saveButton", "deleteConfirmationButton", "closeToast", "generateXml",
                          "generateXmlDisabled", "deleteConfirmationButton",
                          "printButton", "transmitterRequiredAlert", "issuerRequiredAlert",
                          "contactPersonRequiredAlert", "toastTitle", "closeToast", "notes", "toastMessage"]
        drop_down_fields = ["transmitter", "xmlType", "issuer", "contactPerson", "companyName", "addressInfo"]
        # ignored_fields += drop_down_fields
        for element, x_path in t4_summary_elements2.items():
            if element in ignored_fields:
                continue
            if element in drop_down_fields:
                # self.get_element_presence(t4_elements[element])
                field_data = self.get_elements(t4_summary_elements2[element]).text
                assert field_data == expected_dict[element], str(element) + "Value not matched"
            else:
                field_data = self.get_elements(t4_summary_elements2[element]).get_attribute("value")
                assert field_data == expected_dict[element], str(element) + " not matched"

    @pytest.mark.skip
    def test_remittance_calculation_t4_summary(self):
        """
        Testing the remittance calculation of T4 summary screen
        :return:
        """
        t4_setup = T4Setup(self.driver)
        t4Summary = T4Summary(self.driver)
        t4_summary_elements = t4Summary.t4_summary_xpaths
        self.get_login()
        self.navigate_sidebar_menu(sub_menu_type='t4Summary')
        self.get_text_prasence_in_element(t4_summary_elements['addressInfo'], "ichra lahore")
        total_deduction = self.get_elements(t4_summary_elements['totalDeductionReport']).get_attribute("value")

        """Checking when remittance transfer has balance due"""
        t4Summary.actions.double_click(self.get_elements(t4_summary_elements["minusRemittance"])).perform()
        self.get_elements(t4_summary_elements["minusRemittance"]).send_keys("5000")
        self.get_elements(t4_summary_elements["totalDeductionReport"]).click()
        difference = self.get_elements(t4_summary_elements["difference"]).get_attribute('value')
        assert float(difference) == round(float(total_deduction) - 5000.00, 2)
        balanceDue = self.get_elements(t4_summary_elements["balanceDue"]).get_attribute('value')
        assert float(balanceDue) == round(float(total_deduction) - 5000.00, 2)
        overPayment = self.get_elements(t4_summary_elements["overPayment"]).get_attribute('value')
        assert overPayment == ""

        """Checking when remittance transfer is overpayment"""
        t4Summary.actions.double_click(self.get_elements(t4_summary_elements["minusRemittance"])).perform()
        self.get_elements(t4_summary_elements["minusRemittance"]).send_keys('13000')
        self.get_elements(t4_summary_elements["totalDeductionReport"]).click()
        difference = self.get_elements(t4_summary_elements["difference"]).get_attribute('value')
        assert float(difference) == round(13000 - float(total_deduction), 2)
        balanceDue = self.get_elements(t4_summary_elements["balanceDue"]).get_attribute('value')
        assert balanceDue == ""
        overPayment = self.get_elements(t4_summary_elements["overPayment"]).get_attribute('value')
        assert float(overPayment) == round(13000 - float(total_deduction), 2)

    @pytest.mark.skip
    def test_mask_info_and_conditions_t4_summary(self):
        """
        Testing the mask and unmask info on t4 summary screen
        :return:
        """
        t4_setup = T4Setup(self.driver)
        t4Summary = T4Summary(self.driver)
        header_setup = Header(self.driver)
        header_elements = header_setup.Xpaths
        user_credentials = Credentials.users_credentials
        t4_summary_elements = t4Summary.t4_summary_xpaths
        self.get_login()
        self.navigate_sidebar_menu(sub_menu_type='t4Summary')
        self.get_text_prasence_in_element(t4_summary_elements['addressInfo'], "ichra lahore")
        sin1 = self.get_elements(t4_summary_elements['sin1OfProprietor']).get_attribute('value')
        assert str(sin1) == "000-***-***"
        sin2 = self.get_elements(t4_summary_elements['sin2OfProprietor']).get_attribute('value')
        assert str(sin2) == "000-***-***"
        self.get_element_click_able(header_elements['maskButton'])
        self.get_elements(header_elements['maskButton']).click()
        self.get_element_presence(header_elements['unmaskPassword'])
        self.get_elements(header_elements['unmaskPassword']).send_keys(user_credentials['password'])
        self.get_elements(header_elements['verifyButton']).click()
        time.sleep(2)
        sin1 = self.get_elements(t4_summary_elements['sin1OfProprietor']).get_attribute('value')
        assert str(sin1) == "000-000-000"
        sin2 = self.get_elements(t4_summary_elements['sin2OfProprietor']).get_attribute('value')
        assert str(sin2) == "000-000-000"

    @pytest.mark.skip
    def test_confirmation_no_disabling_conditions_without_adjustment(self):
        """
        Confirmation no disabling conditions when slips are not adjusted And then deleting the confirmation no and
        checking the disabled buttons are enabled again
        :return:
        """
        side_menu = SidebarMenu(self.driver)
        menu_element = side_menu.menu_xpaths
        emp_list = EmployeeList(self.driver)
        emp_list_elements = emp_list.employee_list_xpath
        emp_setup = EmployeeSetup(self.driver)
        emp_setup_elements = emp_setup.employee_xpaths
        t4_setup = T4Setup(self.driver)
        t4_setup_elements = t4_setup.t4_xpaths
        adjustments = Adjustments(self.driver)
        adjustments_elements = adjustments.adjustment_xpath
        adjustmentOptions = AdjustmentOptions(self.driver)
        adjustment_options_elements = adjustmentOptions.adjustment_option_xpath
        t4_list = T4List(self.driver)
        t4_list_elements = t4_list.t4_list_xpaths
        t4Summary = T4Summary(self.driver)
        t4_summary_elements = t4Summary.t4_summary_xpaths
        self.get_login()
        """Undoing the remittance transfer and unadjusting the slips"""
        self.get_element_click_able(menu_element['adjustmentMenu'])
        self.get_elements(menu_element['adjustmentMenu']).click()
        self.get_element_click_able(menu_element['adjustments'])
        self.get_elements(menu_element['adjustments']).click()
        self.get_element_presence(adjustments_elements['undoTransferRemittance'])
        self.get_elements(adjustments_elements['undoTransferRemittance']).click()
        self.get_element_presence(adjustments_elements['ignoreTransferRemittance'])
        self.get_elements(adjustments_elements['unadjustAllSlips']).click()
        self.get_text_prasence_in_element(adjustments_elements['toastMessage'], "Adjustments Removed")
        self.get_elements(adjustments_elements['closeToast']).click()

        "Adding confirmation no in summary"
        self.navigate_sidebar_menu(sub_menu_type='t4Summary')
        self.get_text_prasence_in_element(t4_summary_elements['addressInfo'], "ichra lahore")
        time.sleep(3)
        self.get_elements(t4_summary_elements['confirmationNo']).send_keys('123')
        self.get_elements(t4_summary_elements['saveButton']).click()
        self.get_element_presence(t4_summary_elements['deleteConfirmationButton'])
        self.get_text_prasence_in_element(t4_summary_elements['toastMessage'], "updated")
        self.get_elements(t4_summary_elements['closeToast']).click()
        summary_save_button = self.get_elements(t4_summary_elements['saveButton']).is_enabled()
        assert str(summary_save_button) == 'False', "Save button is not disabled"
        summary_XML_button = self.get_elements(t4_summary_elements['generateXmlDisabled']).is_enabled()
        assert str(summary_XML_button) == 'False', "Generate XML button is not disabled"
        self.navigate_sidebar_menu(main_menu="peopleMenu", sub_menu_type="employeeMenu", expand_parent=False)
        self.get_element_presence(emp_list_elements["empListDeleteButtons"])
        self.get_elements(emp_list_elements['headerListCheckBox']).click()
        "list of all delete button of employees"
        emp_del_list = self.get_elements_in_list(emp_list_elements['empListDeleteButtons'])
        for btn in emp_del_list:
            check_button = btn.is_enabled()
            assert str(check_button) == "False"
        self.get_element_presence(emp_list_elements['deleteBtn'])
        del_all_emp = self.get_elements(emp_list_elements['deleteBtn']).is_enabled()
        assert str(del_all_emp) == "False"

        "Checking disabled buttons on t4 list screen"
        self.navigate_sidebar_menu(sub_menu_type="t4List")
        self.get_element_presence(t4_list_elements["t4ListDeleteButtons"])
        self.get_element_click_able(t4_list_elements['headerListCheckBox'])
        time.sleep(3)
        # TODO: Time sleep is used because previous list checkbox data is loaded first in t4 list which is a
        #  performance issue so we have to wait that data first unload from list then we click
        self.get_elements(t4_list_elements['headerListCheckBox']).click()

        "list of all delete button of t4s"
        t4_del_list = self.get_elements_in_list(t4_list_elements['t4ListDeleteButtons'])
        for t4_btn in t4_del_list:
            check_button = t4_btn.is_enabled()
            assert str(check_button) == "False"
        self.get_element_presence(t4_list_elements['deleteButton'])
        del_all_slips = self.get_elements(t4_list_elements['deleteButton']).is_enabled()
        assert str(del_all_slips) == "False"

        "Checking disabled button on t4 setup screen"

        self.get_elements(menu_element['t4Setup']).click()
        self.get_element_presence(t4_setup_elements['fName'], 20)
        saveButton = self.get_elements(t4_setup_elements['saveButton']).is_enabled()
        assert str(saveButton) == "False"
        resetButton = self.get_elements(t4_setup_elements['resetButton']).is_enabled()
        assert str(resetButton) == "False"
        del_button = self.get_elements(t4_setup_elements['deleteButton']).is_enabled()
        assert str(del_button) == "False"

        "Checking adjustment options save button"
        self.get_element_click_able(menu_element['adjustmentMenu'])
        self.get_elements(menu_element['adjustmentMenu']).click()
        self.get_element_click_able(menu_element['adjustmentOptions'])
        self.get_elements(menu_element['adjustmentOptions']).click()
        self.get_element_presence(adjustment_options_elements['resetButton'])
        saveButton = self.get_elements(adjustment_options_elements['saveButton']).is_enabled()
        assert str(saveButton) == "False"

        "Checking adjustments screen disabled buttons"
        self.get_element_click_able(menu_element['adjustments'])
        self.get_elements(menu_element['adjustments']).click()
        self.get_element_presence(adjustments_elements['adjustAllSlipDisablingSign'])
        adjust_all_slips = self.get_elements(adjustments_elements['adjustAllSlips']).is_enabled()
        assert str(adjust_all_slips) == "False"

        """ Now removing the confirmation no and checking that disabled buttons are enabled again"""
        self.navigate_sidebar_menu(sub_menu_type='t4Summary')
        self.get_element_presence(t4_summary_elements['generateXmlDisabled'])
        self.get_elements(t4_summary_elements['deleteConfirmationButton']).click()
        self.get_text_prasence_in_element(t4_summary_elements['toastMessage'], "deleted")
        self.get_elements(t4_summary_elements['closeToast']).click()
        summary_save_button = self.get_elements(t4_summary_elements['saveButton']).is_enabled()
        assert str(summary_save_button) == 'True', "Save button is not disabled"
        summary_XML_button = self.get_elements(t4_summary_elements['generateXml']).is_enabled()
        assert str(summary_XML_button) == 'True', "Generate XML button is not disabled"
        self.get_elements(menu_element["peopleMenu"]).click()
        self.get_element_presence(menu_element["employeeMenu"])
        self.get_elements(menu_element["employeeMenu"]).click()
        self.get_element_presence(emp_list_elements["empListDeleteButtons"])
        self.get_elements(emp_list_elements['headerListCheckBox']).click()
        "list of all delete button of employees"
        emp_del_list = self.get_elements_in_list(emp_list_elements['empListDeleteButtons'])
        for btn in emp_del_list:
            check_button = btn.is_enabled()
            assert str(check_button) == "True"
        self.get_element_presence(emp_list_elements['deleteBtn'])
        del_all_emp = self.get_elements(emp_list_elements['deleteBtn']).is_enabled()
        assert str(del_all_emp) == "True"

        "Checking disabled buttons on t4 list screen"
        self.navigate_sidebar_menu(sub_menu_type="t4List")
        self.get_element_presence(t4_list_elements["t4ListDeleteButtons"])
        self.get_element_click_able(t4_list_elements['headerListCheckBox'])
        time.sleep(3)
        # TODO: Time sleep is used because previous list checkbox data is loaded first in t4 list which is a
        #  performance issue so we have to wait that data first unload from list then we click
        self.get_elements(t4_list_elements['headerListCheckBox']).click()

        "list of all delete button of t4s"
        t4_del_list = self.get_elements_in_list(t4_list_elements['t4ListDeleteButtons'])
        for t4_btn in t4_del_list:
            check_button = t4_btn.is_enabled()
            assert str(check_button) == "True"
        self.get_element_presence(t4_list_elements['deleteButton'])
        del_all_slips = self.get_elements(t4_list_elements['deleteButton']).is_enabled()
        assert str(del_all_slips) == "True"

        "Checking disabled button on t4 setup screen"

        self.get_elements(menu_element['t4Setup']).click()
        self.get_element_presence(t4_setup_elements['fName'])
        saveButton = self.get_elements(t4_setup_elements['saveButton']).is_enabled()
        assert str(saveButton) == "True"
        resetButton = self.get_elements(t4_setup_elements['resetButton']).is_enabled()
        assert str(resetButton) == "True"
        del_button = self.get_elements(t4_setup_elements['deleteButton']).is_enabled()
        assert str(del_button) == "True"

        "Checking adjustment options save button"
        self.get_element_click_able(menu_element['adjustmentMenu'])
        self.get_elements(menu_element['adjustmentMenu']).click()
        self.get_element_click_able(menu_element['adjustmentOptions'])
        self.get_elements(menu_element['adjustmentOptions']).click()
        self.get_element_presence(adjustment_options_elements['resetButton'])
        saveButton = self.get_elements(adjustment_options_elements['saveButton']).is_enabled()
        assert str(saveButton) == "True"

        "Checking adjustments screen disabled buttons"
        self.get_element_click_able(menu_element['adjustments'])
        self.get_elements(menu_element['adjustments']).click()
        self.get_element_presence(adjustments_elements['adjustAllSlips'])
        adjust_all_slips = self.get_elements(adjustments_elements['adjustAllSlips']).is_enabled()
        assert str(adjust_all_slips) == "True"

    "This test case is skipped due to the bug of middle page Bug ID # 008 on bug sheet"
    @pytest.mark.skip
    def test_confirmation_no_disabling_conditions(self):
        """
        Confirmation no disabling conditions when slips are adjusted and and remittance difference is transferred
        And then deleting the confirmation no and checking the disabled buttons are enabled again
        :return:
        """
        side_menu = SidebarMenu(self.driver)
        menu_element = side_menu.menu_xpaths
        emp_list = EmployeeList(self.driver)
        emp_list_elements = emp_list.employee_list_xpath
        emp_setup = EmployeeSetup(self.driver)
        emp_setup_elements = emp_setup.employee_xpaths
        t4_setup = T4Setup(self.driver)
        t4_setup_elements = t4_setup.t4_xpaths
        adjustments = Adjustments(self.driver)
        adjustments_elements = adjustments.adjustment_xpath
        adjustmentOptions = AdjustmentOptions(self.driver)
        adjustment_options_elements = adjustmentOptions.adjustment_option_xpath
        t4_list = T4List(self.driver)
        t4_list_elements = t4_list.t4_list_xpaths
        t4Summary = T4Summary(self.driver)
        t4_summary_elements = t4Summary.t4_summary_xpaths
        self.get_login()
        self.navigate_sidebar_menu(sub_menu_type='t4Summary')
        self.get_text_prasence_in_element(t4_summary_elements['addressInfo'], "ichra lahore")
        self.get_elements(t4_summary_elements['confirmationNo']).send_keys('123')
        self.get_elements(t4_summary_elements['saveButton']).click()
        self.get_text_prasence_in_element(t4_summary_elements['toastMessage'], "updated")
        self.get_elements(t4_summary_elements['closeToast']).click()
        self.get_element_presence(t4_summary_elements['deleteConfirmationButton'])
        summary_save_button = self.get_elements(t4_summary_elements['saveButton']).is_enabled()
        assert str(summary_save_button) == 'False', "Save button is not disabled"
        summary_XML_button = self.get_elements(t4_summary_elements['generateXmlDisabled']).is_enabled()
        assert str(summary_XML_button) == 'False', "Generate XML button is not disabled"
        self.navigate_sidebar_menu(main_menu="peopleMenu", sub_menu_type="employeeMenu", expand_parent=False)
        # self.get_elements(menu_element["peopleMenu"]).click()
        # self.get_element_presence(menu_element["employeeMenu"])
        # self.get_elements(menu_element["employeeMenu"]).click()
        self.get_element_presence(emp_list_elements["empListDeleteButtons"])
        self.get_elements(emp_list_elements['headerListCheckBox']).click()
        "list of all delete button of employees"
        emp_del_list = self.get_elements_in_list(emp_list_elements['empListDeleteButtons'])
        for btn in emp_del_list:
            check_button = btn.is_enabled()
            assert str(check_button) == "False"
        self.get_element_presence(emp_list_elements['deleteBtn'])
        del_all_emp = self.get_elements(emp_list_elements['deleteBtn']).is_enabled()
        assert str(del_all_emp) == "False"

        "Checking disabled buttons on t4 list screen"
        self.navigate_sidebar_menu(sub_menu_type='t4List')
        self.get_element_presence(t4_list_elements["t4ListDeleteButtons"])
        self.get_element_click_able(t4_list_elements['headerListCheckBox'])
        time.sleep(3)
        # TODO: Time sleep is used because previous list checkbox data is loaded first in t4 list which is a
        #  performance issue so we have to wait that data first unload from list then we click
        self.get_elements(t4_list_elements['headerListCheckBox']).click()

        "list of all delete button of t4s"
        t4_del_list = self.get_elements_in_list(t4_list_elements['t4ListDeleteButtons'])
        for t4_btn in t4_del_list:
            check_button = t4_btn.is_enabled()
            assert str(check_button) == "False"
        self.get_element_presence(t4_list_elements['deleteButton'])
        del_all_slips = self.get_elements(t4_list_elements['deleteButton']).is_enabled()
        assert str(del_all_slips) == "False"

        "Checking disabled button on t4 setup screen"

        self.get_elements(menu_element['t4Setup']).click()
        self.get_element_presence(t4_setup_elements['fName'])
        saveButton = self.get_elements(t4_setup_elements['saveButton']).is_enabled()
        assert str(saveButton) == "False"
        resetButton = self.get_elements(t4_setup_elements['resetButton']).is_enabled()
        assert str(resetButton) == "False"
        del_button = self.get_elements(t4_setup_elements['deleteButton']).is_enabled()
        assert str(del_button) == "False"

        "Checking adjustment options save button"
        self.get_element_click_able(menu_element['adjustmentMenu'])
        self.get_elements(menu_element['adjustmentMenu']).click()
        self.get_element_click_able(menu_element['adjustmentOptions'])
        self.get_elements(menu_element['adjustmentOptions']).click()
        self.get_element_presence(adjustment_options_elements['resetButton'])
        saveButton = self.get_elements(adjustment_options_elements['saveButton']).is_enabled()
        assert str(saveButton) == "False"

        "Checking adjustments screen disabled buttons"
        self.get_element_click_able(menu_element['adjustments'])
        self.get_elements(menu_element['adjustments']).click()
        self.get_element_presence(adjustments_elements['undoTransferRemittance'])
        unadjustAllSlips = self.get_elements(adjustments_elements['unadjustAllSlips']).is_enabled()
        assert str(unadjustAllSlips) == "False"
        undoTransferRemittance = self.get_elements(adjustments_elements['undoTransferRemittance']).is_enabled()
        assert str(undoTransferRemittance) == "False"
        """ Now removing the confirmation no and checking that disabled buttons are enabled again"""
        self.navigate_sidebar_menu(sub_menu_type='t4Summary')
        # self.get_element_presence(menu_element["complianceMenu"])
        # self.get_elements(menu_element['complianceMenu']).click()
        # self.get_element_click_able(menu_element['t4Menu'])
        # self.get_elements(menu_element['t4Menu']).click()
        # self.get_element_click_able(menu_element['t4Summary'])
        # self.get_elements(menu_element['t4Summary']).click()
        self.get_element_presence(t4_summary_elements['generateXmlDisabled'])
        self.get_elements(t4_summary_elements['deleteConfirmationButton']).click()
        self.get_text_prasence_in_element(t4_summary_elements['toastMessage'], "deleted")
        self.get_elements(t4_summary_elements['closeToast']).click()
        summary_save_button = self.get_elements(t4_summary_elements['saveButton']).is_enabled()
        assert str(summary_save_button) == 'True', "Save button is not disabled"
        summary_XML_button = self.get_elements(t4_summary_elements['generateXml']).is_enabled()
        assert str(summary_XML_button) == 'True', "Generate XML button is not disabled"
        self.navigate_sidebar_menu(main_menu="peopleMenu", sub_menu_type="employeeMenu", expand_parent=False)
        # self.get_elements(menu_element["peopleMenu"]).click()
        # self.get_element_presence(menu_element["employeeMenu"])
        # self.get_elements(menu_element["employeeMenu"]).click()
        self.get_element_presence(emp_list_elements["empListDeleteButtons"])
        self.get_elements(emp_list_elements['headerListCheckBox']).click()
        "list of all delete button of employees"
        emp_del_list = self.get_elements_in_list(emp_list_elements['empListDeleteButtons'])
        for btn in emp_del_list:
            check_button = btn.is_enabled()
            assert str(check_button) == "True"
        self.get_element_presence(emp_list_elements['deleteBtn'])
        del_all_emp = self.get_elements(emp_list_elements['deleteBtn']).is_enabled()
        assert str(del_all_emp) == "True"

        "Checking disabled buttons on t4 list screen"
        self.navigate_sidebar_menu(sub_menu_type='t4List')
        # self.get_element_presence(menu_element["complianceMenu"])
        # self.get_elements(menu_element['complianceMenu']).click()
        # self.get_element_click_able(menu_element['t4Menu'])
        # self.get_elements(menu_element['t4Menu']).click()
        # self.get_element_click_able(menu_element["t4List"])
        # self.get_elements(menu_element["t4List"]).click()
        self.get_element_presence(t4_list_elements["t4ListDeleteButtons"])
        self.get_element_click_able(t4_list_elements['headerListCheckBox'])
        time.sleep(3)
        # TODO: Time sleep is used because previous list checkbox data is loaded first in t4 list which is a
        #  performance issue so we have to wait that data first unload from list then we click
        self.get_elements(t4_list_elements['headerListCheckBox']).click()

        "list of all delete button of t4s"
        t4_del_list = self.get_elements_in_list(t4_list_elements['t4ListDeleteButtons'])
        for t4_btn in t4_del_list:
            check_button = t4_btn.is_enabled()
            assert str(check_button) == "False"
        self.get_element_presence(t4_list_elements['deleteButton'])
        del_all_slips = self.get_elements(t4_list_elements['deleteButton']).is_enabled()
        assert str(del_all_slips) == "False"

        "Checking disabled button on t4 setup screen"
        self.get_elements(menu_element['t4Setup']).click()
        self.get_element_presence(t4_setup_elements['fName'])
        saveButton = self.get_elements(t4_setup_elements['saveButton']).is_enabled()
        assert str(saveButton) == "False"
        resetButton = self.get_elements(t4_setup_elements['resetButton']).is_enabled()
        assert str(resetButton) == "False"
        del_button = self.get_elements(t4_setup_elements['deleteButton']).is_enabled()
        assert str(del_button) == "False"

        "Checking adjustment options save button"
        self.get_element_click_able(menu_element['adjustmentMenu'])
        self.get_elements(menu_element['adjustmentMenu']).click()
        self.get_element_click_able(menu_element['adjustmentOptions'])
        self.get_elements(menu_element['adjustmentOptions']).click()
        self.get_element_presence(adjustment_options_elements['resetButton'])
        saveButton = self.get_elements(adjustment_options_elements['saveButton']).is_enabled()
        assert str(saveButton) == "False"

        "Checking adjustments screen disabled buttons"
        self.get_element_click_able(menu_element['adjustments'])
        self.get_elements(menu_element['adjustments']).click()
        self.get_element_presence(adjustments_elements['undoTransferRemittance'])
        unadjustAllSlips = self.get_elements(adjustments_elements['unadjustAllSlips']).is_enabled()
        assert str(unadjustAllSlips) == "True"
        undoTransferRemittance = self.get_elements(adjustments_elements['undoTransferRemittance']).is_enabled()
        assert str(undoTransferRemittance) == "True"

    def test_Deleting_filing_resource_and_employees(self):
        """
        Deleting the filing resource and employees created for t4 summary test cases
        :return:
        """
        side_menu = SidebarMenu(self.driver)
        menu_element = side_menu.menu_xpaths
        header_setup = Header(self.driver)
        header_elements = header_setup.Xpaths
        filing_resource_list = FilingResourceList(self.driver)
        filing_resource_list_elements = filing_resource_list.X_paths
        filing_resource_setup = FilingResourceSetup(self.driver)
        employee_list = EmployeeList(self.driver)
        employee_list_elements = employee_list.employee_list_xpath
        self.get_login()
        self.navigate_sidebar_menu(main_menu="peopleMenu", sub_menu_type="employeeMenu", expand_parent=False)
        self.get_element_click_able(employee_list_elements["headerListCheckBox"])
        self.get_elements(employee_list_elements["headerListCheckBox"]).click()
        self.get_element_click_able(employee_list_elements["deleteBtn"])
        self.get_elements(employee_list_elements["deleteBtn"]).click()
        self.get_element_click_able(employee_list_elements["OKBtn"])
        self.get_elements(employee_list_elements["OKBtn"]).click()
        self.verify_toast_message('delete')
        self.get_element_click_able(header_elements['accountOptions'])
        self.get_elements(header_elements['accountOptions']).click()
        self.get_element_click_able(header_elements['fillingResource'])
        self.get_elements(header_elements['fillingResource']).click()
        time.sleep(3)
        self.get_element_click_able(filing_resource_list_elements["selectAllCheckBox"])
        self.get_elements(filing_resource_list_elements["selectAllCheckBox"]).click()
        self.get_element_presence(filing_resource_list_elements["deleteAllButton"])
        self.get_elements(filing_resource_list_elements["deleteAllButton"]).click()
        self.get_element_click_able(filing_resource_list_elements['confirmDeleteAll'])
        self.get_elements(filing_resource_list_elements['confirmDeleteAll']).click()
        self.get_text_prasence_in_element(filing_resource_list_elements["toastMessage"], "deleted")
        self.get_element_click_able(filing_resource_list_elements['closeToast'])
        self.get_elements(filing_resource_list_elements['closeToast']).click()

