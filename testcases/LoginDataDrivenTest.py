import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from pageObjects.Nopcommerce_LoginPage import LoginPage
from utilites import XLUtils
from utilites.readProperities import ReadConfig
from utilites.customlogger import LogGen



class Test002_DDT_Login:
    baseURL = ReadConfig.getApplicationUrl("common info", 'baseURL')
    path = "../testdata/Book1.xlsx"
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_login_ddt(self, setup):
        self.logger.info("**************************Test_002_login_ddt test**********************")
        self.lp = LoginPage(setup)
        self.lp.go()
        self.lp.maximize_window()

        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        print("number of rows in Excel:", self.rows)
        # Empty list
        list_status = []

        for r in range(2,self.rows+1):
            self.user = XLUtils.readData(self.path, 'Sheet1', r, 1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', r, 3)

            self.lp.setUsername(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickOnLogin()
            time.sleep(4)

            act_title = self.lp.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exp == 'Pass':
                    self.logger.info("***test pass***")
                    self.lp.clickLogout()
                    list_status.append("Pass")
                elif self.exp == 'Fail':
                    self.logger.info("***test failed***")
                    self.lp.clickLogout()
                    list_status.append("Fail")

            elif act_title != exp_title:
                if self.exp == "Pass":
                    self.logger.info("***test failed***")
                    list_status.append("Fail")
                elif self.exp == 'Fail':
                    self.logger.info("***passed***")
                    list_status.append("Pass")
                print(list_status)
        if "Fail" not in list_status:
            self.logger.info("********Login ddt test passed*********")
            self.lp.close()
            assert True
        else:
            self.logger.info("********Login ddt test failed*********")
            self.lp.close()
            assert False
        self.logger.info("******* End of Login DDT Test **********")
        self.logger.info("**************** Completed  TC_LoginDDT_002 ************* ")