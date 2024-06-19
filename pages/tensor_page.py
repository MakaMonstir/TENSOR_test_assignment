from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class TensorPage(BasePage):
    STRENGTH_IN_PEOPLE_BLOCK = (By.XPATH, '/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div[1]/div/div[5]/div/div/div[1]/div/p[1]')
    MORE_DETAILS_LINK = (By.XPATH, '/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div[1]/div/div[5]/div/div/div[1]/div/p[4]/a')
    ABOUT_URL = "https://tensor.ru/about"
    WORK_SECTION_IMAGES = (By.CSS_SELECTOR, ".tensor_ru-About .tensor_ru-About__block3-image")

    def is_strength_in_people_block_present(self):
        self.wait_for_element(*self.STRENGTH_IN_PEOPLE_BLOCK)
        return self.find_element(*self.STRENGTH_IN_PEOPLE_BLOCK).is_displayed()

    def go_to_about(self):
        self.click_element(*self.MORE_DETAILS_LINK)
        self.wait_for_element(By.XPATH, f"//h1[text()='О КОМПАНИИ']")

    def get_work_section_images(self):
        return self.browser.find_elements(*self.WORK_SECTION_IMAGES)

    def are_work_section_images_same_size(self):
        images = self.get_work_section_images()
        if not images:
            return False
        first_image_size = images[0].size
        return all(image.size == first_image_size for image in images)
