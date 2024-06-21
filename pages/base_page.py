from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.webdriver import WebDriver
import logging
import time

class BasePage:
    def __init__(self, browser: WebDriver):
        self.browser = browser
        self.logger = logging.getLogger(self.__class__.__name__)
        

    def open(self, url):
        self.browser.get(url)

    def find_element(self, *locator):
        return self.browser.find_element(*locator)

    def scroll_to_element(self, *locator):
        element = self.find_element(*locator)
        self.browser.execute_script("arguments[0].scrollIntoView(true);", element)

    def click_element(self, *locator):
        element = self.find_element(*locator)
        self.logger.info(f"Clicking element: {locator}")
        self.scroll_to_element(*locator)
        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(locator))
        try:
            element.click()
        except Exception as e:
            self.logger.warning(f"Normal click failed, using JavaScript click. Exception: {e}")
            self.browser.execute_script("arguments[0].click();", element)
        time.sleep(2)

    def wait_for_element(self, *locator, timeout=10):
        WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(locator))
