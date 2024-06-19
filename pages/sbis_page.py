from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import time

class SbisPage(BasePage):
    CONTACTS_LINK = (By.LINK_TEXT, "Контакты")
    TENSOR_BANNER = (By.XPATH, '//*[@id="contacts_clients"]/div[1]/div/div/div[2]/div/a/img')

    def go_to_contacts(self):
        self.click_element(*self.CONTACTS_LINK)

    def click_tensor_banner(self):
        self.click_element(*self.TENSOR_BANNER)
        self.switch_to_new_tab()

    def switch_to_new_tab(self):
        time.sleep(2)
        new_tab = self.browser.window_handles[-1]
        self.browser.switch_to.window(new_tab)