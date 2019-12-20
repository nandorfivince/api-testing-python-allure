from selenium.webdriver.common.by import By

import Utils.Driver


class OurBlogPage:
    blog_dictionary_map = dict(
        {
            'Our_Blog_Btn': '#menu496',
            'Page_Header_Title': '//*[@id="ja-masshead"]/div/h3/span',
        }
    )

    def get_locator_from_my_dict(self, elemkey):
        locator = dict.get(elemkey)
        if str(locator).__contains__("//"):
            return Utils.Driver.Driver.get_instance().find_element(By.XPATH, elemkey)
        else:
            return Utils.Driver.Driver.get_instance().find_element(By.CSS_SELECTOR, elemkey)
