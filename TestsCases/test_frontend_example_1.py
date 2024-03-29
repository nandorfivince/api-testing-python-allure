import pytest
from selenium.webdriver import Chrome

skipifvar = 10


# exec command for group: pytest -m Smoke
# exec command for spec tc: pytest -k test_execute_frontend_example
# exec command for all expect tc: pytest -m "not Sanity"

@pytest.fixture()
def setPath():  # For each test cases
    global driver
    path = "C:\\git\\api-testing-python-allure\\Resources\\chromedriver.exe"
    driver = Chrome(executable_path=path)
    yield  # call for after the test case execution
    driver.close()
    driver.quit()


@pytest.mark.Smoke
def test_execute_frontend_example(setPath):
    driver.get("http://www.thetestingworld.com/testing")
    driver.maximize_window()
    driver.find


@pytest.mark.Sanity
@pytest.mark.skip(reason="I do not want to execute this now")
def test_skip_frontend_example(setPath):
    driver.get("http://www.thetestingworld.com/testing")


@pytest.mark.Integration
@pytest.mark.skipif(skipifvar > 2, reason="Skip if var bigger than 2")
def test_skip_frontend_example(setPath):
    driver.get("http://www.thetestingworld.com/testing")
