import time
import nose.tools as tools
import logging
import sys
import os
import datetime

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login import Login

stream = None


class BaseModule:

    @staticmethod
    def get_driver(capabilities=None):
        driver = None

        try:
            browser = os.environ['AUTOMATION_BROWSER']
        except KeyError:
            browser = 'Chrome'

        try:
            url = os.environ['AUTOMATION_URL']
        except KeyError:
            url = 'https://app.qa1.us-east-1.local/master/geofeed'

        if sys.platform == "win32":
            if browser is 'IE':
                driver = webdriver.Ie(executable_path='../drivers/IEDriverServer_win32_2.53.1.exe', capabilities=capabilities)
            elif browser is 'Firefox':
                driver = webdriver.Firefox(capabilities=capabilities)
            else:
                driver = webdriver.Chrome(executable_path='../drivers/chromedriver_win32.exe', chrome_options=capabilities)
        elif sys.platform == "darwin":
            if browser is 'Safari':
                driver = webdriver.Safari(executable_path='../drivers/SafariDriver.safariextz', desired_capabilities=capabilities)
            elif browser is 'Firefox':
                driver = webdriver.Firefox(capabilities=capabilities)
            else:
                driver = webdriver.Chrome(chrome_options=capabilities)
        elif sys.platform == "linux" or sys.platform == "linux2":
            if browser is 'Firefox':
                driver = webdriver.Firefox(capabilities=capabilities)
            else:
                driver = webdriver.Chrome(executable_path='chromedriver_linux64', chrome_options=capabilities)

        driver.get(url)
        driver.set_window_size(1366, 768)
        return driver

    @staticmethod
    def get_logger(test_name):
        logger = logging.getLogger(test_name)

        if stream:
            ch = logging.StreamHandler(stream)
        else:
            ch = logging.StreamHandler()

        ch.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s %(name)-20s %(levelname)-8s %(message)s')
        ch.setFormatter(formatter)
        logger.addHandler(ch)
        return logger

    @staticmethod
    def do_login(driver, logger):
        try:
            username = os.environ['AUTOMATION_USERNAME']
        except KeyError:
            username = 'tester.two@geofeedia.com'

        try:
            password = os.environ['AUTOMATION_PASSWORD']
        except KeyError:
            password = 'Geofeedia5%'
        #username = 'tester.one@geofeedia.com'
        #password = 'geogeoautomation'
        logger.info('Logging in as ' + username)
        login_page = Login(driver)
        login_page.set_display_name(username)
        login_page.set_password(password)
        login_page.click_login()
        BaseModule.wait(3)

    @staticmethod
    def wait(secs):
        time.sleep(secs)

    @staticmethod
    def wait_for_element_exists(driver, by, timeout):
        WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located(by),
            'The element doesn\'t exist'
        )

    @staticmethod
    def wait_for_element_visible(driver, by, timeout):
        WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located(by),
            'The element is not visible'
        )

    @staticmethod
    def wait_for_element_to_be_clickable(driver, by, timeout):
        WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable(by),
            'The element is not clickable'
        )

    @staticmethod
    def wait_for_element(driver, by, timeout):
        BaseModule.wait_for_element_exists(driver, by, timeout)
        BaseModule.wait_for_element_visible(driver, by, timeout)

    @staticmethod
    def wait_for_file_to_exist(file_path, logger):
        logger.info('Waiting for the file ' + file_path + ' to exist')
        count = 0
        while not os.path.exists(file_path) and count < 10:
            BaseModule.wait(1)
            count += 1

        if os.path.isfile(file_path):
            return True
        else:
            raise ValueError('%s isn\'t a file!' % file_path)

    @staticmethod
    def verify_file_not_empty(file_path, logger):
        logger.info('Verifying file ' + file_path + ' to have contents')
        tools.assert_true(os.stat(file_path).st_size != 0)

    @staticmethod
    def delete_file(file_path, logger):
        logger.info('Deleting file ' + file_path)
        os.remove(file_path)

    @staticmethod
    def switch_to_popup(driver):
        previous = driver.current_window_handle
        for handle in driver.window_handles:
            driver.switch_to.window(handle)
        return previous

    @staticmethod
    def set_window_handler(driver, handle):
        driver.switch_to.window(handle)

    @staticmethod
    def handle_fail(driver, logger):
        # if sys.exc_info()[0]:
        logger.info('Test FAILED')
        fail_url = driver.current_url
        logger.info('Current URL: ' + fail_url)
        now = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S-%f')
        driver.get_screenshot_as_file('./%s.png' % now)

