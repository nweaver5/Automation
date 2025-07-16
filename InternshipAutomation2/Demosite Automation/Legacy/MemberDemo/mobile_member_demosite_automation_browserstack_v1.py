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

def main():
	'''cont = True

	while (cont):
		operSys = input("Enter 1 for iOS or 2 for Android: ")

		if operSys == "1":
			print("1 = iPhone 5 with iOS 6.1")
			print("2 = iPhone 5s with iOS 7")
			print("3 = iPad Air with iOS 7")
			browser = input("Enter desired device: ")

			if browser == "1":
				desired_cap = {'browserName': 'iPhone', 'platform': 'MAC', 'device': 'iPhone 5'}
				print("iPhone 5/iOS 6.1 - HX Mobile Member Demo\n")
				cont = False
			elif browser == "2":
				desired_cap = {'browserName': 'iPhone', 'platform': 'MAC', 'device': 'iPhone 5S'}
				print("iPhone 5s/iOS 7 - HX Mobile Member Demo\n")
				cont = False
			elif browser == "3":
				desired_cap = {'browserName': 'iPad', 'platform': 'MAC', 'device': 'iPad Air'}
				print("iPad Air/iOS 7 - HX Mobile Member Demo\n")
				cont = False
			else:
				print("Invalid Input")

		elif operSys == "2":
			print("1 = Galaxy S5 with Android 4.4")
			print("2 = Galaxy S4 with Android 4.3")
			print("3 = Galaxy S3 with Android 4.1")
			print("4 = HTC One M8 with Android 4.4")
			print("5 = Motorola Razr with Android 4.0")
			print("6 = Sony Xperia Tipo with Android 4.0")
			print("7 = Nexus 7 with Android 4.1")
			print("8 = Nexus 5 with Android 5.0")
			print("9 = Nexus 4 with Android 4.2")
			print("10 = Kindle Fire HDX 7 with Android 4.3")
			print("11 = Galaxy Tab 4 10.1 with Android 4.4")
			browser = input("Enter desired device: ")

			if browser == "1":
				desired_cap = {'browserName': 'android', 'platform': 'ANDROID', 'device': 'Samsung Galaxy S5'}
				print("Galaxy S5/Android 4.4 - HX Mobile Member Demo\n")
				cont = False
			elif browser == "2":
				desired_cap = {'browserName': 'android', 'platform': 'ANDROID', 'device': 'Samsung Galaxy S4'}
				print("Galaxy S4/Android 4.3 - HX Mobile Member Demo\n")
				cont = False
			elif browser == "3":
				desired_cap = {'browserName': 'android', 'platform': 'ANDROID', 'device': 'Samsung Galaxy S3'}
				print("Galaxy S3/Android 4.1 - HX Mobile Member Demo\n")
				cont = False
			elif browser == "4":
				desired_cap = {'browserName': 'android', 'platform': 'ANDROID', 'device': 'HTC One M8'}
				print("HTC One M8/Android 4.4 - HX Mobile Member Demo\n")
				cont = False
			elif browser == "5":
				desired_cap = {'browserName': 'android', 'platform': 'ANDROID', 'device': 'Motorola Razr'}
				print("Motorola Razr/Android 4.0 - HX Mobile Member Demo\n")
				cont = False
			elif browser == "6":
				desired_cap = {'browserName': 'android', 'platform': 'ANDROID', 'device': 'Sony Xperia Tipo'}
				print("Sony Xperia Tipo/Android 4.0 - HX Mobile Member Demo\n")
				cont = False
			elif browser == "7":
				desired_cap = {'browserName': 'android', 'platform': 'ANDROID', 'device': 'Google Nexus 7'}
				print("Nexus 7/Android 4.1 - HX Mobile Member Demo\n")
				cont = False
			elif browser == "8":
				desired_cap = {'browserName': 'android', 'platform': 'ANDROID', 'device': 'Google Nexus 5'}
				print("Nexus 5/Android 5.0 - HX Mobile Member Demo\n")
				cont = False
			elif browser == "9":
				desired_cap = {'browserName': 'android', 'platform': 'ANDROID', 'device': 'Google Nexus 4'}
				print("Nexus 4/Android 4.2 - HX Mobile Member Demo\n")
				cont = False
			elif browser == "10":
				desired_cap = {'browserName': 'android', 'platform': 'ANDROID', 'device': 'Amazon Kindle Fire HDX 7'}
				print("Kindle Fire HDX 7/Android 4.3 - HX Mobile Member Demo\n")
				cont = False
			elif browser == "11":
				desired_cap = {'browserName': 'android', 'platform': 'ANDROID', 'device': 'Samsung Galaxy Tab 4 10.1'}
				print("Galaxy Tab 4 10.1/Android 4.4 - HX Mobile Member Demo\n")
				cont = False
				safari = True
			else:
				print("Invalid Input")
		else:
			print("Invalid Input")'''

	outputFile = ("BStackLogs\\mobile_member_demosite_automation_browserstack_" + time.strftime("%m-%d-%H-%M") + ".log")
	output = open(outputFile, 'w', encoding='utf-8')
	sys.stdout = output

	#driver = webdriver.Remote(command_executor='http://nickweaver1:xdWSmwPJzazSzVFTBhvb@hub.browserstack.com:80/wd/hub', desired_capabilities=desired_cap)
	driver = webdriver.Chrome(executable_path='C:\Python34\Scripts\chromedriver.exe')
	#driver = webdriver.Firefox()
	#driver = webdriver.Ie(executable_path='C:\Python34\Scripts\IEDriverServer.exe')

	results = []

	start = time.time()
	driver.get('https://secure.healthx.com/mobile/login.aspx?bc=c194e884-5276-461b-85aa-039d0cf6601a&serviceid=eea79cb5-b7b8-4555-943f-f466ce51b7b0')

	print("LOGIN")

	try:
		driver.find_element_by_id("txtUserName").send_keys('plan.member14')
	except NoSuchElementException:
		print("Login Not Found")
		driver.quit()

	try:
		driver.find_element_by_name("txtPassword").send_keys('American1')
	except NoSuchElementException:
		print("Password Not Found")
		driver.quit()

	try:
		driver.find_element_by_id("loginbutton").click()
	except NoSuchElementException:
		print("Login Button Not Found")
		driver.quit()

	time.sleep(5)

	try:
		driver.find_element_by_xpath(".//*[@id='ServicesMenu']/li[1]/a")
	except NoSuchElementException:
		results.append(("Login", "Fail", "Login Unsuccessful"))
		print(tabulate(results, headers = ["Section", "Result", "Comment"], tablefmt="fancy_grid"))
		driver.quit()

	##### SUMMARY #####

	print("SUMMARY")

	try:
		WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='ServicesMenu']/li[1]/a"))).click()
	except TimeoutException:
		results.append(("Summary", "Fail", "Element Not Located After 5 Seconds"))
	else:
		results.append(("Summary", "Pass", ""))

		try:
			memberId = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='SummaryDetail_e4a0233f-3e9c-4709-8ed8-98c1b7955fd8']/div/ul[1]/li/table/tbody/tr[1]/td[2]/label"))).text

			if memberId == '11111111100':
				results.append(("Member ID", "Pass", ""))
			else:
				results.append(("Member ID", "Fail", "Incorrect Member ID"))
		except TimeoutException:
			results.append(("Member ID", "Fail", "Element Not Located After 5 Seconds"))

		try:
			planId = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='SummaryDetail_e4a0233f-3e9c-4709-8ed8-98c1b7955fd8']/div/ul[2]/li[2]/table/tbody/tr[2]/td[2]/label"))).text

			if planId == '111111110':
				results.append(("Plan ID", "Pass", ""))
			else:
				results.append(("Plan ID", "Fail", "Incorrect Member ID"))
		except TimeoutException:
			results.append(("Plan ID", "Fail", "Element Not Located After 5 Seconds"))

		try:
			memberDropDown = Select(driver.find_element_by_xpath(".//*[@id='dd_MemberName_e4a0233f-3e9c-4709-8ed8-98c1b7955fd8']"))
			memberDropDown.select_by_visible_text("Elizabeth Jones")
		except NoSuchElementException:
			results.append(("Drop Down", "Fail", "Element Not Found"))
		else:
			results.append(("Drop Down", "Pass", ""))

			time.sleep(10)

			try:
				elizError = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='SummaryDetail_e4a0233f-3e9c-4709-8ed8-98c1b7955fd8']"))).text

				if elizError == "ErrorfalseUnknown error":
					results.append(("Elizabeth Jones Page", "Pass", ""))
				else:
					results.append(("Elizabeth Jones Page", "Fail", "Error Message Not Found"))
			except TimeoutException:
				results.append(("Elizabeth Jones Page", "Fail", "Page Did Not Load Properly"))

	driver.back()

	print(tabulate(results, headers = ["Section", "Result", "Comment"], tablefmt="fancy_grid"))
	results = []

	print("ID CARD")

	##### ID CARD #####

	time.sleep(2)

	try:
		WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='ServicesMenu']/li[2]/a"))).click()
	except TimeoutException:
		results.append(("ID Card", "Fail", "Element Not Located After 5 Seconds"))
	else:
		results.append(("ID Card", "Pass", ""))

		time.sleep(10)

		try:
			WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='IDCardFront_07fe206a-44a4-4e5e-ad71-4ab1fd84cd9d']")))
		except TimeoutException:
			results.append(("ID Front", "Fail", "Element Not Located After 5 Seconds"))
		else:
			results.append(("ID Front", "Pass", ""))

		try:
			WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='IDCardBack_07fe206a-44a4-4e5e-ad71-4ab1fd84cd9d']")))
		except TimeoutException:
			results.append(("ID Back", "Fail", "Element Not Located After 5 Seconds"))
		else:
			results.append(("ID Back", "Pass", ""))

	driver.back()

	print(tabulate(results, headers = ["Section", "Result", "Comment"], tablefmt="fancy_grid"))
	results = []

	time.sleep(2)

	print("CLAIMS")

	##### CLAIMS #####

	try:
		WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='ServicesMenu']/li[3]/a"))).click()
	except TimeoutException:
		results.append(("Claims", "Fail", "Element Not Located After 5 Seconds"))
	else:
		results.append(("Claims", "Pass", ""))

		time.sleep(5)

		try:
			driver.find_element_by_xpath(".//*[@id='ClaimsList_88fd36ba-5c4f-437f-b9d3-9875d7515438']/li[2]/a")
			driver.find_element_by_xpath(".//*[@id='ClaimsList_88fd36ba-5c4f-437f-b9d3-9875d7515438']/li[3]/a")
			driver.find_element_by_xpath(".//*[@id='ClaimsList_88fd36ba-5c4f-437f-b9d3-9875d7515438']/li[4]/a")
			driver.find_element_by_xpath(".//*[@id='ClaimsList_88fd36ba-5c4f-437f-b9d3-9875d7515438']/li[5]/a")
			driver.find_element_by_xpath(".//*[@id='ClaimsList_88fd36ba-5c4f-437f-b9d3-9875d7515438']/li[6]/a")
			driver.find_element_by_xpath(".//*[@id='ClaimsList_88fd36ba-5c4f-437f-b9d3-9875d7515438']/li[7]/a")
			driver.find_element_by_xpath(".//*[@id='ClaimsList_88fd36ba-5c4f-437f-b9d3-9875d7515438']/li[8]/a")
			driver.find_element_by_xpath(".//*[@id='ClaimsList_88fd36ba-5c4f-437f-b9d3-9875d7515438']/li[9]/a")
			driver.find_element_by_xpath(".//*[@id='ClaimsList_88fd36ba-5c4f-437f-b9d3-9875d7515438']/li[10]/a")
			driver.find_element_by_xpath(".//*[@id='ClaimsList_88fd36ba-5c4f-437f-b9d3-9875d7515438']/li[11]/a")
		except NoSuchElementException:
			results.append(("Claims Results", "Fail", "Not All 10 Results Found"))
		else:
			results.append(("Claims Results", "Pass", ""))

		try:
			driver.find_element_by_xpath(".//*[@id='ClaimsList_88fd36ba-5c4f-437f-b9d3-9875d7515438']/li[3]/a").click()
		except NoSuchElementException:
			results.append(("Claims Link", "Fail", "Claim Not Found"))
		else:
			results.append(("Claims Link", "Pass", ""))

			try:
				claimsCheck = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='ClaimView_88fd36ba-5c4f-437f-b9d3-9875d7515438']/div/h2[1]"))).text

				if claimsCheck == "Claim N636186001":
					results.append(("Claims Page", "Pass", ""))
					driver.back()
				else:
					results.append(("Claims Page", "Fail", "Incorrect Claim Loaded"))
					driver.back()
			except TimeoutException:
				results.append(("Claims Page", "Fail", "Element Not Located After 5 Seconds"))

	
	driver.back()

	print(tabulate(results, headers = ["Section", "Result", "Comment"], tablefmt="fancy_grid"))
	results = []

	time.sleep(2)

	print("MESSAGING")

	##### MESSAGING #####

	try:
		WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='ServicesMenu']/li[5]/a"))).click()
	except TimeoutException:
		results.append(("Messaging", "Fail", "Element Not Located After 5 Seconds"))
	else:
		results.append(("Messaging", "Pass", ""))

		try:
			WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='Messaging_4d634237-7bf2-4030-b5c4-bfb450e2c503']/div[2]/a[2]"))).click()
		except TimeoutException:
			results.append(("Search Link", "Fail", "Element Not Located After 5 Seconds"))
		else:
			results.append(("Search Link", "Pass", ""))

			time.sleep(5)

			try:
				driver.find_element_by_xpath(".//*[@id='SearchByLast10List_4d634237-7bf2-4030-b5c4-bfb450e2c503']/li[2]/a")
				driver.find_element_by_xpath(".//*[@id='SearchByLast10List_4d634237-7bf2-4030-b5c4-bfb450e2c503']/li[3]/a")
				driver.find_element_by_xpath(".//*[@id='SearchByLast10List_4d634237-7bf2-4030-b5c4-bfb450e2c503']/li[4]/a")
				driver.find_element_by_xpath(".//*[@id='SearchByLast10List_4d634237-7bf2-4030-b5c4-bfb450e2c503']/li[5]/a")
				driver.find_element_by_xpath(".//*[@id='SearchByLast10List_4d634237-7bf2-4030-b5c4-bfb450e2c503']/li[6]/a")
				driver.find_element_by_xpath(".//*[@id='SearchByLast10List_4d634237-7bf2-4030-b5c4-bfb450e2c503']/li[7]/a")
				driver.find_element_by_xpath(".//*[@id='SearchByLast10List_4d634237-7bf2-4030-b5c4-bfb450e2c503']/li[8]/a")
				driver.find_element_by_xpath(".//*[@id='SearchByLast10List_4d634237-7bf2-4030-b5c4-bfb450e2c503']/li[9]/a")
				driver.find_element_by_xpath(".//*[@id='SearchByLast10List_4d634237-7bf2-4030-b5c4-bfb450e2c503']/li[10]/a")
				driver.find_element_by_xpath(".//*[@id='SearchByLast10List_4d634237-7bf2-4030-b5c4-bfb450e2c503']/li[11]/a")
			except NoSuchElementException:
				results.append(("Search Last 10 Results", "Fail", "Not All 10 Results Found"))
			else:
				results.append(("Search Last 10 Results", "Pass", ""))

			try:
				WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='SearchByLast10Page_4d634237-7bf2-4030-b5c4-bfb450e2c503']/div[2]/div/ul/li[3]/a"))).click()
			except TimeoutException:
				results.append(("Search By ID Link", "Fail", "Element Not Located After 5 Seconds"))
			else:
				results.append(("Search By ID Link", "Pass", ""))

				try:
					WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='TrackingID_4d634237-7bf2-4030-b5c4-bfb450e2c503']"))).send_keys('3572681')
					WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='SearchByTrackingIDForm_4d634237-7bf2-4030-b5c4-bfb450e2c503']/div[2]/input"))).click()
					WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='SearchByTrackingIDList_4d634237-7bf2-4030-b5c4-bfb450e2c503']/li[2]/a"))).click()
				except TimeoutException:
					results.append(("Search By ID", "Fail", "Element Not Located After 5 Seconds"))
				else:
					results.append(("Search By ID", "Pass", ""))

					time.sleep(2)
					
					try:
						messageCheck = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='msgViewTrackingID_4d634237-7bf2-4030-b5c4-bfb450e2c503']"))).text
						print(messageCheck)
						if messageCheck == "3572681":
							results.append(("Message", "Pass", ""))
						else:
							results.append(("Message", "Fail", "Incorrect Message Loaded"))
					except TimeoutException:
						results.append(("Message", "Fail", "Element Not Located After 5 Seconds"))

	print(tabulate(results, headers = ["Section", "Result", "Comment"], tablefmt="fancy_grid"))
	results = []

	print("LOGOUT")

	##### LOGOUT #####

	time.sleep(2)

	try:
		WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='MessageReader_4d634237-7bf2-4030-b5c4-bfb450e2c503']/header/nav/div[2]/img"))).click()
	except TimeoutException:
		results.append(("Logout Button", "Fail", "Element Not Located After 5 Seconds"))
	else:
		results.append(("Logout Button", "Pass", ""))

		try:
			WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "loginbutton")))
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