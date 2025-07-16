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
        cls.main_screen = MainScreen(cls.driver)
        cls.main_screen_steps = MainScreenSteps(cls.driver, cls.logger)
        cls.data_manager = DataManager(cls.driver)
        cls.new_alert = NewAlert(cls.driver)

    def test(self):
        self.logger.info('Maximizing window')
        BaseModule.do_login(self.driver, self.logger)
        self.logger.info('Clicking on User Notifications button')
        self.main_screen.click_user_notifications_button()
        self.logger.info('Clicking on clear all notifications')
        self.main_screen.click_clear_all_notifications()
        self.logger.info('Clicking on App Manager')
        self.main_screen.click_app_manager()
        BaseModule.wait(1)
        self.logger.info('Clicking on the Alerts option')
        self.main_screen.click_app_data_manager_button(1)  # Alerts
        BaseModule.wait(2)
        self.main_screen_steps.wait_until_load_finish()
        self.logger.info('Clicking on New Alert')
        self.data_manager.click_on_new_alert_button()
        alert_name = '0 - Automation Alert'
        keywords_allowed = 'new york, new, nyc'
        keywords_excluded = 'city'
        self.logger.info('Setting new Alert name to ' + alert_name)
        self.new_alert.set_alert_name(alert_name)
        self.logger.info('Setting allowed keywords to ' + keywords_allowed)
        self.new_alert.set_keywords_allowed(keywords_allowed)
        self.logger.info('Setting excluded keywords to ' + keywords_excluded)
        self.new_alert.set_keywords_excluded(keywords_excluded)
        BaseModule.wait(2)
        self.logger.info('Clicking on the recording checkbox')
        self.new_alert.click_on_manhattan_recording_checkbox()
        self.logger.info('Clicking on the user checkbox')
        self.new_alert.click_on_tester_one_checkbox()
        self.logger.info('Clicking on Activate Alert')
        self.new_alert.click_on_activate_alert()
        BaseModule.wait(2)
        self.main_screen_steps.wait_until_load_finish()
        self.data_manager.click_on_alert_activation_message()
        # self.logger.info('Clicking on new search')
        # self.main_screen.click_new_search()
        self.logger.info('Cleaning up notifications')
        self.main_screen.click_user_notifications_button()
        BaseModule.wait(1)
        self.main_screen.click_notifications_clear_link()
        self.main_screen.click_user_notifications_button()
        self.logger.info('Waiting for alert to be populated')
        BaseModule.wait(90)
        self.logger.info('Clicking on User Notifications button')
        self.main_screen.click_user_notifications_button()
        BaseModule.wait(2)
        self.logger.info('Clicking on the notifications for the alert')
        self.main_screen.click_notification(alert_name)
        self.main_screen_steps.wait_until_load_finish()
        BaseModule.wait(2)
        self.main_screen_steps.validate_feed_counter(0)
        self.logger.info('Clicking on Collage link')
        self.main_screen.click_collage_link()
        BaseModule.wait(1)
        self.main_screen_steps.validate_collage_items()
        self.logger.info('Clicking on App Manager')
        self.main_screen.click_app_manager()
        BaseModule.wait(1)
        self.logger.info('Clicking on the Alerts option')
        self.main_screen.click_app_data_manager_button(1)  # Alerts
        BaseModule.wait(2)
        self.main_screen_steps.wait_until_load_finish()
        BaseModule.wait(3)
        self.logger.info('Checking the alert checkbox')
        self.data_manager.click_on_alert_checkbox(0)
        BaseModule.wait(3)
        self.logger.info('Clickling on the Alerts delete button')
        self.data_manager.click_on_alerts_trash_button()
        self.logger.info('Confirming the deletion')
        self.data_manager.click_on_confirm_delete_button()

    @classmethod
    def tearDown(cls):
        cls.logger.info('Test finished')
        cls.driver.quit()
