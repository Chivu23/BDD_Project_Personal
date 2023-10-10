from selenium.webdriver.common.by import By

from base_page import BasePage


class LoginPage(BasePage):
    USERNAME = (By.ID, "user-name")
    PASS = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-button")
    ERROR_MSG = (By.TAG_NAME, "h3")

    def navigate_to_login_page(self):
        self.browser.get(self.BASE_URL)

    def insert_correct_username(self):
        username = self.browser.find_element(*self.USERNAME)
        username.send_keys("standard_user")

    def insert_incorrect_username(self):
        username = self.browser.find_element(*self.USERNAME)
        username.send_keys("incorrect_user")

    def insert_block_username(self):
        username = self.browser.find_element(*self.USERNAME)
        username.send_keys("locked_out_user")

    def insert_correct_password(self):
        password = self.browser.find_element(*self.PASS)
        password.send_keys("secret_sauce")

    def insert_incorrect_password(self):
        password = self.browser.find_element(*self.PASS)
        password.send_keys("incorrect_pass")

    def click_login_button(self):
        login_btn = self.browser.find_element(*self.LOGIN_BTN)
        login_btn.click()

    def check_error_message_invalid_pwd(self):
        expected_error = "Epic sadface: Username and password do not match any user in this service"
        error_element = self.browser.find_element(*self.ERROR_MSG)
        actual_error = error_element.text
        assert actual_error == actual_error

    def check_error_message_invalid_username(self):
        expected_error = "Epic sadface: Username and password do not match any user in this service"
        error_element = self.browser.find_element(*self.ERROR_MSG)
        actual_error = error_element.text
        assert actual_error == expected_error

    def check_error_message_none_password(self):
        expected_error = "Epic sadface: Password is required"
        error_element = self.browser.find_element(*self.ERROR_MSG)
        actual_error = error_element.text
        assert actual_error == expected_error

    def check_error_message_none_username(self):
        expected_error = "Epic sadface: Username is required"
        error_element = self.browser.find_element(*self.ERROR_MSG)
        actual_error = error_element.text
        assert actual_error == expected_error

    def check_error_msg_blocked_username(self):
        expected_err = 'Epic sadface: Sorry, this user has been locked out.'
        error_msg = self.browser.find_element(*self.ERROR_MSG)
        actual_err = error_msg.text
        assert expected_err == actual_err
