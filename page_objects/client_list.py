"""Client list page elements are define here"""

from page_objects.common_objects import CommonObjects
from settings.development import CLIENT_XPATH


class ClientList(CommonObjects):
    """This class contains webElements of client list page """

    clint_list_x_paths = {"addClintButton": "//span[contains(text(),'Add Client')]",
                          "testCompany": CLIENT_XPATH}

    client_xpaths = {"addClient": "//span[contains(text(),'Add Client')]",
                     "searchList": "//input[@id='input-72']",
                     "filterBtn": "//button[@id='__BVID__65__BV_toggle_']",
                     "testCompany": CLIENT_XPATH,
                     "Email": "//input[@id='id_email']",
                     "Password": "//input[@id='id_password']",
                     "Submit": "//button[@type='submit']",
                     }
