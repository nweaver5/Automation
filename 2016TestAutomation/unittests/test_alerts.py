import unittest

from steps.main_screen_steps import MainScreenSteps
from steps.base_module import BaseModule
from pages.main_screen import MainScreen
from pages.data_manager import DataManager
from pages.new_alert import NewAlert

# 1. Go to App Menu
# 2. Click on Alerts
# 3. Click on Create New Alert
# 4. Alert Name should be "0 - Automation Alert"
# 5. Include Keywords "new, city, manhattan, love"
# 6. Exclude Keywords "york, happy"
# 7. Click on the Manhattan Recording check box
# 8. Click on the user check box
# 9. Click on Activate Alert
# 10. Click on New Search
# 11. Pause for 1 minute
# 12. Click on notifications icon
# 13. Verify that the alert you created has items
# 14. Click on the alert
# 15. Verify that you were redirected to the alert view page
# 16. Verify that the collage view is populated
# 17. Go to App Menu
# 18. Click on Alerts
# 19. Click on the Automation Alert check box
# 20. Delete the alert


class Alerts(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.driver = BaseModule.get_driver()

        cls.logger = BaseModule.get_logger('Alerts')
        cls.logger.info('Test started')
        cls.logger.info('Webdriver created: ' + str(cls.driver))
        cls.driver.maximize_window()
        cls.main_screen = MainScreen(cls.driver)
        cls.main_screen_steps = MainScreenSteps(cls.driver, cls.logger)
        cls.data_manager = DataManager(cls.driver)
        cls.new_alert = NewAlert(cls.driver)

    def test(self):
        self.logger.info('Maximizing window')
        BaseModule.do_login(self.driver, self.logger)
        self.logger.info('Clicking on App Manager')
        self.main_screen.click_app_manager()
        BaseModule.wait(1)
        self.logger.info('Clicking on the Alerts option')
        self.main_screen.click_app_data_manager_button(14)  # Alerts
        BaseModule.wait(2)
        self.main_screen_steps.wait_until_load_finish()
        self.logger.info('Clicking on New Alert')
        self.data_manager.click_on_new_alert_button()
        BaseModule.wait(1)
        alert_name = '0 - Automation Alert'
        recording_name = 'Manhattan Recording'
        keywords_allowed = 'new york, new, nyc'
        keywords_excluded = 'city'
        recipient = 'tester'
        self.logger.info('Setting new Alert name to ' + alert_name)
        self.new_alert.set_alert_name(alert_name)
        self.logger.info('Selecting Recording')
        self.new_alert.set_recordings_selection(recording_name)
        BaseModule.wait(2)
        self.new_alert.press_enter_recording()
        self.new_alert.click_on_alert_type_select2(0)
        self.new_alert.click_on_alert_type(0)
        BaseModule.wait(1)
        self.new_alert.click_on_add_alert_keyword_field_button()
        self.logger.info('Setting allowed keywords to ' + keywords_allowed)
        self.new_alert.set_keywords_allowed(keywords_allowed)
        self.new_alert.click_on_keyword_dropdown()
        self.new_alert.select_keyword_dropdown_option()
        self.logger.info('Setting excluded keywords to ' + keywords_excluded)
        self.new_alert.set_keywords_excluded(keywords_excluded)
        BaseModule.wait(2)
        self.logger.info('Setting Alert Recipient to ' + recipient)
        self.new_alert.set_recipient_selection(recipient)
        BaseModule.wait(2)
        self.new_alert.press_enter_recipient()
        self.logger.info('Clicking on Activate Alert')
        self.new_alert.click_on_activate_alert()
        BaseModule.wait(5)
        self.logger.info('Checking the alert checkbox')
        self.data_manager.click_on_alert_checkbox(0)
        BaseModule.wait(1)
        self.data_manager.click_on_actions_menu()
        BaseModule.wait(1)
        self.data_manager.click_on_trash_button()
        self.logger.info('Confirming the deletion')
        self.data_manager.click_on_alert_confirm_delete()
        self.main_screen_steps.wait_until_load_finish()

    @classmethod
    def tearDown(cls):
        cls.logger.info('Test finished')
        cls.driver.quit()
