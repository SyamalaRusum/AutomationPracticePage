from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self,driver):
        self.driver = driver  #assigning class var to the instance var self

    shop=(By.CSS_SELECTOR,"a[href*='shop']")    #find web elem loc and def in tup

    #now find the locator for the home page form
    name=(By.XPATH,"//label[text()='Name']/following-sibling::input")
    email=(By.NAME,'email')
    password=(By.ID,'exampleInputPassword1')
    chechbox=(By.ID,'exampleCheck1')
    gender=(By.ID,'exampleFormControlSelect1')
    submit=(By.XPATH,"//input[@value='Submit']")
    successmsg=(By.XPATH,"//div[contains(@class,'alert')]")
    empstatus=(By.XPATH,"//input[@id='inlineRadio2']")
    dob=(By.NAME,'bday')


    #now define methods for all the web elem

    def shopTab(self):             #format to define method
        return self.driver.find_element(*HomePage.shop)      #passing elem to the driver

    def getName(self):
        return self.driver.find_element(*HomePage.name)
    def getEmail(self):
        return self.driver.find_element(*HomePage.email)
    def getPwd(self):
        return self.driver.find_element(*HomePage.password)
    def getCheckbox(self):
        return self.driver.find_element(*HomePage.chechbox)
    def getGender(self):
        return self.driver.find_element(*HomePage.gender)
    def submitForm(self):
        return self.driver.find_element(*HomePage.submit)
    def getsuccMsg(self):
        return self.driver.find_element(*HomePage.successmsg)

    def getEmpstatus(self):
        return self.driver.find_element(*HomePage.empstatus)

    def getDob(self):
        return self.driver.find_element(*HomePage.dob)









