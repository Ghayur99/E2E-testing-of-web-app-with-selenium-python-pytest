"""Dashboard page elements are define here"""

from page_objects.common_objects import CommonObjects


class Dashboard(CommonObjects):
    """This class contains webElements of dashboard page """

    dashboard_X_paths = {
                        "t4a": "//body/div[@id='__nuxt']/div[@id='__layout']/div[@id='inspire']/div[1]/main[1]/div[1]"
                               "/div[1]/div[1]/div[3]/div[3]/div[1]/div[2]/div[1]/a[2]/div[1]/div[2]/div[1]",
                        "rl1": "//body/div[@id='__nuxt']/div[@id='__layout']/div[@id='inspire']/div[1]/main[1]/div[1]"
                               "/div[1]/div[1]/div[3]/div[3]/div[1]/div[2]/div[1]/a[3]/div[1]/div[2]/div[1]"
                        }


