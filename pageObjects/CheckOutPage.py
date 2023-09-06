from selenium.webdriver.common.by import By


class CheckOutPage:
    def __init__(self,driver):
        self.driver=driver

    checkout=(By.CSS_SELECTOR,"a[class*='btn-primary']")
    #now we get the names of the phones  and use find_elements method for all the names
    checkoutitems = (By.XPATH,"//h4[@class='card-title']/a")
    #now find the loc of add button
    addtocartbtn=(By.XPATH,"//div[@class='card-footer']/button")
    checkout2=(By.CSS_SELECTOR,"button[class*='btn-success']")
    def getCheckoutbtn(self):
        return self.driver.find_element(*CheckOutPage.checkout)

    def getCheckoutItems(self):
        return self.driver.find_elements(*CheckOutPage.checkoutitems)

    def Addtocart(self):
        return self.driver.find_elements(*CheckOutPage.addtocartbtn)
    def getFinalCheckout(self):
        return self.driver.find_element(*CheckOutPage.checkout2)

