import copy
import time
import pytest
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from page_objects.dashboard import Dashboard
from page_objects.filing_resource_list import FilingResourceList
from page_objects.filing_resource_setup import FilingResourceSetup
from page_objects.sidebar_menu import SidebarMenu
from page_objects.t4a_list import T4aList
from page_objects.t4a_setup import T4aSetup
from page_objects.t4a_summary import T4ASummary
from test_data.filing_resource_data import FilingResourceData
from test_data.t4a_data import DataT4a
from test_data.t4a_summary_data import T4ASummaryData
from utilities.base_class import BaseClass


class TestT4ASummary(BaseClass):
	"""
	This class contains the test cases of t4a summary
	
	"""
	def test_all_required_fields(self):
		""" Test all required fields in t4a summary"""
		t4a_summary = T4ASummary(self.driver)
		t4a_summary_element = t4a_summary.t4a_summary_xpaths
		self.get_login()
		self.navigate_sidebar_menu(menu_type='t4aMenu', sub_menu_type='t4aSummary')
		self.get_element_presence(t4a_summary_element["saveButton"])
		self.get_elements(t4a_summary_element["saveButton"]).click()
		trans_alert = self.get_elements(t4a_summary_element["transmitterAlertRequired"]).text
		assert trans_alert == "This field is required"
		issuer_alert = self.get_elements(t4a_summary_element["issuerAlertRequired"]).text
		assert issuer_alert == "This field is required"
		contact_alert = self.get_elements(t4a_summary_element["contactRequiredAlert"]).text
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

	def test_summary_values(self):
		"""Test t4a summary values"""
		side_menu = SidebarMenu(self.driver)
		menu_element = side_menu.menu_xpaths
		t4a_summary = T4ASummary(self.driver)
		t4a_summary_element = t4a_summary.t4a_summary_xpaths
		dashboard_obj = Dashboard(self.driver)
		t4a_setup = T4aSetup(self.driver)
		t4a_list = T4aList(self.driver)
		t4a_data = DataT4a
		t4a_elements = t4a_setup.t4a_x_paths
		t4a_list_elements = t4a_list.t4a_list_xpaths
		dashboard_elements = dashboard_obj.dashboard_X_paths
		test_case_data = t4a_data.test_case1
		test_case_data_3 = t4a_data.test_case3
		expected_dict = T4ASummaryData.expected_dic_1
		self.get_login()
		self.get_element_presence(dashboard_elements['t4a'])
		self.get_elements(dashboard_elements['t4a']).click()
		self.get_element_presence(t4a_list_elements['createSlip'])
		self.get_elements(t4a_list_elements['createSlip']).click()
		self.get_element_presence(t4a_elements['loadVendor'])
		for key, value in t4a_elements.items():
			if key not in ["loadVendor", "AddMore", "country", "loadSlip", "saveButton", "toastMessage", "closeToast"] \
					and "Button" not in key:
				try:
					self.get_elements(value).send_keys(test_case_data[key])
				except NoSuchElementException:
					print("Element not found")

		self.get_elements(t4a_elements['saveButton']).click()
		self.verify_toast_message()
		self.get_element_presence(t4a_elements['resetButton'])
		self.get_elements(t4a_elements['resetButton']).click()
		self.driver.execute_script("window.scrollTo(0, document.body.scrollLength);")
		self.get_element_presence(t4a_elements['sin'])
		t4a_setup.actions.double_click(self.get_elements(t4a_elements["sin"])).perform()
		t4a_setup.actions.click(self.get_elements(t4a_elements["sin"])).perform()
		self.get_elements(t4a_elements["sin"]).send_keys(Keys.BACKSPACE)
		self.get_element_presence(t4a_elements['email'])
		t4a_setup.actions.double_click(self.get_elements(t4a_elements["email"])).perform()
		t4a_setup.actions.click(self.get_elements(t4a_elements["email"])).perform()
		self.get_elements(t4a_elements["email"]).send_keys(Keys.BACKSPACE)
		self.get_element_presence(t4a_elements['loadVendor'])
		for key, value in t4a_elements.items():
			if key not in ["loadVendor", "AddMore", "country", "loadSlip", "saveButton", "toastMessage", "closeToast"] \
					and "Button" not in key:
				try:
					self.get_elements(value).send_keys(test_case_data_3[key])
				except NoSuchElementException:
					print("Element not found")
		self.get_elements(t4a_elements['saveButton']).click()
		self.verify_toast_message()
		time.sleep(3)
		self.get_element_presence(menu_element['t4aSummary'])
		self.get_elements(menu_element['t4aSummary']).click()
		time.sleep(2)
		"""Select company persons and then verify the t4a summary"""
		self.get_element_presence(t4a_summary_element['transmitter'])
		self.get_elements(t4a_summary_element['transmitter']).send_keys('Gha')
		self.get_elements(t4a_summary_element['issuer']).send_keys('Gha')
		self.get_elements(t4a_summary_element['contactPerson']).send_keys('Gha')
		self.get_elements(t4a_summary_element['saveButton']).click()
		self.verify_toast_message('updated')
		self.unmask_data()
		time.sleep(2)
		# Updating the drop down xpaths so we can read the selected option in them
		t4a_summary_element2 = {}
		t4a_summary_element2 = copy.deepcopy(t4a_summary_element)
		t4a_summary_element2.update({
			"transmitter": "//*[@id='el_Transmitter']/div/div/div/div[1]/div[1]",
			"xmlType": "//*[@id='el_XMLType']/div/div/div/div[1]/div[1]",
			"issuer": "//*[@id='el_Issuer']/div/div/div/div[1]/div[1]",
			"contactPerson": "//*[@id='el_Persontocontact']/div/div/div/div[1]/div[1]"
		})
		ignored_fields = ["saveButton", "deleteConfirmationButton", "closeToast", "generateXmlButton",
		                  "printButton", "transmitterAlertRequired", "issuerAlertRequired",
		                  "contactRequiredAlert", "toastTitle", "notes", "toastMessage"]
		drop_down_fields = ["transmitter", "xmlType", "issuer", "contactPerson", "clientName", "companyAddressInfo"]
		# ignored_fields += drop_down_fields
		for element, x_path in t4a_summary_element2.items():
			if element in ignored_fields:
				continue
			if element in drop_down_fields:
				self.get_element_presence(t4a_summary_element2[element])
				field_data = self.get_elements(t4a_summary_element2[element]).text
				assert field_data == expected_dict[element], str(element) + "Value not matched"
			else:
				field_data = self.get_elements(t4a_summary_element2[element]).get_attribute("value")
				assert field_data == expected_dict[element], str(element) + " not matched"

	def test_remittance_calculation(self):
		t4a_summary = T4ASummary(self.driver)
		t4a_summary_element = t4a_summary.t4a_summary_xpaths
		self.get_login()
		self.navigate_sidebar_menu(menu_type='t4aMenu', sub_menu_type='t4aSummary')
		"""checking the remittance of balance due"""
		self.get_element_presence(t4a_summary_element['totalIncomeTaxDeducted'])
		total_income_tax = self.get_elements(t4a_summary_element["totalIncomeTaxDeducted"]).get_attribute('value')
		t4a_summary.actions.double_click(self.get_elements(t4a_summary_element["remittance"])).perform()
		self.get_elements(t4a_summary_element["remittance"]).send_keys(Keys.BACKSPACE)
		self.get_elements(t4a_summary_element['remittance']).send_keys('10000')
		self.get_elements(t4a_summary_element['difference']).click()
		difference = self.get_elements(t4a_summary_element["difference"]).get_attribute('value')
		# assert float(difference) == round(float(total_income_tax) - 10000.00, 2)
		balance_due = self.get_elements(t4a_summary_element["balanceDue"]).get_attribute('value')
		
		"""checking the remittance of overpayment"""
		self.get_element_presence(t4a_summary_element['totalIncomeTaxDeducted'])
		t4a_summary.actions.double_click(self.get_elements(t4a_summary_element["remittance"])).perform()
		self.get_elements(t4a_summary_element["remittance"]).send_keys(Keys.BACKSPACE)
		self.get_elements(t4a_summary_element['remittance']).send_keys('110000')
		self.get_elements(t4a_summary_element['difference']).click()
		difference = self.get_elements(t4a_summary_element["difference"]).get_attribute('value')
		over_payment = self.get_elements(t4a_summary_element["overpayment"]).get_attribute('value')

	@pytest.mark.skip
	def test_generate_xml_and_print_validations(self):
		t4a_summary = T4ASummary(self.driver)
		t4a_summary_element = t4a_summary.t4a_summary_xpaths
		self.get_login()
		self.navigate_sidebar_menu(menu_type='t4aMenu', sub_menu_type='t4aSummary')
		self.get_element_click_able(t4a_summary_element["generateXmlButton"])
		self.get_elements(t4a_summary_element["generateXmlButton"]).click()
		self.verify_toast_message('unmask_xml')
		time.sleep(3)
		self.get_element_click_able(t4a_summary_element["printButton"])
		self.get_elements(t4a_summary_element["printButton"]).click()
		self.verify_toast_message('unmask_print')
		self.unmask_data()
		self.get_elements(t4a_summary_element["generateXmlButton"]).click()
		invoice_modal = self.get_elements(t4a_summary_element["invoiceModal"]).text
		assert invoice_modal == "Invoice(s) Due", "Modal is not showing"
		self.get_elements(t4a_summary_element["closeToast"]).click()
		time.sleep(3)
		self.get_elements(t4a_summary_element["printButton"]).click()
		invoice_modal = self.get_elements(t4a_summary_element["invoiceModal"]).text
		assert invoice_modal == "Invoice(s) Due", "Modal is not showing"
		self.get_elements(t4a_summary_element["closeToast"]).click()
