from selenium.webdriver import Chrome
import pytest

skipifvar = 10
# exec command for group: pytest -m Smoke
# exec command for spec tc: pytest -k test_execute_frontend_example
# exec command for all expect tc: pytest -m "not Sanity"

@pytest.fixture(scope="module")  # For all test cases in this module
def setPath():
    global driver
    path = "C:\\git\\api-testing-python-allure\\resources\\chromedriver.exe"
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