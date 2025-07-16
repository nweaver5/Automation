from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from .base_page import BasePage
from steps.base_module import BaseModule
from selenium.webdriver.support.ui import Select


class MainScreen(BasePage):
    search_field = (By.CSS_SELECTOR, '#map-toolbar .search')
    show_pin_text = (By.CSS_SELECTOR, '#map-toolbar .showPinText')
    by_circle_button = (By.CSS_SELECTOR, '.hint-popup .location-pin-popup-content .circle')
    post_counter = (By.ID, 'leftPostCounter')
    social_network_name = (By.CSS_SELECTOR, '.socialNetworkListContainer .socialNetworkItem .socialNetworkName')
    social_network_counter = (By.CSS_SELECTOR, '.socialNetworkListContainer .socialNetworkItem .counter')
    analytics_loading_cover = (By.CLASS_NAME, 'new-analytics-cover')
    collage_link = (By.CLASS_NAME, 'collageLink')
    load_more_link = (By.ID, 'loadMore')
    collage_item = (By.CLASS_NAME, 'feed-item-container')
    analytics_link = (By.CLASS_NAME, 'analyticLink')
    analytics_post_count = (By.CSS_SELECTOR, '.posts-count .mainText')
    save_location_button = (By.ID, 'saveLocationButton')
    save_recording_button = (By.ID, 'recordingButton')
    mini_data_manager_button = (By.ID, 'data-manager-nav-button')
    mini_data_manager_item = (By.CSS_SELECTOR, '.basePopupContent a')
    mini_data_manager_dropdown = (By.CSS_SELECTOR, '.basePopupContent .category-dropdown')
    app_manager = (By.ID, 'apps-menu-nav-button')
    app_data_manager_buttons = (By.CLASS_NAME, 'li-container')
    new_search = (By.CLASS_NAME, 'new-search-btn')
    new_search_down_arrow = (By.CSS_SELECTOR, '#backToSearch .down-arrow')
    discovery_search_option = (By.CSS_SELECTOR, 'input.discoverySearchDisabled')
    search_keyword_input = (By.ID, 'main-search-input')
    search_apply_button = (By.CLASS_NAME, 'search-button')
    keyword_search_option = (By.CSS_SELECTOR, 'input.keywordSearchDisabled')
    options_button = (By.ID, 'options')
    options_button_contents = (By.CSS_SELECTOR, '.optionMenu-item')
    download_csv_button = (By.ID, 'downloadCsv')
    download_pdf_icon = (By.ID, 'pdfDownloadIcon')
    download_pdf_button = (By.ID, 'download-button')
    user_notifications_button = (By.ID, 'user-notifications-button')
    notification_title = (By.CLASS_NAME, 'notificationTitle')
    clear_all_notifications = (By.CSS_SELECTOR, '.qtip-content #notificationClearButton')
    user_menu_button = (By.ID, 'user-menu-nav-button')
    user_menu_option = (By.CSS_SELECTOR, '.qtip-content .optionMenu-item')
    halflings_search = (By.CLASS_NAME, 'halflings-search')
    notifications_clear_link = (By.CSS_SELECTOR, '.qtip-content #notificationClearButton')

    def __init__(self, driver):
        super().__init__(driver)

    def get_post_counter(self):
        BaseModule.wait_for_element(self.driver, self.post_counter, 5)
        return self.driver.find_element(*self.post_counter)

    def get_search_field(self):
        return self.driver.find_element(*self.search_field)

    def get_pin_text(self):
        BaseModule.wait_for_element(self.driver, self.show_pin_text, 5)
        return self.driver.find_element(*self.show_pin_text)

    def get_by_circle_button(self):
        BaseModule.wait_for_element(self.driver, self.by_circle_button, 5)
        return self.driver.find_element(*self.by_circle_button)

    def get_collage_link(self):
        BaseModule.wait_for_element(self.driver, self.collage_link, 5)
        return self.driver.find_element(*self.collage_link)

    def get_analytics_link(self):
        BaseModule.wait_for_element(self.driver, self.analytics_link, 5)
        return self.driver.find_element(*self.analytics_link)

    def get_load_more_link(self):
        return self.driver.find_element(*self.load_more_link)

    def get_loading_thingy(self):
        return self.driver.find_element(*self.analytics_loading_cover)

    def get_collage_items(self):
        return self.driver.find_elements(*self.collage_item)

    def get_analytics_post_count(self):
        return self.driver.find_element(*self.analytics_post_count)

    def get_social_network_names(self):
        return self.driver.find_elements(*self.social_network_name)

    def get_social_network_counters(self):
        return self.driver.find_elements(*self.social_network_counter)

    def get_save_location_button(self):
        return self.driver.find_element(*self.save_location_button)

    def get_save_recording_button(self):
        return self.driver.find_element(*self.save_recording_button)

    def get_mini_data_manager_button(self):
        return self.driver.find_element(*self.mini_data_manager_button)

    def get_mini_data_manager_items(self):
        return self.driver.find_elements(*self.mini_data_manager_item)

    def get_mini_data_manager_dropdown(self):
        return self.driver.find_element(*self.mini_data_manager_dropdown)

    def get_app_manager(self):
        return self.driver.find_element(*self.app_manager)

    def get_app_data_manager_buttons(self):
        return self.driver.find_elements(*self.app_data_manager_buttons)

    def get_new_search(self):
        return self.driver.find_element(*self.new_search)

    def get_new_search_down_arrow(self):
        return self.driver.find_element(*self.new_search_down_arrow)

    def get_discovery_search_option(self):
        return self.driver.find_element(*self.discovery_search_option)

    def get_search_keyword_input(self):
        return self.driver.find_element(*self.search_keyword_input)

    def get_search_apply_button(self):
        return self.driver.find_element(*self.search_apply_button)

    def get_keyword_search_option(self):
        return self.driver.find_element(*self.keyword_search_option)

    def get_options_button(self):
        return self.driver.find_element(*self.options_button)

    def get_options_button_contents(self):
        return self.driver.find_elements(*self.options_button_contents)

    def get_download_csv_button(self):
        return self.driver.find_element(*self.download_csv_button)

    def get_download_pdf_icon(self):
        return self.driver.find_element(*self.download_pdf_icon)

    def get_download_pdf_button(self):
        return self.driver.find_element(*self.download_pdf_button)

    def get_user_notifications_button(self):
        return self.driver.find_element(*self.user_notifications_button)

    def get_clear_notifications_link(self):
        return self.driver.find_element(*self.clear_all_notifications)

    def get_notification_by_name(self, name):
        notifications = self.driver.find_elements(*self.notification_title)

        for each in notifications:
            if each.text == name:
                return each

    def get_user_menu_button(self):
        return self.driver.find_element(*self.user_menu_button)

    def get_user_menu_options(self):
        return self.driver.find_elements(*self.user_menu_option)

    def get_halflings_search(self):
        return self.driver.find_element(*self.halflings_search)

    def get_notifications_clear_link(self):
        return self.driver.find_element(*self.notifications_clear_link)

    def set_search_field(self, keys):
        search_element = self.get_search_field()
        search_element.send_keys(keys)

    def press_enter_search_field(self):
        search_element = self.get_search_field()
        search_element.send_keys(Keys.RETURN)

    def click_pin_text(self):
        show_pin_text_element = self.get_pin_text()
        show_pin_text_element.click()

    def click_by_circle(self):
        by_circle_button_element = self.get_by_circle_button()
        by_circle_button_element.click()

    def click_collage_link(self):
        collage_link_element = self.get_collage_link()
        collage_link_element.click()

    def click_load_more_link(self):
        load_more_link_element = self.get_load_more_link()
        load_more_link_element.click()

    def click_analytics_link(self):
        analytics_link_element = self.get_analytics_link()
        analytics_link_element.click()

    def click_save_location_button(self):
        save_location_button_element = self.get_save_location_button()
        save_location_button_element.click()

    def click_save_recording_button(self):
        save_recording_button_element = self.get_save_recording_button()
        save_recording_button_element.click()

    def click_mini_data_manager_button(self):
        data_manager_button_element = self.get_mini_data_manager_button()
        data_manager_button_element.click()

    def set_mini_data_manager_dropdown(self, index):
        data_manager_select = Select(self.get_mini_data_manager_dropdown())
        data_manager_select.select_by_index(index)

    def click_app_manager(self):
        app_manager_element = self.get_app_manager()
        app_manager_element.click()

    def click_app_data_manager_button(self, index):
        data_manager_button = self.get_app_data_manager_buttons()
        data_manager_button[index].click()

    def click_new_search_down_arrow(self):
        new_search_down_arrow = self.get_new_search_down_arrow()
        new_search_down_arrow.click()

    def click_discovery_search_option(self):
        discovery_search_option = self.get_discovery_search_option()
        discovery_search_option.click()

    def set_search_keyword_input(self, keys):
        search_keyword_input = self.get_search_keyword_input()
        search_keyword_input.send_keys(keys)

    def click_search_apply_button(self):
        discovery_search_apply_button = self.get_search_apply_button()
        discovery_search_apply_button.click()

    def click_keyword_search_option(self):
        keyword_search_option = self.get_keyword_search_option()
        keyword_search_option.click()

    def click_options_button(self):
        BaseModule.wait_for_element_to_be_clickable(self.driver, self.options_button, 10)
        options_button = self.get_options_button()
        options_button.click()

    def click_options_button_item(self, item):
        items = self.get_options_button_contents()
        items[item].click()

    def click_download_pdf_icon(self):
        pdf_icon = self.get_download_pdf_icon()
        pdf_icon.click()

    def click_download_pdf_button(self):
        pdf_download_button = self.get_download_pdf_button()
        pdf_download_button.click()

    def click_download_csv_button(self):
        download_csv_button = self.get_download_csv_button()
        download_csv_button.click()

    def click_new_search(self):
        new_search = self.get_new_search()
        new_search.click()

    def click_user_notifications_button(self):
        user_notifications_button = self.get_user_notifications_button()
        user_notifications_button.click()

    def click_notification(self, name):
        notification = self.get_notification_by_name(name)
        notification.click()

    def click_clear_all_notifications(self):
        self.get_clear_notifications_link().click()

    def click_user_menu_button(self):
        BaseModule.wait_for_element_visible(self.driver, self.user_menu_button, 5)
        self.get_user_menu_button().click()

    def click_user_menu_option(self, index):
        self.get_user_menu_options()[index].click()

    def click_halflings_search(self):
        self.get_halflings_search().click()

    def click_improved_search_experience_button(self):
        self.get_improved_search_experience_button().click()

    def click_notifications_clear_link(self):
        self.get_notifications_clear_link().click()
