import nose.tools as tools

from pages.data_manager import DataManager


class DataManagerSteps:

    def __init__(self, driver, logger):
        self.driver = driver
        self.logger = logger
        self.data_manager = DataManager(self.driver)

    def verify_location_grid_text(self, index, text):
        self.logger.info('Verifying location text to be ' + text)
        grids = self.data_manager.get_locations_grid_records()
        tools.assert_in(text, grids[index].text, 'The field didn\'t match')

    def verify_recording_grid_text(self, index, text):
        self.logger.info('Verifying recording text to be ' + text)
        grids = self.data_manager.get_recording_grid_records()
        tools.assert_in(text, grids[index].text, 'The field didn\'t match')

    def verify_recording_templates_grid_text(self, index, text):
        self.logger.info('Verifying templates text to be ' + text)
        grids = self.data_manager.get_recording_templates_grid_records()
        tools.assert_in(text, grids[index].text, 'The field didn\'t match')

    def verify_collections_grid_text(self, index, text):
        self.logger.info('Verifying collections text to be ' + text)
        grids = self.data_manager.get_collections_grid_records()
        tools.assert_in(text, grids[index].text, 'The field didn\'t match')

    def verify_folder_name(self, text):
        self.logger.info('Verifying folder name to be ' + text)
        name = self.data_manager.get_folder_row_name()
        tools.assert_in(text, name.text, 'The name didn\'t match')

    def verify_no_data_found(self, text):
        self.logger.info('Verifying no data found message present')
        message = self.data_manager.get_no_data_found_message(text)
        tools.assert_true(message.is_displayed())
