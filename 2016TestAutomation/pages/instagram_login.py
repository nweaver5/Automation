from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class InstagramLogin(BasePage):
    username = (By.ID, 'id_username')
    password = (By.ID, 'id_password')
    login_button = (By.CLASS_NAME, 'button-green')

    def __init__(self, driver):
        super().__init__(driver)

    def get_username(self):
        return self.driver.find_element(*self.username)

    def get_password(self):
        return self.driver.find_element(*self.password)

    def get_login_button(self):
        return self.driver.find_element(*self.login_button)

    def set_username(self, text):
        username = self.get_username()
        username.send_keys(text)

    def set_password(self, text):
        password = self.get_password()
        password.send_keys(text)

    def click_login_button(self):
        self.get_login_button().click()
