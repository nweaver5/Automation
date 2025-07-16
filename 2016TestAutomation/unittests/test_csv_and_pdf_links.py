import nose.tools as tools
import unittest
import sys
import os

from steps.main_screen_steps import MainScreenSteps
from steps.base_module import BaseModule
from pages.main_screen import MainScreen
from selenium import webdriver

# 1. Go to mini data manager, click on a recording
# 2. Go to Options and click download CSV
# 3. Wait for CSV to download
# 4. Verify that CSV was downloaded
# 5. Go to analytics page
# 6. Click on PDF download
# 7. Click on Download button
# 8. Wait for PDF to download
# 9. Verify PDF was downloaded.


class CVSAndPDFLinksTest(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.logger = BaseModule.get_logger('CVSAndPDFLinksTest')
        cls.logger.info('Test started')
        options = webdriver.ChromeOptions()
        cls.downloads_dir = os.path.abspath(os.sep) + 'tmp'
        csv_filename = cls.downloads_dir + os.sep + 'Manhattan-Completed-Recording'
        cls.csv_path = csv_filename + '.csv'
        pdf_filename = cls.downloads_dir + os.sep + 'Manhattan Completed Recording'
        cls.pdf_path = pdf_filename + '.pdf'

        cls.logger.info('Setting CSV filename to: ' + cls.csv_path)
        cls.logger.info('Setting PDF filename to: ' + cls.pdf_path)

        prefs = {'download.default_directory': cls.downloads_dir, 'download.prompt_for_download': 'false'}
        options.add_experimental_option('prefs', prefs)

        cls.driver = BaseModule.get_driver(options)

        cls.logger.info('Webdriver created: ' + str(cls.driver))
        cls.driver.maximize_window()
        cls.main_screen = MainScreen(cls.driver)
        cls.main_screen_steps = MainScreenSteps(cls.driver, cls.logger)

    def test(self):
        BaseModule.do_login(self.driver, self.logger)

        # CSV
        self.logger.info('Clicking on Mini Data Manager button')
        self.main_screen.click_mini_data_manager_button()
        BaseModule.wait(1)
        self.logger.info('Selecting Recordings on the dropdown')
        self.main_screen.set_mini_data_manager_dropdown(3)
        BaseModule.wait(1)
        self.logger.info('Clicking on the first recording')
        self.main_screen_steps.click_mini_data_manager_item(0)
        self.main_screen_steps.wait_until_load_finish()
        BaseModule.wait(1)
        self.logger.info('Clicking on options button')
        self.main_screen.click_options_button()
        self.main_screen.click_options_button_item(3)
        self.logger.info('Downloading CSV')
        self.main_screen.click_download_csv_button()
        tools.assert_true(BaseModule.wait_for_file_to_exist(self.csv_path, self.logger))
        BaseModule.verify_file_not_empty(self.csv_path, self.logger)
        BaseModule.delete_file(self.csv_path, self.logger)
        self.logger.info('CSV validated correctly')

        # PDF
        self.logger.info('Clicking on Analytics link')
        self.main_screen.click_analytics_link()
        BaseModule.wait(1)
        self.logger.info('Downloading PDF')
        self.main_screen.click_download_pdf_icon()
        BaseModule.wait_for_element_visible(self.driver, self.main_screen.download_pdf_button, 2)
        BaseModule.wait_for_element_to_be_clickable(self.driver, self.main_screen.download_pdf_button, 2)
        self.main_screen.click_download_pdf_button()
        tools.assert_true(BaseModule.wait_for_file_to_exist(self.pdf_path, self.logger))
        BaseModule.verify_file_not_empty(self.pdf_path, self.logger)
        BaseModule.delete_file(self.pdf_path, self.logger)
        self.logger.info('PDF validated correctly')

    @classmethod
    def tearDown(cls):
        cls.logger.info('Test finished')
        cls.driver.quit()
