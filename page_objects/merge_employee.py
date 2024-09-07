from page_objects.common_objects import CommonObjects

class MergeEmployee(CommonObjects):
    """This class contains webElements of merge employee page"""
    merge_employee_xpath = {
        "headerListCheckBox": "//thead/tr[1]/th[1]/div[1]/i[1]",
        "mergeButton": "//button[contains(text(),'Merge')]",
        "toastMessage": "//div[@class='toast-body']",
        "closeToast": "//button[contains(text(),'×')]",
        "sin": "//tbody/tr[1]/td[4]",
        "mergeToastMsg": "//div[@class='toast-body']",
        "unMergeAction": "//small[contains(text(),'Un-Merge Employee')]",
        "unMergeButton": "//button[contains(text(),'Un Merge')]",
        "ignoreButton": "//button[contains(text(),'Ignore')]",
        "un_ignore_button": "//button[contains(text(),'Un Ignored')]",
        "ignoreEmployee": "//small[contains(text(),'Ignored Employee')]",
        "duplicate_slip": "//div[contains(text(),'Zahid Badar')]",
        "row_1_rl1_slip": "//tbody/tr[1]/td[3]/div[1]",
        "row_2_rl1_slip": "//tbody/tr[2]/td[3]/div[1]",
        "keep_record_row1": "//tbody/tr[1]/td[3]/div[1]/div[1]/div[1]",
        "poe_row1": "//tbody/tr[1]/td[9]",
        "keep_record_row2": "//tbody/tr[1]/td[3]/div[1]/div[1]/div[1]",
        "unmerge_employee_name1": "//tbody/tr[1]/td[2]/div[1]",
        "unmerge_employee_name2": "//tbody/tr[2]/td[2]/div[1]",
        "unmerge_employee_sin2": "//td[contains(text(),'990-000-010')]",
        "ignored_employee_name1": "//tbody/tr[1]/td[2]/div[1]",
        "ignored_employee_name2": "//tbody/tr[2]/td[2]/div[1]",
        "merge_employee_name1": "//tbody/tr[1]/td[2]/div[1]/span[1]",
        "merge_employee_name2": "//tbody/tr[2]/td[2]/div[1]/span[1]",
        "slip_status": "//tbody/tr[1]/td[8]"

    }
