"""
This file consists of base class in which all the common functions are written
"""
import inspect
import logging
import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from page_objects.common_objects import CommonObjects
from page_objects.dashboard import Dashboard
from page_objects.employee_list import EmployeeList
from page_objects.employee_setup import EmployeeSetup
from page_objects.merge_employee import MergeEmployee
from page_objects.sidebar_menu import SidebarMenu
from page_objects.t4a_list import T4aList
from page_objects.vendor_list import VendorList
from test_data.credentials import Credentials
from page_objects.client_list import ClientList
from page_objects.header import Header
from page_objects.login_page import LoginPage


@pytest.mark.usefixtures("setup")
class BaseClass:
    """Baseclass consists of all the common functions used in the framework """

    def get_text_prasence(self, text, seconds=15):
        """

        :param text:
        :param seconds:
        :return:
        """
        wait = WebDriverWait(self.driver, seconds)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))

    def get_text_prasence_in_element(self, Xpath, text, seconds=15):
        """

        :param Xpath:
        :param text:
        :param seconds:
        :return:
        """

        wait = WebDriverWait(self.driver, seconds)
        wait.until(expected_conditions.text_to_be_present_in_element((By.XPATH, Xpath), text))

    def get_element_presence(self, Xpath, seconds=20):
        """

        :param Xpath:
        :param seconds:
        :return:
        """

        wait = WebDriverWait(self.driver, seconds)
        wait.until(expected_conditions.presence_of_element_located((By.XPATH, Xpath)))

    def get_element_click_able(self, Xpath, seconds=20):
        """

        :param Xpath:
        :param seconds:
        :return:
        """
        wait = WebDriverWait(self.driver, seconds)
        wait.until(expected_conditions.element_to_be_clickable((By.XPATH, Xpath)))

    def get_element_text_readable(self, Xpath, seconds=15):
        """

        :param Xpath:
        :param seconds:
        :return:
        """
        wait = WebDriverWait(self.driver, seconds)
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, Xpath)))

    def select_options_by_text(self, locator, text):
        """

        :param locator:
        :param text:
        :return:
        """

        # function to select an option in dropDown based on his locator and text
        sel = Select(locator)
        sel.select_by_visible_text(text)

    def test_logging(self):
        """
        For log files
        :return:
        """
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        file_handler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s : %(message)s")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)  # file handler object
        logger.setLevel(logging.DEBUG)
        return logger

    def get_visibility_element(self, Xpath, seconds=15):
        """
        Expected clickable element wait
         aram Xpath: locating clickable element
        :return:
        """
        wait = WebDriverWait(self.driver, seconds)
        wait.until(expected_conditions.visibility_of_any_elements_located((By.XPATH, Xpath)))
    def get_stale_element(self, Xpath, seconds=15):
        """
        Expected clickable element wait
         aram Xpath: locating clickable element
        :return:
        """
        wait = WebDriverWait(self.driver, seconds)
        wait.until(expected_conditions.staleness_of((By.XPATH, Xpath)))

    def get_current_url(self):
        """
        To get the current URL of the screen
        :return:
        """
        return self.driver.current_url

    def clear_entire_text(self):
        """
        To clear any text from the field
        :return:
        """
        self.send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)

    def get_login(self):
        """
        used for login into the app
        """
        user_credentials = Credentials.users_credentials
        login_page = LoginPage(self.driver)
        login_elements = login_page.login_xpaths
        client_list = ClientList(self.driver)
        client_list_elements = client_list.clint_list_x_paths
        header_setup = Header(self.driver)
        header_elements = header_setup.Xpaths

        if self.get_current_url() != "https://app.taxslips.com/#/login":
            self.get_element_click_able(header_elements["accountOptions"], 20)
            self.get_elements(header_elements["accountOptions"]).click()

            self.get_element_presence(header_elements["Logout"], 20)
            element = self.get_elements(header_elements["Logout"])
            self.driver.execute_script("arguments[0].click();", element)

        time.sleep(2)
        self.driver.get("https://app.taxslips.com/#/login")
        self.get_element_presence(login_elements['email'])
        self.get_elements(login_elements['email']).send_keys(user_credentials['loginEmail'])
        self.get_elements(login_elements['passwordField']).send_keys(user_credentials['password'])
        self.get_elements(login_elements['signInButton']).click()
        # time.sleep(2)
        self.get_element_click_able(client_list_elements['testCompany'])
        self.get_elements(client_list_elements['testCompany']).click()

    def get_elements(self, element_path):
        """
        To get the elements from the dictionary
        :param element_path: Xpath of the element will be entered as parameter
        :return:
        """
        return self.driver.find_element(*(By.XPATH, element_path))
    
    def delete_merge_emp(self):
        """
        Used to delete the merge employees against merge test cases
        """
        employee_list = EmployeeList(self.driver)
        list_elements = employee_list.employee_list_xpath
        merge_employee = MergeEmployee(self.driver)
        merge_elements = merge_employee.merge_employee_xpath

        """Delete from employee list"""
        self.navigate_sidebar_menu(main_menu="peopleMenu", sub_menu_type="employeeMenu", expand_parent=False)
        time.sleep(3)
        self.get_element_click_able(list_elements["moreActions"])

        self.get_elements(list_elements["moreActions"]).click()
        self.get_element_presence(merge_elements["unMergeAction"])
        self.get_elements(merge_elements["unMergeAction"]).click()
        time.sleep(3)
        self.get_element_presence(merge_elements["headerListCheckBox"])
        self.get_elements(merge_elements["headerListCheckBox"]).click()
        self.get_element_presence(merge_elements["unMergeButton"])
        self.get_elements(merge_elements["unMergeButton"]).click()

        # TODO: Toast is not shown if user unmerge the employees
       
        time.sleep(2)
        self.navigate_sidebar_menu(main_menu="peopleMenu", sub_menu_type="employeeMenu", expand_parent=False)

        time.sleep(3)
        self.get_element_click_able(merge_elements["headerListCheckBox"])
        self.get_elements(merge_elements["headerListCheckBox"]).click()
        time.sleep(3)
        self.get_element_click_able(list_elements["deleteBtn"])
        self.get_elements(list_elements["deleteBtn"]).click()
        time.sleep(3)
        self.get_element_click_able(list_elements["OKBtn"])
        self.get_elements(list_elements["OKBtn"]).click()
        self.verify_toast_message('delete')

    def get_invisibility_element(self, Xpath, seconds=15):
        """
        wait until elements gets invisible
        :param Xpath:
        :param seconds:
        :return:
        """
        wait = WebDriverWait(self.driver, seconds)
        wait.until(expected_conditions.visibility_of_any_elements_located((By.XPATH, Xpath)))

    def get_elements_in_list(self, Xpath):
        """
        wait until elements gets invisible
        :param Xpath:
        :return:
        """
        return self.driver.find_elements(*(By.XPATH, Xpath))

    def get_wait_until_url_changes(self, URL, seconds=15):
        """

        :param Xpath:
        :param seconds:
        :return:
        """
        wait = WebDriverWait(self.driver, seconds)
        wait.until(expected_conditions.url_changes((By.XPATH, URL)))

    def unmask_data(self):
        """
        This is used for unmask sensitive data
        """
        header_setup = Header(self.driver)
        header_elements = header_setup.Xpaths
        user_credentials = Credentials.users_credentials
        self.get_element_click_able(header_elements['maskButton'])
        self.get_elements(header_elements['maskButton']).click()
        self.get_element_presence(header_elements['unmaskPassword'])
        self.get_elements(header_elements['unmaskPassword']).send_keys(user_credentials['password'])
        self.get_elements(header_elements['verifyButton']).click()
        time.sleep(2)

    def check_unmaking(self):
        """To check masking of sensitive data, verify the data and unmask that data"""
        header_setup = Header(self.driver)
        header_elements = header_setup.Xpaths
        merge_employee = MergeEmployee(self.driver)
        merge_elements = merge_employee.merge_employee_xpath
        user_credentials = Credentials.users_credentials
        self.get_element_presence(merge_elements["sin"])
        checkMasking = self.get_elements(header_elements['maskButton']).text
        if checkMasking == "Unmask":
            sin_masked = self.get_elements(merge_elements["sin"]).text
            assert "***" in sin_masked, "sin number is not masked"

        else:
            self.get_elements(header_elements['maskButton']).click()
            sin_masked = self.get_elements(merge_elements['sin']).get_attribute("value")
            assert "**" in sin_masked, "sin number is not masked"
        self.get_elements(header_elements['maskButton']).click()
        self.get_element_presence(header_elements['unmaskPassword'])
        self.get_elements(header_elements['unmaskPassword']).send_keys(user_credentials['password'])
        self.get_elements(header_elements['verifyButton']).click()
        time.sleep(2)
        sin_masked = self.get_elements(merge_elements["sin"]).text
        assert "990-000-010" == sin_masked, "sin number is not unmasked"
        time.sleep(2)

    def go_to_create_t4a(self):
        """
        This is used to create t4a slip
        """
        dashboard_obj = Dashboard(self.driver)
        t4a_list = T4aList(self.driver)
        dashboard_elements = dashboard_obj.dashboard_X_paths
        t4a_list_elements = t4a_list.t4a_list_xpaths
        self.get_element_click_able(dashboard_elements['t4a'], 10)
        self.get_elements(dashboard_elements['t4a']).click()
        self.get_element_click_able(t4a_list_elements['createSlip'], 10)
        self.get_elements(t4a_list_elements['createSlip']).click()

    def go_to_merge_screen(self):
        """
        This is used to for going to merge screen
        """
        employee_list = EmployeeList
        list_elements = employee_list.employee_list_xpath
        merge_employee = MergeEmployee(self.driver)
        merge_elements = merge_employee.merge_employee_xpath
        self.navigate_sidebar_menu(main_menu="peopleMenu", sub_menu_type="employeeMenu", expand_parent=False)
        self.get_element_click_able(list_elements["moreActions"])
        self.get_elements(list_elements["moreActions"]).click()
        self.get_element_click_able(list_elements["mergeEmployee"])
        self.get_elements(list_elements["mergeEmployee"]).click()
        time.sleep(4)
        self.get_element_click_able(merge_elements["headerListCheckBox"])
        self.get_elements(merge_elements["headerListCheckBox"]).click()
        time.sleep(3)

    def go_to_add_vendor(self):
        """
        This is used to create vendor
        """
        vendor_list = VendorList(self.driver)
        vendorList_elements = vendor_list.vendor_list_Xpaths
        self.navigate_sidebar_menu(main_menu="peopleMenu", sub_menu_type="vendorMenu", expand_parent=False)
        self.get_element_click_able(vendorList_elements["addVendor"])
        self.get_elements(vendorList_elements["addVendor"]).click()

    def go_to_add_employee(self):
        """
        This is used to create employee
        """
        employee_setup = EmployeeSetup(self.driver)
        employee_elements = employee_setup.employee_xpaths
        self.navigate_sidebar_menu(main_menu="peopleMenu", sub_menu_type="employeeMenu", expand_parent=False)
        self.get_element_click_able(employee_elements["addEmployee"])
        self.get_elements(employee_elements["addEmployee"]).click()

    def verify_toast_message(self, toast_type='added'):
        """
        This is used to verify toast messages i.e. add, delete, update, etc.
        """
        common_obj = CommonObjects(self.driver)
        global_paths = common_obj.global_xpath
        message = ''
        if toast_type == 'added':
            message = 'Record has been added successfully.'
        elif toast_type == 'update':
            message = 'Record has been updated successfully.'
        elif toast_type == 'updated':
            message = 'Record has been updated.'
        elif toast_type == 'delete':
            message = 'Record deleted successfully'
        elif toast_type == 'unmask':
            message = 'Please Unmask sensitive data for merge record(s).'
        elif toast_type == 'merge':
            message = 'Merge employees successfully.'
        elif toast_type == 'unmerge':
            message = 'Un Merge employees successfully.'
        elif toast_type == 'unmask_ignore':
            message = 'Please Unmask sensitive data for ignore record(s).'
        elif toast_type == 'ignore':
            message = 'Record as ignored successfully'
        elif toast_type == 'un_ignore':
            message = 'Record as un ignored successfully'
        elif toast_type == 'unmask_xml':
            message = 'Please Unmask sensitive data for XML generation.'
        elif toast_type == 'unmask_print':
            message = 'Please Unmask sensitive data for PDF printing.'

        self.get_text_prasence_in_element(global_paths['toastMessage'], message)
        success_message = self.get_elements(global_paths['toastMessage']).text
        assert success_message == message, "Alert is not shown"
        self.get_visibility_element(global_paths['closeToast'])
        self.get_elements(global_paths['closeToast']).click()

    def navigate_sidebar_menu(self, main_menu="complianceMenu", menu_type='t4Menu',
                              sub_menu_type='t4Setup', expand_compliance=True, expand_parent=True):
        """
        :param main_menu: pass the top level menu x paths key defined in page object side bar to expand the menu
        :param menu_type: pass the 2nd level expandable menu x path key
        :param sub_menu_type: pass the clickable menu x path which navigate to the page
        :param expand_compliance: True in case when needs to expand top level menu False other wise
        :param expand_parent: True in case when needs to expand 2nd level menu False otherwise
        :return: void navigate to the desired menu
        """
        side_menu = SidebarMenu(self.driver)
        menu_element = side_menu.menu_xpaths
        if expand_compliance:
            self.get_element_click_able(menu_element[main_menu])
            self.get_elements(menu_element[main_menu]).click()

        if expand_parent:
            self.get_element_click_able(menu_element[menu_type])
            self.get_elements(menu_element[menu_type]).click()

        self.get_element_click_able(menu_element[sub_menu_type])
        self.get_elements(menu_element[sub_menu_type]).click()
