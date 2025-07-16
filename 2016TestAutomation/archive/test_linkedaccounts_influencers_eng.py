import unittest

from steps.main_screen_steps import MainScreenSteps
from steps.base_module import BaseModule
from pages.main_screen import MainScreen
from pages.data_manager import DataManager
from pages.instagram_login import InstagramLogin
from pages.twitter_login import TwitterLogin
from pages.profile import Profile
from steps.profile_steps import ProfileSteps
from pages.influencers import Influencers
from steps.influencers_steps import InfluencersSteps

# 1. Go to My Account
# 2. Go to Linked Accounts
# 3. Link an Instagram Account
# 4. Username: geotestingman password: Gardee32
# 5. Verify that the account is added properly
# 6. Click on Test and verify that it changes to OK
# 7. Link a twitter Account
# 8. Username: geotestingadam password: Gardee32
# 9. Verify that the account is added properly
# 10. Click on Test and verify that it changes to OK
# 11. Click on App menu and go to influencers
# 12. Click on Add User
# 13. Click on Twitter
# 14. Verify that the account chosen is geotestingadam (might have to change capitalization)
# 15. Add user gardee32 in the username field
# 16. Click on Add User
# 17. Verify that Gardee32 is in the main section (capitalization matters)
# 18. Click on Add User
# 19. Click on Instagram
# 20. Verify that the account chosen is geotestingman (might have to change capitalization)
# 22. Add user gardee32 in the username field
# 23. Click on Add User
# 24. Verify that gardee32 is in the main section (capitalization matters)
# 25. Click on Gardee32
# 26. Verify that the collage view is populated
# 27. Go back to the main page
# 28. Click on gardee32
# 29. Verify that the collage view is populated


class LinkedAccountsInfluencersEngagement(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.driver = BaseModule.get_driver()

        cls.logger = BaseModule.get_logger('LinkedAccountsInfluencersEngagement')
        cls.logger.info('Test started')
        cls.logger.info('Webdriver created: ' + str(cls.driver))
        cls.main_screen = MainScreen(cls.driver)
        cls.main_screen_steps = MainScreenSteps(cls.driver, cls.logger)
        cls.data_manager = DataManager(cls.driver)
        cls.profile = Profile(cls.driver)
        cls.profile_steps = ProfileSteps(cls.driver, cls.logger)
        cls.instagram = InstagramLogin(cls.driver)
        cls.twitter = TwitterLogin(cls.driver)
        cls.influencers = Influencers(cls.driver)
        cls.influencers_steps = InfluencersSteps(cls.driver, cls.logger)

    def test(self):
        instagram_username = 'geofeediaauto'
        instagram_password = 'geogeoautomation2'
        twitter_username = 'GeofeediaAuto'
        twitter_password = 'geogeoautomation'

        BaseModule.do_login(self.driver, self.logger)
        self.logger.info('Clicking My Account button')
        self.main_screen.click_user_menu_button()
        BaseModule.wait(1)
        self.main_screen.click_user_menu_option(0)
        self.logger.info('Clicking Linked Accounts tab')
        BaseModule.wait(3)
        self.profile.click_linked_accounts_tab()
        self.logger.info('Linking an Instagram account')
        self.profile.click_link_account_button(0)
        BaseModule.wait(3)
        prev = BaseModule.switch_to_popup(self.driver)
        self.logger.info('Setting Instagram login data')
        BaseModule.wait(1)
        self.instagram.set_username(instagram_username)
        self.instagram.set_password(instagram_password)
        self.instagram.click_login_button()
        self.logger.info('Login onto Instagram...')
        BaseModule.set_window_handler(self.driver, prev)
        self.logger.info('Validating Instagram account added')
        BaseModule.wait(1)
        self.profile_steps.validate_instagram_account()
        self.profile.click_instagram_test_account()
        self.logger.info('Clicking on Instagram\'s account test link')
        BaseModule.wait(2)
        self.profile_steps.validate_instagram_test_ok()
        self.logger.info('Linking a Twitter account')
        self.profile.click_link_account_button(1)
        BaseModule.wait(3)
        prev = BaseModule.switch_to_popup(self.driver)
        self.logger.info('Setting Twitter login data')
        BaseModule.wait(1)
        self.twitter.set_username(twitter_username)
        self.twitter.set_password(twitter_password)
        self.twitter.click_login_button()
        self.logger.info('Login onto Twitter...')
        BaseModule.set_window_handler(self.driver, prev)
        self.logger.info('Validating Twitter account added')
        BaseModule.wait(1)
        self.profile_steps.validate_twitter_account()
        self.profile.click_twitter_test_account()
        self.logger.info('Clicking on Twitter\'s account test link')
        BaseModule.wait(2)
        self.profile_steps.validate_twitter_test_ok()
        self.logger.info('Clicking on Influencers')
        self.main_screen.click_app_manager()
        BaseModule.wait(1)
        self.main_screen.click_app_data_manager_button(4)
        BaseModule.wait(2)
        self.logger.info('Dismissing \'Try User Track\' popup')
        self.influencers.click_try_user_track_button()
        self.logger.info('Adding a Twitter user')
        # self.influencers.click_add_user()
        BaseModule.wait(2)
        self.influencers.click_add_user_twitter()
        self.logger.info('Validating the required account is selected on dropdown')
        self.influencers_steps.validate_selected_account(twitter_username)
        self.influencers.set_add_account_username(twitter_username)
        self.logger.info('Adding user...')
        self.influencers.click_add_user_button()
        BaseModule.wait(1)
        self.influencers.click_done_button()
        BaseModule.wait(2)
        self.logger.info('Validating addded account on main section')
        self.influencers_steps.validate_account_main_section(0, twitter_username, 'twitter')
        self.logger.info('Adding an Instagram user')
        self.influencers.click_add_user()
        BaseModule.wait(2)
        self.influencers.click_add_user_instagram()
        self.logger.info('Validating the required account is selected on dropdown')
        self.influencers_steps.validate_selected_account(instagram_username)
        self.influencers.set_add_account_username(instagram_username)
        self.logger.info('Adding user...')
        self.influencers.click_add_user_button()
        BaseModule.wait(1)
        self.influencers.click_done_button()
        BaseModule.wait(2)
        self.logger.info('Validating addded account on main section')
        self.influencers_steps.validate_account_main_section(0, instagram_username, 'instagram')
        BaseModule.wait(1)
        self.logger.info('Clicking on first account')
        self.influencers.click_main_section_row(0)
        BaseModule.wait(4)
        self.main_screen_steps.validate_collage_items()
        self.main_screen.click_app_manager()
        self.main_screen.click_app_data_manager_button(4)
        BaseModule.wait(2)
        self.logger.info('Clicking on second account')
        self.influencers.click_main_section_row(1)
        BaseModule.wait(4)
        self.main_screen_steps.validate_collage_items()

        # Cleanup

        self.logger.info('Clicking on Influencers')
        self.main_screen.click_app_manager()
        BaseModule.wait(1)
        self.main_screen.click_app_data_manager_button(4)
        BaseModule.wait(2)
        self.logger.info('Deleting first user')
        self.influencers.click_more_button(0)
        self.influencers.click_delete_user_button()
        self.influencers.click_confirm_delete_button()
        BaseModule.wait(1)
        self.logger.info('Deleting second user')
        self.influencers.click_more_button(0)
        self.influencers.click_delete_user_button()
        self.influencers.click_confirm_delete_button()
        BaseModule.wait(1)

        self.logger.info('Clicking My Account button')
        self.main_screen.click_user_menu_button()
        BaseModule.wait(1)
        self.main_screen.click_user_menu_option(0)
        self.logger.info('Clicking Linked Accounts tab')
        BaseModule.wait(3)
        self.profile.click_linked_accounts_tab()
        BaseModule.wait(1)
        self.profile.click_delete_account_link(0)
        self.profile.click_confirm_delete_button()
        BaseModule.wait(3)
        self.profile.click_delete_account_link(0)
        self.profile.click_confirm_delete_button()

    @classmethod
    def tearDown(cls):
        cls.logger.info('Test finished')
        cls.driver.quit()
