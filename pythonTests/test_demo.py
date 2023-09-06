import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Test1:
    def test_demo(self):
        driver=webdriver.Chrome()
        driver.get("https://rahulshettyacademy.com/angularpractice/")
        driver.maximize_window()

        drpdwn=Select(driver.find_element(By.ID,'exampleFormControlSelect1'))
        drpdwn.select_by_index(1)
        time.sleep(5)
        drpdwn.select_by_visible_text("Male")