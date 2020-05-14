from Pages.LoginPages import  Login
import pytest
from Data.Testdata import *

@pytest.mark.usefixtures("test_setup")

class TestLogin():
    def test_fb(self):
        driver=self.driver
        lg=Login(driver)
        lg.Login1(Username,Password)



