import pytest
from selenium.webdriver import Chrome

@pytest.fixture()
def environment_setup():
    global driver
    path = "C:\\git\\api-testing-python-allure\\Resources\\chromedriver.exe"
    driver = Chrome(executable_path=path)
    driver.get("https://www.thetestingworld.com/testing")
    driver.maximize_window()
    driver.
    yield
    driver.close()


def test_execute_frontend_example3(environment_setup):
    driver.find_element_by_xpath('//*[@id="menu498"]/span').click()
