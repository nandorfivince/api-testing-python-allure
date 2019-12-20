import os
import time

from selenium import webdriver

import Utils.UrlDataProvider


class Driver:
    global CHROME_DRIVER_SERVER_LOCATION
    global driver

    CHROME_DRIVER_SERVER_LOCATION = "C:\\git\\api-testing-python-allure\\Resources\\chromedriver.exe"
    driver = None

    def get_instance(self):
        if os.getenv("browser") is not None:
            if os.getenv("browser") is "Chrome":
                driver = webdriver.Chrome(executable_path=CHROME_DRIVER_SERVER_LOCATION)
                driver.implicitly_wait(10)
                driver.get(Utils.UrlDataProvider.BASE_URL)
        driver.maximize_window()
        time.sleep(2)
        return driver

    def close_browser(self, driver):
        driver.close()
        driver.quit()
