"""RL-1 list objects are define here"""
from page_objects.common_objects import CommonObjects


class Rl1List(CommonObjects):
    """This class contains webElements of Rl_1 list """
    rl1_list_xpaths ={
        "createSlip": "//span[contains(text(),'Create Slip')]",
        "testMask": "//*[contains(text(),'test Masking')]",
        }
