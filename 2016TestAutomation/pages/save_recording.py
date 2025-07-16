from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from .base_page import BasePage


class SaveRecordingPopup(BasePage):
    recording_name = (By.ID, 'recording-name')
    recording_visibility = (By.ID, 'recording-visibility')
    left_tabs = (By.CSS_SELECTOR, '#leftColumn .menu-container')
    left_tabs_popup = (By.CLASS_NAME, 'tabControlItem')
    selected_location = (By.CSS_SELECTOR, '.select2-selection__rendered .select2-selection__choice')
    activate_recording_button = (By.ID, 'define-recording-step-apply')
    view_recording_button = (By.ID, 'recording-activated-step-apply')
    unlock_source_checkbox = (By.CSS_SELECTOR, '#sources > div.confirm-restrict-recording.dont-restrict-recording > label > input[type="checkbox"]')

    def get_recording_name(self):
        return self.driver.find_element(*self.recording_name)

    def get_recording_visibility(self):
        return self.driver.find_element(*self.recording_visibility)

    def get_left_tabs(self):
        return self.driver.find_elements(*self.left_tabs)

    def get_left_tabs_popup(self):
        return self.driver.find_elements(*self.left_tabs_popup)

    def get_selected_location(self):
        return self.driver.find_element(*self.selected_location)

    def get_source_checkbox(self, source):
        return self.driver.find_element(*(By.CSS_SELECTOR, 'li.sourceItem.' + source + '.checked > input'))

    def get_activate_recording_button(self):
        return self.driver.find_element(*self.activate_recording_button)

    def get_view_recording_button(self):
        return self.driver.find_element(*self.view_recording_button)

    def get_unlock_source_checkbox(self):
        return self.driver.find_element(*self.unlock_source_checkbox)

    def set_recording_name(self, keys):
        recording_name = self.get_recording_name()
        recording_name.send_keys(keys)

    def set_recording_visibility(self, index):
        visibility_select = Select(self.get_recording_visibility())
        visibility_select.select_by_index(index)

    def click_on_left_tab(self, tab_index):
        tab = self.get_left_tabs()[tab_index]
        tab.click()

    def click_on_left_tab_popup(self, tab_index):
        tab = self.get_left_tabs_popup()[tab_index]
        tab.click()

    def click_on_source_checkbox(self, source):
        self.get_source_checkbox(source).click()

    def click_on_activate_recording(self):
        self.get_activate_recording_button().click()

    def click_on_view_recording(self):
        self.get_view_recording_button().click()

    def click_on_unlock_source_checkbox(self):
        self.get_unlock_source_checkbox().click()
