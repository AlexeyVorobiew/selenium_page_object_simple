from selenium.webdriver.common.by import By

class loginPageLocators():
    FIRST_SIGN_IN_BUTTON = (By.CLASS_NAME, 'ph-login')
    USERNAME_FIELD = (By.XPATH, '//*[contains(@name, \'username\')]')
    LOGIN_IFRAME = (By.XPATH, '//*[contains(@class, \'ag-popup__frame__layout__iframe\')]')
    SUBMIT_USERNAME_BUTTON = (By.CLASS_NAME,'submit-button-wrap')
    PASSWORD_FIELD = (By.XPATH, '//*[contains(@name, \'password\')]')
    FINAL_SIGN_IN_BUTTON = (By.CLASS_NAME, 'submit-button-wrap')

class mailPageLocators():
    NEW_MESSAGE_BUTTON = (By.XPATH, '//*[contains(@title, \'Написать письмо\')]')
    TO_WHOM_FIELD = (By.XPATH, '//*[contains(@class, \'container--H9L5q\')]')
    THEME_FIELD = (By.XPATH, '//*[contains(@name, \'Subject\')]')
    MESSAGE_FIELD = (By.XPATH, '//*[contains(@role, \'textbox\')]')
    SEND_MESSAGE_BUTTON = (By.XPATH, '//*[contains(@class, \'button2__txt\')]')


