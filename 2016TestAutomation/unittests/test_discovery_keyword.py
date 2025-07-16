import unittest
import sys

from steps.main_screen_steps import MainScreenSteps
from steps.data_manager_steps import DataManagerSteps
from steps.base_module import BaseModule
from pages.main_screen import MainScreen
from pages.data_manager import DataManager
from selenium import webdriver

# 1. In the New Search drop down menu, select discovery search
# 2. Type in something that will yield a lot of results, for example "Nike, Mcdonalds, Starbucks"
# 3. Verify the results number is populated
# 4. Verify that the pills are > 0
# 5. Click on the collage view tab
# 6. Verify that the collage view is populated
# 7. Click on the analytics tab
# 8. Verify that the fields are populated and accurate
# 9. In the New Search drop down menu, select keyword search
# 10. Search something simple like "dog"
# 11. Verify that 100 results showed up
# 12. Verify that the twitter pill matches
# 13. Click load more
# 14. Verify that the new results is 200 (should be 200)
# 15. Verify that the pill still matches
# 16. Verify that the collage is populated
# 17. Click on the Analytics tab
# 18. Verify that the fields are populated and accurate


class DiscoveryAndKeywordSearch(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.driver = BaseModule.get_driver()

        cls.logger = BaseModule.get_logger('DiscoveryAndKeywordSearch')
        cls.logger.info('Test started')
        cls.logger.info('Webdriver created: ' + str(cls.driver))
        cls.driver.maximize_window()
        cls.main_screen = MainScreen(cls.driver)
        cls.data_manager = DataManager(cls.driver)
        cls.main_screen_steps = MainScreenSteps(cls.driver, cls.logger)
        cls.data_manager_steps = DataManagerSteps(cls.driver, cls.logger)

    def test(self):
        BaseModule.do_login(self.driver, self.logger)

        # Discovery Search
        self.logger.info('In the New Search drop down menu, selecting discovery search')
        self.main_screen.click_new_search()
        self.main_screen.click_discovery_search_option()
        self.logger.info('Typing \'Nike, Mcdonalds, Starbucks\' in the discovery search field')
        self.main_screen.set_search_keyword_input('Nike, Mcdonalds, Starbucks')
        self.main_screen.click_search_apply_button()
        BaseModule.wait(2)
        self.main_screen_steps.validate_feed_counter(0)
        self.main_screen_steps.validate_social_network_counters()
        self.main_screen.click_collage_link()
        BaseModule.wait(1)
        self.main_screen_steps.validate_collage_items()
        self.main_screen_steps.validate_analytics_data()

        # Keyword search
        self.logger.info('In the New Search drop down menu, selecting keyword search')
        self.main_screen.click_new_search()
        self.main_screen.click_keyword_search_option()
        self.logger.info('Typing \'donald trump\' in the keyword search field')
        self.main_screen.set_search_keyword_input('donald trump')
        self.main_screen.click_search_apply_button()
        BaseModule.wait(2)
        self.main_screen_steps.validate_feed_counter(90)
        self.main_screen_steps.validate_social_network_counters()
        self.main_screen.click_load_more_link()
        self.main_screen_steps.validate_feed_counter(190)
        self.main_screen_steps.validate_collage_items()
        self.main_screen_steps.validate_analytics_data()

    @classmethod
    def tearDown(cls):
        cls.logger.info('Test finished')
        cls.driver.quit()
