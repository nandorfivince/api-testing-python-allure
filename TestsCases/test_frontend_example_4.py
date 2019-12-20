import pytest

import Utils.ContactUsPage
import Utils.Driver

global contactUsPage
contactUsPage = Utils.ContactUsPage


@pytest.fixture()
def environment_setup():
    global driver
    driver = Utils.Driver.Driver.driver.get_instance()
    yield
    driver.close_browser()


def test_execute_frontend_example4(environment_setup):
    contactUsPage.get_locator_from_my_dict("Contact_Us_Btn").click()
