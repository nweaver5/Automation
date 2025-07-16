from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys
import os
sys.path.append(os.path.abspath('.'))

from TestAutomation.supplements.driverSetup import *
from TestAutomation.supplements.loginSelectors import *

start = time.time()
driver = driver_setup()
# Alternative: driver_setup()

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

### VERIFYING DASHBOARD
driver.implicitly_wait(10)

headerTitle = header_title_selector(driver)

expectedHeader = "Dashboard"
actualHeader = headerTitle.text
if (expectedHeader == actualHeader):
   print("SUCCESS: " + actualHeader)
else:
   print("FAILURE: " + actualHeader)

### LOGGING OUT ###

avatarContainer = avatar_container_selector(driver)
time.sleep(1)
avatarContainer.click()
time.sleep(1)

# logOut = avatarContainer.find_element(By.CSS_SELECTOR, "a[href='/logout.do']")
# logOut.click()

# get_url = driver.current_url
# if (str(get_url == start_url)):
#    print("SUCCESS: LOGOUT")

time.sleep(1)
end = time.time()
print("Time: " + str(end - start) + " seconds")

driver.quit()