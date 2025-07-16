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
scriptPath = os.path.dirname(userProfile + '\\Desktop\\Demosite Automation\\ProviderDemo\\FirefoxLogs\\')
outputFile = os.path.join(scriptPath, "provider_demosite_automation_firefox_hxweb06_" + time.strftime("%m-%d-%H-%M") + ".log")
output = open(outputFile, 'w', encoding='utf-8')
sys.stdout = output

def main():
	#driver = webdriver.Chrome(executable_path='C:\Python34\Scripts\chromedriver.exe')
	driver = webdriver.Firefox()
	#driver = webdriver.Ie(executable_path='C:\Python34\Scripts\IEDriverServer.exe')

	results = []

	start = time.time()
	driver.get('https://hxweb06.healthx.com/provider_template.aspx')

	print("Firefox - hxweb06\n")
	print("LOGIN")

	try:
		driver.find_element_by_id("username").send_keys('plan.provider.template')
	except NoSuchElementException:
		print("Login Not Found")
		driver.quit()

	try:
		driver.find_element_by_name("password").send_keys('american')
	except NoSuchElementException:
		print("Password Not Found")
		driver.quit()

	try:
		driver.find_element_by_id("loginButton").click()
	except NoSuchElementException:
		print("Login Button Not Found")
		driver.quit()

	time.sleep(4)

	try:
		viewAllPatientsLink = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.LINK_TEXT, "View All Patients")))
	except TimeoutException:
		results.append(("Login", "Fail", "Page Didn't Load Properly"))
		results.append(("Provider Dashboard", "Fail", "Element Not Located After 5 Seconds"))
		print(tabulate(results, headers = ["Section", "Result", "Comment"], tablefmt="fancy_grid"))
		results = []
	else:
		results.append(("Login", "Pass", ""))
		results.append(("Provider Dashboard", "Pass", ""))

	print(tabulate(results, headers = ["Section", "Result", "Comment"], tablefmt="fancy_grid"))
	results = []

	########## ELIGIBILITY SECTION ##########

	print("ELIGIBILITY SECTION")

	viewAllPatientsLink.click()

	try:
		WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "eligSearchHeader")))
	except TimeoutException:
		results.append(("Eligibility Header", "Fail", "Element Not Located After 5 Seconds"))
		driver.find_element_by_xpath(".//*[@id='hxUserMenu']/li[1]/a").click()
	else:
		results.append(("Eligibility Header", "Pass", ""))

		try:
			firstEligLink = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, ".//*[@id='aspnetForm']/div[5]/div[2]/div/table/tbody/tr[2]/td[1]/p/a")))
		except TimeoutException:
			results.append(("Elig Link 1", "Fail", "Link Not Found After 5 Seconds"))
		else:
			firstEligLinkText = driver.find_element_by_xpath(".//*[@id='aspnetForm']/div[5]/div[2]/div/table/tbody/tr[2]/td[4]/p").text
			firstEligLink.click()

			try:
				firstEligCheck = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='aspnetForm']/div[5]/div[3]/div[3]/div[3]/div[1]/table[1]/tbody/tr[4]/td[4]"))).text
				
				if firstEligCheck == firstEligLinkText:
					results.append(("Elig Link 1", "Pass", ""))
					driver.back()
				else:
					results.append(("Elig Link 1", "Fail", "Link Went To Incorrect Page"))
			except TimeoutException:
				results.append(("Elig Link 1", "Fail", "Link Didn't Go To Correct Page"))
				driver.back()

		time.sleep(2)

		try:
			secondEligLink = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, ".//*[@id='aspnetForm']/div[5]/div[2]/div/table/tbody/tr[3]/td[1]/p/a")))
		except TimeoutException:
			results.append(("Elig Link 2", "Fail", "Link Not Found After 5 Seconds"))
		else:
			secondEligLinkText = driver.find_element_by_xpath(".//*[@id='aspnetForm']/div[5]/div[2]/div/table/tbody/tr[3]/td[4]/p").text
			secondEligLink.click()
			time.sleep(3)

			try:
				secondEligCheck = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='aspnetForm']/div[5]/div[3]/div[3]/div[3]/div[1]/table[1]/tbody/tr[4]/td[4]"))).text
				
				if secondEligCheck == secondEligLinkText:
					results.append(("Elig Link 2", "Pass", ""))
					driver.back()
				else:
					results.append(("Elig Link 2", "Fail", "Link Went To Incorrect Page"))
			except TimeoutException:
				results.append(("Elig Link 2", "Fail", "Link Didn't Go To Correct Page"))
				driver.back()

		time.sleep(2)
		
		try:
			thirdEligLink = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, ".//*[@id='aspnetForm']/div[5]/div[2]/div/table/tbody/tr[4]/td[1]/p/a")))
		except TimeoutException:
			results.append(("Elig Link 3", "Fail", "Link Not Found After 5 Seconds"))
		else:
			thirdEligLinkText = driver.find_element_by_xpath(".//*[@id='aspnetForm']/div[5]/div[2]/div/table/tbody/tr[4]/td[4]/p").text
			thirdEligLink.click()
			time.sleep(3)

			try:
				thirdEligCheck = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='aspnetForm']/div[5]/div[3]/div[3]/div[3]/div[1]/table[1]/tbody/tr[4]/td[4]"))).text
				if thirdEligCheck == thirdEligLinkText:
					results.append(("Elig Link 3", "Pass", ""))
					driver.back()
				else:
					results.append(("Elig Link 3", "Fail", "Link Went To Incorrect Page"))
			except TimeoutException:
				results.append(("Elig Link 3", "Fail", "Link Didn't Go To Correct Page"))
				driver.back()

		time.sleep(2)
		
		try:
			fourthEligLink = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, ".//*[@id='aspnetForm']/div[5]/div[2]/div/table/tbody/tr[5]/td[1]/p/a")))
		except TimeoutException:
			results.append(("Elig Link 4", "Fail", "Link Not Found After 5 Seconds"))
		else:
			fourthEligLinkText = driver.find_element_by_xpath(".//*[@id='aspnetForm']/div[5]/div[2]/div/table/tbody/tr[5]/td[4]/p").text
			fourthEligLink.click()
			time.sleep(3)

			try:
				fourthEligCheck = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='aspnetForm']/div[5]/div[3]/div[3]/div[3]/div[1]/table[1]/tbody/tr[4]/td[4]"))).text
				if fourthEligCheck == fourthEligLinkText:
					results.append(("Elig Link 4", "Pass", ""))
					driver.back()
				else:
					results.append(("Elig Link 4", "Fail", "Link Went To Incorrect Page"))
			except TimeoutException:
				results.append(("Elig Link 4", "Fail", "Link Didn't Go To Correct Page"))
				driver.back()

		time.sleep(2)

		try:
			fifthEligLink = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, ".//*[@id='aspnetForm']/div[5]/div[2]/div/table/tbody/tr[6]/td[1]/p/a")))
		except TimeoutException:
			results.append(("Elig Link 5", "Fail", "Link Not Found After 5 Seconds"))
		else:
			fifthEligLinkText = driver.find_element_by_xpath(".//*[@id='aspnetForm']/div[5]/div[2]/div/table/tbody/tr[6]/td[4]/p").text
			fifthEligLink.click()
			time.sleep(3)

			try:
				fifthEligCheck = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='aspnetForm']/div[5]/div[3]/div[3]/div[3]/div[1]/table[1]/tbody/tr[4]/td[4]"))).text
				if fifthEligCheck == fifthEligLinkText:
					results.append(("Elig Link 5", "Pass", ""))
					driver.back()
				else:
					results.append(("Elig Link 5", "Fail", "Link Went To Incorrect Page"))
			except TimeoutException:
				results.append(("Elig Link 5", "Fail", "Link Didn't Go To Correct Page"))
				driver.back()

		time.sleep(3)
		
		try:
			sixthEligLink = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, ".//*[@id='aspnetForm']/div[5]/div[2]/div/table/tbody/tr[7]/td[1]/p/a")))
		except TimeoutException:
			results.append(("Elig Link 6", "Fail", "Link Not Found After 5 Seconds"))
		else:
			sixthEligLinkText = driver.find_element_by_xpath(".//*[@id='aspnetForm']/div[5]/div[2]/div/table/tbody/tr[7]/td[4]/p").text
			sixthEligLink.click()
			time.sleep(4)

			try:
				sixthEligCheck = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='aspnetForm']/div[5]/div[3]/div[3]/div[3]/div[1]/table[1]/tbody/tr[4]/td[4]"))).text
				if sixthEligCheck == sixthEligLinkText:
					results.append(("Elig Link 6", "Pass", ""))
					driver.back()
				else:
					results.append(("Elig Link 6", "Fail", "Link Went To Incorrect Page"))
			except TimeoutException:
				results.append(("Elig Link 6", "Fail", "Link Didn't Go To Correct Page"))
				driver.back()

		time.sleep(3)
		
		try:
			seventhEligLink = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, ".//*[@id='aspnetForm']/div[5]/div[2]/div/table/tbody/tr[8]/td[1]/p/a")))
		except TimeoutException:
			results.append(("Elig Link 7", "Fail", "Link Not Found After 5 Seconds"))
		else:
			seventhEligLinkText = driver.find_element_by_xpath(".//*[@id='aspnetForm']/div[5]/div[2]/div/table/tbody/tr[8]/td[4]/p").text
			seventhEligLink.click()
			time.sleep(4)

			try:
				seventhEligCheck = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='aspnetForm']/div[5]/div[3]/div[3]/div[3]/div[1]/table[1]/tbody/tr[4]/td[4]"))).text
				if seventhEligCheck == seventhEligLinkText:
					results.append(("Elig Link 7", "Pass", ""))
					driver.back()
				else:
					results.append(("Elig Link 7", "Fail", "Link Went To Incorrect Page"))
			except TimeoutException:
				results.append(("Elig Link 7", "Fail", "Link Didn't Go To Correct Page"))
				driver.back()

		time.sleep(3)
		
		try:
			eighthEligLink = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, ".//*[@id='aspnetForm']/div[5]/div[2]/div/table/tbody/tr[9]/td[1]/p/a")))
		except TimeoutException:
			results.append(("Elig Link 8", "Fail", "Link Not Found After 5 Seconds"))
		else:
			eighthEligLinkText = driver.find_element_by_xpath(".//*[@id='aspnetForm']/div[5]/div[2]/div/table/tbody/tr[9]/td[4]/p").text
			eighthEligLink.click()
			time.sleep(4)

			try:
				eighthEligCheck = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='aspnetForm']/div[5]/div[3]/div[3]/div[3]/div[1]/table[1]/tbody/tr[4]/td[4]"))).text
				if eighthEligCheck == eighthEligLinkText:
					results.append(("Elig Link 8", "Pass", ""))
					driver.back()
				else:
					results.append(("Elig Link 8", "Fail", "Link Went To Incorrect Page"))
			except TimeoutException:
				results.append(("Elig Link 8", "Fail", "Link Didn't Go To Correct Page"))
				driver.back()

		time.sleep(3)
		
		try:
			ninethEligLink = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, ".//*[@id='aspnetForm']/div[5]/div[2]/div/table/tbody/tr[10]/td[1]/p/a")))
		except TimeoutException:
			results.append(("Elig Link 9", "Fail", "Link Not Found After 5 Seconds"))
		else:
			ninethEligLinkText = driver.find_element_by_xpath(".//*[@id='aspnetForm']/div[5]/div[2]/div/table/tbody/tr[10]/td[4]/p").text
			ninethEligLink.click()
			time.sleep(4)

			try:
				ninethEligCheck = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='aspnetForm']/div[5]/div[3]/div[3]/div[3]/div[1]/table[1]/tbody/tr[4]/td[4]"))).text
				if ninethEligCheck == ninethEligLinkText:
					results.append(("Elig Link 9", "Pass", ""))
					driver.back()
				else:
					results.append(("Elig Link 9", "Fail", "Link Went To Incorrect Page"))
			except TimeoutException:
				results.append(("Elig Link 9", "Fail", "Link Didn't Go To Correct Page"))
				driver.back()

		try:
			WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "memberID"))).send_keys('11111111100')
		except TimeoutException:
			results.append(("Elig Search", "Fail", "Search Box Not Found After 5 Seconds"))
		else:
			driver.find_element_by_xpath(".//*[@id='aspnetForm']/div[5]/div[1]/div[1]/div/div[6]/button").click()
			time.sleep(3)
			eligSearchCheck = driver.find_element_by_xpath(".//*[@id='aspnetForm']/div[5]/div[2]/div/table/tbody/tr[2]/td[4]/p").text

			if eligSearchCheck == '11111111100':
				results.append(("Elig Search", "Pass", ""))
			else:
				results.append(("Elig Search", "Fail", "Search Resulted In Incorrect Account"))


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

	########## NEWSLETTER ITEM ##########

	time.sleep(3)

	try:
		WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.LINK_TEXT, "Spring Newsletter")))
	except NoSuchElementException:
		results.append(("Newsletter Content Item", "Fail", "Element Not Located After 5 Seconds"))
	else:
		results.append(("Newsletter Content Item", "Pass", ""))

	########## PAYMENTS SECTION ##########

	print("NEWSLETTER/PAYMENTS SECTION")
	
	try:
		WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='hxUserMenu']/li[3]/a"))).click()
		WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='svc_132fe0b2-1ce3-484a-adeb-4272ae2b374f']/a"))).click()
	except TimeoutException:
		results.append(("Payments Link", "Fail", "Element Not Located After 5 Seconds"))
	else:
		results.append(("Payments Link", "Pass", ""))

		time.sleep(1)

		try:
			WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='aspnetForm']/div[3]/div[1]/div/div[4]/button"))).click()
		except TimeoutException:
			results.append(("Payments Search Button", "Fail", "Element Not Located After 5 Seconds"))
		else:
			results.append(("Payments Search Button", "Pass", ""))

			time.sleep(1)

			try:
				WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='aspnetForm']/div[3]/div[2]/div/table/tbody/tr[2]/td[1]")))
			except TimeoutException:
				results.append(("Payments Search Results", "Fail", "Results Not Found After 5 Seconds"))
			else:
				results.append(("Payments Search Results", "Pass", ""))

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

	########## CLAIMS SECTION ##########

	print("CLAIMS SECTION")
	
	try:
		WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, ".//*[@id='hxUserMenu']/li[4]/a"))).click()
	except TimeoutException:
		results.append(("Claims Button", "Fail", "Element Not Located After 5 Seconds"))
		print(tabulate(results, headers = ["Section", "Result", "Comment"], tablefmt="fancy_grid"))
		driver.quit()
	else:
		results.append(("Claims Button", "Pass", ""))

		time.sleep(1)

		try:
			WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "claimNumbers"))).send_keys('N636186001')
		except TimeoutException:
			results.append(("Claims Search", "Fail", "Element Not Located After 5 Seconds"))
		else:
			results.append(("Claims Search", "Pass", ""))

			time.sleep(1)

			try:
				WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "searchControl")))
			except TimeoutException:
				results.append(("Claims Search Button", "Fail", "Element Not Located After 5 Seconds"))
			else:
				results.append(("Claims Search Button", "Pass", ""))

				time.sleep(1)

				try:
					WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.LINK_TEXT, "N636186001"))).click()
				except TimeoutException:
					results.append(("Claims Search Results", "Fail", "Results Didn't Load"))
				else:
					results.append(("Claims Search Results", "Pass", ""))

					time.sleep(1)

					try:
						claimsSearchCheck = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='viewArea']/div[1]/div/h3"))).text

						if claimsSearchCheck == "Claim #N636186001":
							results.append(("Claims Search Results Page", "Pass", ""))
						else:
							results.append(("Claims Search Results Page", "Fail", "Search Resulted In Incorrect Claim"))
					except TimeoutException:
						results.append(("Claims Search Results Page", "Fail", "Element Not Located After 5 Seconds"))

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

	########## AUTHORIZATIONS SECTION ##########

	print("AUTHORIZATIONS SECTION")
	
	try:
		WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, ".//*[@id='hxUserMenu']/li[5]/a"))).click()
	except TimeoutException:
		results.append(("Auth Button", "Fail", "Element Not Located After 5 Seconds"))
		print(tabulate(results, headers = ["Section", "Result", "Comment"], tablefmt="fancy_grid"))
		driver.quit()
	else:
		results.append(("Auth Button", "Pass", ""))

		time.sleep(3)

		try:
			WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "searchControl"))).click()
		except TimeoutException:
			results.append(("Auth Search Button", "Fail", "Element Not Located After 5 Seconds"))
		else:
			results.append(("Auth Search Button", "Pass", ""))

			time.sleep(1)

			try:
				authResultsLink = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='resultContainer']/table/tbody/tr[2]/td[1]/p/a")))
				authResultsLinkText = authResultsLink.text
				authResultsLink.click()
			except TimeoutException:
				results.append(("Auth Search Results", "Fail", "Results Didn't Load"))
			else:
				results.append(("Auth Search Results", "Pass", ""))

				driver.switch_to_active_element()

				time.sleep(1)

				try:
					authResultsCheck = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='viewArea']/table[1]/tbody/tr/td[2]"))).text

					if authResultsCheck == authResultsLinkText:
						results.append(("Auth Search Results Page", "Pass", ""))
					else:
						results.append(("Auth Search Results Page", "Fail", "Search Resulted In Incorrect Claim"))
				except TimeoutException:
					results.append(("Auth Search Results Page", "Fail", "Element Not Located After 5 Seconds"))

				time.sleep(1)

				try:
					driver.find_element_by_xpath("html/body/div[4]/div[1]/a").click()
				except NoSuchElementException:
					results.append(("Exit Button", "Fail", "Element Not Located"))
					print(tabulate(results, headers = ["Section", "Result", "Comment"], tablefmt="fancy_grid"))
					driver.quit()

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

	########## CARE PLAN ##########

	print("CARE PLAN")
	
	try:
		WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, ".//*[@id='hxUserMenu']/li[6]/a"))).click()
	except TimeoutException:
		results.append(("Care Plan Button", "Fail", "Element Not Located After 5 Seconds"))
		print(tabulate(results, headers = ["Section", "Result", "Comment"], tablefmt="fancy_grid"))
		driver.quit()
	else:
		results.append(("Care Plan Button", "Pass", ""))

		time.sleep(1)

		try:
			WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "memberID"))).send_keys('11111111100')
			WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "dob"))).send_keys('01/05/1962')
		except TimeoutException:
			results.append(("Care Plan Data Fields", "Fail", "Element Not Located After 5 Seconds"))
		else:
			results.append(("Care Plan Data Fields", "Pass", ""))

			time.sleep(1)

			try:
				WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "submit"))).click()
			except TimeoutException:
				results.append(("Care Plan Search", "Fail", "Element Not Located After 5 Seconds"))
			else:
				results.append(("Care Plan Search", "Pass", ""))

				time.sleep(1)

				try:
					carePlanResults = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "memberID_detail"))).text

					if carePlanResults == '11111111100':
						results.append(("Care Plan Results", "Pass", ""))
					else:
						results.append(("Care Plan Results", "Fail", "Incorrect Search Results"))
				except TimeoutException:
					results.append(("Care Plan Results", "Fail", "Element Not Located After 5 Seconds"))

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
				WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, ".//*[@id='ctl00_MainContent_uxMessagingOptions']/ul/li[3]/a"))).click()
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
								WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='ctl00_MainContent_uxTrackingNumberSearchForm_ctl02_uxTrackingNumberText_textbox']"))).send_keys('3529347')
								WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, ".//*[@id='ctl00_MainContent_uxTrackingNumberSearchForm_ctl03_uxTrackingNumberSearchButton']"))).click()
							except TimeoutException:
								results.append(("Messages Search Button", "Fail", "Page Did Not Load Properly After 5 Seconds"))
							else:
								results.append(("Messages Search Button", "Pass", ""))

								try:
									messagesSearchCheck = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='ctl00_MainContent_uxInformationLabel']/b"))).text
									
									if messagesSearchCheck == "Tracking # 3529347":
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

	try:
		WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, ".//*[@id='hxUserMenu']/li[1]/a"))).click()
	except TimeoutException:
		results.append(("Home Button", "Fail", "Element Not Located After 5 Seconds"))
		print(tabulate(results, headers = ["Section", "Result", "Comment"], tablefmt="fancy_grid"))
		driver.quit()
	else:
		results.append(("Home Button", "Pass", ""))

	print(tabulate(results, headers = ["Section", "Result", "Comment"], tablefmt="fancy_grid"))
	results = []

	##### SIDE MENU #####

	print("Side Menu")

	try:
		WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.LINK_TEXT, "News & Bulletins"))).click()
	except TimeoutException:
		results.append(("Side Menu Link 1", "Fail", "Element Not Located After 5 Seconds"))
	else:
		results.append(("Side Menu Link 1", "Pass", ""))

		try:
			WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.LINK_TEXT, "Spring  Newsletter")))
		except TimeoutException:
			results.append(("Side Menu Page 1", "Fail", "Page Did Not Load Properly After 5 Seconds"))
		else:
			results.append(("Side Menu Page 1", "Pass", ""))

		driver.back()

	results.append(("Side Menu Link 2", "Skipped", "Unabled to Automate"))

	try:
		WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.LINK_TEXT, "Credentialing"))).click()
	except TimeoutException:
		results.append(("Side Menu Link 3", "Fail", "Element Not Located After 5 Seconds"))
	else:
		results.append(("Side Menu Link 3", "Pass", ""))

		try:
			WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.LINK_TEXT, "Online Facility Credentialing Application")))
		except TimeoutException:
			results.append(("Side Menu Page 3", "Fail", "Page Did Not Load Properly After 5 Seconds"))
		else:
			results.append(("Side Menu Page 3", "Pass", ""))

		driver.back()

	try:
		WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.LINK_TEXT, "Formulary"))).click()
	except TimeoutException:
		results.append(("Side Menu Link 4", "Fail", "Element Not Located After 5 Seconds"))
	else:
		results.append(("Side Menu Link 4", "Pass", ""))

		try:
			WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.LINK_TEXT, "Specialty Medication Prior Authorization")))
		except TimeoutException:
			results.append(("Side Menu Page 4", "Fail", "Page Did Not Load Properly After 5 Seconds"))
		else:
			results.append(("Side Menu Page 4", "Pass", ""))

		driver.back()

	try:
		WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.LINK_TEXT, "Provider Directory"))).click()
	except TimeoutException:
		results.append(("Side Menu Link 5", "Fail", "Element Not Located After 5 Seconds"))
	else:
		results.append(("Side Menu Link 5", "Pass", ""))

		try:
			WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='submitProvSearch']")))
		except TimeoutException:
			results.append(("Provider Tool", "Fail", "Page Did Not Load Properly After 5 Seconds"))
		else:
			results.append(("Provider Tool", "Pass", ""))

			WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "providerZip"))).send_keys("54601")
			time.sleep(4)
			WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "submitProvSearch"))).click()
			time.sleep(10)

			try:
				WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "resultsList")))
			except TimeoutException:
				results.append(("Provider Results", "Fail", "Element Not Located After 5 Seconds"))
			else:
				results.append(("Provider Results", "Pass", ""))

				try:
					WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, ".//*[@id='hxUserMenu']/li[1]/a"))).click()
				except TimeoutException:
					results.append(("Home Button", "Fail", "Element Not Located After 5 Seconds"))
					print(tabulate(results, headers = ["Section", "Result", "Comment"], tablefmt="fancy_grid"))
					driver.quit()
				else:
					results.append(("Home Button", "Pass", ""))

	try:
		WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.LINK_TEXT, "Provider Manual"))).click()
	except TimeoutException:
		results.append(("Side Menu Link 6", "Fail", "Element Not Located After 5 Seconds"))
	else:
		results.append(("Side Menu Link 6", "Pass", ""))

		try:
			WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.LINK_TEXT, "here")))
		except TimeoutException:
			results.append(("Side Menu Page 6", "Fail", "Page Did Not Load Properly After 5 Seconds"))
		else:
			results.append(("Side Menu Page 6", "Pass", ""))

		driver.back()

	results.append(("Side Menu Link 7", "Skipped", "Unable to Automate"))

	try:
		WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.LINK_TEXT, "Frequently Asked Questions"))).click()
	except TimeoutException:
		results.append(("Side Menu Link 8", "Fail", "Element Not Located After 5 Seconds"))
	else:
		results.append(("Side Menu Link 8", "Pass", ""))

		try:
			WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.LINK_TEXT, "Here")))
		except TimeoutException:
			results.append(("Side Menu Page 8", "Fail", "Page Did Not Load Properly After 5 Seconds"))
		else:
			results.append(("Side Menu Page 8", "Pass", ""))

		driver.back()

	results.append(("Side Menu Link 9", "Skipped", "Repeat of Profile Test"))

	print(tabulate(results, headers = ["Section", "Result", "Comment"], tablefmt="fancy_grid"))
	results = []

	##### LOGOUT #####

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