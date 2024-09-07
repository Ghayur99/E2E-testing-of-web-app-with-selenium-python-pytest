"""T4A list objects are define here"""
from page_objects.common_objects import CommonObjects


class T4aList(CommonObjects):
    """This class contains webElements of T4A list """
    t4a_list_xpaths ={
        "createSlip": "//span[contains(text(),'Create Slip')]",
        "testMask": "//*[contains(text(),'test Masking')]",
        }





