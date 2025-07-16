from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import sys
import os
sys.path.append(os.path.abspath('.'))

from TestAutomation.supplements.driverSetup import *
from TestAutomation.supplements.loginSelectors import *
from TestAutomation.supplements.filterSelectors import *

start = time.time()
driver = driver_setup()

start_url = "https://tenonworkshop.service-now.com/navpage.do"

driver.get(start_url)
driver.implicitly_wait(5)

logIn(driver)

# *In case ServiceNow requires you to log in again
get_url = driver.current_url

if ("https://tenonworkshop.service-now.com/navpage.do" == str(get_url)):
   logIn(driver)
   get_url = driver.current_url

### AFTER LOGGING IN ###

driver.implicitly_wait(30)

original_window = driver.current_window_handle
filter = driver.find_element(By.ID, "filter")
filter.send_keys("tenon work")
filter.send_keys(Keys.ENTER)

tenonWork = driver.find_element(By.XPATH, "//div[text()='Tenon Work']")
tenonWork.click()

### AFTER OPENING TENON
wait = WebDriverWait(driver, 5)
wait.until(EC.number_of_windows_to_be(2))

for window_handle in driver.window_handles:
  if window_handle != original_window:
      driver.switch_to.window(window_handle)
      time.sleep(5)
      break

### NAVIGATING TO 'Tasks' ###

cadso_menu_container = tasks_side_selector(driver)

buttons = cadso_menu_container.find_element(By.CSS_SELECTOR, "div[class='Buttons']")
taskButton = buttons.find_element(By.CSS_SELECTOR, "button[aria-describedby='tooltip-Tasks']")
taskButton.click()

driver.implicitly_wait(30)
time.sleep(5)

### CREATING NEW FILTER ###

cadso_complex_list_filter_root_div = filter_selector(driver)
filterButton = cadso_complex_list_filter_root_div.find_element(By.CSS_SELECTOR, "button")

filterButton.click()
driver.implicitly_wait(30)
time.sleep(1)

field = 'Status'
operation = 'is not'
option = 'Upcoming'

createFilter(driver, 0, field, operation, option)
saveCondition(driver)

### Save Filter ###
name = "Automation Filter Private"
saveFilter(driver, name, "Private")

### Clearing the Filter ###

clearFilter(driver, True)

### Verifying that Automation Filter Private exists in Private Filters section ###

verifyPrivate(driver, name)

time.sleep(10)
driver.quit()