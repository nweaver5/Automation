from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from .base_page import BasePage


class SaveLocationPopup(BasePage):
    location_name = (By.ID, 'location-name')
    location_visibility = (By.ID, 'location-visibility')
    save_location_button = (By.ID, 'create-location-step-apply')

    def get_location_name(self):
        return self.driver.find_element(*self.location_name)

    def get_location_visibility(self):
        return self.driver.find_element(*self.location_visibility)

    def get_save_location_button(self):
        return self.driver.find_element(*self.save_location_button)

    def set_location_name(self, keys):
        location_name = self.get_location_name()
        location_name.send_keys(keys)

    def set_location_visibility(self, index):
        visibility_select = Select(self.get_location_visibility())
        visibility_select.select_by_index(index)

    def click_save_location_button(self):
        save_button = self.get_save_location_button()
        save_button.click()
