from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import time

class SbisPage(BasePage):
    CONTACTS_LINK = (By.LINK_TEXT, "Контакты")
    TENSOR_BANNER = (By.XPATH, '//*[@id="contacts_clients"]/div[1]/div/div/div[2]/div/a/img')
    REGION_LABEL = (By.XPATH, "/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div[1]/div/div[3]/div[2]/div[1]/div/div[2]/span/span")
    CURRENT_PARTNERS_LIST = (By.XPATH, "/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div[1]/div/div[4]/div[3]/div/div[2]/div[2]/div/div[2]/div[1]/div[3]/div[2]")
    KAMCHATKA_PARTNERS_LIST = (By.XPATH, "/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div[1]/div/div[4]/div[3]/div/div[2]/div[2]/div/div[2]/div[1]/div[3]/div[1]/div/div")
    REGION_DROPDOWN = (By.XPATH, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div[2]/div/div")
    REGION_SEARCH_INPUT = (By.XPATH, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div[2]/div/div/div[1]/div[2]/div/div[2]/input")
    KAMCHATKA_OPTION = (By.XPATH, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div[2]/div/ul/li/span")

    def go_to_contacts(self):
        self.click_element(*self.CONTACTS_LINK)

    def check_region(self, expected_region):
        region = self.find_element(*self.REGION_LABEL).text
        self.logger.info(f"Current region: {region}")
        return region == expected_region

    def change_region(self, new_region):
        self.click_element(*self.REGION_LABEL)
        self.logger.info("Clicked on region label")
        self.wait_for_element(*self.REGION_DROPDOWN)
        self.find_element(*self.REGION_SEARCH_INPUT).send_keys(new_region)
        time.sleep(2)
        self.wait_for_element(*self.KAMCHATKA_OPTION)
        self.logger.info(f"Entered region: {new_region}")
        self.click_element(*self.KAMCHATKA_OPTION)
        self.logger.info(f"Selected region: {new_region}")

    def check_partners_list(self):
        partners = self.find_element(*self.CURRENT_PARTNERS_LIST)
        self.logger.info(f"Found partners list: {partners.is_displayed()}")
        return partners.is_displayed()

    def verify_region_in_url_and_title(self):
        current_url = self.browser.current_url
        current_title = self.browser.title
        current_partners_list = self.browser.find_element(*self.KAMCHATKA_PARTNERS_LIST).text
        
        self.logger.info(f"Current URL: {current_url}")
        self.logger.info(f"Current Title: {current_title}")
        return "41-kamchatskij-kraj" in current_url and "Камчатский край" in current_title and "Камчатский" in current_partners_list