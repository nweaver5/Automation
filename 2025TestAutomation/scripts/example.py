import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://www.google.com/')
time.sleep(5)
search_box = driver.find_element('name', 'q')
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(5)
driver.quit()
