from selenium.webdriver.common.by import By
from pageObjects.base_page import BasePage
from pageObjects.base_element import BaseElement
from pageObjects.locator import Locator


class LoginPage(BasePage):
    url = "https://admin-demo.nopcommerce.com/"

    def setUsername(self, username):
        locator = Locator(By.ID, "Email")
        setuname = BaseElement(self.driver, locator)
        setuname.find()
        setuname.input_text(username)


    def setPassword(self, password):
        locator = Locator(By.ID, "Password")
        setpass = BaseElement(self.driver, locator)
        setpass.find()
        setpass.input_text(password)


    def clickOnLogin(self):
        locator = Locator(By.XPATH, "//button[@type='submit']")
        login_btn = BaseElement(self.driver, locator)
        login_btn.find()
        login_btn.click()


    def clickLogout(self):
        locator = Locator(By.LINK_TEXT, "Logout")
        logout_btn = BaseElement(self.driver, locator)
        logout_btn.find()
        logout_btn.click()