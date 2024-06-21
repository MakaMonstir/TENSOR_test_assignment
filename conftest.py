import pytest
from selenium import webdriver
from logger_config import configure_logging

@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture(scope="session", autouse=True)
def setup_logging():
    configure_logging()