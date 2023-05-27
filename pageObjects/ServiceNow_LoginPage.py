from selenium.webdriver.common.by import By
from pageObjects.base_page import BasePage
from pageObjects.base_element import BaseElement
from pageObjects.locator import Locator


class LoginPage(BasePage):
    url="https://dev166512.service-now.com"

    def setusername(self, username):
        locator = Locator(By.CSS_SELECTOR, "input[id='user_name']")
        input_username = BaseElement(self.driver, locator)
        input_username.find()
        input_username.input_text(username)

    def setpassword(self, password):
        locator = Locator(By.CSS_SELECTOR, "input[id='user_password']")
        input_password = BaseElement(self.driver, locator)
        input_password.find()
        input_password.input_text(password)

    def clickOnLogin(self):
        locator = (By.CSS_SELECTOR, "button[id='sysverb_login']")
        login_btn = BaseElement(self.driver, locator)
        login_btn.find()
        login_btn.click()

    def clickOnLogout(self):
        pass

    def loginbuttontextvisible(self):
        locator = (By.CSS_SELECTOR, "button[id='sysverb_login']")
        login_btn = BaseElement(self.driver, locator)
        login_btn.find()
        login_btn_text = login_btn.text
        return login_btn_text

    def usernametextvisible(self):
        locator = Locator(By.CSS_SELECTOR, "label[for='user_name']")
        username_element = BaseElement(self.driver, locator)
        username_element.find()
        username_text = username_element.text
        return username_text

    def passwordtextvisible(self):
        locator = Locator(By.CSS_SELECTOR, "label[for='user_password']")
        password_element = BaseElement(self.driver, locator)
        password_element.find()
        password_text = password_element.text
        return password_text

    def forgotpasswordtextvisible(self):
        locator = Locator(By.LINK_TEXT, "Forgot Password ?")
        passwordforget_element = BaseElement(self.driver, locator)
        passwordforget_element.find()
        passwordforget_text = passwordforget_element.text
        return passwordforget_text

