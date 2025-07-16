import unittest
import sys

from steps.main_screen_steps import MainScreenSteps
from steps.base_module import BaseModule
from selenium import webdriver


class RealTimeSearch(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.driver = BaseModule.get_driver()

        cls.logger = BaseModule.get_logger('RealTimeSearch')
        cls.logger.info('Test started')
        cls.logger.info('Webdriver created: ' + str(cls.driver))

        cls.driver.maximize_window()
        cls.main_screen_steps = MainScreenSteps(cls.driver, cls.logger)

    def test(self):
        BaseModule.do_login(self.driver, self.logger)
        self.main_screen_steps.do_search()
        self.main_screen_steps.validate_feed_counter(0)
        self.main_screen_steps.validate_social_network_counters()
        self.main_screen_steps.get_more_in_collage()
        self.main_screen_steps.validate_feed_counter(0)
        self.main_screen_steps.validate_collage_items()
        self.main_screen_steps.validate_analytics_data()

    @classmethod
    def tearDown(cls):
        cls.logger.info('Test finished')
        cls.driver.quit()
