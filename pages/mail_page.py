from selenium_page_object_simple import test_data
from . basic import core
from . locators import mailPageLocators
from datetime import datetime
import time


class mailPage(core):


    def send_message(self):
        assert self.is_element_exist(*mailPageLocators.NEW_MESSAGE_BUTTON), "cannot find new message button"
        new_message_button = self.browser.find_element(*mailPageLocators.NEW_MESSAGE_BUTTON)
        new_message_button.click()
        assert self.is_element_exist(*mailPageLocators.TO_WHOM_FIELD), "cannot find to whom field"
        whom_field = self.browser.find_element(*mailPageLocators.TO_WHOM_FIELD)
        whom_field.send_keys(test_data.username)
        assert self.is_element_exist(*mailPageLocators.THEME_FIELD), "cannot find  theme field"
        theme_field = self.browser.find_element(*mailPageLocators.THEME_FIELD)
        theme_field.send_keys(test_data.message_theme + str(datetime.now()))
        assert self.is_element_exist(*mailPageLocators.MESSAGE_FIELD), "cannot find  message field"
        message_field = self.browser.find_element(*mailPageLocators.MESSAGE_FIELD)
        message_field.send_keys(test_data.message + str(datetime.now()))
        assert self.is_element_exist(*mailPageLocators.SEND_MESSAGE_BUTTON), "cannot find send message button"
        send_message_button = self.browser.find_element(*mailPageLocators.SEND_MESSAGE_BUTTON)
        send_message_button.click()
        time.sleep(10)

