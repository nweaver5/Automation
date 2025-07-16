import unittest
import sys

from steps.main_screen_steps import MainScreenSteps
from steps.data_manager_steps import DataManagerSteps
from steps.base_module import BaseModule
from pages.main_screen import MainScreen
from pages.data_manager import DataManager
from selenium import webdriver

# 1. Click on the App Manager
# 2. Select Data Manager
# 3. Verify that saved locations are there
# 4. Click on Recordings Tab
# 5. Verify that active recordings are there
# 6. Click on scheduled
# 7. Verify that scheduled recordings are there
# 8. Click on Completed
# 9. Verify that completed recordings are there
# 10. Click on Recording Templates
# 11. Verify that templates are there
# 12. Click on Collections
# 13. Verify that collections are there
# 14. Click on Alerts
# 15. Verify that active alerts are there
# 16. Click on Inactive
# 17. Verify that inactive alerts are there
# 18. Verify and identify the location folders are there
# 19. Click on location folders-edit
# 20. Click on new folder
# 21. Name the new folder Automation Test Folder
# 22. Click on Create Folder
# 23. Verify that the new folder appears in the left side menu
# 24. Find the folder you just created, and click on delete
# 25. Verify that folder you just created is now gone.


class DataManagerTest(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.driver = BaseModule.get_driver()

        cls.logger = BaseModule.get_logger('DataManagerTest')
        cls.logger.info('Test started')
        cls.logger.info('Webdriver created: ' + str(cls.driver))
        cls.driver.maximize_window()
        cls.main_screen = MainScreen(cls.driver)
        cls.data_manager = DataManager(cls.driver)
        cls.main_screen_steps = MainScreenSteps(cls.driver, cls.logger)
        cls.data_manager_steps = DataManagerSteps(cls.driver, cls.logger)

    def test(self):
        BaseModule.do_login(self.driver, self.logger)
        self.logger.info('Clicking app manager')
        self.main_screen.click_app_manager()
        BaseModule.wait(1)
        self.logger.info('Clicking Data Manager button')
        self.main_screen.click_app_data_manager_button(9)  # Data Manager
        BaseModule.wait(1)
        self.data_manager_steps.verify_location_grid_text(0, 'Manhattan')
        self.logger.info('Clicking on Recordings tab')
        self.data_manager.click_on_left_tab(1)  # Recordings
        BaseModule.wait(3)
        self.data_manager_steps.verify_recording_grid_text(0, 'Manhattan Recording')
        self.logger.info('Clicking on Scheduled tab')
        self.data_manager.click_on_scheduled_subtab()  # Scheduled
        BaseModule.wait(3)
        self.data_manager_steps.verify_recording_grid_text(0, 'Manhattan Scheduled Recording')
        self.logger.info('Clicking on Completed tab')
        self.data_manager.click_on_completed_subtab()  # Completed
        BaseModule.wait(3)
        self.data_manager_steps.verify_recording_grid_text(0, 'Manhattan Completed Recording')
        self.logger.info('Clicking on Keyword templates tab')
        self.data_manager.click_on_left_tab(2)  # Templates
        BaseModule.wait(3)
        self.data_manager_steps.verify_recording_templates_grid_text(0, 'Automation Keyword Template')
        self.logger.info('Clicking on Recording templates tab')
        self.data_manager.click_on_recording_template_subtab(1) #Recording Templates
        BaseModule.wait(3)
        self.data_manager_steps.verify_recording_templates_grid_text(0, 'Manhattan Recording Template')
        self.logger.info('Clicking on Collections tab')
        self.data_manager.click_on_left_tab(3)  # Collections
        BaseModule.wait(3)
        self.data_manager_steps.verify_collections_grid_text(0, 'Manhattan Collection')
        self.logger.info('Clicking on Locations folder edit link')
        self.data_manager.click_on_location_folder_edit_link()
        BaseModule.wait(1)
        self.logger.info('Clicking on new folder button')
        self.data_manager.click_on_new_folder_button()
        BaseModule.wait(1)
        location_folder_name = 'Automation Test Folder'
        self.logger.info('Setting Location folder name to ' + location_folder_name)
        self.data_manager.set_location_folder_name(location_folder_name)
        self.logger.info('Clicking on create folder button')
        self.data_manager.click_on_create_folder_button()
        BaseModule.wait(2)
        self.data_manager_steps.verify_folder_name('Automation Test Folder')
        self.logger.info('Deleting folder')
        self.data_manager.click_on_folder_button(0)
        BaseModule.wait(1)
        self.data_manager.click_on_folder_delete()
        self.data_manager.click_on_delete_folder_button()
        self.main_screen_steps.wait_until_load_finish()
        #self.data_manager_steps.verify_no_data_found(self.data_manager.no_data_found_message_foldersActive)

    @classmethod
    def tearDown(cls):
        cls.logger.info('Test finished')
        cls.driver.quit()
