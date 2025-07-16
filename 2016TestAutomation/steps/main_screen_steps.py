import nose.tools as tools

from selenium.common.exceptions import TimeoutException
from pages.main_screen import MainScreen
from steps.base_module import BaseModule


class MainScreenSteps:

    def __init__(self, driver, logger):
        self.driver = driver
        self.main_screen = MainScreen(driver)
        self.feeds = ''
        self.logger = logger

    def do_search(self, text='New York City'):
        self.logger.info('Performing a new search for: ' + str(text))
        self.main_screen.set_search_field(text)
        self.main_screen.press_enter_search_field()
        BaseModule.wait(3)
        self.main_screen.click_halflings_search()
        BaseModule.wait(1)
        # self.main_screen.click_pin_text()
        # self.main_screen.click_by_circle()

    def validate_feed_counter(self, count):
        self.logger.info('Validating that feed counters are greater than ' + str(count))
        self.wait_until_load_finish()
        counter = self.main_screen.get_post_counter()
        self.feeds = counter.text.replace(',', '')
        tools.assert_greater(int(self.feeds), count, 'The feed counter was less than ' + str(count))
        self.logger.info('Total number of posts: ' + self.feeds)

    def validate_social_network_counters(self):
        self.logger.info('Validating social network counters')
        counters = self.main_screen.get_social_network_counters()
        names = self.main_screen.get_social_network_names()
        tools.assert_greater(len(counters), 0, 'Couldn\'t retrieve social item counters')

        for num in range(0, len(counters)):
            self.logger.info('Social network counter for ' + str(names[num].text) + ': ' + str(counters[num].text))
            print(names[num].text + ': ' + counters[num].text)

    def wait_until_load_finish(self):
        self.logger.info('Waiting for load to finish')
        while True:
            try:
                BaseModule.wait_for_element_visible(self.driver, self.main_screen.analytics_loading_cover, 5)
            except TimeoutException:
                return

    def get_more_in_collage(self):
        self.logger.info('Getting more items on Collage')
        self.main_screen.click_collage_link()
        BaseModule.wait(1)
        self.main_screen.click_load_more_link()

    def validate_collage_items(self):
        self.logger.info('Validating collage items')
        self.wait_until_load_finish()
        items = self.main_screen.get_collage_items()
        tools.assert_greater(len(items), 0, 'There was no collage items')
        self.logger.info('Number of collage items: ' + str(len(items)))

    def validate_analytics_data(self):
        self.logger.info('Validating analytics data')
        self.main_screen.click_analytics_link()
        BaseModule.wait(1)
        analytics_count = self.main_screen.get_analytics_post_count().text.replace(',', '')
        tools.assert_equal(self.feeds, analytics_count, 'Analytics data is not accurate')
        self.logger.info('Analytics data is accurate')

    def validate_data_manager_popup_item(self, expected):
        self.logger.info('Validating data manager popup items')
        items = self.main_screen.get_data_manager_items()
        tools.assert_greater(len(items), 0, 'Couldn\'t retrieve data manager items')
        tools.assert_in(expected, items[0].text, 'The selected location doesn\'t match')

    def click_mini_data_manager_item(self, item):
        self.logger.info('Clicking \'mini\' data manager')
        items = self.main_screen.get_mini_data_manager_items()
        items[item].click()
