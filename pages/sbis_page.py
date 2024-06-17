from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class SbisPage(BasePage):
    CONTACTS_LINK = (By.LINK_TEXT, "Контакты")
    TENSOR_BANNER = (By.CSS_SELECTOR, "a[href='https://tensor.ru/']")

    def go_to_contacts(self):
        self.click_element(*self.CONTACTS_LINK)

    def click_tensor_banner(self):
        self.click_element(*self.TENSOR_BANNER)
    