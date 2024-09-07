"""
class contains merge,unmerge and ignored employee testcases
"""
import copy
import time
import pytest
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from page_objects.employee_list import EmployeeList
from page_objects.employee_setup import EmployeeSetup
from page_objects.merge_employee import MergeEmployee
from page_objects.rl1_setup import Rl1Setup
from page_objects.t4_list import T4List
from page_objects.t4_setup import T4Setup
from test_data.credentials import Credentials
from test_data.merge_employee_data import MergeEmployeeData
from utilities.base_class import BaseClass


class TestMergeEmployee(BaseClass):

    def test_merge_employees(self):
        """
        test to merge t4s with same poe, non-QC, mask info and merge duplicate employees and where EI insurable and
        cpp Pensionable earnings reach there max limit, other info code 73 merging which exceeds max limit
        :return:
        """
        employee_list = EmployeeList(self.driver)
        list_elements = employee_list.employee_list_xpath
        merge_employee = MergeEmployee(self.driver)
        merge_elements = merge_employee.merge_employee_xpath
        t4_setup = T4Setup(self.driver)
        t4_elements = t4_setup.t4_xpaths
        t4_drop_down_elements = t4_setup.drop_down_xpath
        test_case1_data = MergeEmployeeData.test_case1_data1
        test_case2_data = MergeEmployeeData.test_case1_data2
        expected_dict = MergeEmployeeData.case1_expected_dict
        expected_dict_2 = MergeEmployeeData.case1_expected_dict_2
        self.get_login()
        time.sleep(2)
        self.navigate_sidebar_menu()
        """Creating the employees to merge"""
        time.sleep(2)
        self.get_element_presence(t4_elements["reflectEmployee"])
        for key, value in t4_elements.items():
            if key not in ["loadEmployee", "AddMore", "country", "loadSlip", "saveButton", "toastMessage",
                           "dateOfBirth", "closeToast", "qppContribution", "ppipPremiums", "ppipInsurableEarning",
                           "insurableEarning", "pensionableEarning", "deleteButton"] \
                    and "Button" not in key and "Checkbox" \
                    not in key and "exempt" not in key and "pensionablePeriod" not in key:
                try:
                    self.get_elements(value).send_keys(test_case1_data[key])
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
                           "dateOfBirth", "closeToast", "qppContribution", "ppipPremiums", "deleteButton",
                           "ppipInsurableEarning", "insurableEarning", "pensionableEarning", "otherInfoCode3",
                           "otherInfoAmount3", "otherInfoCode4", "otherInfoAmount4"] \
                    and "Button" not in key and "Checkbox" not in key \
                    and "exempt" not in key and "pensionablePeriod" not in key:
                try:
                    self.get_elements(value).send_keys(test_case2_data[key])
                except NoSuchElementException:
                    print("otherInfo element not found")
        self.driver.execute_script("window.scrollTo(0, document.body.scrollLength);")
        self.get_element_presence(t4_elements["saveButton"])
        self.get_elements(t4_elements["saveButton"]).click()
        self.verify_toast_message()
        time.sleep(3)

        """merging the employees here"""

        self.go_to_merge_screen()
        self.get_element_click_able(merge_elements["mergeButton"])
        self.get_elements(merge_elements["mergeButton"]).click()
        self.verify_toast_message('unmask')
        time.sleep(2)
        self.check_unmaking()
        time.sleep(2)
        self.get_element_click_able(merge_elements["mergeButton"])
        self.get_elements(merge_elements["mergeButton"]).click()
        time.sleep(2)
        self.verify_toast_message('merge')
        self.get_element_click_able(list_elements["moreActions"])
        self.get_elements(list_elements["moreActions"]).click()
        self.get_element_click_able(merge_elements["unMergeAction"])
        self.get_elements(merge_elements["unMergeAction"]).click()
        time.sleep(3)
        self.navigate_sidebar_menu(sub_menu_type='t4List')
        time.sleep(2)
        self.get_element_presence(merge_elements["duplicate_slip"])
        time.sleep(4)
        self.get_elements(merge_elements["duplicate_slip"]).click()
        time.sleep(2)
        # Updating the drop down xpath so we can read the selected option in them
        """Comparing the merged employees with expected data dict"""
        t4_drop_down_fields = {}
        t4_drop_down_fields = copy.deepcopy(t4_elements)
        t4_drop_down_fields.update(t4_drop_down_elements)
        self.get_element_presence(t4_drop_down_fields["city"])
        city = self.get_elements(t4_drop_down_fields["city"]).get_attribute("value")

        if city == expected_dict_2["city"]:
            expected_dict = expected_dict_2
        ignored_fields = ["saveButton", "toastMessage", "closeToast", "dateOfBirth", "deleteButton",
                          "loadEmployee", "resetButton", "qppContribution", "ppipPremiums",
                          "ppipInsurableEarning", "exemptCpp", "exemptEi", "exemptPpip"]
        checkbox_fields = ["eiInsurableCheckbox", "cppPensionableCheckbox"]
        drop_down_fields = ["reflectEmployee", "province", "payPeriod", "slipType", "poe", "reducedEi", "status",
                            "employmentCode", "otherInfoCode0", "otherInfoCode1", "otherInfoCode2", "otherInfoCode3",
                            "otherInfoCode4"]
        # ignored_fields += drop_down_fields
        ignored_fields += checkbox_fields  # Adding checkbox list to the ignored list
        for element, x_path in t4_drop_down_fields.items():
            if element in ignored_fields:
                continue
            if element in drop_down_fields:
                # self.get_element_presence(t4_elements[element])
                field_data = self.get_elements(t4_drop_down_fields[element]).text
                assert field_data == expected_dict[element], str(element) + "Value not matched"
            else:
                self.get_element_presence(t4_drop_down_fields[element])
                field_data = self.get_elements(t4_drop_down_fields[element]).get_attribute("value")
                assert field_data == expected_dict[element], str(element) + " not matched"
        self.delete_merge_emp()

    def test_merge_with_one_is_exempted(self):
        """
        test to duplicate t4s with same poe with one employee is exempted
        :return:
        """
        employee_list = EmployeeList(self.driver)
        list_elements = employee_list.employee_list_xpath
        merge_employee = MergeEmployee(self.driver)
        merge_elements = merge_employee.merge_employee_xpath
        t4_setup = T4Setup(self.driver)
        t4_elements = t4_setup.t4_xpaths
        t4_drop_down_elements = t4_setup.drop_down_xpath
        test_case2_data1 = MergeEmployeeData.test_case2_data1
        test_case2_data = MergeEmployeeData.test_case2_data2
        expected_dict = MergeEmployeeData.case2_expected_dict
        expected_dict_2 = MergeEmployeeData.case2_expected_dict_2
        self.get_login()
        time.sleep(2)
        self.navigate_sidebar_menu()
        """Creating the employees to merge"""
        time.sleep(2)
        self.get_element_presence(t4_elements["reflectEmployee"])
        for key, value in t4_elements.items():
            if key not in ["loadEmployee", "AddMore", "country", "loadSlip", "saveButton", "toastMessage",
                           "dateOfBirth", "closeToast", "qppContribution", "ppipPremiums",
                           "ppipInsurableEarning", "insurableEarning", "pensionableEarning"] \
                    and "Button" not in key and "Checkbox" \
                    not in key and "exempt" not in key and "pensionablePeriod" not in key:
                try:
                    self.get_elements(value).send_keys(test_case2_data1[key])
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
                           "dateOfBirth", "closeToast", "qppContribution", "ppipPremiums",
                           "ppipInsurableEarning", "insurableEarning", "pensionableEarning", "otherInfoCode3",
                           "otherInfoAmount3", "otherInfoCode4", "otherInfoAmount4"] \
                    and "Button" not in key and "Checkbox" \
                    not in key and "pensionablePeriod" not in key:

                if "exempt" not in key:
                    try:
                        self.get_elements(value).send_keys(test_case2_data[key])
                    except NoSuchElementException:
                        print("otherInfo element not found")
                if "exempt" in key:
                    self.get_elements(value).click()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollLength);")
        self.get_element_presence(t4_elements["saveButton"])
        self.get_elements(t4_elements["saveButton"]).click()
        self.verify_toast_message()
        time.sleep(3)

        """merging the employees here"""

        self.navigate_sidebar_menu(main_menu="peopleMenu", sub_menu_type="employeeMenu", expand_parent=False)
        self.get_element_click_able(list_elements["moreActions"])
        self.get_elements(list_elements["moreActions"]).click()
        self.get_element_click_able(list_elements["mergeEmployee"])
        self.get_elements(list_elements["mergeEmployee"]).click()
        time.sleep(4)
        self.get_elements(merge_elements["headerListCheckBox"]).click()
        time.sleep(3)
        self.get_element_click_able(merge_elements["mergeButton"])
        self.get_elements(merge_elements["mergeButton"]).click()
        self.verify_toast_message('unmask')
        self.check_unmaking()
        time.sleep(2)
        self.get_element_click_able(merge_elements["mergeButton"])
        self.get_elements(merge_elements["mergeButton"]).click()
        time.sleep(2)
        self.verify_toast_message('merge')
        self.get_element_click_able(list_elements["moreActions"])
        self.get_elements(list_elements["moreActions"]).click()
        self.get_element_click_able(merge_elements["unMergeAction"])
        self.get_elements(merge_elements["unMergeAction"]).click()
        time.sleep(3)
        self.navigate_sidebar_menu(sub_menu_type='t4List')
        self.get_element_presence(merge_elements["duplicate_slip"])
        time.sleep(4)
        self.get_elements(merge_elements["duplicate_slip"]).click()
        time.sleep(2)
        """Comparing the merged employees with expected data dict"""
        # Updating the drop down xpath so we can read the selected option in them
        t4_drop_down_fields = {}
        t4_drop_down_fields = copy.deepcopy(t4_elements)
        t4_drop_down_fields.update(t4_drop_down_elements)
        self.get_element_presence(t4_drop_down_fields["city"])
        city = self.get_elements(t4_drop_down_fields["city"]).get_attribute("value")
        if city == expected_dict_2["city"]:
            expected_dict = expected_dict_2
        ignored_fields = ["saveButton", "toastMessage", "closeToast", "dateOfBirth", "deleteButton",
                          "loadEmployee", "resetButton", "qppContribution",
                          "ppipPremiums", "ppipInsurableEarning", "insurableEarning", "pensionableEarning"]
        checkbox_fields = ["eiInsurableCheckbox", "cppPensionableCheckbox"]
        drop_down_fields = ["reflectEmployee", "province", "payPeriod", "slipType", "poe", "reducedEi", "status",
                            "employmentCode", "otherInfoCode0", "otherInfoCode1", "otherInfoCode2", "otherInfoCode3",
                            "otherInfoCode4"]
        # ignored_fields += drop_down_fields
        ignored_fields += checkbox_fields  # Adding checkbox list to the ignored list
        for element, x_path in t4_drop_down_fields.items():
            if element in ignored_fields:
                continue
            if element in ["exemptCpp", "exemptEi", "exemptPpip"]:
                is_exempted = self.get_elements(t4_drop_down_fields[element]).is_selected()
                assert str(is_exempted).lower() == expected_dict[element], str(element) + " not matched"
            if element in drop_down_fields:
                # self.get_element_presence(t4_elements[element])
                field_data = self.get_elements(t4_drop_down_fields[element]).text
                assert field_data == expected_dict[element], str(element) + "Value not matched"
            else:

                self.get_element_presence(t4_drop_down_fields[element])
                field_data = self.get_elements(t4_drop_down_fields[element]).get_attribute("value")
                assert field_data == expected_dict[element], str(element) + " not matched"
        """Delete from employee list"""
        self.delete_merge_emp()

    def test_merge_employees_QC(self):
        """
        test to duplicate t4s,RL-1 with same POE QC, mask info and merge duplicate employees,
        unmerge employee and delete emp
        :return:
        """
        rl1_setup = Rl1Setup(self.driver)
        rl1_elements = rl1_setup.rl1_x_paths
        employee_list = EmployeeList(self.driver)
        list_elements = employee_list.employee_list_xpath
        merge_employee = MergeEmployee(self.driver)
        merge_elements = merge_employee.merge_employee_xpath
        t4_setup = T4Setup(self.driver)
        t4_elements = t4_setup.t4_xpaths
        t4_drop_down_elements = t4_setup.drop_down_xpath
        rl1_drop_down_elements = rl1_setup.drop_down_xpath_rl1
        test_case3_data_1 = MergeEmployeeData.test_case5_data1
        test_rl1case3_data_1 = MergeEmployeeData.test_rl1_case5_data1
        test_rl1case3_data_2 = MergeEmployeeData.test_rl1_case5_data2
        test_case5_data_2 = MergeEmployeeData.test_case5_data2
        expected_dict = MergeEmployeeData.case5_expected_dict
        expected_dict_3 = MergeEmployeeData.case5_expected_dict_5
        expected_dict5_rl1 = MergeEmployeeData.expected_dict5_rl1
        expected_dict_5_rl1 = MergeEmployeeData.case5_expected_dict_rl1
        self.get_login()
        """Creating the employees to merge"""
        time.sleep(3)
        self.navigate_sidebar_menu()
        time.sleep(2)
        self.get_element_presence(t4_elements["reflectEmployee"])
        for key, value in t4_elements.items():
            if key not in ["loadEmployee", "AddMore", "country", "loadSlip", "saveButton", "toastMessage",
                           "dateOfBirth", "closeToast", "insurableEarning", "pensionableEarning"] \
                    and "Button" not in key and "Checkbox" \
                    not in key and "exempt" not in key and "pensionablePeriod" not in key:
                try:
                    self.get_elements(value).send_keys(test_case3_data_1[key])
                except NoSuchElementException:
                    print("otherInfo element not found")
    
        self.driver.execute_script("window.scrollTo(0, document.body.scrollLength);")
        self.get_element_presence(t4_elements["saveButton"])
        self.get_elements(t4_elements["saveButton"]).click()
        self.verify_toast_message()
        time.sleep(3)
        self.navigate_sidebar_menu(menu_type='rl1Menu', sub_menu_type='rl1List', expand_compliance=False)
        time.sleep(3)
        self.get_element_presence(merge_elements["row_1_rl1_slip"])
        self.get_elements(merge_elements["row_1_rl1_slip"]).click()
        time.sleep(3)
        rl1_setup.actions.double_click(self.get_elements(rl1_elements["E-Impôt du Québec retenu"])).perform()
        rl1_setup.actions.click(self.get_elements(rl1_elements["E-Impôt du Québec retenu"])).perform()
        self.get_elements(rl1_elements["E-Impôt du Québec retenu"]).send_keys(Keys.BACKSPACE)
        self.get_elements(rl1_elements["E-Impôt du Québec retenu"]).send_keys("1520.21")
        time.sleep(2)
        for key, value in rl1_elements.items():
            if key not in ["loadEmployee", "AddMore", "country", "loadSlip", "saveButton", "toastMessage",
                           "dateOfBirth", "closeToast", "reflectInMasterData", "sin", "firstName", "lastName",
                           "initials", "address", "city", "postCode", "province", "country", "email", "payPeriod",
                           "slipType", "A-Revenus d'emploi", "B-Cotisation au RRQ", "C- Cot. à l'assurance emploi",
                           "D- Cotisation à un RPA", "G-Salaire admissible au RRQ", "H-Cotisation au RQAP",
                           "I-Salaire admissible au RQAP"] \
                    and "Button" not in key and "Checkbox" \
                    not in key and "exempt" not in key and "pensionablePeriod" not in key:
                try:
                    self.get_elements(value).send_keys(test_rl1case3_data_1[key])
                except NoSuchElementException:
                    print("otherInfo element not found")
    
        self.driver.execute_script("window.scrollTo(0, document.body.scrollLength);")
        self.get_element_presence(rl1_elements["saveButton"])
        self.get_elements(rl1_elements["saveButton"]).click()
        self.verify_toast_message('update')
        time.sleep(4)
        self.navigate_sidebar_menu(menu_type='t4Menu', sub_menu_type='t4Setup', expand_compliance=False)
        time.sleep(3)
        t4_setup.actions = ActionChains(self.driver)
        self.get_element_presence(t4_elements["reflectEmployee"])
        for key, value in t4_elements.items():
            if key not in ["loadEmployee", "cppContribution", "AddMore", "country", "loadSlip", "saveButton",
                           "toastMessage", "dateOfBirth", "closeToast", "insurableEarning",
                           "pensionableEarning", "otherInfoCode3", "otherInfoAmount3", "otherInfoCode4",
                           "otherInfoAmount4"] \
                    and "Button" not in key and "Checkbox" \
                    not in key and "exempt" not in key and "pensionablePeriod" not in key:
                try:
                    self.get_elements(value).send_keys(test_case5_data_2[key])
                except NoSuchElementException:
                    print("otherInfo element not found")
    
        self.driver.execute_script("window.scrollTo(0, document.body.scrollLength);")
        self.get_element_presence(t4_elements["saveButton"])
        self.get_elements(t4_elements["saveButton"]).click()
        self.verify_toast_message()
        time.sleep(3)
        self.navigate_sidebar_menu(menu_type='rl1Menu', sub_menu_type='rl1List', expand_compliance=False)
        time.sleep(3)
        self.get_element_presence(merge_elements["row_2_rl1_slip"])
        status = self.get_elements(merge_elements["slip_status"]).text
        if status != "Completed":
            self.get_elements(merge_elements["row_1_rl1_slip"]).click()
        else:
            self.get_elements(merge_elements["row_2_rl1_slip"]).click()
    
        time.sleep(6)
        self.get_element_presence(rl1_elements["E-Impôt du Québec retenu"])
        rl1_setup.actions = ActionChains(self.driver)
        try:
            rl1_setup.actions.double_click(self.get_elements(rl1_elements["E-Impôt du Québec retenu"])).perform()
            rl1_setup.actions.click(self.get_elements(rl1_elements["E-Impôt du Québec retenu"])).perform()
        except Exception as e:
            pass
        self.get_elements(rl1_elements["E-Impôt du Québec retenu"]).send_keys(Keys.BACKSPACE)
        self.get_elements(rl1_elements["E-Impôt du Québec retenu"]).send_keys("1520.21")
        for key, value in rl1_elements.items():
            if key not in ["loadEmployee", "AddMore", "country", "loadSlip", "saveButton", "toastMessage",
                           "dateOfBirth", "closeToast", "reflectInMasterData", "sin", "firstName", "lastName",
                           "initials", "address", "city", "postCode", "province", "country", "email", "payPeriod",
                           "slipType", "A-Revenus d'emploi", "B-Cotisation au RRQ", "C- Cot. à l'assurance emploi",
                           "D- Cotisation à un RPA", "G-Salaire admissible au RRQ", "H-Cotisation au RQAP",
                           "I-Salaire admissible au RQAP", "OtherInfo3", "amount3"] \
                    and "Button" not in key and "Checkbox" not in key and "exempt" \
                    not in key and "pensionablePeriod" not in key:
                try:
                    self.get_elements(value).send_keys(test_rl1case3_data_2[key])
                except NoSuchElementException:
                    print("otherInfo element not found")
    
        self.driver.execute_script("window.scrollTo(0, document.body.scrollLength);")
        self.get_element_presence(rl1_elements["saveButton"])
        self.get_elements(rl1_elements["saveButton"]).click()
        self.verify_toast_message('update')
        time.sleep(3)
        """merging the employees here """
        self.go_to_merge_screen()
        self.get_element_click_able(merge_elements["mergeButton"])
        self.get_elements(merge_elements["mergeButton"]).click()
        self.verify_toast_message('unmask')
        """checking mask info"""
        self.check_unmaking()
        time.sleep(2)
        self.get_element_click_able(merge_elements["mergeButton"])
        self.get_elements(merge_elements["mergeButton"]).click()
        time.sleep(2)
        self.verify_toast_message('merge')
        time.sleep(2)
        """To verify the merge employees and slips data"""
        self.navigate_sidebar_menu(sub_menu_type='t4List')
        time.sleep(2)
        self.get_element_presence(merge_elements["duplicate_slip"])
        time.sleep(4)
        self.get_elements(merge_elements["duplicate_slip"]).click()
        time.sleep(4)
        """Updating the drop down of t4 xpath so we can read the selected option in them"""
        t4_drop_down_fields = {}
        t4_drop_down_fields = copy.deepcopy(t4_elements)
        t4_drop_down_fields.update(t4_drop_down_elements)
        self.get_element_presence(t4_drop_down_fields["city"])
        city = self.get_elements(t4_drop_down_fields["city"]).get_attribute("value")
        if city == expected_dict_3["city"]:
            expected_dict = expected_dict_3
        post_code = self.get_elements(t4_drop_down_fields["postCode"]).get_attribute("value")
        if post_code == expected_dict_3["postCode"]:
            expected_dict = expected_dict_3
        ignored_fields = ["saveButton", "toastMessage", "closeToast", "dateOfBirth", "cppContribution",
                          "loadEmployee", "resetButton", "exemptCpp", "exemptEi", "exemptPpip", "deleteButton"]
        checkbox_fields = ["eiInsurableCheckbox", "cppPensionableCheckbox"]
        drop_down_fields = ["reflectEmployee", "province", "payPeriod", "slipType", "poe", "reducedEi", "status",
                            "employmentCode", "otherInfoCode0", "otherInfoCode1", "otherInfoCode2", "otherInfoCode3",
                            "otherInfoCode4"]
        ignored_fields += drop_down_fields
        ignored_fields += checkbox_fields  # Adding checkbox list to the ignored list
        for element, x_path in t4_drop_down_fields.items():
            if element in ignored_fields:
                continue
            if element in drop_down_fields:
                self.get_element_presence(t4_drop_down_fields[element])
                field_data = self.get_elements(t4_drop_down_fields[element]).text
                assert field_data == expected_dict[element], str(element) + "Value not matched"
            else:
                # self.get_element_presence(t4_elements[element])
                field_data = self.get_elements(t4_drop_down_fields[element]).get_attribute("value")
                assert field_data == expected_dict[element], str(element) + " not matched"
        time.sleep(2)
        self.navigate_sidebar_menu(menu_type='rl1Menu', sub_menu_type='rl1List', expand_compliance=False)
        time.sleep(3)
        self.get_element_presence(merge_elements["row_1_rl1_slip"])
        self.get_elements(merge_elements["row_1_rl1_slip"]).click()
        time.sleep(4)
        """Updating the drop down of RL-1 xpath so we can read the selected option in them"""
        rl1_drop_down_fields = {}
        rl1_drop_down_fields = copy.deepcopy(rl1_elements)
        rl1_drop_down_fields.update(rl1_drop_down_elements)
        self.get_element_presence(rl1_drop_down_fields["city"])
        city = self.get_elements(rl1_drop_down_fields["city"]).get_attribute("value")
        if city == expected_dict_5_rl1["city"]:
            expected_dict5_rl1 = expected_dict_5_rl1
        post_code = self.get_elements(rl1_drop_down_fields["postCode"]).get_attribute("value")
        if post_code == expected_dict_5_rl1["postCode"]:
            expected_dict5_rl1 = expected_dict_5_rl1
        ignored_fields = ["saveButton", "deleteButton", "toastMessage", "closeToast", "dateOfBirth", "cppContribution",
                          "loadEmployee", "loadSlip", "country", "resetButton", "exemptCpp", "exemptEi", "exemptPpip",
                          "amount3", "deleteButton"]
        checkbox_fields = ["eiInsurableCheckbox", "cppPensionableCheckbox"]
        drop_down_fields = ["reflectInMasterData", "province", "payPeriod", "slipType", "poe", "status",
                            "Code (Case O)", "OtherInfo0", "OtherInfo1", "OtherInfo2", "OtherInfo3",
                            ]
        ignored_fields += drop_down_fields
        ignored_fields += checkbox_fields  # Adding checkbox list to the ignored list
        for element, x_path in rl1_drop_down_fields.items():
            if element in ignored_fields:
                continue
            if element in drop_down_fields:
                self.get_element_presence(rl1_drop_down_fields[element])
                field_data = self.get_elements(rl1_drop_down_fields[element]).text
                assert field_data == expected_dict5_rl1[element], str(element) + "Value not matched"
            else:
                # self.get_element_presence(rl1_elements[element])
                field_data = self.get_elements(rl1_drop_down_fields[element]).get_attribute("value")
                assert field_data == expected_dict5_rl1[element], str(element) + " not matched"
        time.sleep(3)
        # delete employee
        self.navigate_sidebar_menu(main_menu="peopleMenu", sub_menu_type="employeeMenu", expand_parent=False)
        time.sleep(3)
        self.get_element_click_able(list_elements["moreActions"])
        self.get_elements(list_elements["moreActions"]).click()
        self.get_element_click_able(merge_elements["unMergeAction"])
        self.get_elements(merge_elements["unMergeAction"]).click()
        time.sleep(3)
        self.get_element_click_able(merge_elements["headerListCheckBox"])
        self.get_elements(merge_elements["headerListCheckBox"]).click()
        time.sleep(2)
        self.get_element_click_able(merge_elements["unMergeButton"])
        self.get_elements(merge_elements["unMergeButton"]).click()
        self.verify_toast_message('unmerge')
        time.sleep(2)
        self.navigate_sidebar_menu(main_menu="peopleMenu", sub_menu_type="employeeMenu", expand_parent=False)
        time.sleep(3)
        self.get_element_click_able(merge_elements["headerListCheckBox"])
        self.get_elements(merge_elements["headerListCheckBox"]).click()
        time.sleep(2)
        self.get_element_click_able(list_elements["deleteBtn"])
        self.get_elements(list_elements["deleteBtn"]).click()
        time.sleep(2)
        self.get_element_click_able(list_elements["OKBtn"])
        self.get_elements(list_elements["OKBtn"]).click()
        self.verify_toast_message('delete')
    
    def test_merge_with_diff_poe(self):
        """
        test to merge employees and t4s of different provinces but both are non-QC and
        To check merged employees appear on un-merged screen
        :return:
        """
        employee_list = EmployeeList(self.driver)
        list_elements = employee_list.employee_list_xpath
        merge_employee = MergeEmployee(self.driver)
        merge_elements = merge_employee.merge_employee_xpath
        t4_setup = T4Setup(self.driver)
        t4_list = T4List(self.driver)
        emp_setup = EmployeeSetup(self.driver)
        emp_setup_elements = emp_setup.employee_xpaths
        t4_elements = t4_setup.t4_xpaths
        t4_list_elements = t4_list.t4_list_xpaths
        test_case1_data = MergeEmployeeData.test_case4_data1
        test_case2_data = MergeEmployeeData.test_case4_data2
        self.get_login()
        self.navigate_sidebar_menu()
        time.sleep(2)
        """Creating the employees to merge"""
        self.get_element_presence(t4_elements["reflectEmployee"])
        for key, value in t4_elements.items():
            if key not in ["loadEmployee", "AddMore", "country", "loadSlip", "saveButton", "toastMessage",
                           "dateOfBirth", "closeToast", "qppContribution", "ppipPremiums", "ppipInsurableEarning",
                           "insurableEarning", "pensionableEarning", "otherInfoCode3",
                           "otherInfoAmount3", "otherInfoCode4", "otherInfoAmount4"] \
                    and "Button" not in key and "Checkbox" \
                    not in key and "exempt" not in key and "pensionablePeriod" not in key:
                try:
                    self.get_elements(value).send_keys(test_case1_data[key])
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
                           "dateOfBirth", "closeToast", "qppContribution", "ppipPremiums", "ppipInsurableEarning",
                           "insurableEarning", "pensionableEarning", "otherInfoCode3",
                           "otherInfoAmount3", "otherInfoCode4", "otherInfoAmount4"] \
                    and "Button" not in key and "Checkbox" not in key \
                    and "exempt" not in key and "pensionablePeriod" not in key:
                try:
                    self.get_elements(value).send_keys(test_case2_data[key])
                except NoSuchElementException:
                    print("otherInfo element not found")
        self.driver.execute_script("window.scrollTo(0, document.body.scrollLength);")
        self.get_element_presence(t4_elements["saveButton"])
        self.get_elements(t4_elements["saveButton"]).click()
        self.verify_toast_message()
        time.sleep(3)

        """merging the employees here"""

        self.go_to_merge_screen()
        self.get_element_click_able(merge_elements["mergeButton"])
        self.get_elements(merge_elements["mergeButton"]).click()
        self.verify_toast_message('unmask')
        self.check_unmaking()
        province = self.get_elements(merge_elements["poe_row1"]).text
        if province != "MB":
            self.get_elements(merge_elements["keep_record_row2"]).click()
        time.sleep(2)
        self.get_element_click_able(list_elements["moreActions"])
        self.get_elements(list_elements["moreActions"]).click()
        self.get_element_click_able(merge_elements["mergeButton"])
        self.get_elements(merge_elements["mergeButton"]).click()
        time.sleep(4)
        """To check merged employees appear on un-merged screen"""
        self.get_element_click_able(list_elements["moreActions"])
        self.get_elements(list_elements["moreActions"]).click()
        self.get_element_click_able(merge_elements["unMergeAction"])
        self.get_elements(merge_elements["unMergeAction"]).click()
        time.sleep(3)
        self.get_element_presence(merge_elements["unmerge_employee_name1"])
        emp_name_1 = self.get_elements(merge_elements["unmerge_employee_name1"]).text
        emp_name_2 = self.get_elements(merge_elements["unmerge_employee_name2"]).text
        sin_no_2 = self.get_elements(merge_elements["unmerge_employee_sin2"]).text
        time.sleep(4)
        # TODO: merge toast message is not shown
        """ Checking the t4 list screen that slips are merged or not"""
        time.sleep(3)
        self.navigate_sidebar_menu(sub_menu_type='t4List')
        self.get_text_prasence_in_element(t4_list_elements["noOfRowsOnPage"], "1-2 of 2")
        no_of_slips = self.get_elements(t4_list_elements["noOfRowsOnPage"]).text
        assert no_of_slips == "1-2 of 2"
        """ Checking the employee list that employees are merged or not also verify the employee merged data"""
        time.sleep(3)
        self.navigate_sidebar_menu(main_menu="peopleMenu", sub_menu_type="employeeMenu", expand_parent=False)
        self.get_text_prasence_in_element(list_elements["noOfRowsOnPage"], "1-1 of 1")
        no_of_employees = self.get_elements(list_elements["noOfRowsOnPage"]).text
        assert no_of_employees == "1-1 of 1"
        self.get_elements(merge_elements["duplicate_slip"]).click()
        self.get_element_presence(emp_setup_elements["firstName"])
        first_name = self.get_elements(emp_setup_elements["firstName"]).get_attribute('value')

        last_name = self.get_elements(emp_setup_elements["lastName"]).get_attribute('value')

        initial_name = self.get_elements(emp_setup_elements["initials"]).get_attribute('value')

        employee_code = self.get_elements(emp_setup_elements["employeeCode"]).get_attribute('value')

        sin = self.get_elements(emp_setup_elements["sin"]).get_attribute('value')

        type = self.get_elements(emp_setup_elements["type"]).get_attribute('value')

        status = self.get_elements(emp_setup_elements["status"]).get_attribute('value')
        time.sleep(3)
        """Delete from employee list"""
        self.delete_merge_emp()

    def test_merge_with_diff_poe_one_QC(self):
        """
        test to merge employees and t4s of different provinces but one QC and other NonQC and
        To check merged employees appear on un-merged screen
        :return:
        """
        rl1_setup = Rl1Setup(self.driver)
        rl1_elements = rl1_setup.rl1_x_paths
        employee_list = EmployeeList(self.driver)
        list_elements = employee_list.employee_list_xpath
        merge_employee = MergeEmployee(self.driver)
        merge_elements = merge_employee.merge_employee_xpath
        t4_setup = T4Setup(self.driver)
        t4_elements = t4_setup.t4_xpaths
        t4_list_elements = T4List.t4_list_xpaths
        emp_setup = EmployeeSetup(self.driver)
        emp_setup_elements = emp_setup.employee_xpaths
        test_case1_data = MergeEmployeeData.test_case4_data1
        test_case3_data_1 = MergeEmployeeData.test_case5_data1
        test_rl1case3_data_1 = MergeEmployeeData.test_rl1_case5_data1
        test_rl1case3_data_2 = MergeEmployeeData.test_rl1_case5_data2
        test_case5_data_2 = MergeEmployeeData.test_case5_data2
        expected_dict = MergeEmployeeData.case5_expected_dict
        expected_dict_3 = MergeEmployeeData.case5_expected_dict_5
        expected_dict5_rl1 = MergeEmployeeData.expected_dict5_rl1
        expected_dict_5_rl1 = MergeEmployeeData.case5_expected_dict_rl1
        user_credentials = Credentials.users_credentials
        self.get_login()
        """Creating the employees to merge"""
        time.sleep(3)
        self.navigate_sidebar_menu()
        time.sleep(2)
        self.get_element_presence(t4_elements["reflectEmployee"])
        for key, value in t4_elements.items():
            if key not in ["loadEmployee", "AddMore", "country", "loadSlip", "saveButton", "toastMessage",
                           "dateOfBirth", "closeToast", "insurableEarning", "pensionableEarning"] \
                    and "Button" not in key and "Checkbox" \
                    not in key and "exempt" not in key and "pensionablePeriod" not in key:
                try:
                    self.get_elements(value).send_keys(test_case3_data_1[key])
                except NoSuchElementException:
                    print("otherInfo element not found")

        self.driver.execute_script("window.scrollTo(0, document.body.scrollLength);")
        self.get_element_presence(t4_elements["saveButton"])
        self.get_elements(t4_elements["saveButton"]).click()
        self.verify_toast_message()
        time.sleep(3)
        self.navigate_sidebar_menu(menu_type='rl1Menu', sub_menu_type='rl1List', expand_compliance=False)
        time.sleep(3)
        self.get_element_presence(merge_elements["row_1_rl1_slip"])
        self.get_elements(merge_elements["row_1_rl1_slip"]).click()
        time.sleep(4)
        rl1_setup.actions = ActionChains(self.driver)
        time.sleep(3)
        rl1_setup.actions.double_click(self.get_elements(rl1_elements["E-Impôt du Québec retenu"])).perform()
        rl1_setup.actions.click(self.get_elements(rl1_elements["E-Impôt du Québec retenu"])).perform()
        self.get_elements(rl1_elements["E-Impôt du Québec retenu"]).send_keys(Keys.BACKSPACE)
        self.get_elements(rl1_elements["E-Impôt du Québec retenu"]).send_keys("1520.21")
        time.sleep(3)
        for key, value in rl1_elements.items():
            if key not in ["loadEmployee", "AddMore", "country", "loadSlip", "saveButton", "toastMessage",
                           "dateOfBirth", "closeToast", "reflectInMasterData", "sin", "firstName", "lastName",
                           "initials", "address", "city", "postCode", "province", "country", "email", "payPeriod",
                           "slipType", "A-Revenus d'emploi", "B-Cotisation au RRQ", "C- Cot. à l'assurance emploi",
                           "D- Cotisation à un RPA", "G-Salaire admissible au RRQ", "H-Cotisation au RQAP",
                           "I-Salaire admissible au RQAP"] \
                    and "Button" not in key and "Checkbox" \
                    not in key and "exempt" not in key and "pensionablePeriod" not in key:
                try:
                    self.get_elements(value).send_keys(test_rl1case3_data_1[key])
                except NoSuchElementException:
                    print("otherInfo element not found")

        self.driver.execute_script("window.scrollTo(0, document.body.scrollLength);")
        self.get_element_presence(rl1_elements["saveButton"])
        self.get_elements(rl1_elements["saveButton"]).click()
        self.verify_toast_message('update')
        time.sleep(3)
        self.navigate_sidebar_menu(menu_type='t4Menu', sub_menu_type='t4Setup', expand_compliance=False)
        time.sleep(3)
        """Creating the employees to merge"""
        self.get_element_presence(t4_elements["reflectEmployee"])
        for key, value in t4_elements.items():
            if key not in ["loadEmployee", "AddMore", "country", "loadSlip", "saveButton", "toastMessage",
                           "dateOfBirth", "closeToast", "qppContribution", "ppipPremiums", "ppipInsurableEarning",
                           "insurableEarning", "pensionableEarning", "otherInfoCode3",
                           "otherInfoAmount3", "otherInfoCode4", "otherInfoAmount4"] \
                    and "Button" not in key and "Checkbox" \
                    not in key and "exempt" not in key and "pensionablePeriod" not in key:
                try:
                    self.get_elements(value).send_keys(test_case1_data[key])
                except NoSuchElementException:
                    print("otherInfo element not found")

        self.driver.execute_script("window.scrollTo(0, document.body.scrollLength);")
        self.get_element_presence(t4_elements["saveButton"])
        self.get_elements(t4_elements["saveButton"]).click()
        self.verify_toast_message()
        time.sleep(3)
        """merging the employees here"""
        self.go_to_merge_screen()
        self.get_element_click_able(merge_elements["mergeButton"])
        self.get_elements(merge_elements["mergeButton"]).click()
        self.verify_toast_message('unmask')
        self.check_unmaking()
        province = self.get_elements(merge_elements["poe_row1"]).text
        if province != "MB":
            self.get_elements(merge_elements["keep_record_row2"]).click()
        time.sleep(2)
        self.get_element_click_able(list_elements["moreActions"])
        self.get_elements(list_elements["moreActions"]).click()
        self.get_element_click_able(merge_elements["mergeButton"])
        self.get_elements(merge_elements["mergeButton"]).click()
        time.sleep(4)
        """To check merged employees appear on un-merged screen"""
        self.get_element_click_able(list_elements["moreActions"])
        self.get_elements(list_elements["moreActions"]).click()
        self.get_element_click_able(merge_elements["unMergeAction"])
        self.get_elements(merge_elements["unMergeAction"]).click()
        time.sleep(3)
        self.get_element_presence(merge_elements["unmerge_employee_name1"])
        emp_name_1 = self.get_elements(merge_elements["unmerge_employee_name1"]).text
        emp_name_2 = self.get_elements(merge_elements["unmerge_employee_name2"]).text
        sin_no_2 = self.get_elements(merge_elements["unmerge_employee_sin2"]).text
        time.sleep(4)
        """ Checking the t4 list screen that slips are merged or not"""
        time.sleep(3)
        self.navigate_sidebar_menu(sub_menu_type='t4List')
        time.sleep(2)
        self.get_text_prasence_in_element(t4_list_elements["noOfRowsOnPage"], "1-2 of 2")
        no_of_slips = self.get_elements(t4_list_elements["noOfRowsOnPage"]).text
        assert no_of_slips == "1-2 of 2"
        """ Checking the employee list that employees are merged or not also verify the employee merged data"""
        time.sleep(3)
        self.navigate_sidebar_menu(main_menu="peopleMenu", sub_menu_type="employeeMenu", expand_parent=False)
        time.sleep(2)
        self.get_text_prasence_in_element(list_elements["noOfRowsOnPage"], "1-1 of 1")
        no_of_employees = self.get_elements(list_elements["noOfRowsOnPage"]).text
        assert no_of_employees == "1-1 of 1"
        self.get_elements(merge_elements["duplicate_slip"]).click()
        self.get_element_presence(emp_setup_elements["firstName"])
        first_name = self.get_elements(emp_setup_elements["firstName"]).get_attribute('value')
        last_name = self.get_elements(emp_setup_elements["lastName"]).get_attribute('value')
        initial_name = self.get_elements(emp_setup_elements["initials"]).get_attribute('value')
        employee_code = self.get_elements(emp_setup_elements["employeeCode"]).get_attribute('value')
        sin = self.get_elements(emp_setup_elements["sin"]).get_attribute('value')
        type = self.get_elements(emp_setup_elements["type"]).get_attribute('value')
        status = self.get_elements(emp_setup_elements["status"]).get_attribute('value')
        time.sleep(3)
        """Delete from employee list"""
        self.delete_merge_emp()

    def test_ignore_employees(self):
        """
        test ignore and un-ignored functionality
        :return:
        """
        employee_list = EmployeeList(self.driver)
        list_elements = employee_list.employee_list_xpath
        merge_employee = MergeEmployee(self.driver)
        merge_elements = merge_employee.merge_employee_xpath
        t4_setup = T4Setup(self.driver)
        t4_list = T4List(self.driver)
        emp_setup = EmployeeSetup(self.driver)
        emp_setup_elements = emp_setup.employee_xpaths
        t4_elements = t4_setup.t4_xpaths
        t4_list_elements = t4_list.t4_list_xpaths
        test_case4_data = MergeEmployeeData.test_case4_data1
        test_case4_data = MergeEmployeeData.test_case4_data2
        user_credentials = Credentials.users_credentials
        self.get_login()
        time.sleep(3)
        self.navigate_sidebar_menu()
        """Creating the employees to ignored"""
        time.sleep(2)
        self.get_element_presence(t4_elements["reflectEmployee"])
        for key, value in t4_elements.items():
            if key not in ["loadEmployee", "AddMore", "country", "loadSlip", "saveButton", "toastMessage",
                           "dateOfBirth", "closeToast", "qppContribution", "ppipPremiums", "ppipInsurableEarning",
                           "insurableEarning", "pensionableEarning", "otherInfoCode3",
                           "otherInfoAmount3", "otherInfoCode4", "otherInfoAmount4"] \
                    and "Button" not in key and "Checkbox" \
                    not in key and "exempt" not in key and "pensionablePeriod" not in key:
                try:
                    self.get_elements(value).send_keys(test_case4_data[key])
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
                           "dateOfBirth", "closeToast", "qppContribution", "ppipPremiums", "ppipInsurableEarning",
                           "insurableEarning", "pensionableEarning", "otherInfoCode3",
                           "otherInfoAmount3", "otherInfoCode4", "otherInfoAmount4"] \
                    and "Button" not in key and "Checkbox" not in key \
                    and "exempt" not in key and "pensionablePeriod" not in key:
                try:
                    self.get_elements(value).send_keys(test_case4_data[key])
                except NoSuchElementException:
                    print("otherInfo element not found")
        self.driver.execute_script("window.scrollTo(0, document.body.scrollLength);")
        self.get_element_presence(t4_elements["saveButton"])
        self.get_elements(t4_elements["saveButton"]).click()
        self.verify_toast_message()
        time.sleep(3)
        """ignored the employees here"""
        self.go_to_merge_screen()
        self.get_element_click_able(merge_elements["ignoreButton"])
        self.get_elements(merge_elements["ignoreButton"]).click()
        self.verify_toast_message('unmask_ignore')
        """To check the sensitive data is masked"""
        self.check_unmaking()
        province = self.get_elements(merge_elements["poe_row1"]).text
        if province != "MB":
            self.get_elements(merge_elements["keep_record_row2"]).click()
        time.sleep(2)
        self.get_element_click_able(list_elements["moreActions"])
        self.get_elements(list_elements["moreActions"]).click()
        self.get_element_click_able(merge_elements["ignoreButton"])
        self.get_elements(merge_elements["ignoreButton"]).click()
        self.verify_toast_message('ignore')
        time.sleep(4)
        """To check ignore employees appear on ignored employee screen"""
        self.get_element_click_able(list_elements["moreActions"])
        self.get_elements(list_elements["moreActions"]).click()
        self.get_element_click_able(merge_elements["ignoreEmployee"])
        self.get_elements(merge_elements["ignoreEmployee"]).click()
        time.sleep(3)
        self.get_element_presence(merge_elements["ignored_employee_name1"])
        emp_name_1 = self.get_elements(merge_elements["ignored_employee_name1"]).text
        emp_name_2 = self.get_elements(merge_elements["ignored_employee_name2"]).text
        assert emp_name_1, emp_name_2 == "not matched"
        """To check un ignore functionality"""
        time.sleep(3)
        self.get_elements(merge_elements["headerListCheckBox"]).click()
        self.get_element_presence(merge_elements["un_ignore_button"])
        self.get_elements(merge_elements["un_ignore_button"]).click()
        self.verify_toast_message('un_ignore')
        time.sleep(3)
        self.get_element_click_able(list_elements["moreActions"])
        self.get_elements(list_elements["moreActions"]).click()
        self.get_element_click_able(list_elements["mergeEmployee"])
        self.get_elements(list_elements["mergeEmployee"]).click()
        self.get_element_presence(merge_elements["merge_employee_name1"])
        emp_name_1 = self.get_elements(merge_elements["merge_employee_name1"]).text
        emp_name_2 = self.get_elements(merge_elements["merge_employee_name2"]).text
        assert emp_name_1, emp_name_2 == "not matched"
        """To check the delete functionality from employee list"""
        self.navigate_sidebar_menu(main_menu="peopleMenu", sub_menu_type="employeeMenu", expand_parent=False)
        time.sleep(3)
        self.get_element_click_able(merge_elements["headerListCheckBox"])
        self.get_elements(merge_elements["headerListCheckBox"]).click()
        time.sleep(2)
        self.get_element_click_able(list_elements["deleteBtn"])
        self.get_elements(list_elements["deleteBtn"]).click()
        time.sleep(2)
        self.get_element_click_able(list_elements["OKBtn"])
        self.get_elements(list_elements["OKBtn"]).click()
        self.verify_toast_message('delete')

    def test_merge_with_insurable_pensionable_within_limit(self):
        """
        test to merge t4s with same poe, EI insurable and cpp Pensionable earnings dose not reach there max limit
        :return:
        """
        employee_list = EmployeeList(self.driver)
        list_elements = employee_list.employee_list_xpath
        merge_employee = MergeEmployee(self.driver)
        merge_elements = merge_employee.merge_employee_xpath
        t4_setup = T4Setup(self.driver)
        t4_elements = t4_setup.t4_xpaths
        t4_drop_down_elements = t4_setup.drop_down_xpath
        test_case1_data = MergeEmployeeData.testCase3Data1
        test_case2_data = MergeEmployeeData.testCase3Data2
        expected_dict = MergeEmployeeData.case3_expected_dict
        expected_dict_2 = MergeEmployeeData.case3_expected_dict_2
        self.get_login()
        time.sleep(2)
        self.navigate_sidebar_menu()
        """Creating the employees to merge"""
        time.sleep(2)
        self.get_element_presence(t4_elements["reflectEmployee"])
        for key, value in t4_elements.items():
            if key not in ["loadEmployee", "AddMore", "country", "loadSlip", "saveButton", "toastMessage",
                           "dateOfBirth", "closeToast", "qppContribution", "ppipPremiums",
                           "ppipInsurableEarning", "insurableEarning", "pensionableEarning"] \
                    and "Button" not in key and "Checkbox" \
                    not in key and "exempt" not in key and "pensionablePeriod" not in key:
                try:
                    self.get_elements(value).send_keys(test_case1_data[key])
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
                           "dateOfBirth", "closeToast", "qppContribution", "ppipPremiums",
                           "ppipInsurableEarning", "insurableEarning", "pensionableEarning", "otherInfoCode3",
                           "otherInfoAmount3", "otherInfoCode4", "otherInfoAmount4"] \
                    and "Button" not in key and "Checkbox" not in key \
                    and "exempt" not in key and "pensionablePeriod" not in key:
                try:
                    self.get_elements(value).send_keys(test_case2_data[key])
                except NoSuchElementException:
                    print("otherInfo element not found")
        self.driver.execute_script("window.scrollTo(0, document.body.scrollLength);")
        self.get_element_presence(t4_elements["saveButton"])
        self.get_elements(t4_elements["saveButton"]).click()
        self.verify_toast_message()
        time.sleep(3)
        """merging the employees here"""
        self.go_to_merge_screen()
        self.get_element_click_able(merge_elements["mergeButton"])
        self.get_elements(merge_elements["mergeButton"]).click()
        self.verify_toast_message('unmask')
        self.check_unmaking()
        time.sleep(2)
        self.get_element_click_able(merge_elements["mergeButton"])
        self.get_elements(merge_elements["mergeButton"]).click()
        time.sleep(2)
        self.verify_toast_message('merge')
        self.get_element_click_able(list_elements["moreActions"])
        self.get_elements(list_elements["moreActions"]).click()
        self.get_element_click_able(merge_elements["unMergeAction"])
        self.get_elements(merge_elements["unMergeAction"]).click()
        time.sleep(3)
        self.navigate_sidebar_menu(sub_menu_type='t4List')
        self.get_element_presence(merge_elements["duplicate_slip"])
        time.sleep(4)
        self.get_elements(merge_elements["duplicate_slip"]).click()
        time.sleep(2)
        # Updating the drop down xpath so we can read the selected option in them
        """Comparing the merged employees with expected data dict"""
        t4_drop_down_fields = {}
        t4_drop_down_fields = copy.deepcopy(t4_elements)
        t4_drop_down_fields.update(t4_drop_down_elements)
        self.get_element_presence(t4_drop_down_fields["city"])
        city = self.get_elements(t4_drop_down_fields["city"]).get_attribute("value")
        if city == expected_dict_2["city"]:
            expected_dict = expected_dict_2
        ignored_fields = ["saveButton", "toastMessage", "closeToast", "dateOfBirth", "deleteButton",
                          "qppContribution", "ppipPremiums", "ppipInsurableEarning",
                          "loadEmployee", "resetButton", "exemptCpp", "exemptEi", "exemptPpip"]
        checkbox_fields = ["eiInsurableCheckbox", "cppPensionableCheckbox"]
        drop_down_fields = ["reflectEmployee", "province", "payPeriod", "slipType", "poe", "reducedEi", "status",
                            "employmentCode", "otherInfoCode0", "otherInfoCode1", "otherInfoCode2", "otherInfoCode3",
                            "otherInfoCode4"]
        # ignored_fields += drop_down_fields
        ignored_fields += checkbox_fields  # Adding checkbox list to the ignored list
        for element, x_path in t4_drop_down_fields.items():
            if element in ignored_fields:
                continue
            if element in drop_down_fields:
                # self.get_element_presence(t4_elements2[element])
                field_data = self.get_elements(t4_drop_down_fields[element]).text
                assert field_data == expected_dict[element], str(element) + "Value not matched"
            else:
                self.get_element_presence(t4_drop_down_fields[element])
                field_data = self.get_elements(t4_drop_down_fields[element]).get_attribute("value")
                assert field_data == expected_dict[element], str(element) + " not matched"
        """Delete from employee list"""
        self.delete_merge_emp()

    def test_merge_employees_non_qc(self):
        """
        Test Case No. TC-2
        test to duplicate only t4s with same POE(Non-Qc), mask info and merge duplicate employees,
         unmerge employee and delete emp
        :return:
        """
        employee_list = EmployeeList(self.driver)
        list_elements = employee_list.employee_list_xpath
        merge_employee = MergeEmployee(self.driver)
        merge_elements = merge_employee.merge_employee_xpath
        t4_setup = T4Setup(self.driver)
        t4_elements = t4_setup.t4_xpaths
        t4_drop_down_elements = t4_setup.drop_down_xpath
        test_case3_data_1 = MergeEmployeeData.test_case1_data1
        test_case5_data_2 = MergeEmployeeData.test_case1_data2
        expected_dict = MergeEmployeeData.case1_expected_dict
        expected_dict_3 = MergeEmployeeData.case1_expected_dict_2
        self.get_login()
        """Creating the employees to merge"""
        time.sleep(3)
        self.navigate_sidebar_menu()
        time.sleep(2)
        self.get_element_presence(t4_elements["reflectEmployee"])
        for key, value in t4_elements.items():
            if key not in ["loadEmployee", "AddMore", "country", "loadSlip", "saveButton", "toastMessage",
                           "dateOfBirth", "closeToast", "ppipPremiums", "ppipInsurableEarning", "insurableEarning",
                           "pensionableEarning", "qppContribution"] \
                    and "Button" not in key and "Checkbox" \
                    not in key and "exempt" not in key and "pensionablePeriod" not in key:
                try:
                    self.get_elements(value).send_keys(test_case3_data_1[key])
                except NoSuchElementException:
                    print("otherInfo element not found")

        self.driver.execute_script("window.scrollTo(0, document.body.scrollLength);")
        self.get_element_presence(t4_elements["saveButton"])
        self.get_elements(t4_elements["saveButton"]).click()
        self.verify_toast_message()
        time.sleep(2)
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
                           "dateOfBirth", "closeToast", "insurableEarning", "pensionableEarning", "otherInfoCode3",
                           "otherInfoAmount3", "otherInfoCode4", "otherInfoAmount4", "ppipPremiums",
                           "ppipInsurableEarning", "qppContribution"] \
                    and "Button" not in key and "Checkbox" \
                    not in key and "exempt" not in key and "pensionablePeriod" not in key:
                try:
                    self.get_elements(value).send_keys(test_case5_data_2[key])
                except NoSuchElementException:
                    print("otherInfo element not found")

        self.driver.execute_script("window.scrollTo(0, document.body.scrollLength);")
        self.get_element_presence(t4_elements["saveButton"])
        self.get_elements(t4_elements["saveButton"]).click()
        self.verify_toast_message()
        """merging the employees here """
        self.go_to_merge_screen()
        self.get_element_click_able(merge_elements["mergeButton"])
        self.get_elements(merge_elements["mergeButton"]).click()
        self.verify_toast_message('unmask')
        """checking mask info"""
        self.check_unmaking()
        time.sleep(2)
        self.get_element_click_able(merge_elements["mergeButton"])
        self.get_elements(merge_elements["mergeButton"]).click()
        time.sleep(2)
        self.verify_toast_message('merge')
        time.sleep(3)
        """To verify the merge employees and slips data"""
        self.navigate_sidebar_menu(sub_menu_type='t4List')
        time.sleep(2)
        self.get_element_presence(merge_elements["duplicate_slip"])
        time.sleep(4)
        self.get_elements(merge_elements["duplicate_slip"]).click()
        time.sleep(2)
        """Updating the drop down of t4 xpath so we can read the selected option in them"""
        t4_drop_down_fields = {}
        t4_drop_down_fields = copy.deepcopy(t4_elements)
        t4_drop_down_fields.update(t4_drop_down_elements)
        self.get_element_presence(t4_drop_down_fields["city"])
        city = self.get_elements(t4_drop_down_fields["city"]).get_attribute("value")
        if city == expected_dict_3["city"]:
            expected_dict = expected_dict_3
        post_code = self.get_elements(t4_drop_down_fields["postCode"]).get_attribute("value")
        if post_code == expected_dict_3["postCode"]:
            expected_dict = expected_dict_3
        ignored_fields = ["saveButton", "toastMessage", "closeToast", "dateOfBirth", "cppContribution",
                          "loadEmployee", "resetButton", "exemptCpp", "exemptEi", "exemptPpip", "ppipPremiums",
                          "ppipInsurableEarning", "qppContribution", "deleteButton"]
        checkbox_fields = ["eiInsurableCheckbox", "cppPensionableCheckbox"]
        drop_down_fields = ["reflectEmployee", "province", "payPeriod", "slipType", "poe", "reducedEi", "status",
                            "employmentCode", "otherInfoCode0", "otherInfoCode1", "otherInfoCode2", "otherInfoCode3",
                            "otherInfoCode4"]
        ignored_fields += drop_down_fields
        ignored_fields += checkbox_fields  # Adding checkbox list to the ignored list
        for element, x_path in t4_drop_down_fields.items():
            if element in ignored_fields:
                continue
            if element in drop_down_fields:
                self.get_element_presence(t4_drop_down_fields[element])
                field_data = self.get_elements(t4_drop_down_fields[element]).text
                assert field_data == expected_dict[element], str(element) + "Value not matched"
            else:
                # self.get_element_presence(t4_elements[element])
                field_data = self.get_elements(t4_drop_down_fields[element]).get_attribute("value")
                assert field_data == expected_dict[element], str(element) + " not matched"

        time.sleep(3)
        """Delete from employee list"""
        self.delete_merge_emp()
