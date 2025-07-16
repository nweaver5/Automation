import unittest
import nose.tools as tools
import sys

from steps.base_module import BaseModule
from pages.main_screen import MainScreen
from pages.save_location import SaveLocationPopup
from pages.save_recording import SaveRecordingPopup
from steps.main_screen_steps import MainScreenSteps
from pages.data_manager import DataManager
from selenium import webdriver

# 1. Search for a new location typing a location (like New York) in the search bar
# 2. Hitting Enter
# 3. Clicking on the Show address button
# 4. Click on the "by circle"
# 5. Wait for results to show up
# 6. Verify results show up
# 7. Click on the save location button
# 8. In the Name field type in a name like "Automation Saved Location"
# 9. In the visibility drop down, choose public
# 10. Click the save button
# 11. Wait for the page to load
# 12. Click on the new recording button
# 13. In the Name field type in a name like "Automation Recording"
# 14. in the visibility drop down select public
# 15. Click on the Locations Tab
# 16. In the search locations type in the name of the location from step 8
# 17. Select the location searched by either clicking or hitting enter
# 18. in the sources tab, uncheck picasa and flickr
# 19. Click Activate Recording button


class SavedLocationAndRecording(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.driver = BaseModule.get_driver()

        cls.logger = BaseModule.get_logger('SavedLocationAndRecording')
        cls.logger.info('Test started')
        cls.logger.info('Webdriver created: ' + str(cls.driver))

        cls.driver.maximize_window()
        cls.main_screen = MainScreen(cls.driver)
        cls.save_location = SaveLocationPopup(cls.driver)
        cls.save_recording = SaveRecordingPopup(cls.driver)
        cls.main_screen_steps = MainScreenSteps(cls.driver, cls.logger)
        cls.data_manager = DataManager(cls.driver)

    def test(self):
        BaseModule.do_login(self.driver, self.logger)
        self.main_screen_steps.do_search()
        self.main_screen_steps.validate_feed_counter(0)
        self.logger.info('Click on save recording button')
        self.main_screen.click_save_recording_button()
        location_name = '0 - Automation Saved Location'
        self.logger.info('Setting location name to ' + location_name)
        self.save_location.set_location_name(location_name)
        #self.logger.info('Setting location visibility to public')
        #self.save_location.set_location_visibility(1)
        BaseModule.wait(1)
        self.logger.info('Save the location')
        self.save_location.click_save_location_button()
        BaseModule.wait(1)
        self.main_screen_steps.wait_until_load_finish()
        #self.logger.info('Click on save recording button')
        #self.main_screen.click_save_recording_button()
        recording_name = '0 - Automation Recording'
        self.logger.info('Setting recording name to ' + recording_name)
        self.save_recording.set_recording_name(recording_name)
        #self.logger.info('Setting recording visibility to public')
        #self.save_recording.set_recording_visibility(1)
        self.logger.info('Click on the Locations Tab')
        self.save_recording.click_on_left_tab_popup(1)
        BaseModule.wait(1)
        self.verify_selected_location('0 - Automation Saved Location')
        self.logger.info('Click on the Sources Tab')
        self.save_recording.click_on_left_tab_popup(4)
        BaseModule.wait(1)
        self.save_recording.click_on_unlock_source_checkbox()
        self.logger.info('Unchecking flick and picasa checkboxes')
        BaseModule.wait(1)
        self.save_recording.click_on_source_checkbox('flickr')
        self.save_recording.click_on_source_checkbox('picasa')
        self.logger.info('Clicking on Activate recording')
        self.save_recording.click_on_activate_recording()
        BaseModule.wait(2)
        self.logger.info('Clicking on View recording')
        self.save_recording.click_on_view_recording()

        # Delete created data
        self.logger.info('Deleting created data')
        BaseModule.wait(1)
        self.main_screen.click_app_manager()
        BaseModule.wait(2)
        self.main_screen.click_app_data_manager_button(8)  # Data Manager
        BaseModule.wait(1)
        self.main_screen_steps.wait_until_load_finish()
        self.data_manager.click_on_left_tab(0)
        BaseModule.wait(3)
        self.data_manager.click_on_location_checkbox(0)
        BaseModule.wait(3)
        self.data_manager.click_on_actions_menu()
        BaseModule.wait(1)
        self.data_manager.click_on_trash_button()
        BaseModule.wait(1)
        self.data_manager.click_on_location_confirm_delete()
        self.main_screen_steps.wait_until_load_finish()
        BaseModule.wait(1)
        self.data_manager.click_on_left_tab(1)
        BaseModule.wait(3)
        self.data_manager.click_on_recording_checkbox(0)
        BaseModule.wait(3)
        self.data_manager.click_on_actions_menu()
        BaseModule.wait(1)
        self.data_manager.click_on_trash_button()
        BaseModule.wait(1)
        self.data_manager.click_on_recording_confirm_delete()
        self.main_screen_steps.wait_until_load_finish()

    def verify_selected_location(self, required_value):
        self.logger.info('Verifying location: ' + required_value)
        selected_location = self.save_recording.get_selected_location().text
        tools.assert_in(required_value, selected_location, 'The selected location doesn\'t match')

    @classmethod
    def tearDown(cls):
        cls.logger.info('Test finished')
        cls.driver.quit()
