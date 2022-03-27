import time
from selenium_page_object_simple import test_data
from . basic import core
from . locators import loginPageLocators


class loginPage(core):


# отдельный тест на наличие элементов
    def are_elements_exist(self):
       assert self.is_element_exist(*loginPageLocators.FIRST_SIGN_IN_BUTTON), "cannot find sign in button"

    def sign_in(self):
        assert self.is_element_exist(*loginPageLocators.FIRST_SIGN_IN_BUTTON), "cannot find sign in button"
        sign_in_button = self.browser.find_element(*loginPageLocators.FIRST_SIGN_IN_BUTTON)
        sign_in_button.click()
        assert self.is_element_exist(*loginPageLocators.LOGIN_IFRAME), "cannot find login frame"
        self.go_to_frame(*loginPageLocators.LOGIN_IFRAME)
        assert self.is_element_exist(*loginPageLocators.USERNAME_FIELD), "cannot find username field"
        username_field = self.browser.find_element(*loginPageLocators.USERNAME_FIELD)
        username_field.send_keys(test_data.username)
        assert self.is_element_exist(*loginPageLocators.SUBMIT_USERNAME_BUTTON), "cannot find username button"
        username_submit_button = self.browser.find_element(*loginPageLocators.SUBMIT_USERNAME_BUTTON)
        username_submit_button.click()
        assert self.is_element_exist(*loginPageLocators.PASSWORD_FIELD), "cannot find password field"
        password_field = self.browser.find_element(*loginPageLocators.PASSWORD_FIELD)
        password_field.send_keys(test_data.password)
        assert self.is_element_exist(*loginPageLocators.FINAL_SIGN_IN_BUTTON), "cannot find final sign in button"
        final_sign_in_button = self.browser.find_element(*loginPageLocators.FINAL_SIGN_IN_BUTTON)
        final_sign_in_button.click()
        time.sleep(10)
