import pytest
from selenium import webdriver
from selenium_page_object_simple import test_data

@pytest.fixture(scope="session")
def browser():
    browser_driver = webdriver.Chrome(
        test_data.path_to_webdriver)
    yield browser_driver
    browser_driver.quit()