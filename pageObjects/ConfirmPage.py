from selenium.webdriver.common.by import By


class ConfirmPage:
    def __init__(self,driver):
        self.driver=driver

    country=(By.ID,"country")
    countryval=(By.LINK_TEXT,'India')   #select india and inspect
    checkbox=(By.XPATH,"//div[contains(@class,'checkbox-primary')]")
    purchase=(By.XPATH,"//input[@value='Purchase']")
    successMsg=(By.CSS_SELECTOR,"div[class*='alert-success']")

    def getCountry(self):
        return self.driver.find_element(*ConfirmPage.country)

    def getCountryvalue(self):
        return self.driver.find_element(*ConfirmPage.countryval)


    def getCheckbox(self):
        return self.driver.find_element(*ConfirmPage.checkbox)

    def getPurchase(self):
        return self.driver.find_element(*ConfirmPage.purchase)

    def getsuccessmsg(self):
        return self.driver.find_element(*ConfirmPage.successMsg)





