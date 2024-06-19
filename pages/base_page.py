from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def open(self, url):
        self.browser.get(url)

    def find_element(self, *locator):
        return self.browser.find_element(*locator)

    def scroll_to_element(self, *locator):
        element = self.find_element(*locator)
        self.browser.execute_script("arguments[0].scrollIntoView(true);", element)

    def click_element(self, *locator):
        element = self.find_element(*locator)
        if not element:
            raise NoSuchElementException
        
        self.scroll_to_element(*locator)
        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(locator))
        self.browser.execute_script("arguments[0].click();", element)

    def wait_for_element(self, *locator, timeout=10):
        WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(locator))
