from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class Influencers(BasePage):
    try_user_track_button = (By.ID, 'tryUserTrack')
    add_user = (By.ID, 'addUser')
    add_user_twitter = (By.CSS_SELECTOR, '.qtip-content .twitter .logo')
    add_user_instagram = (By.CSS_SELECTOR, '.qtip-content .instagram .logo')
    selected_account = (By.CSS_SELECTOR, '#linkedAccountSelect option')
    add_account_username = (By.CSS_SELECTOR, '.qtip-content .userName')
    add_user_button = (By.ID, 'addUserOk')
    done_button = (By.ID, 'doneOk')
    main_section_row = (By.CSS_SELECTOR, '#usersFolderGrid .row')
    delete_user_button = (By.CSS_SELECTOR, '.qtip-content .delete-user-button')
    confirm_delete_button = (By.CSS_SELECTOR, '.qtip-content .ok')

    def __init__(self, driver):
        super().__init__(driver)

    def get_try_user_track_button(self):
        return self.driver.find_element(*self.try_user_track_button)

    def get_add_user(self):
        return self.driver.find_element(*self.add_user)

    def get_add_user_twitter(self):
        return self.driver.find_element(*self.add_user_twitter)

    def get_add_user_instagram(self):
        return self.driver.find_element(*self.add_user_instagram)

    def get_selected_account(self):
        return self.driver.find_element(*self.selected_account)

    def get_add_account_username(self):
        return self.driver.find_element(*self.add_account_username)

    def get_add_user_button(self):
        return self.driver.find_element(*self.add_user_button)

    def get_done_button(self):
        return self.driver.find_element(*self.done_button)

    def get_main_section_rows(self):
        return self.driver.find_elements(*self.main_section_row)

    def get_delete_user_button(self):
        return self.driver.find_element(*self.delete_user_button)

    def get_confirm_delete_button(self):
        return self.driver.find_element(*self.confirm_delete_button)

    def click_try_user_track_button(self):
        self.get_try_user_track_button().click()

    def click_add_user(self):
        self.get_add_user().click()

    def click_add_user_twitter(self):
        self.get_add_user_twitter().click()

    def click_add_user_instagram(self):
        self.get_add_user_instagram().click()

    def set_add_account_username(self, keys):
        add_account_username = self.get_add_account_username()
        add_account_username.send_keys(keys)

    def click_add_user_button(self):
        self.get_add_user_button().click()

    def click_done_button(self):
        self.get_done_button().click()

    def click_main_section_row(self, index):
        self.get_main_section_rows()[index].find_element(*(By.CSS_SELECTOR, '.cellWithPointer:nth-child(2)')).click()

    def click_more_button(self, idx):
        self.get_main_section_rows()[idx].find_element(*(By.CLASS_NAME, 'more')).click()

    def click_delete_user_button(self):
        self.get_delete_user_button().click()

    def click_confirm_delete_button(self):
        self.get_confirm_delete_button().click()
