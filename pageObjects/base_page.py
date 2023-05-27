from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage(object):

    url = None

    def __init__(self, driver):
        self.driver = driver

    def go(self):
        self.driver.get(self.url)

    def forward(self):
        self.driver.forward()

    def back(self):
        self.driver.back()

    def refresh(self):
        self.driver.refresh()

    def scroll_downpage(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def quit(self):
        self.driver.quit()

    def close(self):
        self.driver.close()

    def maximize_window(self):
        self.driver.maximize_window()

    def minimize_window(self):
        self.driver.minimize_window()

    def getscreenshotasFile(self, name):
        self.driver.get_screenshot_as_file("../screenshots/" + name + ".png")

    def newTab(self, url):
        self.driver.execute_script('window.open("{}","_blank");'.format(url))

    def titleIs(self, title_str):
        return WebDriverWait(self.driver, 10).until(EC.title_is(title=title_str))

    def getpageSource(self):
        page_source_value = self.driver.page_source
        return page_source_value
