import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

ch = webdriver.Chrome(executable_path='C:\Python34\Scripts\chromedriver.exe')
#ch = webdriver.Firefox()
#ch = webdriver.Ie(executable_path='C:\Python34\Scripts\IEDriverServer.exe')

print("Navigating to Healthx Demo Site")
ch.get('https://hxweb01.healthx.com/newsweetness.aspx')

print("Logging In")
login = ch.find_element_by_id("username").send_keys('Plan.member14')
password = ch.find_element_by_xpath(".//*[@id='ContentItem100_0']/div[2]/fieldset/input[2]").send_keys('american1')
submit_btn = ch.find_element_by_id("loginButton").click()
print("Login Successful")

time.sleep(5)
print("Skipping Splash Screen")

def skip_splash_screen():
	try:
		WebDriverWait(ch, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[contains(text(), 'Skip to Home Page')]"))).click()
	except NoSuchElementException:
		return False
	return True

if skip_splash_screen():
	print("Splash Screen Skipped")
else:
	print("Splash Screen Element Undetected, Cannot Continue Test")
	ch.quit()

time.sleep(3)
print("\nChecking Eligibility Dashboard")

def check_coverage_element():
	try:
		ch.find_element_by_id("ContentItem200_2")
	except NoSuchElementException:
		return False
	return True

def check_coverage_section():
	viewAllCoverageLink = ch.find_element_by_xpath(".//*[@id='dependentList']/tbody/tr[1]/td[2]/a").click()

	def check_viewall_page():
		try:
			WebDriverWait(ch, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='serviceContainer']/div[3]")))
		except NoSuchElementException:
			return False
		return True

	if check_viewall_page():
		print("View All Coverages Link is working properly")
	else:
		print("View All coverages Link isn't working properly")

	ch.back()
	time.sleep(2)

	lizLink = ch.find_element_by_xpath(".//*[@id='theDependentList']/td[1]/a").click()

	time.sleep(2)

	def check_dep_link():
		try:
			WebDriverWait(ch, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='ctl00_MainContent_uxMessageLabel']")))
		except NoSuchElementException:
			return False
		return True

	if check_dep_link():
		print("Elizabeth Jones Link Works Properly")
	else:
		print("Elizabeth Jones Link Doesn't Work Properly")

	ch.back()
	time.sleep(2)

	danLink = ch.find_element_by_xpath(".//*[@id='theDependentList']/td[2]/a").click()

	time.sleep(2)

	if check_dep_link():
		print("Daniel Jones Link Works Properly")
	else:
		print("Daniel Jones Link Doesn't Work Properly")

	ch.back()
	time.sleep(2)

	aliLink = ch.find_element_by_xpath(".//*[@id='theDependentList']/td[3]/a").click()

	time.sleep(2)

	if check_dep_link():
		print("Alicia Jones Link Works Properly")
	else:
		print("Alicia Jones Link Doesn't Work Properly")

	ch.back()
	time.sleep(2)

if check_coverage_element():
	print("Coverage Element Found")
	print("Checking Coverage links")
	check_coverage_section()
else:
	print("Coverage Element Not Found")
	print("Skipping Links")

print("Finished Checking Eligibility Dashboard\n")
print("Checking Balance Summary Section")

def verify_balances_section():
	try:	
		ch.find_element_by_xpath(".//*[@id='ContentItem200_3']/div")
	except NoSuchElementException:
		return False
	return True

if verify_balances_section():
	print("Balance Summary Element Present")
else:
	print("Balance Summary Element Not Present")

print("Finished Checking Balance Summary Section\n")
print("Checking Claims Dashboard")

def verify_claims_section():
	try:	
		ch.find_element_by_xpath(".//*[@id='ContentItem200_4']/div")
	except NoSuchElementException:
		return False
	return True

def check_claims_section():
	claimsLink = ch.find_element_by_link_text("Proceed to my Claims").click()

	def check_claims_phi():
		try:
			WebDriverWait(ch, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='ctl00_MainContent_uxClaimsMessageLabel']")))
		except NoSuchElementException:
			return False
		return True

	if check_claims_phi():
		print("PHI Found")
	else:
		print("PHI Not Found")

	time.sleep(2)
	claimFormLink = ch.find_element_by_link_text("Member Claims Submission").click()
	time.sleep(2)
	claimFormCheck = ch.find_element_by_xpath(".//*[@id='ctl00_MainContent_uxForm_ctl02_EMAIL_textbox']").text
	print(claimFormCheck)
	if claimFormCheck == "mweston@healthx.com":
		print("Claims Form Loaded Properly")
	else:
		print("Claims Form Didn't Load Properly")

	ch.back()
	time.sleep(3)

	try:
		firstClaim = ch.find_element_by_link_text("4557784597").click()
		firstClaimCheck = ch.find_element_by_xpath(".//*[@id='serviceContainer']/div[2]/div[3]/div[1]/h3").text

		if firstClaimCheck == "Claim #4557784597":
			print("First   Claims Link Works Properly")
		else:
			print("First Claims Link Doesn't Work Properly")
	except NoSuchElementException:
		print("Element Not Found")

	ch.back()
	time.sleep(2)

	try:
		secondClaim = ch.find_element_by_link_text("9156395414").click()
		secondClaimCheck = ch.find_element_by_xpath(".//*[@id='serviceContainer']/div[2]/div[3]/div[1]/h3").text
	
		if secondClaimCheck == "Claim #9156395414":
			print("Second  Claims Link Works Properly")
		else:
			print("Second Claims Link Doesn't Work Properly")
	except NoSuchElementException:
		print("Element Not Found")

	ch.back()

	try:
		thirdClaim = ch.find_element_by_link_text("4021764337").click()
		thirdClaimCheck = ch.find_element_by_xpath(".//*[@id='serviceContainer']/div[2]/div[3]/div[1]/h3").text
	
		if thirdClaimCheck == "Claim #4021764337":
			print("Third   Claims Link Works Properly")
		else:
			print("Third Claims Link Doesn't Work Properly")
	except NoSuchElementException:
		return False
	return True

	ch.back()

	try:
		fourthClaim = ch.find_element_by_link_text("6755069099").click()
		fourthClaimCheck = ch.find_element_by_xpath(".//*[@id='serviceContainer']/div[2]/div[3]/div[1]/h3").text
	
		if fourthClaimCheck == "Claim #6755069099":
			print("Fourth  Claims Link Works Properly")
		else:
			print("Fourth Claims Link Doesn't Work Properly")
	except NoSuchElementException:
		return False
	return True

	ch.back()

	try:
		fifthClaim = ch.find_element_by_link_text("0964388342").click()
		fifthClaimCheck = ch.find_element_by_xpath(".//*[@id='serviceContainer']/div[2]/div[3]/div[1]/h3").text
	
		if fifthClaimCheck == "Claim #0964388342":
			print("Fifth   Claims Link Works Properly")
		else:
			print("Fifth Claims Link Doesn't Work Properly")
	except NoSuchElementException:
		return False
	return True

	ch.back()

	try:
		sixthClaim = ch.find_element_by_link_text("1674315135").click()
		sixthClaimCheck = ch.find_element_by_xpath(".//*[@id='serviceContainer']/div[2]/div[3]/div[1]/h3").text
	
		if sixthClaimCheck == "Claim #1674315135":
			print("Sixth   Claims Link Works Properly")
		else:
			print("Sixth Claims Link Doesn't Work Properly")
	except NoSuchElementException:
		return False
	return True

	ch.back()

	try:
		seventhClaim = ch.find_element_by_link_text("7973735542").click()
		seventhClaimCheck = ch.find_element_by_xpath(".//*[@id='serviceContainer']/div[2]/div[3]/div[1]/h3").text
	
		if seventhClaimCheck == "Claim #7973735542":
			print("Seventh Claims Link Works Properly")
		else:
			print("Seventh Claims Link Doesn't Work Properly")
	except NoSuchElementException:
		return False
	return True

	ch.back()

	try:
		eighthClaim = ch.find_element_by_link_text("8128013376").click()
		eighthClaimCheck = ch.find_element_by_xpath(".//*[@id='serviceContainer']/div[2]/div[3]/div[1]/h3").text
	
		if eighthClaimCheck == "Claim #8128013376":
			print("Eighth  Claims Link Works Properly")
		else:
			print("Eighth Claims Link Doesn't Work Properly")
	except NoSuchElementException:
		return False
	return True

	ch.back()

	try:
		ninethClaim = ch.find_element_by_link_text("9982984085").click()
		ninethClaimCheck = ch.find_element_by_xpath(".//*[@id='serviceContainer']/div[2]/div[3]/div[1]/h3").text
	
		if ninethClaimCheck == "Claim #9982984085":
			print("Nineth  Claims Link Works Properly")
		else:
			print("Nineth Claims Link Doesn't Work Properly")
	except NoSuchElementException:
		return False
	return True

	ch.back()

	try:
		tenthClaim = ch.find_element_by_link_text("1382195851").click()
		tenthClaimCheck = ch.find_element_by_xpath(".//*[@id='serviceContainer']/div[2]/div[3]/div[1]/h3").text
	
		if tenthClaimCheck == "Claim #1382195851":
			print("Tenth   Claims Link Works Properly")
		else:
			print("Tenth Claims Link Doesn't Work Properly")
	except NoSuchElementException:
		return False
	return True

	ch.back()

if verify_claims_section():
	print("Claims Element Present")
	print("Checking Claims Page and Links")
	check_claims_section()
else:
	print("Claims Element Not Present")
	print("Skipping Links")

print("Finished Checking Claims Section\n")
ch.back()

time.sleep(5)
print("Checking Payments Section")

def verify_payments_section():
	try:	
		ch.find_element_by_xpath(".//*[@id='ContentItem200_6']/div")
	except NoSuchElementException:
		return False
	return True

def check_payments_section():
	proceedPaymentLink = ch.find_element_by_xpath(".//*[@id='hxUserMenu']/li[4]/a").click()

	def check_payments_link():
		try:
			WebDriverWait(ch, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='flexAccounts']/a")))
		except NoSuchElementException:
			return False
		return True

	if check_payments_link():
		print("Payments Page Loaded Properly")
	else:
		print("Payments Page Not Loaded Properly")

	def first_payment_link():
		try:
			firstPaymentLink = ch.find_element_by_link_text("1444789").click()
			time.sleep(1)
			ch.switch_to_active_element()
			exitBtn = ch.find_element_by_xpath("html/body/div[3]/div[1]/a").click()
		except NoSuchElementException:
			return False
		return True

	if first_payment_link():
		print("First    Payment Link Works Properly")
	else:
		print("First    Payment Link Doesn't Work Properly")

	time.sleep(1.5)
	
	def second_payment_link():
		try:
			secondPaymentLink = ch.find_element_by_link_text("1425445").click()
			time.sleep(1)
			ch.switch_to_active_element()
			exitBtn = ch.find_element_by_xpath("html/body/div[3]/div[1]/a").click()
		except NoSuchElementException:
			return False
		return True

	if second_payment_link():
		print("Second   Payment Link Works Properly")
	else:
		print("Second   Payment Link Doesn't Work Properly")

	time.sleep(1.5)
	
	def third_payment_link():
		try:
			thirdPaymentLink = ch.find_element_by_link_text("1453467").click()
			time.sleep(1)
			ch.switch_to_active_element()
			exitBtn = ch.find_element_by_xpath("html/body/div[3]/div[1]/a").click()
		except NoSuchElementException:
			return False
		return True

	if third_payment_link():
		print("Third    Payment Link Works Properly")
	else:
		print("Third    Payment Link Doesn't Work Properly")

	time.sleep(1.5)
	
	def fourth_payment_link():
		try:
			fourthPaymentLink = ch.find_element_by_link_text("1380178").click()
			time.sleep(1)
			ch.switch_to_active_element()
			exitBtn = ch.find_element_by_xpath("html/body/div[3]/div[1]/a").click()
		except NoSuchElementException:
			return False
		return True

	if fourth_payment_link():
		print("Fourth   Payment Link Works Properly")
	else:
		print("Fourth   Payment Link Doesn't Work Properly")

	time.sleep(1.5)
	
	def fifth_payment_link():
		try:
			fifthPaymentLink = ch.find_element_by_link_text("1370479").click()
			time.sleep(1)
			ch.switch_to_active_element()
			exitBtn = ch.find_element_by_xpath("html/body/div[3]/div[1]/a").click()
		except NoSuchElementException:
			return False
		return True

	if fifth_payment_link():
		print("Fifth    Payment Link Works Properly")
	else:
		print("Fifth    Payment Link Doesn't Work Properly")

	time.sleep(1.5)
	
	def sixth_payment_link():
		try:
			sixthPaymentLink = ch.find_element_by_link_text("1479221").click()
			time.sleep(1)
			ch.switch_to_active_element()
			exitBtn = ch.find_element_by_xpath("html/body/div[3]/div[1]/a").click()
		except NoSuchElementException:
			return False
		return True

	if sixth_payment_link():
		print("Sixth    Payment Link Works Properly")
	else:
		print("Sixth    Payment Link Doesn't Work Properly")

	time.sleep(1.5)
	
	def seventh_payment_link():
		try:
			seventhPaymentLink = ch.find_element_by_link_text("1414898").click()
			time.sleep(1)
			ch.switch_to_active_element()
			exitBtn = ch.find_element_by_xpath("html/body/div[3]/div[1]/a").click()
		except NoSuchElementException:
			return False
		return True

	if seventh_payment_link():
		print("Seventh  Payment Link Works Properly")
	else:
		print("Seventh  Payment Link Doesn't Work Properly")

	time.sleep(1.5)
	
	def eighth_payment_link():
		try:
			eighthPaymentLink = ch.find_element_by_link_text("1471462").click()
			time.sleep(1)
			ch.switch_to_active_element()
			exitBtn = ch.find_element_by_xpath("html/body/div[3]/div[1]/a").click()
		except NoSuchElementException:
			return False
		return True

	if eighth_payment_link():
		print("Eighth   Payment Link Works Properly")
	else:
		print("Eighth   Payment Link Doesn't Work Properly")

	time.sleep(1.5)
	
	def nineth_payment_link():
		try:
			ninethPaymentLink = ch.find_element_by_link_text("1401260").click()
			time.sleep(1)
			ch.switch_to_active_element()
			exitBtn = ch.find_element_by_xpath("html/body/div[3]/div[1]/a").click()
		except NoSuchElementException:
			return False
		return True

	if nineth_payment_link():
		print("Nineth   Payment Link Works Properly")
	else:
		print("Nineth   Payment Link Doesn't Work Properly")

	time.sleep(1.5)
	
	def tenth_payment_link():
		try:
			tenthPaymentLink = ch.find_element_by_link_text("1391391").click()
			time.sleep(1)
			ch.switch_to_active_element()
			exitBtn = ch.find_element_by_xpath("html/body/div[3]/div[1]/a").click()
		except NoSuchElementException:
			return False
		return True

	if tenth_payment_link():
		print("Tenth    Payment Link Works Properly")
	else:
		print("Tenth    Payment Link Doesn't Work Properly")

	time.sleep(1.5)
	
	def eleventh_payment_link():
		try:
			eleventhPaymentLink = ch.find_element_by_link_text("1462699").click()
			time.sleep(1)
			ch.switch_to_active_element()
			exitBtn = ch.find_element_by_xpath("html/body/div[3]/div[1]/a").click()
		except NoSuchElementException:
			return False
		return True

	if eleventh_payment_link():
		print("Eleventh Payment Link Works Properly")
	else:
		print("Eleventh Payment Link Doesn't Work Properly")

	time.sleep(1.5)
	
	def twelfth_payment_link():
		try:
			twelfthPaymentLink = ch.find_element_by_link_text("1436000").click()
			time.sleep(1)
			ch.switch_to_active_element()
			exitBtn = ch.find_element_by_xpath("html/body/div[3]/div[1]/a").click()
		except NoSuchElementException:
			return False
		return True

	if twelfth_payment_link():
		print("Twelfth  Payment Link Works Properly")
	else:
		print("Twelfth  Payment Link Doesn't Work Properly")
	
if verify_payments_section():
	print("Payments Element Present")
	print("Checking Payments Page")
	check_payments_section()
else:
	print("Payments Element not Present")

print("\nFinished Checking Payments Section")
homeBtn = ch.find_element_by_xpath(".//*[@id='hxUserMenu']/li[1]/a").click()

print("\nChecking Authorizations Section")

authBtn = ch.find_element_by_xpath(".//*[@id='hxUserMenu']/li[6]/a").click()

def verify_auth_section():
	try:
		WebDriverWait(ch, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[contains(text(), 'View your Care Plan')]")))
	except NoSuchElementException:
		return False
	return True

def check_authorization_section():
	firstAuth = ch.find_element_by_link_text("HX000014801").click()
	firstAuthCheck = ch.find_element_by_xpath(".//*[@id='serviceContainer']/div[2]/div[3]/div[2]/table/tbody/tr[2]/td[2]/p").text

	if firstAuthCheck == "HX000014801":
		print("First   Authorization Link Works Properly")
	else:
		print("First   Authorization Link Doesn't Work Properly")

	ch.back()

	secondAuth = ch.find_element_by_link_text("HX000014800").click()
	secondAuthCheck = ch.find_element_by_xpath(".//*[@id='serviceContainer']/div[2]/div[3]/div[2]/table/tbody/tr[2]/td[2]/p").text

	if secondAuthCheck == "HX000014800":
		print("Second  Authorization Link Works Properly")
	else:
		print("Second  Authorization Link Doesn't Work Properly")

	ch.back()

	thirdAuth = ch.find_element_by_link_text("HX000014701").click()
	thirdAuthCheck = ch.find_element_by_xpath(".//*[@id='serviceContainer']/div[2]/div[3]/div[2]/table/tbody/tr[2]/td[2]/p").text

	if thirdAuthCheck == "HX000014701":
		print("Third   Authorization Link Works Properly")
	else:
		print("Third   Authorization Link Doesn't Work Properly")

	ch.back()

	fourthAuth = ch.find_element_by_link_text("HX000014700").click()
	fourthAuthCheck = ch.find_element_by_xpath(".//*[@id='serviceContainer']/div[2]/div[3]/div[2]/table/tbody/tr[2]/td[2]/p").text

	if fourthAuthCheck == "HX000014700":
		print("Fourth  Authorization Link Works Properly")
	else:
		print("Fourth  Authorization Link Doesn't Work Properly")

	ch.back()

	fifthAuth = ch.find_element_by_link_text("HX000014601").click()
	fifthAuthCheck = ch.find_element_by_xpath(".//*[@id='serviceContainer']/div[2]/div[3]/div[2]/table/tbody/tr[2]/td[2]/p").text

	if fifthAuthCheck == "HX000014601":
		print("Fifth   Authorization Link Works Properly")
	else:
		print("Fifth   Authorization Link Doesn't Work Properly")

	ch.back()

	sixthAuth = ch.find_element_by_link_text("HX000014600").click()
	sixthAuthCheck = ch.find_element_by_xpath(".//*[@id='serviceContainer']/div[2]/div[3]/div[2]/table/tbody/tr[2]/td[2]/p").text

	if sixthAuthCheck == "HX000014600":
		print("Sixth   Authorization Link Works Properly")
	else:
		print("Sixth   Authorization Link Doesn't Work Properly")

	ch.back()

	seventhAuth = ch.find_element_by_link_text("HX000014501").click()
	seventhAuthCheck = ch.find_element_by_xpath(".//*[@id='serviceContainer']/div[2]/div[3]/div[2]/table/tbody/tr[2]/td[2]/p").text

	if seventhAuthCheck == "HX000014501":
		print("Seventh Authorization Link Works Properly")
	else:
		print("Seventh Authorization Link Doesn't Work Properly")

	ch.back()

	eighthAuth = ch.find_element_by_link_text("HX000014500").click()
	eighthAuthCheck = ch.find_element_by_xpath(".//*[@id='serviceContainer']/div[2]/div[3]/div[2]/table/tbody/tr[2]/td[2]/p").text

	if eighthAuthCheck == "HX000014500":
		print("Eighth  Authorization Link Works Properly")
	else:
		print("Eighth  Authorization Link Doesn't Work Properly")

	ch.back()

	ninethAuth = ch.find_element_by_link_text("HX000014401").click()
	ninethAuthCheck = ch.find_element_by_xpath(".//*[@id='serviceContainer']/div[2]/div[3]/div[2]/table/tbody/tr[2]/td[2]/p").text

	if ninethAuthCheck == "HX000014401":
		print("Nineth  Authorization Link Works Properly")
	else:
		print("Nineth  Authorization Link Doesn't Work Properly")

	ch.back()

	tenthAuth = ch.find_element_by_link_text("HX000014400").click()
	tenthAuthCheck = ch.find_element_by_xpath(".//*[@id='serviceContainer']/div[2]/div[3]/div[2]/table/tbody/tr[2]/td[2]/p").text

	if tenthAuthCheck == "HX000014400":
		print("Tenth   Authorization Link Works Properly")
	else:
		print("Tenth   Authorization Link Doesn't Work Properly")

	ch.back()

if verify_auth_section():
	print("Authorizations Secion Loaded Properly")
	print("Checking Authorization Links")
	check_authorization_section()
else:
	print("Authorizations Section Didn't Load Properly")
	ch.back()

print("\nFinished Checking Authorizations Section")
homeBtn = ch.find_element_by_xpath(".//*[@id='hxUserMenu']/li[1]/a").click()
print("\nChecking Provider Section")

providerBtn = ch.find_element_by_xpath(".//*[@id='hxUserMenu']/li[7]/a").click()
time.sleep(2)

def verify_auth_section():
	try:
		WebDriverWait(ch, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='submitProvSearch']")))
	except NoSuchElementException:
		return False
	return True

def check_prov_section():
	provZip = ch.find_element_by_xpath(".//*[@id='providerZip']").send_keys("54601")
	provSearch = ch.find_element_by_xpath(".//*[@id='submitProvSearch']").click()

	time.sleep(7)
	provDownload = ch.find_element_by_xpath(".//*[@id='downloadResultsLink']").click()
	time.sleep(3)

	if os.path.isfile('C:\\Users\\NWeaver\\Downloads\\ProviderDirectory.pdf'):
		print("Provider Directory Downloaded Properly")
	else:
		print("Provider Directory Didn't Download")

if verify_auth_section():
	print("Provider Tool Loaded Properly")
	print("Checking Provider Tool")
	check_prov_section()
else:
	print("Provider Tool Didn't Load Properly")
	ch.back()

homeBtn = ch.find_element_by_xpath(".//*[@id='hxUserMenu']/li[1]/a").click()
print("Test Finished")
print("Logging Out")
logoutBtn = ch.find_element_by_xpath(".//*[@id='basicShell']/header/nav[1]/ul/li[3]/a").click()
print("Successfully Logged Out")