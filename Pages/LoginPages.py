from selenium import webdriver
from Pages.Webgeneric import Webgeneric

class Login(Webgeneric):
    def __init__(self,driver):
        Webgeneric.__init__(self,driver)
        self.driver=driver
        self.un_id="email"
        self.pwd_name="pass"
        self.login_btn_xpath="//input[@type='submit']"

    def Login1(self,un,pwd):
        wg=Webgeneric(self.driver)
        wg.enter(self.un_id,un)
        wg.enter(self.pwd_name,pwd)
        wg.subimt(self.login_btn_xpath)



        self.driver.find_element_by_id("email").send_keys(un)
        self.driver.find_element_by_id("pass").send_keys(pwd)
        self.driver.find_element_by_xpath().click()