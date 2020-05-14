import pytest

@pytest.fixture(scope='class')
def test_setup(request):
    from selenium import webdriver
    driver=webdriver.Chrome(executable_path="C:/Users/Admin/Downloads/New drivers find/chromedriver.exe")
    driver.get("https://www.facebook.com/")
    driver.implicitly_wait(30)
    request.cls.driver=driver
