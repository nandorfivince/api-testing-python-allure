from selenium.webdriver import Chrome


def test_frontend_example():
    path = "C:\\git\\api-testing-python-allure\\resources\\chromedriver.exe"
    driver = Chrome(executable_path=path)
    driver.get("http://www.thetestingworld.com/testing")