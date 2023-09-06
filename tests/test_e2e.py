import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.ConfirmPage import ConfirmPage
from pageObjects.HomePage import HomePage
from pageObjects.CheckOutPage import CheckOutPage

#create a class for all the tc exec
# we have to create a fixture
@pytest.mark.usefixtures("setup")
class TestOne:
    def teste2e(self):
        #now we have to connect the homepge class to this actual class
        #so, for this we have to create an obj for that HomePage
        homepage=HomePage(self.driver)      #here import that homepage from pageobj
        homepage.getName().send_keys("Sai")     #calling name method by using this obj
        homepage.getEmail().send_keys("abc@gmail.com")
        #time.sleep(2)
        homepage.getPwd().send_keys("12345")
        homepage.getCheckbox().click()
        #time.sleep(2)
        homepage.getGender().click()
        homepage.submitForm().click()
        msg=homepage.getsuccMsg().text
        homepage.getEmpstatus().click()
        homepage.getDob().send_keys("09-09-1999")
        time.sleep(2)
        print(msg)
# nav to the SHOP page
        homepage.shopTab().click()
    #now create an obj for that checkoutoage
        checkoutpageobj = CheckOutPage(self.driver)
    # get the text of the item name
        names=checkoutpageobj.getCheckoutItems()
    # now loop through the all names of items and select  one itemnames
        i=0
        for name in names:
            cardtext=name.text  #for accesing text in that names list
            if cardtext == "Blackberry":
                checkoutpageobj.Addtocart()[i].click()  #it click the addtocat when name is blackberry

    #afet adding item then click checkout btn
        checkoutpageobj.getCheckoutbtn().click()
        checkoutpageobj.getFinalCheckout().click()

#navigate to the CONFIRM PAGE
        confirmpageobj=ConfirmPage(self.driver)
        confirmpageobj.getCountry().send_keys("ind")
        self.verifyPresenceofELement("India")    #calling explicit wait
        confirmpageobj.getCountryvalue().click()
        confirmpageobj.getCheckbox().click()
        confirmpageobj.getPurchase().click()
        #printing the last succes msg and compare it with assert
        sucmsg=confirmpageobj.getsuccessmsg().text
        assert ("Success" in sucmsg)   #checking that success word is present in that msg
    #writing method for providign explicit wait for searching india
    def verifyPresenceofELement(self,text):
        element=WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.LINK_TEXT,text)))





