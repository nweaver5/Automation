from .base_page import BasePage
from selenium.webdriver.common.by import By


class DataManager(BasePage):
    left_tab = (By.CSS_SELECTOR, '#accordion > div > a.list-group-item.ng-scope')
    locations_grid_records = (By.XPATH, '//*[@id="main"]/div/ui-view/div/div/div[2]/div/div[1]/div/div[1]/table/tbody/tr/td[3]/a')
    recording_grid_records = (By.XPATH, '//*[@id="main"]/div/ui-view/div/div/div[2]/div/div[1]/div/div[1]/table/tbody/tr/td[3]/span/a')
    recording_templates_grid_records = (By.XPATH, '//*[@id="main"]/div/ui-view/div/div/div[2]/div/ui-view/div[1]/div/div[1]/table/tbody/tr/td[3]/span')
    collections_grid_records = (By.XPATH, '//*[@id="main"]/div/ui-view/div/div/div[2]/div/div[1]/div/div[1]/table/tbody/tr/td[3]/a')
    scheduled_subtab = (By.LINK_TEXT, 'Scheduled')
    completed_subtab = (By.LINK_TEXT, 'Completed')
    recording_template_subtab = (By.LINK_TEXT, 'Recordings')
    location_folder_edit_link = (By.LINK_TEXT, 'edit')
    new_folder = (By.XPATH, '//*[@id="bs-example-navbar-collapse-1"]/div/button')
    location_folder_name = (By.ID, 'nameField')
    create_folder_button = (By.ID, 'editFolderButton')
    close_popup_button = (By.ID, 'buttonCloseEndMessagePopup')
    folder_row_name = (By.XPATH, '//*[@id="main"]/div/ui-view/div/div/div[2]/div/div[1]/div/div[1]/table/tbody/tr[1]/td[3]/span')
    folder_button = (By.XPATH, '//*[@id="main"]/div/ui-view/div/div/div[2]/div/div[1]/div/div[1]/table/tbody/tr[1]/td[1]/span')
    folder_delete = (By.XPATH, '//*[@id="main"]/div/ui-view/div/div/div[2]/div/div[1]/div/div[2]/div[4]')
    delete_folder_button = (By.ID, 'deleteFolderButton')
    location_checkbox = (By.XPATH, '//input[@ng-model="item.selected"]')
    recording_checkbox = (By.XPATH, '//input[@ng-model="item.selected"]')
    alert_checkbox = (By.XPATH, '//input[@ng-model="item.selected"]')
    actions_menu = (By.LINK_TEXT, 'Actions')
    trash_button = (By.LINK_TEXT, 'Delete')
    alerts_trash_button = (By.ID, 'alertsTrashButton')
    location_confirm_delete = (By.ID, 'deleteLocationsButton')
    recording_confirm_delete = (By.ID, 'deleteRecordingsButton')
    alert_confirm_delete = (By.ID, 'deleteAlertsButton')
    new_alert_button = (By.XPATH, '//*[@id="bs-example-navbar-collapse-1"]/div/button')
    alert_activation_message = (By.CSS_SELECTOR, '.alertActivationMessage .fancy-button')

    no_data_found_message_locations = 'Locations'
    no_data_found_message_activeRecording = 'activeRecording'
    no_data_found_message_scheduledRecording = 'scheduledRecording'
    no_data_found_message_completedRecording = 'completedRecording'
    no_data_found_message_recordingTemplates = 'recordingTemplates'
    no_data_found_message_collections = 'collections'
    no_data_found_message_foldersActive = 'foldersActive'

    def get_left_tabs(self):
        return self.driver.find_elements(*self.left_tab)

    def get_scheduled_subtab(self):
        return self.driver.find_element(*self.scheduled_subtab)

    def get_completed_subtab(self):
        return self.driver.find_element(*self.completed_subtab)

    def get_recording_template_subtab(self):
        return self.driver.find_elements(*self.recording_template_subtab)

    def get_locations_grid_records(self):
        return self.driver.find_elements(*self.locations_grid_records)

    def get_recording_grid_records(self):
        return self.driver.find_elements(*self.recording_grid_records)

    def get_recording_templates_grid_records(self):
        return self.driver.find_elements(*self.recording_templates_grid_records)

    def get_collections_grid_records(self):
        return self.driver.find_elements(*self.collections_grid_records)

    def get_location_folder_edit_link(self):
        return self.driver.find_element(*self.location_folder_edit_link)

    def get_new_folder_button(self):
        return self.driver.find_element(*self.new_folder)

    def get_location_folder_name_field(self):
        return self.driver.find_element(*self.location_folder_name)

    def get_create_folder_button(self):
        return self.driver.find_element(*self.create_folder_button)

    def get_close_popup_button(self):
        return self.driver.find_element(*self.close_popup_button)

    def get_folder_row_name(self):
        return self.driver.find_element(*self.folder_row_name)

    def get_folder_buttons(self):
        return self.driver.find_elements(*self.folder_button)

    def get_folder_delete(self):
        return self.driver.find_element(*self.folder_delete)

    def get_delete_folder_button(self):
        return self.driver.find_element(*self.delete_folder_button)

    def get_no_data_found_message(self, clazz):
        return self.driver.find_element(*(By.CSS_SELECTOR, '.noDataFoundMessage.' + clazz))

    def get_location_checkbox(self):
        return self.driver.find_elements(*self.location_checkbox)

    def get_recording_checkbox(self):
        return self.driver.find_elements(*self.recording_checkbox)

    def get_alert_checkbox(self):
        return self.driver.find_elements(*self.alert_checkbox)

    def get_actions_menu(self):
        return self.driver.find_element(*self.actions_menu)

    def get_trash_button(self):
        return self.driver.find_element(*self.trash_button)

    def get_location_confirm_delete(self):
        return self.driver.find_element(*self.location_confirm_delete)

    def get_recording_confirm_delete(self):
        return self.driver.find_element(*self.recording_confirm_delete)

    def get_alert_confirm_delete(self):
        return self.driver.find_element(*self.alert_confirm_delete)

    def get_new_alert_button(self):
        return self.driver.find_element(*self.new_alert_button)

    def get_alert_activation_message(self):
        return self.driver.find_element(*self.alert_activation_message)

    def click_on_left_tab(self, index):
        tabs = self.get_left_tabs()
        tabs[index].click()

    def click_on_scheduled_subtab(self):
        self.get_scheduled_subtab().click()

    def click_on_completed_subtab(self):
        self.get_completed_subtab().click()

    def click_on_recording_template_subtab(self, index):
        tabs = self.get_recording_template_subtab()
        tabs[index].click()

    def click_on_location_folder_edit_link(self):
        self.get_location_folder_edit_link().click()

    def click_on_new_folder_button(self):
        self.get_new_folder_button().click()

    def set_location_folder_name(self, text):
        name_element = self.get_location_folder_name_field()
        name_element.send_keys(text)

    def click_on_create_folder_button(self):
        self.get_create_folder_button().click()

    def click_on_close_popup_button(self):
        self.get_close_popup_button().click()

    def click_on_folder_button(self, index):
        buttons = self.get_folder_buttons()
        buttons[index].click()

    def click_on_folder_delete(self):
        self.get_folder_delete().click()

    def click_on_delete_folder_button(self):
        self.get_delete_folder_button().click()

    def click_on_location_checkbox(self, index):
        self.get_location_checkbox()[index].click()

    def click_on_recording_checkbox(self, index):
        self.get_recording_checkbox()[index].click()

    def click_on_alert_checkbox(self, index):
        self.get_alert_checkbox()[index].click()

    def click_on_actions_menu(self):
        self.get_actions_menu().click()

    def click_on_trash_button(self):
        self.get_trash_button().click()

    def click_on_location_confirm_delete(self):
        self.get_location_confirm_delete().click()

    def click_on_recording_confirm_delete(self):
        self.get_recording_confirm_delete().click()

    def click_on_alert_confirm_delete(self):
        self.get_alert_confirm_delete().click()

    def click_on_new_alert_button(self):
        self.get_new_alert_button().click()

    def click_on_alert_activation_message(self):
        self.get_alert_activation_message().click()
