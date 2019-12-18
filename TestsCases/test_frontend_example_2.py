import pytest
from selenium.webdriver import Chrome


@pytest.fixture(scope="module")  # For all test cases in this module
def setPath():
    global driver
    path = "C:\\git\\api-testing-python-allure\\Resources\\chromedriver.exe"
    driver = Chrome(executable_path=path)
    yield  # call for after the test case execution
    driver.close()
    driver.quit()


def test_execute_frontend_example2(setPath):
    driver.get("http://www.thetestingworld.com/testing")
    driver.maximize_window()
    assert driver.current_url == "https://www.thetestingworld.com/testing"


def test_skip_frontend_example2(setPath):
    driver.get("http://www.thetestingworld.com/testing")
    assert driver.title == "Testing World Experienced in making experts"
