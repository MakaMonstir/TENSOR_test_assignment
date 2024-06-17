from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def open(self, url):
        self.browser.get(url)

    def find_element(self, *locator):
        return self.browser.find_element(*locator)

    def click_element(self, *locator):
        element = self.find_element(*locator)
        element.click()

    def wait_for_element(self, *locator, timeout=10):
        WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(locator))