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

userProfile = os.environ['USERPROFILE']
scriptPath = os.path.dirname(userProfile + '\\Desktop\\Demosite Automation\\MemberDemo\\ChromeLogs\\')
outputFile = os.path.join(scriptPath, "member_demosite_automation_chrome_hxweb01_" + time.strftime("%m-%d-%H-%M") + ".log")
output = open(outputFile, 'w', encoding='utf-8')
sys.stdout = output

def main():
	driver = webdriver.Chrome(executable_path='C:\Python34\Scripts\chromedriver.exe')
	#driver = webdriver.Firefox()
	#driver = webdriver.Ie(executable_path='C:\Python34\Scripts\IEDriverServer.exe')

	results = []

	start = time.time()
	driver.get('https://secure.healthx.com/newsweetness.aspx')

	print("Chrome - hxweb01\n")
	print("LOGIN")

	try:
		driver.find_element_by_id("username").send_keys('Plan.member14')
	except NoSuchElementException:
		print("Login Not Found")
		driver.quit()

	try:
		driver.find_element_by_name("password").send_keys('american1')
	except NoSuchElementException:
		print("Password Not Found")
		driver.quit()

	try:
		driver.find_element_by_id("loginButton").click()
	except NoSuchElementException:
		print("Login Button Not Found")
		driver.quit()

	time.sleep(2)

	try:
		driver.find_element_by_link_text("Skip to Home Page").click()
	except NoSuchElementException:
		results.append(("Login", "Fail", "Element Not Found"))
		results.append(("Splash Screen", "Fail", "Element Not Found"))
		print(tabulate(results, headers = ["Section", "Result", "Comment"], tablefmt="fancy_grid"))
		driver.quit()
	except TimeoutException:
		results.append(("Login", "Fail", ""))
		results.append(("Splash Screen", "Fail", "Element Not Found in 10 Seconds"))
		print(tabulate(results, headers = ["Section", "Result", "Comment"], tablefmt="fancy_grid"))
		driver.quit()
	else:
		results.append(("Login", "Pass", ""))
		results.append(("Splash Screen", "Pass", ""))

	print(tabulate(results, headers = ["Section", "Result", "Comment"], tablefmt="fancy_grid"))
	results = []

	print("ELIGIBILITY DASHBOARD")

	##### COVERAGE SECTION #####

	try:
		WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "ContentItem200_2")))
	except TimeoutException:
		results.append(("Coverage Section", "Fail", "Element Not Located After 5 Seconds"))
	else:
		results.append(("Coverage Section", "Pass", ""))

		try:
			WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.LINK_TEXT, "View all Coverage & Benefits"))).click()
		except TimeoutException:
			results.append(("View All Link", "Fail", "Element Not Located After 5 Seconds"))
		else:
			results.append(("View All Link", "Pass", ""))
			try:
				WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.LINK_TEXT, "Schedule of Benefits")))
			except TimeoutException:
				results.append(("View All Link Page", "Fail", "Page Did Not Load Properly After 5 Seconds"))
			else:
				results.append(("View All Link Page", "Pass", ""))
				driver.back()

		try:
			WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.LINK_TEXT, "Elizabeth Jones"))).click()
		except TimeoutException:
			results.append(("Elizabeth Jones Link", "Fail", "Element Not Found"))
		else:
			results.append(("Elizabeth Jones Link", "Pass", ""))
			try:
				WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "ctl00_MainContent_uxMessageLabel")))
			except TimeoutException:
				results.append(("Elizabeth Jones Link Page", "Fail", "Page Did Not Load Properly After 5 Seconds"))
			else:
				results.append(("Elizabeth Jones Link Page", "Pass", ""))
				driver.back()
		
		try:
			WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.LINK_TEXT, "Daniel Jones"))).click()
		except NoSuchElementException:
			results.append(("Daniel Jones Link", "Fail", "Element Not Found"))
		else:
			results.append(("Daniel Jones Link", "Pass", ""))
			try:
				WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "ctl00_MainContent_uxMessageLabel")))
			except TimeoutException:
				results.append(("Daniel Jones Link Page", "Fail", "Page Did Not Load Properly After 5 Seconds"))
			else:
				results.append(("Daniel Jones Link Page", "Pass", ""))
				driver.back()
		
		try:
			WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.LINK_TEXT, "Alicia Jones"))).click()
		except NoSuchElementException:
			results.append(("Alicia Jones Link", "Fail", "Element Not Found"))
		else:
			results.append(("Alicia Jones Link", "Pass", ""))
			try:
				WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "ctl00_MainContent_uxMessageLabel")))
			except TimeoutException:
				results.append(("Elizabeth Jones Link Page", "Fail", "Page Did Not Load Properly After 5 Seconds"))
			else:
				results.append(("Elizabeth Jones Link Page", "Pass", ""))
				driver.back()

	print(tabulate(results, headers = ["Section", "Result", "Comment"], tablefmt="fancy_grid"))
	results = []

	print("BALANCE SECTION")

	##### BALANCES SECTION #####

	try:
		WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "ContentItem200_3")))
	except TimeoutException:
		results.append(("Balances Section", "Fail", "Element Not Located After 5 Seconds"))
	else:
		results.append(("Balances Section", "Pass", ""))

	print(tabulate(results, headers = ["Section", "Result", "Comment"], tablefmt="fancy_grid"))
	results = []

	print("CLAIMS DASHBOARD")

	##### CLAIMS SECTION ######

	try:
		WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "ContentItem200_4")))
	except TimeoutException:
		results.append(("Claims Section", "Fail", "Element Not Located After 5 Seconds"))
	else:
		results.append(("Claims Section", "Pass", ""))

		try:
			WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.LINK_TEXT, "Proceed to my Claims"))).click()
		except TimeoutException:
			results.append(("Claims Link", "Fail", "Element Not Located After 5 Seconds"))
		else:
			results.append(("Claims Link", "Pass", ""))

			try:
				WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='serviceContainer']/div[2]/div/div[2]")))
			except TimeoutException:
				results.append(("Claims Link Page", "Fail", "Element Not Located After 5 Seconds"))
			else:
				results.append(("Claims Link Page", "Pass", ""))

			try:
				driver.find_element_by_link_text("Member Claims Submission").click()
			except NoSuchElementException:
				results.append(("Claims Form Link", "Fail", "Element Not Found"))
			else:
				results.append(("Claims Form Link", "Pass", ""))
				try:
					WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "ctl00_MainContent_uxForm_ctl03_uxFormSubmitButton")))
				except TimeoutException:
					results.append(("Claims Form", "Fail", "Page Did Not Load Properly After 5 Seconds"))
				else:
					results.append(("Claims Form", "Pass", ""))
					driver.back()

			try:
				WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.LINK_TEXT, "4557784597"))).click()
			except TimeoutException:
				results.append(("Claims Link 1", "Fail", "Element Not Located After 5 Seconds"))
			else:
				try:
					firstClaimCheck = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='serviceContainer']/div[2]/div[3]/div[1]/h3"))).text

					if firstClaimCheck == "Claim #4557784597":
						results.append(("Claims Link 1", "Pass", ""))
						driver.back()
				except TimeoutException:
					results.append(("Claims Link 1", "Fail", "Element Not Located After 5 Seconds"))

			try:
				WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.LINK_TEXT, "9156395414"))).click()
			except TimeoutException:
				results.append(("Claims Link 2", "Fail", "Element Not Located After 5 Seconds"))
			else:
				try:
					secondClaimCheck = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='serviceContainer']/div[2]/div[3]/div[1]/h3"))).text

					if secondClaimCheck == "Claim #9156395414":
						results.append(("Claims Link 2", "Pass", ""))
						driver.back()
				except TimeoutException:
					results.append(("Claims Link 2", "Fail", "Element Not Located After 5 Seconds"))

			try:
				WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.LINK_TEXT, "4021764337"))).click()
			except TimeoutException:
				results.append(("Claims Link 3", "Fail", "Element Not Located After 5 Seconds"))
			else:
				try:
					thirdClaimCheck = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='serviceContainer']/div[2]/div[3]/div[1]/h3"))).text

					if thirdClaimCheck == "Claim #4021764337":
						results.append(("Claims Link 3", "Pass", ""))
						driver.back()
				except TimeoutException:
					results.append(("Claims Link 3", "Fail", "Element Not Located After 5 Seconds"))

			try:
				WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.LINK_TEXT, "6755069099"))).click()
			except TimeoutException:
				results.append(("Claims Link 4", "Fail", "Element Not Located After 5 Seconds"))
			else:
				try:
					fourthClaimCheck = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='serviceContainer']/div[2]/div[3]/div[1]/h3"))).text

					if fourthClaimCheck == "Claim #6755069099":
						results.append(("Claims Link 4", "Pass", ""))
						driver.back()
				except TimeoutException:
					results.append(("Claims Link 4", "Fail", "Element Not Located After 5 Seconds"))

			try:
				WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.LINK_TEXT, "0964388342"))).click()
			except TimeoutException:
				results.append(("Claims Link 5", "Fail", "Element Not Located After 5 Seconds"))
			else:
				try:
					fifthClaimCheck = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='serviceContainer']/div[2]/div[3]/div[1]/h3"))).text

					if fifthClaimCheck == "Claim #0964388342":
						results.append(("Claims Link 5", "Pass", ""))
						driver.back()
				except TimeoutException:
					results.append(("Claims Link 5", "Fail", "Element Not Located After 5 Seconds"))

			try:
				WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.LINK_TEXT, "1674315135"))).click()
			except TimeoutException:
				results.append(("Claims Link 6", "Fail", "Element Not Located After 5 Seconds"))
			else:
				try:
					sixthClaimCheck = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='serviceContainer']/div[2]/div[3]/div[1]/h3"))).text

					if sixthClaimCheck == "Claim #1674315135":
						results.append(("Claims Link 6", "Pass", ""))
						driver.back()
				except TimeoutException:
					results.append(("Claims Link 6", "Fail", "Element Not Located After 5 Seconds"))

			try:
				WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.LINK_TEXT, "7973735542"))).click()
			except TimeoutException:
				results.append(("Claims Link 7", "Fail", "Element Not Located After 5 Seconds"))
			else:
				try:
					seventhClaimCheck = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='serviceContainer']/div[2]/div[3]/div[1]/h3"))).text

					if seventhClaimCheck == "Claim #7973735542":
						results.append(("Claims Link 7", "Pass", ""))
						driver.back()
				except TimeoutException:
					results.append(("Claims Link 7", "Fail", "Element Not Located After 5 Seconds"))

			try:
				WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.LINK_TEXT, "8128013376"))).click()
			except TimeoutException:
				results.append(("Claims Link 8", "Fail", "Element Not Located After 5 Seconds"))
			else:
				try:
					eighthClaimCheck = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='serviceContainer']/div[2]/div[3]/div[1]/h3"))).text

					if eighthClaimCheck == "Claim #8128013376":
						results.append(("Claims Link 8", "Pass", ""))
						driver.back()
				except TimeoutException:
					results.append(("Claims Link 8", "Fail", "Element Not Located After 5 Seconds"))

			try:
				WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.LINK_TEXT, "9982984085"))).click()
			except TimeoutException:
				results.append(("Claims Link 9", "Fail", "Element Not Located After 5 Seconds"))
			else:
				try:
					ninethClaimCheck = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='serviceContainer']/div[2]/div[3]/div[1]/h3"))).text

					if ninethClaimCheck == "Claim #9982984085":
						results.append(("Claims Link 9", "Pass", ""))
						driver.back()
				except TimeoutException:
					results.append(("Claims Link 9", "Fail", "Element Not Located After 5 Seconds"))

			try:
				WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.LINK_TEXT, "1382195851"))).click()
			except TimeoutException:
				results.append(("Claims Link 10", "Fail", "Element Not Located After 5 Seconds"))
			else:
				try:
					tenthClaimCheck = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='serviceContainer']/div[2]/div[3]/div[1]/h3"))).text

					if tenthClaimCheck == "Claim #1382195851":
						results.append(("Claims Link 10", "Pass", ""))
						driver.back()
				except TimeoutException:
					results.append(("Claims Link 10", "Fail", "Element Not Located After 5 Seconds"))

	print(tabulate(results, headers = ["Section", "Result", "Comment"], tablefmt="fancy_grid"))
	results = []

	try:
		WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, ".//*[@id='hxUserMenu']/li[1]/a"))).click()
	except TimeoutException:
		results.append(("Home Button", "Fail", "Element Not Located After 5 Seconds"))
		print(tabulate(results, headers = ["Section", "Result", "Comment"], tablefmt="fancy_grid"))
		driver.quit()
	else:
		results.append(("Home Button", "Pass", ""))

	##### PAYMENTS SECTION #####

	print("PAYMENTS SECTION")

	try:
		WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "ContentItem200_5")))
	except TimeoutException:
		results.append(("Payments Section", "Fail", "Element Not Located After 5 Seconds"))
	else:
		results.append(("Payments Section", "Pass", ""))

		try:
			WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, ".//*[@id='hxUserMenu']/li[4]/a"))).click()
		except TimeoutException:
			results.append(("Payments Link", "Fail", "Element Not Located After 5 Seconds"))
		else:
			results.append(("Payments Link", "Pass", ""))

			try:
				WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='ViewPanel']/span/table/tbody/tr/td/table/tbody/tr/td")))
			except TimeoutException:
				results.append(("Payments Page", "Fail", "Page Did Not Load Properly After 5 Seconds"))
			else:
				results.append(("Payments Page", "Pass", ""))

	print(tabulate(results, headers = ["Section", "Result", "Comment"], tablefmt="fancy_grid"))
	results = []

	try:
		WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, ".//*[@id='hxUserMenu']/li[1]/a"))).click()
	except TimeoutException:
		results.append(("Home Button", "Fail", "Element Not Located After 5 Seconds"))
		print(tabulate(results, headers = ["Section", "Result", "Comment"], tablefmt="fancy_grid"))
		driver.quit()
	else:
		results.append(("Home Button", "Pass", ""))

	##### AUTHORIZATIONS SECTION #####

	print("AUTHORIZATIONS SECTION")

	try:
		WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, ".//*[@id='hxUserMenu']/li[5]/a"))).click()
	except TimeoutException:
		results.append(("Authorizations Link", "Fail", "Element Not located After 5 Seconds"))
	else:
		results.append(("Authorizations Link", "Pass", ""))
		try:
			WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.LINK_TEXT, "View your Care Plan")))
		except TimeoutException:
			results.append(("Authorizations Page", "Fail", "Page Did Not Load Properly After 5 Seconds"))
		else:
			results.append(("Authorizations Page", "Pass", ""))

			try:
				firstAuthLink = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, ".//*[@id='ctl00_MainContent_uxAuthorizationsGrid']/tbody/tr[2]/td[1]/a")))
				firstAuthLinkText = firstAuthLink.text
				firstAuthLink.click()
				firstAuthCheck = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='serviceContainer']/div[2]/div[3]/div[2]/table/tbody/tr[2]/td[2]/p"))).text
				
				if firstAuthCheck == firstAuthLinkText:
					results.append(("Auth Link 1", "Pass", ""))
					driver.back()
			except TimeoutException:
				results.append(("Auth Link 1", "Fail", "Element Not located After 5 Seconds"))

			try:
				secondAuthLink = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, ".//*[@id='ctl00_MainContent_uxAuthorizationsGrid']/tbody/tr[3]/td[1]/a")))
				secondAuthLinkText = secondAuthLink.text
				secondAuthLink.click()
				secondAuthCheck = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='serviceContainer']/div[2]/div[3]/div[2]/table/tbody/tr[2]/td[2]/p"))).text

				if secondAuthCheck == secondAuthLinkText:
					results.append(("Auth Link 2", "Pass", ""))
					driver.back()
			except TimeoutException:
				results.append(("Auth Link 2", "Fail", "Element Not located After 5 Seconds"))

			try:
				thirdAuthLink = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, ".//*[@id='ctl00_MainContent_uxAuthorizationsGrid']/tbody/tr[4]/td[1]/a")))
				thirdAuthLinkText = thirdAuthLink.text
				thirdAuthLink.click()
				thirdAuthCheck = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='serviceContainer']/div[2]/div[3]/div[2]/table/tbody/tr[2]/td[2]/p"))).text

				if thirdAuthCheck == thirdAuthLinkText:
					results.append(("Auth Link 3", "Pass", ""))
					driver.back()
			except TimeoutException:
				results.append(("Auth Link 3", "Fail", "Element Not located After 5 Seconds"))

			try:
				fourthAuthLink = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, ".//*[@id='ctl00_MainContent_uxAuthorizationsGrid']/tbody/tr[5]/td[1]/a")))
				fourthAuthLinkText = fourthAuthLink.text
				fourthAuthLink.click()
				fourthAuthCheck = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='serviceContainer']/div[2]/div[3]/div[2]/table/tbody/tr[2]/td[2]/p"))).text

				if fourthAuthCheck == fourthAuthLinkText:
					results.append(("Auth Link 4", "Pass", ""))
					driver.back()
			except TimeoutException:
				results.append(("Auth Link 4", "Fail", "Element Not located After 5 Seconds"))

			try:
				fifthAuthLink = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, ".//*[@id='ctl00_MainContent_uxAuthorizationsGrid']/tbody/tr[6]/td[1]/a")))
				fifthAuthLinkText = fifthAuthLink.text
				fifthAuthLink.click()
				fifthAuthCheck = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='serviceContainer']/div[2]/div[3]/div[2]/table/tbody/tr[2]/td[2]/p"))).text

				if fifthAuthCheck == fifthAuthLinkText:
					results.append(("Auth Link 5", "Pass", ""))
					driver.back()
			except TimeoutException:
				results.append(("Auth Link 5", "Fail", "Element Not located After 5 Seconds"))

			try:
				sixthAuthLink = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, ".//*[@id='ctl00_MainContent_uxAuthorizationsGrid']/tbody/tr[7]/td[1]/a")))
				sixthAuthLinkText = sixthAuthLink.text
				sixthAuthLink.click()
				sixthAuthCheck = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='serviceContainer']/div[2]/div[3]/div[2]/table/tbody/tr[2]/td[2]/p"))).text

				if sixthAuthCheck == sixthAuthLinkText:
					results.append(("Auth Link 6", "Pass", ""))
					driver.back()
			except TimeoutException:
				results.append(("Auth Link 6", "Fail", "Element Not located After 5 Seconds"))

			try:
				seventhAuthLink = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, ".//*[@id='ctl00_MainContent_uxAuthorizationsGrid']/tbody/tr[8]/td[1]/a")))
				seventhAuthLinkText = seventhAuthLink.text
				seventhAuthLink.click()
				seventhAuthCheck = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='serviceContainer']/div[2]/div[3]/div[2]/table/tbody/tr[2]/td[2]/p"))).text

				if seventhAuthCheck == seventhAuthLinkText:
					results.append(("Auth Link 7", "Pass", ""))
					driver.back()
			except TimeoutException:
				results.append(("Auth Link 7", "Fail", "Element Not located After 5 Seconds"))

			try:
				eighthAuthLink = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, ".//*[@id='ctl00_MainContent_uxAuthorizationsGrid']/tbody/tr[9]/td[1]/a")))
				eighthAuthLinkText = eighthAuthLink.text
				eighthAuthLink.click()
				eighthAuthCheck = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='serviceContainer']/div[2]/div[3]/div[2]/table/tbody/tr[2]/td[2]/p"))).text

				if eighthAuthCheck == eighthAuthLinkText:
					results.append(("Auth Link 8", "Pass", ""))
					driver.back()
			except TimeoutException:
				results.append(("Auth Link 8", "Fail", "Element Not located After 5 Seconds"))

			try:
				ninethAuthLink = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, ".//*[@id='ctl00_MainContent_uxAuthorizationsGrid']/tbody/tr[10]/td[1]/a")))
				ninethAuthLinkText = ninethAuthLink.text
				ninethAuthLink.click()
				ninethAuthCheck = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='serviceContainer']/div[2]/div[3]/div[2]/table/tbody/tr[2]/td[2]/p"))).text

				if ninethAuthCheck == ninethAuthLinkText:
					results.append(("Auth Link 9", "Pass", ""))
					driver.back()
			except TimeoutException:
				results.append(("Auth Link 9", "Fail", "Element Not located After 5 Seconds"))

			try:
				tenthAuthLink = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, ".//*[@id='ctl00_MainContent_uxAuthorizationsGrid']/tbody/tr[11]/td[1]/a")))
				tenthAuthLinkText = tenthAuthLink.text
				tenthAuthLink.click()
				tenthAuthCheck = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='serviceContainer']/div[2]/div[3]/div[2]/table/tbody/tr[2]/td[2]/p"))).text

				if tenthAuthCheck == tenthAuthLinkText:
					results.append(("Auth Link 10", "Pass", ""))
					driver.back()
			except TimeoutException:
				results.append(("Auth Link 10", "Fail", "Element Not located After 5 Seconds"))

	print(tabulate(results, headers = ["Section", "Result", "Comment"], tablefmt="fancy_grid"))
	results = []

	try:
		WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, ".//*[@id='hxUserMenu']/li[1]/a"))).click()
	except TimeoutException:
		results.append(("Home Button", "Fail", "Element Not Located After 5 Seconds"))
		print(tabulate(results, headers = ["Section", "Result", "Comment"], tablefmt="fancy_grid"))
		driver.quit()
	else:
		results.append(("Home Button", "Pass", ""))

	##### PROVIDE SECTION #####

	print("PROVIDER SECTION")

	try:
		WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, ".//*[@id='hxUserMenu']/li[6]/a"))).click()
	except TimeoutException:
		results.append(("Provider Tool Link", "Fail", "Element Not Located After 5 Seconds"))
	else:
		results.append(("Provider Tool Link", "Pass", ""))

		try:
			WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='submitProvSearch']")))
		except TimeoutException:
			results.append(("Provider Tool", "Fail", "Page Did Not Load Properly After 5 Seconds"))
		else:
			results.append(("Provider Tool", "Pass", ""))

			WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "providerZip"))).send_keys("54601")
			time.sleep(3)
			WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "submitProvSearch"))).click()
			time.sleep(10)

			try:
				WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "resultsList")))
			except TimeoutException:
				results.append(("Provider Results", "Fail", "Element Not Located After 5 Seconds"))
			else:
				results.append(("Provider Results", "Pass", ""))

	print(tabulate(results, headers = ["Section", "Result", "Comment"], tablefmt="fancy_grid"))
	results = []

	try:
		WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, ".//*[@id='hxUserMenu']/li[1]/a"))).click()
	except TimeoutException:
		results.append(("Home Button", "Fail", "Element Not Located After 5 Seconds"))
		print(tabulate(results, headers = ["Section", "Result", "Comment"], tablefmt="fancy_grid"))
		driver.quit()
	else:
		results.append(("Home Button", "Pass", ""))

	##### WELLNESS #####

	try:
		WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, ".//*[@id='hxUserMenu']/li[7]/a"))).click()
	except TimeoutException:
		results.append(("Welness Button", "Fail", "Element Not Located After 5 Seconds"))
	else:
		results.append(("Welness Button", "Pass", ""))

		try:
			WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='serviceContainer']/div[2]")))
		except TimeoutException:
			results.append(("Wellness Page", "Fail", "Page Did Not Load Properly After 5 Seconds"))
		else:
			results.append(("Wellness Page", "Pass", ""))

	print(tabulate(results, headers = ["Section", "Result", "Comment"], tablefmt="fancy_grid"))
	results = []

	try:
		WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, ".//*[@id='hxUserMenu']/li[1]/a"))).click()
	except TimeoutException:
		results.append(("Home Button", "Fail", "Element Not Located After 5 Seconds"))
		print(tabulate(results, headers = ["Section", "Result", "Comment"], tablefmt="fancy_grid"))
		driver.quit()
	else:
		results.append(("Home Button", "Pass", ""))

	##### SIDE MENU #####

	print("SIDE MENU")

	try:
		WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.LINK_TEXT, "Print or Request an ID Card"))).click()
	except TimeoutException:
		results.append(("Side Menu Link 1", "Fail", "Element Not Located After 5 Seconds"))
	else:
		results.append(("Side Menu Link 1", "Pass", ""))

		try:
			WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='idcardtemplate']/table[1]/tbody/tr[2]/td[2]/table/tbody/tr[1]/td[1]/img")))
		except TimeoutException:
			results.append(("Side Menu Page 1", "Fail", "Page Did Not Load Properly After 5 Seconds"))
		else:
			results.append(("Side Menu Page 1", "Pass", ""))
			driver.back()

	time.sleep(1)

	try:
		WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.LINK_TEXT, "Enrollment Form"))).click()
	except TimeoutException:
		results.append(("Side Menu Link 2", "Fail", "Element Not Located After 5 Seconds"))
	else:
		results.append(("Side Menu Link 2", "Pass", ""))

		try:
			WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='ctl00_MainContent_uxForm_ctl03_uxFormSubmitButton']")))
		except TimeoutException:
			results.append(("Side Menu Page 2", "Fail", "Page Did Not Load Properly After 5 Seconds"))
		else:
			results.append(("Side Menu Page 2", "Pass", ""))
			driver.back()

	time.sleep(1)
	
	try:
		WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.LINK_TEXT, "Prescription Benefit"))).click()
	except TimeoutException:
		results.append(("Side Menu Link 3", "Fail", "Element Not Located After 5 Seconds"))
	else:
		results.append(("Side Menu Link 3", "Pass", ""))

		try:
			WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='top']/div[1]")))
		except TimeoutException:
			results.append(("Side Menu Page 3", "Fail", "External Page Not Our Problem"))
			driver.back()
		else:
			results.append(("Side Menu Page 3", "Pass", "External Page"))
			driver.back()

	time.sleep(1)
	
	try:
		WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.LINK_TEXT, "Change My PCP"))).click()
	except TimeoutException:
		results.append(("Side Menu Link 4", "Fail", "Element Not Located After 5 Seconds"))
	else:
		results.append(("Side Menu Link 4", "Pass", ""))

		try:
			sideMenuPageText = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='ctl00_MainContent_uxProviderViewControl_uxTabPanel']/div[2]/div[4]/fieldset[1]/legend"))).text

			if sideMenuPageText == "Practitioner Search":
				results.append(("Side Menu Page 4", "Pass", ""))
				driver.back()
			else:
				results.append(("Side Menu Page 4", "Fail", "Page Did Not Load Properly"))
		except TimeoutException:
			results.append(("Side Menu Page 4", "Fail", "Page Did Not Load Properly After 5 Seconds"))

	time.sleep(1)
	
	try:
		WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.LINK_TEXT, "FAQ's"))).click()
	except TimeoutException:
		results.append(("Side Menu Link 5", "Fail", "Element Not Located After 5 Seconds"))
	else:
		results.append(("Side Menu Link 5", "Pass", ""))

		try:
			WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.LINK_TEXT, "Is this website secure?")))
		except TimeoutException:
			results.append(("Side Menu Page 5", "Fail", "Element Not Located After 5 Seconds"))
		else:
			results.append(("Side Menu Page 5", "Pass", ""))
			driver.back()

	time.sleep(1)
	
	try:
		WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.LINK_TEXT, "Change Name and/or Address"))).click()
	except TimeoutException:
		results.append(("Side Menu Link 6", "Fail", "Element Not Located After 5 Seconds"))
	else:
		results.append(("Side Menu Link 6", "Pass", ""))

		try:
			WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='ctl00_MainContent_uxForm_ctl03_uxFormSubmitButton']")))
		except TimeoutException:
			results.append(("Side Menu Page 6", "Fail", "Element Not Located After 5 Seconds"))
		else:
			results.append(("Side Menu Page 6", "Pass", ""))
			driver.back()

	print(tabulate(results, headers = ["Section", "Result", "Comment"], tablefmt="fancy_grid"))
	results = []

	##### MESSAGES AND PROFILE #####

	print("MESSAGES AND PROFILE")

	try:
		WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, ".//*[@id='basicShell']/header/nav[1]/ul/li[1]/a"))).click()
	except TimeoutException:
		results.append(("Messages Button", "Fail", "Element Not Located After 5 Seconds"))
	else:
		results.append(("Messages Button", "Pass", ""))

		try:
			WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "main")))
		except TimeoutException:
			results.append(("Messages Main Page", "Fail", "Page Did Not Load Properly After 5 Seconds"))
		else:
			results.append(("Messages Main Page", "Pass", ""))

			try:
				WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, ".//*[@id='ctl00_MainContent_uxMessagingOptions']/ul/li[2]/a"))).click()
			except TimeoutException:
				results.append(("Messages Saved Page Link", "Fail", "Element Not Located After 5 Seconds"))
			else:
				results.append(("Messages Saved Page Link", "Pass", ""))

				try:
					WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='ctl00_MainContent_uxMessageGrid']/tbody/tr[2]/td[2]")))
				except TimeoutException:
					results.append(("Messages Saved Page", "Fail", "Page Did Not Load Properly After 5 Seconds"))
				else:
					results.append(("Messages Saved Page", "Pass", ""))

					try:
						WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, ".//*[@id='ctl00_MainContent_uxMessagingOptions']/ul/li[4]/a"))).click()
					except TimeoutException:
						results.append(("Messages Search Page Link", "Fail", "Element Not Located After 5 Seconds"))
					else:
						results.append(("Messages Search Page Link", "Pass", ""))

						try:
							WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.LINK_TEXT, "Tracking Number Search"))).click()
						except TimeoutException:
							results.append(("Messages Search Page", "Fail", "Element Not Located After 5 Seconds"))
						else:
							results.append(("Messages Search Page", "Pass", ""))

							try:
								WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='ctl00_MainContent_uxTrackingNumberSearchForm_ctl02_uxTrackingNumberText_textbox']"))).send_keys('3502821')
								WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, ".//*[@id='ctl00_MainContent_uxTrackingNumberSearchForm_ctl03_uxTrackingNumberSearchButton']"))).click()
							except TimeoutException:
								results.append(("Messages Search Button", "Fail", "Page Did Not Load Properly After 5 Seconds"))
							else:
								results.append(("Messages Search Button", "Pass", ""))

								try:
									messagesSearchCheck = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='ctl00_MainContent_uxInformationLabel']/b"))).text
									
									if messagesSearchCheck == "Tracking # 3502821":
										results.append(("Messages Search", "Pass", ""))
									else:
										results.append(("Messages Search", "Fail", "Search Didn't Yield Proper Results"))
								except TimeoutException:
									results.append(("Messages Search", "Fail", "Element Not Located After 5 Seconds"))
									
	try:
		WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.LINK_TEXT, "Profile"))).click()
	except TimeoutException:
		results.append(("Profile Button", "Fail", "Element Not Located After 5 Seconds"))
	else:
		results.append(("Profile Button", "Pass", ""))

		try:
			WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='ctl00_MainContent_accountInfo_TopTable_Row1_Cell1']")))
		except TimeoutException:
			results.append(("Profile Page", "Fail", "Page Did Not Load Properly After 5 Seconds"))
		else:
			results.append(("Profile Page", "Pass", ""))

	print(tabulate(results, headers = ["Section", "Result", "Comment"], tablefmt="fancy_grid"))
	results = []

	##### LOGOUT #####
	
	print("LOGOUT")

	try:
		WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.LINK_TEXT, "Logout"))).click()
	except TimeoutException:
		results.append(("Logout Button", "Fail", "Element Not Located After 5 Seconds"))
		print(tabulate(results, headers = ["Section", "Result", "Comment"], tablefmt="fancy_grid"))
		driver.quit()
	else:
		results.append(("Logout Button", "Pass", ""))

	try:
		WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "username")))
	except TimeoutException:
		results.append(("Logout", "Fail", "Element Not Located After 5 Seconds"))
	else:
		results.append(("Logout", "Pass", ""))

	print(tabulate(results, headers = ["Section", "Result", "Comment"], tablefmt="fancy_grid"))
	results = []

	end = time.time() - start
	print("\nTotal Elapsed Test Time %.2f" % end)

	output.close()
	sys.stdout = sys.__stdout__
	driver.quit()

main()