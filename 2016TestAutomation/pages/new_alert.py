from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from .base_page import BasePage

class NewAlert(BasePage):
    alert_name = (By.ID, 'AlertField-Name')
    recording_select2 = (By.XPATH, '//*[@id="AlertSettings"]/div[2]/div[2]/div/span/span[1]/span/ul/li/input')
    alert_type_select2 = (By.CLASS_NAME, 'select2-selection__arrow')
    alert_type = (By.CLASS_NAME, 'alert-type-select-option-title')
    add_keyword_field_button = (By.ID, 'AddAlertKeywordField')
    keywords_allowed = (By.ID, 'keyword-template-basic-select-1-textarea')
    keywords_excluded = (By.ID, 'keyword-template-basic-select-2-textarea')
    keyword_dropdown = (By.XPATH, '//*[@id="AlertSettings"]/div[2]/div[5]/div/div[1]/div[2]/select[1]')
    keyword_dropdown_option = (By.XPATH, '//*[@id="AlertSettings"]/div[2]/div[5]/div/div[1]/div[2]/select[1]/option[3]')
    alert_recipient_select2 = (By.XPATH, '//*[@id="AlertDelivery"]/div[2]/div[1]/div/span/span[1]/span/ul/li/input')
    activate_alert = (By.ID, 'SaveAlert')

    def get_alert_name(self):
        return self.driver.find_element(*self.alert_name)

    def get_recording_select2(self):
        return self.driver.find_element(*self.recording_select2)

    def get_alert_type_select2(self):
        return self.driver.find_elements(*self.alert_type_select2)

    def get_alert_type(self):
        return self.driver.find_elements(*self.alert_type)

    def get_add_alert_keyword_field_button(self):
        return self.driver.find_element(*self.add_keyword_field_button)

    def get_keywords_allowed(self):
        return self.driver.find_element(*self.keywords_allowed)

    def get_keywords_excluded(self):
        return self.driver.find_element(*self.keywords_excluded)

    def get_keyword_dropdown(self):
        return self.driver.find_element(*self.keyword_dropdown)

    def get_keyword_dropdown_option(self):
        return self.driver.find_element(*self.keyword_dropdown_option)

    def get_alert_recipient_select2(self):
        return self.driver.find_element(*self.alert_recipient_select2)

    def get_activate_alert(self):
        return self.driver.find_element(*self.activate_alert)

    def set_alert_name(self, keys):
        alert_name = self.get_alert_name()
        alert_name.send_keys(keys)

    def set_recordings_selection(self, keys):
        recording_name = self.get_recording_select2()
        recording_name.send_keys(keys)

    def press_enter_recording(self):
        option = self.get_recording_select2()
        option.send_keys(Keys.RETURN)

    def click_on_alert_type_select2(self, index):
        dropdown_arrow = self.get_alert_type_select2()
        dropdown_arrow[index].click()

    def click_on_alert_type(self, index):
        alert_type = self.get_alert_type()
        alert_type[index].click()

    def click_on_add_alert_keyword_field_button(self):
        self.get_add_alert_keyword_field_button().click()

    def set_keywords_allowed(self, keys):
        keywords_allowed = self.get_keywords_allowed()
        keywords_allowed.send_keys(keys)

    def set_keywords_excluded(self, keys):
        keywords_excluded = self.get_keywords_excluded()
        keywords_excluded.send_keys(keys)

    def click_on_keyword_dropdown(self):
        dropdown = self.get_keyword_dropdown()
        dropdown.click()

    def select_keyword_dropdown_option(self):
        option = self.get_keyword_dropdown_option()
        option.click()

    def set_recipient_selection(self, keys):
        recipient = self.get_alert_recipient_select2()
        recipient.send_keys(keys)

    def press_enter_recipient(self):
        option = self.get_alert_recipient_select2()
        option.send_keys(Keys.RETURN)

    def click_on_activate_alert(self):
        activate_alert = self.get_activate_alert()
        activate_alert.click()
