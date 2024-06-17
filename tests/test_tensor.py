import pytest
from pages.sbis_page import SbisPage
from pages.tensor_page import TensorPage
from selenium.webdriver.common.by import By

def test_tensor_navigation(browser):
    sbis_page = SbisPage(browser)
    tensor_page = TensorPage(browser)

    sbis_page.open("https://sbis.ru/")
    sbis_page.go_to_contacts()
    sbis_page.click_tensor_banner()
    
    tensor_page.wait_for_element(By.TAG_NAME, 'h1')
    assert tensor_page.browser.current_url == "https://tensor.ru/"

    assert tensor_page.is_strength_in_people_block_present()
    tensor_page.go_to_about()
    assert tensor_page.browser.current_url == tensor_page.ABOUT_URL

    assert tensor_page.are_work_section_images_same_size()
