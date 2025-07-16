from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class Profile(BasePage):
    linked_accounts_tab = (By.LINK_TEXT, 'Linked Accounts')
    link_account_button = (By.CLASS_NAME, 'linked-box')
    instagram_linked_accounts = (By.CSS_SELECTOR, '.instagram-area .row')
    instagram_test_account = (By.CSS_SELECTOR, '.instagram-area .row .test-account')
    twitter_linked_accounts = (By.CSS_SELECTOR, '.twitter-area .row')
    twitter_test_account = (By.CSS_SELECTOR, '.twitter-area .row .test-account')
    delete_account = (By.PARTIAL_LINK_TEXT, 'Delete')
    confirm_delete_button = (By.CSS_SELECTOR, '.qtip-content .ok')

    def __init__(self, driver):
        super().__init__(driver)

    def get_linked_accounts_tab(self):
        return self.driver.find_element(*self.linked_accounts_tab)

    def get_link_account_button(self):
        return self.driver.find_elements(*self.link_account_button)

    def get_instagram_linked_accounts(self):
        return self.driver.find_elements(*self.instagram_linked_accounts)

    def get_instagram_test_account(self):
        return self.driver.find_element(*self.instagram_test_account)

    def get_twitter_linked_accounts(self):
        return self.driver.find_elements(*self.twitter_linked_accounts)

    def get_twitter_test_account(self):
        return self.driver.find_element(*self.twitter_test_account)

    def get_delete_account_link(self):
        return self.driver.find_elements(*self.delete_account)

    def get_confirm_delete_button(self):
        return self.driver.find_element(*self.confirm_delete_button)

    def click_linked_accounts_tab(self):
        self.get_linked_accounts_tab().click()

    def click_link_account_button(self, idx):
        self.get_link_account_button()[idx].click()

    def click_instagram_test_account(self):
        self.get_instagram_test_account().click()

    def click_twitter_test_account(self):
        self.get_twitter_test_account().click()

    def click_delete_account_link(self, idx):
        self.get_delete_account_link()[idx].click()

    def click_confirm_delete_button(self):
        self.get_confirm_delete_button().click()
