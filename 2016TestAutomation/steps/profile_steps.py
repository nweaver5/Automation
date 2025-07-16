import nose.tools as tools

from pages.profile import Profile
from steps.base_module import BaseModule


class ProfileSteps:

    def __init__(self, driver, logger):
        self.driver = driver
        self.logger = logger
        self.profile = Profile(self.driver)

    def validate_instagram_account(self):
        BaseModule.wait_for_element(self.driver, self.profile.instagram_linked_accounts, 5)

    def validate_instagram_test_ok(self):
        tools.assert_in('OK', self.profile.get_instagram_test_account().text, 'The Instagram account test failed')

    def validate_twitter_account(self):
        BaseModule.wait_for_element(self.driver, self.profile.twitter_linked_accounts, 5)

    def validate_twitter_test_ok(self):
        tools.assert_in('OK', self.profile.get_twitter_test_account().text, 'The Twitter account test failed')
