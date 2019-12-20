import pytest
import Utils.Driver
import Utils.ContactUsPage
from selenium.webdriver import Chrome

global contactUsPage
contactUsPage = Utils.ContactUsPage


@pytest.fixture()
def environment_setup():
    global driver
    driver = Utils.Driver.Driver.driver.get_instance()
    yield
    driver.close_browser()


def test_execute_frontend_example4(environment_setup):
    driver