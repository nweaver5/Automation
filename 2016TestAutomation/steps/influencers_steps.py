import nose.tools as tools

from selenium.webdriver.common.by import By
from pages.influencers import Influencers


class InfluencersSteps:

    def __init__(self, driver, logger):
        self.driver = driver
        self.logger = logger
        self.influencers = Influencers(self.driver)

    def validate_selected_account(self, text):
        tools.assert_in(text, self.influencers.get_selected_account().text, 'The selected account didn\'t match')

    def validate_account_main_section(self, index, username, clazz):
        columns = self.influencers.get_main_section_rows()[index].find_elements(*(By.CLASS_NAME, 'cellWithPointer'))
        tools.assert_in(username, columns[0].find_element(By.CLASS_NAME, 'clickableCell').text,
                        'The account information didn\'t match')
        tools.assert_in(clazz, columns[1].find_element(By.CLASS_NAME, 'folderView').get_attribute('class'),
                        'The account type didn\'t match')

