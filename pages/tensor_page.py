from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class TensorPage(BasePage):
    STRENGTH_IN_PEOPLE_BLOCK = (By.XPATH, "//p[contains(text(), 'Сила в людях')]/ancestor::div[contains(@class, 'tensor_ru-Index__block4-content tensor_ru-Index__card')]")
    MORE_DETAILS_LINK = (By.XPATH, "//a[contains(text(), 'Сила в людях')]/ancestor::div[contains(@class, 'tensor_ru-Index__block4-content tensor_ru-Index__card')]//p[contains(text(), 'Подробнее')]")
    ABOUT_URL = "https://tensor.ru/about"
    WORK_SECTION_IMAGES = (By.CSS_SELECTOR, ".chronology img")

    def is_strength_in_people_block_present(self):
        self.wait_for_element(*self.STRENGTH_IN_PEOPLE_BLOCK)
        return self.find_element(*self.STRENGTH_IN_PEOPLE_BLOCK).is_displayed()

    def go_to_about(self):
        self.click_element(*self.MORE_DETAILS_LINK)
        self.wait_for_element(By.XPATH, f"//h1[text()='О компании']")

    def get_work_section_images(self):
        return self.browser.find_elements(*self.WORK_SECTION_IMAGES)

    def are_work_section_images_same_size(self):
        images = self.get_work_section_images()
        if not images:
            return False
        first_image_size = images[0].size
        return all(image.size == first_image_size for image in images)
