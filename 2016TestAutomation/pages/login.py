from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class Login(BasePage):
    display_name = (By.ID, 'DisplayNameOrEmailAddress')
    password = (By.ID, 'password')
    submit_login = (By.ID, 'submitLogin')

    def __init__(self, driver):
        super().__init__(driver)

    def get_display_name(self):
        return self.driver.find_element(*self.display_name)

    def get_password(self):
        return self.driver.find_element(*self.password)

    def get_submit_login_button(self):
        return self.driver.find_element(*self.submit_login)

    def set_display_name(self, email):
        display_name_element = self.get_display_name()
        display_name_element.send_keys(email)

    def set_password(self, password):
        password_element = self.get_password()
        password_element.send_keys(password)

    def click_login(self):
        submit_element = self.get_submit_login_button()
        submit_element.click()
