from selenium.webdriver.common.by import By

import Utils.Driver


class ContactPage:
    contact_dictionary_map = dict(
        {
            'Contact_Us_Btn': '#menu498 > span',
            'Corporate_Training': '//*[@id="Mod109"]/div/div/div/ul/li[1]/a',
            'Campus_Training': '#Mod109 > div > div > div > ul > li.icon-2 > a'
        }
    )

    # https://selenium-python.readthedocs.io/locating-elements.html
    def get_locator_from_my_dict(self, elemkey):
        locator = dict.get(elemkey)
        if str(locator).__contains__("//"):
            return Utils.Driver.Driver.get_instance().find_element(By.XPATH, elemkey)
            # return Utils.Driver.Driver.get_instance().find_element_by_xpath()
        else:
            return Utils.Driver.Driver.get_instance().find_element(By.CSS_SELECTOR, elemkey)
            # return Utils.Driver.Driver.get_instance().find_element_by_css_selector()

