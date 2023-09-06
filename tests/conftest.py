import pytest
from selenium import webdriver
@pytest.fixture()
def setup(request):
    driver=webdriver.Chrome()
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    request.cls.driver=driver       #returning the driver obj
    yield
    #driver.close()         #not need to mention in this latest version it automatically close
    print("test ended")




