class Webgeneric:
    def __init__(self,driver):
        self.driver=driver

    def enter(self,locator,input_val):
        self.driver.find_element_by_id(locator).send_keys(input_val)

    def subimt(self,locator):
        self.driver.find_element_by_xpath(locator).click()