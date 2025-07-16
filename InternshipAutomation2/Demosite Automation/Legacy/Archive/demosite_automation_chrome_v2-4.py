import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

ch = webdriver.Chrome(executable_path='C:\Python34\Scripts\chromedriver.exe')
#ch = webdriver.Firefox()
#ch = webdriver.Ie(executable_path='C:\Python34\Scripts\IEDriverServer.exe')

print("Navigating to Healthx Demo Site")
start = time.time()
ch.get('https://hxweb04.healthx.com/newsweetness.aspx')

print("Logging In")
WebDriverWait(ch, 10).until(EC.presence_of_element_located((By.ID, "username"))).send_keys('Plan.member14')
WebDriverWait(ch, 10).until(EC.presence_of_element_located((By.NAME, "password"))).send_keys('american1')
WebDriverWait(ch, 10).until(EC.presence_of_element_located((By.ID, "loginButton"))).click()

time.sleep(5)

try:
	WebDriverWait(ch, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Skip to Home Page"))).click()
except (NoSuchElementException, TimeoutException):
	print("Splash Screen Element Undetected, Cannot Continue Test")
	ch.quit()
print("Login Successful")
print("Splash Screen Skipped")

time.sleep(3)
print("\nChecking Eligibility Dashboard")

##### COVERAGE SECTION #####

try:
	WebDriverWait(ch, 10).until(EC.presence_of_element_located((By.ID, "ContentItem200_2")))
except (NoSuchElementException, TimeoutException):
	print("Coverage Element Not Found")
	print("Skipping Links")
print("Coverage Element Found")
print("Checking Coverage links")

	
WebDriverWait(ch, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "View all Coverage & Benefits"))).click()

try:
	WebDriverWait(ch, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Schedule of Benefits")))
except (NoSuchElementException, TimeoutException):
	print("View All coverages Link isn't working properly")
print("View All Coverages Link is working properly")

ch.back()

WebDriverWait(ch, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Elizabeth Jones"))).click()

try:
	WebDriverWait(ch, 10).until(EC.presence_of_element_located((By.ID, "ctl00_MainContent_uxMessageLabel")))
except (NoSuchElementException, TimeoutException):
	print("Elizabeth Jones Link Doesn't Work Properly")
print("Elizabeth Jones Link Works Properly")

ch.back()

try:
	WebDriverWait(ch, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Daniel Jones"))).click()
except (NoSuchElementException, TimeoutException):
	print("Daniel Jones Link Doesn't Work Properly")
print("Daniel Jones Link Works Properly")

ch.back()

try:
	WebDriverWait(ch, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Alicia Jones"))).click()
except (NoSuchElementException, TimeoutException):
	print("Alicia Jones Link Doesn't Work Properly")
print("Alicia Jones Link Works Properly")

ch.back()

print("Finished Checking Eligibility Dashboard\n")
print("Checking Balance Summary Section")

##### BALANCES SECTION #####

try:
	WebDriverWait(ch, 10).until(EC.presence_of_element_located((By.ID, "ContentItem200_3")))
except (NoSuchElementException, TimeoutException):
	print("Balance Summary Element Not Present")
print("Balance Summary Element Present")

print("Finished Checking Balance Summary Section\n")
print("Checking Claims Dashboard")

##### CLAIMS SECTION ######

try:
	WebDriverWait(ch, 10).until(EC.presence_of_element_located((By.ID, "ContentItem200_4")))
except (NoSuchElementException, TimeoutException):
	print("Claims Element Not Present")
	print("Skipping Links")
print("Claims Element Present")
print("Checking Claims Page and Links")


WebDriverWait(ch, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Proceed to my Claims"))).click()

try:
	WebDriverWait(ch, 10).until(EC.presence_of_element_located((By.ID, "ctl00_MainContent_uxClaimsMessageLabel")))
except (NoSuchElementException, TimeoutException):
	print("PHI Not Found")
print("PHI Found")

WebDriverWait(ch, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Member Claims Submission"))).click()

try:
	WebDriverWait(ch, 10).until(EC.presence_of_element_located((By.ID, "ctl00_MainContent_uxForm_ctl03_uxFormSubmitButton")))
except (NoSuchElementException, TimeoutException):
	print("Claims Form Didn't Load Properly")
print("Claims Form Loaded Properly")

ch.back()

try:
	WebDriverWait(ch, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "4557784597"))).click()
	firstClaimCheck = WebDriverWait(ch, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='serviceContainer']/div[2]/div[3]/div[1]/h3"))).text

	if firstClaimCheck == "Claim #4557784597":
		print("First   Claims Link Works Properly")
		ch.back()
except (NoSuchElementException, TimeoutException):
	print("First   Claims Link Doesn't Work Properly")

try:
	WebDriverWait(ch, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "9156395414"))).click()
	secondClaimCheck = WebDriverWait(ch, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='serviceContainer']/div[2]/div[3]/div[1]/h3"))).text
	
	if secondClaimCheck == "Claim #9156395414":
		print("Second  Claims Link Works Properly")
		ch.back()
except (NoSuchElementException, TimeoutException):
	print("Second  Claims Link Doesn't Work Properly")

try:
	WebDriverWait(ch, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "4021764337"))).click()
	thirdClaimCheck = WebDriverWait(ch, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='serviceContainer']/div[2]/div[3]/div[1]/h3"))).text
	
	if thirdClaimCheck == "Claim #4021764337":
		print("Third   Claims Link Works Properly")
		ch.back()
except (NoSuchElementException, TimeoutException):
	print("Third   Claims Link Doesn't Work Properly")

try:
	WebDriverWait(ch, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "6755069099"))).click()
	fourthClaimCheck = WebDriverWait(ch, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='serviceContainer']/div[2]/div[3]/div[1]/h3"))).text
	
	if fourthClaimCheck == "Claim #6755069099":
		print("Fourth  Claims Link Works Properly")
		ch.back()
except (NoSuchElementException, TimeoutException):
	print("Fourth  Claims Link Doesn't Work Properly")

try:
	WebDriverWait(ch, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "0964388342"))).click()
	fifthClaimCheck = WebDriverWait(ch, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='serviceContainer']/div[2]/div[3]/div[1]/h3"))).text
	
	if fifthClaimCheck == "Claim #0964388342":
		print("Fifth   Claims Link Works Properly")
		ch.back()
except (NoSuchElementException, TimeoutException):
	print("Fifth   Claims Link Doesn't Work Properly")

try:
	WebDriverWait(ch, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "1674315135"))).click()
	sixthClaimCheck = WebDriverWait(ch, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='serviceContainer']/div[2]/div[3]/div[1]/h3"))).text
	
	if sixthClaimCheck == "Claim #1674315135":
		print("Sixth   Claims Link Works Properly")
		ch.back()
except (NoSuchElementException, TimeoutException):
	print("Sixth   Claims Link Doesn't Work Properly")

try:
	WebDriverWait(ch, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "7973735542"))).click()
	seventhClaimCheck = WebDriverWait(ch, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='serviceContainer']/div[2]/div[3]/div[1]/h3"))).text
	
	if seventhClaimCheck == "Claim #7973735542":
		print("Seventh Claims Link Works Properly")
		ch.back()
except (NoSuchElementException, TimeoutException):
	print("Seventh Claims Link Doesn't Work Properly")

try:
	WebDriverWait(ch, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "8128013376"))).click()
	eighthClaimCheck = WebDriverWait(ch, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='serviceContainer']/div[2]/div[3]/div[1]/h3"))).text
	
	if eighthClaimCheck == "Claim #8128013376":
		print("Eighth  Claims Link Works Properly")
		ch.back()
except (NoSuchElementException, TimeoutException):
	print("Eighth  Claims Link Doesn't Work Properly")

try:
	WebDriverWait(ch, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "9982984085"))).click()
	ninethClaimCheck = WebDriverWait(ch, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='serviceContainer']/div[2]/div[3]/div[1]/h3"))).text
	
	if ninethClaimCheck == "Claim #9982984085":
		print("Nineth  Claims Link Works Properly")
		ch.back()
except (NoSuchElementException, TimeoutException):
	print("Nineth  Claims Link Doesn't Work Properly")

try:
	WebDriverWait(ch, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "1382195851"))).click()
	tenthClaimCheck = WebDriverWait(ch, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='serviceContainer']/div[2]/div[3]/div[1]/h3"))).text
	
	if tenthClaimCheck == "Claim #1382195851":
		print("Tenth   Claims Link Works Properly")
		ch.back()
except (NoSuchElementException, TimeoutException):
	print("Tenth   Claims Link Doesn't Work Properly")

print("Finished Checking Claims Section\n")
ch.back()

##### PAYMENTS SECTION #####
print("Checking Payments Section")

try:
	WebDriverWait(ch, 10).until(EC.presence_of_element_located((By.ID, "ContentItem200_6")))
except (NoSuchElementException, TimeoutException):
	print("Payments Element not Present")
print("Payments Element Present")

print("Checking Payments Page")

WebDriverWait(ch, 10).until(EC.element_to_be_clickable((By.XPATH, ".//*[@id='hxUserMenu']/li[4]/a"))).click()

try:
	WebDriverWait(ch, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='flexAccounts']/a")))
except (NoSuchElementException, TimeoutException):
	print("Payments Page Not Loaded Properly")
print("Payments Page Loaded Properly")

try:
	WebDriverWait(ch, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "1444789"))).click()
	time.sleep(1)
	ch.switch_to_active_element()
	WebDriverWait(ch, 10).until(EC.element_to_be_clickable((By.XPATH, "html/body/div[3]/div[1]/a"))).click()
except (NoSuchElementException, TimeoutException):
	print("First    Payment Link Doesn't Work Properly")
print("First    Payment Link Works Properly")

try:
	WebDriverWait(ch, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "1425445"))).click()
	time.sleep(1)
	ch.switch_to_active_element()
	WebDriverWait(ch, 10).until(EC.element_to_be_clickable((By.XPATH, "html/body/div[3]/div[1]/a"))).click()
except (NoSuchElementException, TimeoutException):
	print("Second   Payment Link Doesn't Work Properly")
print("Second   Payment Link Works Properly")

try:
	WebDriverWait(ch, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "1453467"))).click()
	time.sleep(1)
	ch.switch_to_active_element()
	WebDriverWait(ch, 10).until(EC.element_to_be_clickable((By.XPATH, "html/body/div[3]/div[1]/a"))).click()
except (NoSuchElementException, TimeoutException):
	print("Third    Payment Link Doesn't Work Properly")
print("Third    Payment Link Works Properly")

try:
	WebDriverWait(ch, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "1380178"))).click()
	time.sleep(1)
	ch.switch_to_active_element()
	WebDriverWait(ch, 10).until(EC.element_to_be_clickable((By.XPATH, "html/body/div[3]/div[1]/a"))).click()
except (NoSuchElementException, TimeoutException):
	print("Fourth   Payment Link Doesn't Work Properly")
print("Fourth   Payment Link Works Properly")

try:
	WebDriverWait(ch, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "1370479"))).click()
	time.sleep(1)
	ch.switch_to_active_element()
	WebDriverWait(ch, 10).until(EC.element_to_be_clickable((By.XPATH, "html/body/div[3]/div[1]/a"))).click()
except (NoSuchElementException, TimeoutException):
	print("Fifth    Payment Link Doesn't Work Properly")
print("Fifth    Payment Link Works Properly")
	
try:
	WebDriverWait(ch, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "1479221"))).click()
	time.sleep(1)
	ch.switch_to_active_element()
	WebDriverWait(ch, 10).until(EC.element_to_be_clickable((By.XPATH, "html/body/div[3]/div[1]/a"))).click()
except (NoSuchElementException, TimeoutException):
	print("Sixth    Payment Link Doesn't Work Properly")
print("Sixth    Payment Link Works Properly")
	
try:
	WebDriverWait(ch, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "1414898"))).click()
	time.sleep(1)
	ch.switch_to_active_element()
	WebDriverWait(ch, 10).until(EC.element_to_be_clickable((By.XPATH, "html/body/div[3]/div[1]/a"))).click()
except (NoSuchElementException, TimeoutException):
	print("Seventh  Payment Link Doesn't Work Properly")
print("Seventh  Payment Link Works Properly")

try:
	WebDriverWait(ch, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "1471462"))).click()
	time.sleep(1)
	ch.switch_to_active_element()
	WebDriverWait(ch, 10).until(EC.element_to_be_clickable((By.XPATH, "html/body/div[3]/div[1]/a"))).click()
except (NoSuchElementException, TimeoutException):
	print("Eighth   Payment Link Doesn't Work Properly")
print("Eighth   Payment Link Works Properly")

try:
	WebDriverWait(ch, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "1401260"))).click()
	time.sleep(1)
	ch.switch_to_active_element()
	WebDriverWait(ch, 10).until(EC.element_to_be_clickable((By.XPATH, "html/body/div[3]/div[1]/a"))).click()
except (NoSuchElementException, TimeoutException):
	print("Nineth   Payment Link Doesn't Work Properly")
print("Nineth   Payment Link Works Properly")

try:
	WebDriverWait(ch, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "1391391"))).click()
	time.sleep(1)
	ch.switch_to_active_element()
	WebDriverWait(ch, 10).until(EC.element_to_be_clickable((By.XPATH, "html/body/div[3]/div[1]/a"))).click()
except (NoSuchElementException, TimeoutException):
	print("Tenth    Payment Link Doesn't Work Properly")
print("Tenth    Payment Link Works Properly")
	
try:
	WebDriverWait(ch, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "1462699"))).click()
	time.sleep(1)
	ch.switch_to_active_element()
	WebDriverWait(ch, 10).until(EC.element_to_be_clickable((By.XPATH, "html/body/div[3]/div[1]/a"))).click()
except (NoSuchElementException, TimeoutException):
	print("Eleventh Payment Link Doesn't Work Properly")
print("Eleventh Payment Link Works Properly")

try:
	WebDriverWait(ch, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "1436000"))).click()
	time.sleep(1)
	ch.switch_to_active_element()
	WebDriverWait(ch, 10).until(EC.element_to_be_clickable((By.XPATH, "html/body/div[3]/div[1]/a"))).click()
except (NoSuchElementException, TimeoutException):
	print("Twelfth  Payment Link Doesn't Work Properly")
print("Twelfth  Payment Link Works Properly")

print("\nFinished Checking Payments Section")

WebDriverWait(ch, 10).until(EC.element_to_be_clickable((By.XPATH, ".//*[@id='hxUserMenu']/li[1]/a"))).click()

print("\nChecking Authorizations Section")

WebDriverWait(ch, 10).until(EC.element_to_be_clickable((By.XPATH, ".//*[@id='hxUserMenu']/li[6]/a"))).click()

try:
	WebDriverWait(ch, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "View your Care Plan")))
except (NoSuchElementException, TimeoutException):
	print("Authorizations Section Didn't Load Properly")
	ch.back()
print("Authorizations Secion Loaded Properly")
print("Checking Authorization Links")

try:
	WebDriverWait(ch, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "HX000014801"))).click()
	firstAuthCheck = WebDriverWait(ch, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='serviceContainer']/div[2]/div[3]/div[2]/table/tbody/tr[2]/td[2]/p"))).text

	if firstAuthCheck == "HX000014801":
		print("First   Authorization Link Works Properly")
		ch.back()
except (NoSuchElementException, TimeoutException):
	print("First   Authorization Link Doesn't Work Properly")

try:
	WebDriverWait(ch, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "HX000014800"))).click()
	firstAuthCheck = WebDriverWait(ch, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='serviceContainer']/div[2]/div[3]/div[2]/table/tbody/tr[2]/td[2]/p"))).text

	if firstAuthCheck == "HX000014800":
		print("Second  Authorization Link Works Properly")
		ch.back()
except (NoSuchElementException, TimeoutException):
	print("Second  Authorization Link Doesn't Work Properly")

try:
	WebDriverWait(ch, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "HX000014701"))).click()
	firstAuthCheck = WebDriverWait(ch, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='serviceContainer']/div[2]/div[3]/div[2]/table/tbody/tr[2]/td[2]/p"))).text

	if firstAuthCheck == "HX000014701":
		print("Third   Authorization Link Works Properly")
		ch.back()
except (NoSuchElementException, TimeoutException):
	print("Third   Authorization Link Doesn't Work Properly")

try:
	WebDriverWait(ch, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "HX000014700"))).click()
	firstAuthCheck = WebDriverWait(ch, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='serviceContainer']/div[2]/div[3]/div[2]/table/tbody/tr[2]/td[2]/p"))).text

	if firstAuthCheck == "HX000014700":
		print("Fourth  Authorization Link Works Properly")
		ch.back()
except (NoSuchElementException, TimeoutException):
	print("Fourth  Authorization Link Doesn't Work Properly")

try:
	WebDriverWait(ch, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "HX000014601"))).click()
	firstAuthCheck = WebDriverWait(ch, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='serviceContainer']/div[2]/div[3]/div[2]/table/tbody/tr[2]/td[2]/p"))).text

	if firstAuthCheck == "HX000014601":
		print("Fifth   Authorization Link Works Properly")
		ch.back()
except (NoSuchElementException, TimeoutException):
	print("Fifth   Authorization Link Doesn't Work Properly")

try:
	WebDriverWait(ch, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "HX000014600"))).click()
	firstAuthCheck = WebDriverWait(ch, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='serviceContainer']/div[2]/div[3]/div[2]/table/tbody/tr[2]/td[2]/p"))).text

	if firstAuthCheck == "HX000014600":
		print("Sixth   Authorization Link Works Properly")
		ch.back()
except (NoSuchElementException, TimeoutException):
	print("Sixth   Authorization Link Doesn't Work Properly")

try:
	WebDriverWait(ch, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "HX000014501"))).click()
	firstAuthCheck = WebDriverWait(ch, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='serviceContainer']/div[2]/div[3]/div[2]/table/tbody/tr[2]/td[2]/p"))).text

	if firstAuthCheck == "HX000014501":
		print("Seventh Authorization Link Works Properly")
		ch.back()
except (NoSuchElementException, TimeoutException):
	print("Seventh Authorization Link Doesn't Work Properly")

try:
	WebDriverWait(ch, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "HX000014500"))).click()
	firstAuthCheck = WebDriverWait(ch, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='serviceContainer']/div[2]/div[3]/div[2]/table/tbody/tr[2]/td[2]/p"))).text

	if firstAuthCheck == "HX000014500":
		print("Eighth  Authorization Link Works Properly")
		ch.back()
except (NoSuchElementException, TimeoutException):
	print("Eighth  Authorization Link Doesn't Work Properly")

try:
	WebDriverWait(ch, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "HX000014401"))).click()
	firstAuthCheck = WebDriverWait(ch, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='serviceContainer']/div[2]/div[3]/div[2]/table/tbody/tr[2]/td[2]/p"))).text

	if firstAuthCheck == "HX000014401":
		print("Nineth  Authorization Link Works Properly")
		ch.back()
except (NoSuchElementException, TimeoutException):
	print("Nineth  Authorization Link Doesn't Work Properly")

try:
	WebDriverWait(ch, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "HX000014400"))).click()
	firstAuthCheck = WebDriverWait(ch, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='serviceContainer']/div[2]/div[3]/div[2]/table/tbody/tr[2]/td[2]/p"))).text

	if firstAuthCheck == "HX000014400":
		print("Tenth   Authorization Link Works Properly")
		ch.back()
except (NoSuchElementException, TimeoutException):
	print("Tenth   Authorization Link Doesn't Work Properly")

print("\nFinished Checking Authorizations Section")

WebDriverWait(ch, 10).until(EC.element_to_be_clickable((By.XPATH, ".//*[@id='hxUserMenu']/li[1]/a"))).click()

print("\nChecking Provider Section")

WebDriverWait(ch, 10).until(EC.element_to_be_clickable((By.XPATH, ".//*[@id='hxUserMenu']/li[7]/a"))).click()

try:
	WebDriverWait(ch, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='submitProvSearch']")))
except (NoSuchElementException, TimeoutException):
	print("Provider Tool Didn't Load Properly")
	ch.back()
print("Provider Tool Loaded Properly")
print("Checking Provider Tool")

WebDriverWait(ch, 10).until(EC.presence_of_element_located((By.ID, "providerZip"))).send_keys("54601")
time.sleep(3)
submitBtn = ch.find_element_by_id("submitProvSearch").click()

try:
	WebDriverWait(ch, 10).until(EC.presence_of_element_located((By.ID, "resultsList")))
except (NoSuchElementException, TimeoutException):
	print("Provider Results Didn't Load")
print("Provider Results Loaded")

print("Downloading Provider Directory")

WebDriverWait(ch, 10).until(EC.element_to_be_clickable((By.ID, "downloadResultsLink"))).click()

time.sleep(1)

if os.path.isfile('C:\\Users\\NWeaver\\Downloads\\ProviderDirectory (3).pdf'):
	print("Provider Directory Downloaded Properly")
else:
	print("Provider Directory Didn't Download")

WebDriverWait(ch, 10).until(EC.element_to_be_clickable((By.XPATH, ".//*[@id='hxUserMenu']/li[1]/a"))).click()
print("Test Finished")
print("Logging Out")
WebDriverWait(ch, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Logout"))).click()
try:
	WebDriverWait(ch, 10).until(EC.presence_of_element_located((By.ID, "username")))
except (NoSuchElementException, TimeoutException):
	print("Logout Unsuccessful")
print("Successfully Logged Out")

ch.quit()

end = time.time() - start
print("Total Elapsed Test Time %.2f" % end)