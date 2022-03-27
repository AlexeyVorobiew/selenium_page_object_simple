
from selenium_page_object_simple.pages.login_page import loginPage


def test_elements_exist(browser):
    url_main_page = 'https://mail.ru'
    page = loginPage(browser, url_main_page)
    page.open()
    page.are_elements_exist()

def test_sign_in_correct(browser):
    url_main_page = 'https://mail.ru'
    page = loginPage(browser, url_main_page)
    page.open()
    page.sign_in()

