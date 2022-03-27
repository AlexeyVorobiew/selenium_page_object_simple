from selenium.common.exceptions import NoSuchElementException

class core():

    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def handle_window(self, win_num):
        window_to_switch = self.browser.window_handles[win_num]
        return self.browser.switch_to.window(window_to_switch)

    def go_to_frame(self, how, what):
        frame = self.browser.find_element(how, what)
        self.browser.switch_to.frame(frame)

    def is_element_exist(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True



