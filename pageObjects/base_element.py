from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class BaseElement(object):
    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator
        self.web_element = None
        # self.find()

    def find(self):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator=self.locator))
        self.web_element = element
        return None

    # def finds(self):
    #     element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator=self.locator))
    #     self.web_element = element
    #     return None

    def input_text(self, txt):
        self.web_element.clear()
        self.web_element.send_keys(txt)
        return None

    def click(self):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(mark=self.locator))
        element.click()
        return None

    def doubleclick(self):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(mark=self.locator))
        element.double_click()
        return None

    def clickNhold(self):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(mark=self.locator))
        element.click_and_hold()
        return None

    def rightclick(self):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(mark=self.locator))
        element.context_click()
        return None

    def attribute(self, attr_name):
        attribute = self.web_element.get_attribute(attr_name)
        return attribute

    @property
    def text(self):
        text = self.web_element.text
        return text

