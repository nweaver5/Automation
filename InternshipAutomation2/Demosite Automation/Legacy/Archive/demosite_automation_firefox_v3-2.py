import time
import os
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from tabulate import tabulate

outputFile = ("FirefoxLogs\\demosite_automation_firefox_hxweb02_" + time.strftime("%m-%d-%H-%M") + ".log")
output = open(outputFile, 'w', encoding='utf-8')
sys.stdout = output

ff = webdriver.FirefoxProfile()
ff.set_preference('browser.download.folderList', 2)
ff.set_preference('browser.download.manager.showWhenStarting', False)
ff.set_preference('browser.download.dir', 'C:\\Users\\NWeaver\\Downloads')
ff.set_preference('browser.helperApps.neverAsk.saveToDisk', 'application/pdf')
ff.set_preference('pdfjs.disabled', True)

#driver = webdriver.Chrome(executable_path='C:\Python34\Scripts\chromedriver.exe')
driver = webdriver.Firefox(firefox_profile=ff)
#driver = webdriver.Ie(executable_path='C:\Python34\Scripts\IEDriverServer.exe')

results = []

start = time.time()
driver.get('https://hxweb02.healthx.com/newsweetness.aspx')

print("Firefox - hxweb02\n")
print("LOGIN")

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username"))).send_keys('Plan.member14')
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "password"))).send_keys('american1')
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "loginButton"))).click()

time.sleep(2)

try:
	WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Skip to Home Page"))).click()
except NoSuchElementException:
	results.append(("Login", "Fail", "Element Not Found"))
	results.append(("Splash Screen", "Fail", "Element Not Found"))
	print(tabulate(results))
	driver.quit()
except TimeoutException:
	results.append(("Login", "Fail", "Timed Out"))
	results.append(("Splash Screen", "Fail", "Timed Out"))
	print(tabulate(results))
	driver.quit()
else:
	results.append(("Login", "Pass", ""))
	results.append(("Splash Screen", "Pass", ""))

print(tabulate(results, headers = ["Section", "Result", "Comment"], tablefmt="fancy_grid"))
results = []

time.sleep(3)

print("ELIGIBILITY DASHBOARD")

##### COVERAGE SECTION #####

try:
	WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "ContentItem200_2")))
except NoSuchElementException:
	results.append(("Coverage Section", "Fail", "Element Not Found"))
except TimeoutException:
	results.append(("Coverage Section", "Fail", "Timed Out"))
else:
	results.append(("Coverage Section", "Pass", ""))
	
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "View all Coverage & Benefits"))).click()

try:
	WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Schedule of Benefits")))
except NoSuchElementException:
	results.append(("View All Link", "Fail", "Element Not Found"))
except TimeoutException:
	results.append(("View All Link", "Fail", "Timed Out"))
else:
	results.append(("View All Link", "Pass", ""))

driver.back()

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Elizabeth Jones"))).click()

try:
	WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "ctl00_MainContent_uxMessageLabel")))
except NoSuchElementException:
	results.append(("Elizabeth Jones Link", "Fail", "Element Not Found"))
except TimeoutException:
	results.append(("Elizabeth Jones Link", "Fail", "Timed Out"))
else:
	results.append(("Elizabeth Jones Link", "Pass", ""))

driver.back()

try:
	WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Daniel Jones"))).click()
except NoSuchElementException:
	results.append(("Daniel Jones Link", "Fail", "Element Not Found"))
except TimeoutException:
	results.append(("Daniel Jones Link", "Fail", "Timed Out"))
else:
	results.append(("Daniel Jones Link", "Pass", ""))

driver.back()

try:
	WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Alicia Jones"))).click()
except NoSuchElementException:
	results.append(("Alicia Jones Link", "Fail", "Element Not Found"))
except TimeoutException:
	results.append(("Alicia Jones Link", "Fail", "Timed Out"))
else:
	results.append(("Alicia Jones Link", "Pass", ""))

driver.back()

print(tabulate(results, headers = ["Section", "Result", "Comment"], tablefmt="fancy_grid"))
results = []

print("BALANCE SECTION")

##### BALANCES SECTION #####

try:
	WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "ContentItem200_3")))
except NoSuchElementException:
	results.append(("Balances Section", "Fail", "Element Not Found"))
except TimeoutException:
	results.append(("Balances Section", "Fail", "Timed Out"))
else:
	results.append(("Balances Section", "Pass", ""))

print(tabulate(results, headers = ["Section", "Result", "Comment"], tablefmt="fancy_grid"))
results = []

print("CLAIMS DASHBOARD")

##### CLAIMS SECTION ######

try:
	WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "ContentItem200_4")))
except NoSuchElementException:
	results.append(("Claims Section", "Fail", "Element Not Found"))
except TimeoutException:
	results.append(("Claims Section", "Fail", "Timed Out"))
else:
	results.append(("Claims Section", "Pass", ""))


WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Proceed to my Claims"))).click()

try:
	WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "ctl00_MainContent_uxClaimsMessageLabel")))
except NoSuchElementException:
	results.append(("PHI Located", "Fail", "Element Not Found"))
except TimeoutException:
	results.append(("PHI Located", "Fail", "Timed Out"))
else:
	results.append(("PHI Located", "Pass", ""))

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Member Claims Submission"))).click()

try:
	WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "ctl00_MainContent_uxForm_ctl03_uxFormSubmitButton")))
except NoSuchElementException:
	results.append(("Claims Form", "Fail", "Element Not Found"))
except TimeoutException:
	results.append(("Claims Form", "Fail", "Timed Out"))
else:
	results.append(("Claims Form", "Pass", ""))

driver.back()

try:
	WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "4557784597"))).click()
	firstClaimCheck = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='serviceContainer']/div[2]/div[3]/div[1]/h3"))).text

	if firstClaimCheck == "Claim #4557784597":
		results.append(("Claims Link 1", "Pass", ""))
		driver.back()
except NoSuchElementException:
	results.append(("Claims Link 1", "Fail", "Element Not Found"))
except TimeoutException:
	results.append(("Claims Link 1", "Fail", "Timed Out"))

try:
	WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "9156395414"))).click()
	secondClaimCheck = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='serviceContainer']/div[2]/div[3]/div[1]/h3"))).text
	
	if secondClaimCheck == "Claim #9156395414":
		results.append(("Claims Link 2", "Pass", ""))
		driver.back()
except NoSuchElementException:
	results.append(("Claims Link 2", "Fail", "Element Not Found"))
except TimeoutException:
	results.append(("Claims Link 2", "Fail", "Timed Out"))

try:
	WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "4021764337"))).click()
	thirdClaimCheck = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='serviceContainer']/div[2]/div[3]/div[1]/h3"))).text
	
	if thirdClaimCheck == "Claim #4021764337":
		results.append(("Claims Link 3", "Pass", ""))
		driver.back()
except NoSuchElementException:
	results.append(("Claims Link 3", "Fail", "Element Not Found"))
except TimeoutException:
	results.append(("Claims Link 3", "Fail", "Timed Out"))

try:
	WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "6755069099"))).click()
	fourthClaimCheck = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='serviceContainer']/div[2]/div[3]/div[1]/h3"))).text
	
	if fourthClaimCheck == "Claim #6755069099":
		results.append(("Claims Link 4", "Pass", ""))
		driver.back()
except NoSuchElementException:
	results.append(("Claims Link 4", "Fail", "Element Not Found"))
except TimeoutException:
	results.append(("Claims Link 4", "Fail", "Timed Out"))

try:
	WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "0964388342"))).click()
	fifthClaimCheck = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='serviceContainer']/div[2]/div[3]/div[1]/h3"))).text
	
	if fifthClaimCheck == "Claim #0964388342":
		results.append(("Claims Link 5", "Pass", ""))
		driver.back()
except NoSuchElementException:
	results.append(("Claims Link 5", "Fail", "Element Not Found"))
except TimeoutException:
	results.append(("Claims Link 5", "Fail", "Timed Out"))

try:
	WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "1674315135"))).click()
	sixthClaimCheck = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='serviceContainer']/div[2]/div[3]/div[1]/h3"))).text
	
	if sixthClaimCheck == "Claim #1674315135":
		results.append(("Claims Link 6", "Pass", ""))
		driver.back()
except NoSuchElementException:
	results.append(("Claims Link 6", "Fail", "Element Not Found"))
except TimeoutException:
	results.append(("Claims Link 6", "Fail", "Timed Out"))

try:
	WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "7973735542"))).click()
	seventhClaimCheck = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='serviceContainer']/div[2]/div[3]/div[1]/h3"))).text
	
	if seventhClaimCheck == "Claim #7973735542":
		results.append(("Claims Link 7", "Pass", ""))
		driver.back()
except NoSuchElementException:
	results.append(("Claims Link 7", "Fail", "Element Not Found"))
except TimeoutException:
	results.append(("Claims Link 7", "Fail", "Timed Out"))

try:
	WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "8128013376"))).click()
	eighthClaimCheck = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='serviceContainer']/div[2]/div[3]/div[1]/h3"))).text
	
	if eighthClaimCheck == "Claim #8128013376":
		results.append(("Claims Link 8", "Pass", ""))
		driver.back()
except NoSuchElementException:
	results.append(("Claims Link 8", "Fail", "Element Not Found"))
except TimeoutException:
	results.append(("Claims Link 8", "Fail", "Timed Out"))

try:
	WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "9982984085"))).click()
	ninethClaimCheck = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='serviceContainer']/div[2]/div[3]/div[1]/h3"))).text
	
	if ninethClaimCheck == "Claim #9982984085":
		results.append(("Claims Link 9", "Pass", ""))
		driver.back()
except NoSuchElementException:
	results.append(("Claims Link 9", "Fail", "Element Not Found"))
except TimeoutException:
	results.append(("Claims Link 9", "Fail", "Timed Out"))

try:
	WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "1382195851"))).click()
	tenthClaimCheck = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='serviceContainer']/div[2]/div[3]/div[1]/h3"))).text
	
	if tenthClaimCheck == "Claim #1382195851":
		results.append(("Claims Link 10", "Pass", ""))
		driver.back()
except NoSuchElementException:
	results.append(("Claims Link 10", "Fail", "Element Not Found"))
except TimeoutException:
	results.append(("Claims Link 10", "Fail", "Timed Out"))

print(tabulate(results, headers = ["Section", "Result", "Comment"], tablefmt="fancy_grid"))
results = []

driver.back()

##### PAYMENTS SECTION #####
print("PAYMENTS SECTION")

try:
	WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "ContentItem200_6")))
except NoSuchElementException:
	results.append(("Payments Section", "Fail", "Element Not Found"))
except TimeoutException:
	results.append(("Payments Section", "Fail", "Timed Out"))
else:
	results.append(("Payments Section", "Pass", ""))

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, ".//*[@id='hxUserMenu']/li[4]/a"))).click()

try:
	WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='flexAccounts']/a")))
except NoSuchElementException:
	results.append(("Payments Page", "Fail", "Element Not Found"))
except TimeoutException:
	results.append(("Payments Page", "Fail", "Timed Out"))
else:
	results.append(("Payments Page", "Pass", ""))

try:
	WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "1444789"))).click()
	time.sleep(1)
	driver.switch_to_active_element()
	WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "html/body/div[3]/div[1]/a"))).click()
except NoSuchElementException:
	results.append(("Payments Link 1", "Fail", "Element Not Found"))
except TimeoutException:
	results.append(("Payments Link 1", "Fail", "Timed Out"))
else:
	results.append(("Payments Link 1", "Pass", ""))

try:
	WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "1425445"))).click()
	time.sleep(1)
	driver.switch_to_active_element()
	WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "html/body/div[3]/div[1]/a"))).click()
except NoSuchElementException:
	results.append(("Payments Link 2", "Fail", "Element Not Found"))
except TimeoutException:
	results.append(("Payments Link 2", "Fail", "Timed Out"))
else:
	results.append(("Payments Link 2", "Pass", ""))

try:
	WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "1453467"))).click()
	time.sleep(1)
	driver.switch_to_active_element()
	WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "html/body/div[3]/div[1]/a"))).click()
except NoSuchElementException:
	results.append(("Payments Link 3", "Fail", "Element Not Found"))
except TimeoutException:
	results.append(("Payments Link 3", "Fail", "Timed Out"))
else:
	results.append(("Payments Link 3", "Pass", ""))

try:
	WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "1380178"))).click()
	time.sleep(1)
	driver.switch_to_active_element()
	WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "html/body/div[3]/div[1]/a"))).click()
except NoSuchElementException:
	results.append(("Payments Link 4", "Fail", "Element Not Found"))
except TimeoutException:
	results.append(("Payments Link 4", "Fail", "Timed Out"))
else:
	results.append(("Payments Link 4", "Pass", ""))

try:
	WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "1370479"))).click()
	time.sleep(1)
	driver.switch_to_active_element()
	WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "html/body/div[3]/div[1]/a"))).click()
except NoSuchElementException:
	results.append(("Payments Link 5", "Fail", "Element Not Found"))
except TimeoutException:
	results.append(("Payments Link 5", "Fail", "Timed Out"))
else:
	results.append(("Payments Link 5", "Pass", ""))
	
try:
	WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "1479221"))).click()
	time.sleep(1)
	driver.switch_to_active_element()
	WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "html/body/div[3]/div[1]/a"))).click()
except NoSuchElementException:
	results.append(("Payments Link 6", "Fail", "Element Not Found"))
except TimeoutException:
	results.append(("Payments Link 6", "Fail", "Timed Out"))
else:
	results.append(("Payments Link 6", "Pass", ""))
	
try:
	WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "1414898"))).click()
	time.sleep(1)
	driver.switch_to_active_element()
	WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "html/body/div[3]/div[1]/a"))).click()
except NoSuchElementException:
	results.append(("Payments Link 7", "Fail", "Element Not Found"))
except TimeoutException:
	results.append(("Payments Link 7", "Fail", "Timed Out"))
else:
	results.append(("Payments Link 7", "Pass", ""))

try:
	WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "1471462"))).click()
	time.sleep(1)
	driver.switch_to_active_element()
	WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "html/body/div[3]/div[1]/a"))).click()
except NoSuchElementException:
	results.append(("Payments Link 8", "Fail", "Element Not Found"))
except TimeoutException:
	results.append(("Payments Link 8", "Fail", "Timed Out"))
else:
	results.append(("Payments Link 8", "Pass", ""))

try:
	WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "1401260"))).click()
	time.sleep(1)
	driver.switch_to_active_element()
	WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "html/body/div[3]/div[1]/a"))).click()
except NoSuchElementException:
	results.append(("Payments Link 9", "Fail", "Element Not Found"))
except TimeoutException:
	results.append(("Payments Link 9", "Fail", "Timed Out"))
else:
	results.append(("Payments Link 9", "Pass", ""))

try:
	WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "1391391"))).click()
	time.sleep(1)
	driver.switch_to_active_element()
	WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "html/body/div[3]/div[1]/a"))).click()
except NoSuchElementException:
	results.append(("Payments Link 10", "Fail", "Element Not Found"))
except TimeoutException:
	results.append(("Payments Link 10", "Fail", "Timed Out"))
else:
	results.append(("Payments Link 10", "Pass", ""))
	
try:
	WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "1462699"))).click()
	time.sleep(1)
	driver.switch_to_active_element()
	WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "html/body/div[3]/div[1]/a"))).click()
except NoSuchElementException:
	results.append(("Payments Link 11", "Fail", "Element Not Found"))
except TimeoutException:
	results.append(("Payments Link 11", "Fail", "Timed Out"))
else:
	results.append(("Payments Link 11", "Pass", ""))

try:
	WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "1436000"))).click()
	time.sleep(1)
	driver.switch_to_active_element()
	WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "html/body/div[3]/div[1]/a"))).click()
except NoSuchElementException:
	results.append(("Payments Link 12", "Fail", "Element Not Found"))
except TimeoutException:
	results.append(("Payments Link 12", "Fail", "Timed Out"))
else:
	results.append(("Payments Link 12", "Pass", ""))

print(tabulate(results, headers = ["Section", "Result", "Comment"], tablefmt="fancy_grid"))
results = []

##### AUTHORIZATIONS SECTION #####

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, ".//*[@id='hxUserMenu']/li[1]/a"))).click()

print("AUTHORIZATIONS SECTION")

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, ".//*[@id='hxUserMenu']/li[6]/a"))).click()

try:
	WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "View your Care Plan")))
except NoSuchElementException:
	results.append(("Authorizations Page", "Fail", "Element Not Found"))
except TimeoutException:
	results.append(("Authorizations Page", "Fail", "Timed Out"))
else:
	results.append(("Authorizations Page", "Pass", ""))

try:
	firstAuthLink = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, ".//*[@id='ctl00_MainContent_uxAuthorizationsGrid']/tbody/tr[2]/td[1]/a")))
	firstAuthLinkText = firstAuthLink.text
	firstAuthLink.click()
	firstAuthCheck = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='serviceContainer']/div[2]/div[3]/div[2]/table/tbody/tr[2]/td[2]/p"))).text
	
	if firstAuthCheck == firstAuthLinkText:
		results.append(("Auth Link 1", "Pass", ""))
		driver.back()
except NoSuchElementException:
	results.append(("Auth Link 1", "Fail", "Element Not Found"))
except TimeoutException:
	results.append(("Auth Link 1", "Fail", "Timed Out"))

try:
	secondAuthLink = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, ".//*[@id='ctl00_MainContent_uxAuthorizationsGrid']/tbody/tr[3]/td[1]/a")))
	secondAuthLinkText = secondAuthLink.text
	secondAuthLink.click()
	secondAuthCheck = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='serviceContainer']/div[2]/div[3]/div[2]/table/tbody/tr[2]/td[2]/p"))).text

	if secondAuthCheck == secondAuthLinkText:
		results.append(("Auth Link 2", "Pass", ""))
		driver.back()
except NoSuchElementException:
	results.append(("Auth Link 2", "Fail", "Element Not Found"))
except TimeoutException:
	results.append(("Auth Link 2", "Fail", "Timed Out"))

try:
	thirdAuthLink = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, ".//*[@id='ctl00_MainContent_uxAuthorizationsGrid']/tbody/tr[4]/td[1]/a")))
	thirdAuthLinkText = thirdAuthLink.text
	thirdAuthLink.click()
	thirdAuthCheck = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='serviceContainer']/div[2]/div[3]/div[2]/table/tbody/tr[2]/td[2]/p"))).text

	if thirdAuthCheck == thirdAuthLinkText:
		results.append(("Auth Link 3", "Pass", ""))
		driver.back()
except NoSuchElementException:
	results.append(("Auth Link 3", "Fail", "Element Not Found"))
except TimeoutException:
	results.append(("Auth Link 3", "Fail", "Timed Out"))

try:
	fourthAuthLink = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, ".//*[@id='ctl00_MainContent_uxAuthorizationsGrid']/tbody/tr[5]/td[1]/a")))
	fourthAuthLinkText = fourthAuthLink.text
	fourthAuthLink.click()
	fourthAuthCheck = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='serviceContainer']/div[2]/div[3]/div[2]/table/tbody/tr[2]/td[2]/p"))).text

	if fourthAuthCheck == fourthAuthLinkText:
		results.append(("Auth Link 4", "Pass", ""))
		driver.back()
except NoSuchElementException:
	results.append(("Auth Link 4", "Fail", "Element Not Found"))
except TimeoutException:
	results.append(("Auth Link 4", "Fail", "Timed Out"))

try:
	fifthAuthLink = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, ".//*[@id='ctl00_MainContent_uxAuthorizationsGrid']/tbody/tr[6]/td[1]/a")))
	fifthAuthLinkText = fifthAuthLink.text
	fifthAuthLink.click()
	fifthAuthCheck = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='serviceContainer']/div[2]/div[3]/div[2]/table/tbody/tr[2]/td[2]/p"))).text

	if fifthAuthCheck == fifthAuthLinkText:
		results.append(("Auth Link 5", "Pass", ""))
		driver.back()
except NoSuchElementException:
	results.append(("Auth Link 5", "Fail", "Element Not Found"))
except TimeoutException:
	results.append(("Auth Link 5", "Fail", "Timed Out"))

try:
	sixthAuthLink = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, ".//*[@id='ctl00_MainContent_uxAuthorizationsGrid']/tbody/tr[7]/td[1]/a")))
	sixthAuthLinkText = sixthAuthLink.text
	sixthAuthLink.click()
	sixthAuthCheck = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='serviceContainer']/div[2]/div[3]/div[2]/table/tbody/tr[2]/td[2]/p"))).text

	if sixthAuthCheck == sixthAuthLinkText:
		results.append(("Auth Link 6", "Pass", ""))
		driver.back()
except NoSuchElementException:
	results.append(("Auth Link 6", "Fail", "Element Not Found"))
except TimeoutException:
	results.append(("Auth Link 6", "Fail", "Timed Out"))

try:
	seventhAuthLink = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, ".//*[@id='ctl00_MainContent_uxAuthorizationsGrid']/tbody/tr[8]/td[1]/a")))
	seventhAuthLinkText = seventhAuthLink.text
	seventhAuthLink.click()
	seventhAuthCheck = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='serviceContainer']/div[2]/div[3]/div[2]/table/tbody/tr[2]/td[2]/p"))).text

	if seventhAuthCheck == seventhAuthLinkText:
		results.append(("Auth Link 7", "Pass", ""))
		driver.back()
except NoSuchElementException:
	results.append(("Auth Link 7", "Fail", "Element Not Found"))
except TimeoutException:
	results.append(("Auth Link 7", "Fail", "Timed Out"))

try:
	eighthAuthLink = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, ".//*[@id='ctl00_MainContent_uxAuthorizationsGrid']/tbody/tr[9]/td[1]/a")))
	eighthAuthLinkText = eighthAuthLink.text
	eighthAuthLink.click()
	eighthAuthCheck = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='serviceContainer']/div[2]/div[3]/div[2]/table/tbody/tr[2]/td[2]/p"))).text

	if eighthAuthCheck == eighthAuthLinkText:
		results.append(("Auth Link 8", "Pass", ""))
		driver.back()
except NoSuchElementException:
	results.append(("Auth Link 8", "Fail", "Element Not Found"))
except TimeoutException:
	results.append(("Auth Link 8", "Fail", "Timed Out"))

try:
	ninethAuthLink = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, ".//*[@id='ctl00_MainContent_uxAuthorizationsGrid']/tbody/tr[10]/td[1]/a")))
	ninethAuthLinkText = ninethAuthLink.text
	ninethAuthLink.click()
	ninethAuthCheck = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='serviceContainer']/div[2]/div[3]/div[2]/table/tbody/tr[2]/td[2]/p"))).text

	if ninethAuthCheck == ninethAuthLinkText:
		results.append(("Auth Link 9", "Pass", ""))
		driver.back()
except NoSuchElementException:
	results.append(("Auth Link 9", "Fail", "Element Not Found"))
except TimeoutException:
	results.append(("Auth Link 9", "Fail", "Timed Out"))

try:
	tenthAuthLink = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, ".//*[@id='ctl00_MainContent_uxAuthorizationsGrid']/tbody/tr[11]/td[1]/a")))
	tenthAuthLinkText = tenthAuthLink.text
	tenthAuthLink.click()
	tenthAuthCheck = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='serviceContainer']/div[2]/div[3]/div[2]/table/tbody/tr[2]/td[2]/p"))).text

	if tenthAuthCheck == tenthAuthLinkText:
		results.append(("Auth Link 10", "Pass", ""))
		driver.back()
except NoSuchElementException:
	results.append(("Auth Link 10", "Fail", "Element Not Found"))
except TimeoutException:
	results.append(("Auth Link 10", "Fail", "Timed Out"))

print(tabulate(results, headers = ["Section", "Result", "Comment"], tablefmt="fancy_grid"))
results = []

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, ".//*[@id='hxUserMenu']/li[1]/a"))).click()

print("PROVIDER SECTION")

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, ".//*[@id='hxUserMenu']/li[7]/a"))).click()

try:
	WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='submitProvSearch']")))
except NoSuchElementException:
	results.append(("Provider Tool", "Fail", "Element Not Found"))
except TimeoutException:
	results.append(("Provider Tool", "Fail", "Timed Out"))
else:
	results.append(("Provider Tool", "Pass", ""))

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "providerZip"))).send_keys("54601")

time.sleep(3)

submitBtn = driver.find_element_by_id("submitProvSearch").click()

time.sleep(5)

try:
	WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "resultsList")))
except NoSuchElementException:
	results.append(("Provider Results", "Fail", "Element Not Found"))
except TimeoutException:
	results.append(("Provider Results", "Fail", "Timed Out"))
else:
	results.append(("Provider Results", "Pass", ""))

print(tabulate(results, headers = ["Section", "Result", "Comment"], tablefmt="fancy_grid"))
results = []

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, ".//*[@id='hxUserMenu']/li[1]/a"))).click()

print("LOGOUT")

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Logout"))).click()
try:
	WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username")))
except NoSuchElementException:
	results.append(("Logout", "Fail", "Element Not Found"))
except TimeoutException:
	results.append(("Logout", "Fail", "Timed Out"))
else:
	results.append(("Logout", "Pass", ""))

print(tabulate(results, headers = ["Section", "Result", "Comment"], tablefmt="fancy_grid"))
results = []

end = time.time() - start
print("\nTotal Elapsed Test Time %.2f" % end)

output.close()
sys.stdout = sys.__stdout__
driver.quit()