
from selenium_page_object_simple.pages.mail_page import mailPage


def test_send_message(browser):
    url_main_page = 'https://e.mail.ru/inbox/'
    page = mailPage(browser, url_main_page)
    page.open()
    page.send_message()



