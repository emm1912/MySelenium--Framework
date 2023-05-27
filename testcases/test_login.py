import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from pageObjects.Nopcommerce_LoginPage import LoginPage
from utilites.readProperities import ReadConfig
from utilites.customlogger import LogGen

class Test_01_login:
    baseUrl = ReadConfig.getApplicationUrl("common info", 'baseURL')
    username = ReadConfig.getUserEmail("common info", 'username')
    password = ReadConfig.getUserPassword("common info", 'password')
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_homepageTitle(self, setup):

        self.logger.info("**********************************Testing homepage title***********************************")
        self.lp = LoginPage(setup)
        self.lp.go()

        if self.lp.titleIs("Your store. Login"):
            assert True
            self.lp.close()
        else:
            self.lp.getscreenshotasFile("test_homepageTitle")
            self.lp.close()
            assert False

    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("**********************************Testing test_login Page***********************************")
        self.lp = LoginPage(setup)
        self.lp.go()
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickOnLogin()
        time.sleep(5)
        assert "Dashboard / nopCommerce administration" in self.lp.getpageSource()
        if "Dashboard / nopCommerce administration" in self.lp.getpageSource():
            assert True
            self.lp.close()
        else:
            self.logger.info("*****************************Else condition fail and saving screenshot of the failure******************************")
            self.lp.getscreenshotasFile("test_login")
            self.lp.close()
            assert False


