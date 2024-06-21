import pytest
from pages.sbis_page import SbisPage
from pages.tensor_page import TensorPage
from selenium.webdriver.common.by import By
from logger_config import configure_logging

configure_logging()

@pytest.mark.skip()
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

def test_change_region(browser):
    sbis_page = SbisPage(browser)

    sbis_page.open("https://sbis.ru/")
    sbis_page.go_to_contacts()
    
    assert sbis_page.check_region("г. Москва")
    assert sbis_page.check_partners_list()
    
    sbis_page.change_region("Камчатский край")
    assert sbis_page.check_region("Камчатский край")
    assert sbis_page.check_partners_list()
    assert sbis_page.verify_region_in_url_and_title()