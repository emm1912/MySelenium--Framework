import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from pageObjects.ServiceNow_LoginPage import LoginPage
from utilites.readProperities import ReadConfig
from utilites.customlogger import LogGen

class Test_01_login:
    baseUrl = ReadConfig.getApplicationUrl("servicenow info", 'baseURL')
    username = ReadConfig.getUserEmail("servicenow info", 'username')
    password = ReadConfig.getUserPassword("servicenow info", 'password')
    logger = LogGen.loggen()
# Login POSITIVE
    @pytest.mark.sanity
    def test_homepageTitle(self, setup):

        self.logger.info("**********************************Testing homepage title***********************************")
        self.lp = LoginPage(setup)
        self.lp.go()

        if self.lp.titleIs('Log in | ServiceNow'):
            assert True
            self.lp.close()
        else:
            self.lp.getscreenshotasFile("test_homepageTitle_servicenow")
            self.lp.close()
            assert False

    @pytest.mark.sanity
    def test_password_username_text(self, setup):

        self.logger.info("**********************************Testing password and username text***********************************")
        self.lp = LoginPage(setup)
        self.lp.go()

        username = self.lp.usernametextvisible()
        password = self.lp.passwordtextvisible()

        if username == 'User name' and password == 'Password':
            assert True
            self.lp.close()
        else:
            self.lp.getscreenshotasFile("test_password_username_text_servicenow_fail")
            self.lp.close()
            assert False

    def test_fogotpassword_text_visible(self, setup):

        self.logger.info("**********************************Testing forgot password visible***********************************")
        self.lp = LoginPage(setup)
        self.lp.go()

        forget_text = self.lp.forgotpasswordtextvisible()

        if forget_text == "Forgot Password ?":
            self.lp.close()
            assert True
        else:
            self.lp.getscreenshotasFile("test_forgotpasswordtext_fail")
            self.lp.close()
            assert False

    def test_loginbutton_text_visible(self, setup):

        self.logger.info("**********************************Testing login button visible***********************************")
        self.lp = LoginPage(setup)
        self.lp.go()

        login_text = self.lp.loginbuttontextvisible()

        if login_text == 'Log in':
            self.lp.close()
            assert True
        else:
            self.lp.getscreenshotasFile("test_loginbutton_text_fail")
            self.lp.close()
            assert False

    def test_verify_titleafter_login(self, setup):
        self.logger.info("**********************************Testing title after login***********************************")
        self.lp = LoginPage(setup)
        self.lp.go()
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        time.sleep(2)
        self.lp.clickOnLogin()

        if self.lp.titleIs('ServiceNow'):
            self.lp.close()
            assert True
        else:
            self.lp.getscreenshotasFile("test_title_after_login_text_fail")
            self.lp.close()
            assert False

# Login NEGATIVE

    def loginNegative(self):
        self.logger.info("**********************************Testing title after login***********************************")








