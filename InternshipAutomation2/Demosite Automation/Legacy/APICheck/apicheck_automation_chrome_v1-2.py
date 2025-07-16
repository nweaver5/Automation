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
scriptPath = os.path.dirname(userProfile + '\\Desktop\\Demosite Automation\\APICheck\\ChromeLogs\\')
outputFile = os.path.join(scriptPath, "apicheck_automation_chrome_hxweb02_" + time.strftime("%m-%d-%H-%M") + ".log")
output = open(outputFile, 'w', encoding='utf-8')
sys.stdout = output

def main():
	driver = webdriver.Chrome(executable_path='C:\Python34\Scripts\chromedriver.exe')
	#driver = webdriver.Firefox()
	#driver = webdriver.Ie(executable_path='C:\Python34\Scripts\IEDriverServer.exe')

	results = []

	start = time.time()
	driver.get('https://hxweb02.healthx.com/dev')

	print("API Check - Chrome - hxweb02\n")
	print("LOGIN")

	try:
		driver.find_element_by_id("username").send_keys('documentation.user')
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

	time.sleep(1)

	try:
		WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='hxUserMenu']/li[1]/a")))
	except TimeoutException:
		results.append(("Login", "Fail", ""))
		print(tabulate(results, headers = ["Section", "Result", "Comment"], tablefmt="fancy_grid"))
		results = []
		driver.quit()
	else:
		results.append(("Login", "Pass", ""))

	print(tabulate(results, headers = ["Section", "Result", "Comment"], tablefmt="fancy_grid"))
	results = []

	##### ELIGIBILITY SECTION #####

	print("Eligibility Section")

	try:
		WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='hxUserMenu']/li[3]/a"))).click()
		WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='svc_277856eb-8136-4a4a-9202-5f88034f806e']/a"))).click()
	except TimeoutException:
		results.append(("Eligibility Link", "Fail", "Element Not Located After 5 Seconds"))
	else:
		results.append(("Eligibility Link", "Pass", ""))

		try:
			WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, ".//*[text()='\"0c8c57cb-dc2d-413a-acec-226700e368a9\"']")))
		except TimeoutException:
			results.append(("Accumulator ID", "Fail", "Element Not Located After 5 Seconds"))
		else:
			results.append(("Accumulator ID", "Pass", ""))
			
		try:
			WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, ".//*[text()='\"56db6094-92cc-4c06-a5c6-686e562b9eca\"']")))
		except TimeoutException:
			results.append(("Item ID", "Fail", "Element Not Located After 5 Seconds"))
		else:
			results.append(("Item ID", "Pass", ""))

		try:
			WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, ".//*[text()='\"7cf82977-b4d1-4a04-90aa-253643e7e753\"']")))
		except TimeoutException:
			results.append(("Eligibility ID", "Fail", "Element Not Located After 5 Seconds"))
		else:	
			results.append(("Eligibility ID", "Pass", ""))

	print(tabulate(results, headers = ["Section", "Result", "Comment"], tablefmt="fancy_grid"))
	results = []

	##### CLAIMS API #####

	print("Claims API")

	try:
		WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.LINK_TEXT, "MemberDateSearch"))).click()
	except TimeoutException:
		results.append(("Claims Link", "Fail", "Element Not Located After 5 Seconds"))
	else:
		results.append(("Claims Link", "Pass", ""))

		try:
			WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, ".//*[text()='\"7e0e5a6b-72ec-4452-85a5-fbca7af151b1\"']")))
		except TimeoutException:
			results.append(("Claim ID", "Fail", "Element Not Located After 5 Seconds"))
		else:
			results.append(("Claim ID", "Pass", ""))

	print(tabulate(results, headers = ["Section", "Result", "Comment"], tablefmt="fancy_grid"))
	results = []

	##### USER API #####

	print("User API")

	try:
		WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.LINK_TEXT, "GetUser"))).click()
	except TimeoutException:
		results.append(("User Link", "Fail", "Element Not Located After 5 Seconds"))
	else:
		results.append(("User Link", "Pass", ""))

		try:
			WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, ".//*[text()='\"cafcd812-40d2-49f8-860b-4f318d8311df\"']")))
		except TimeoutException:
			results.append(("User ID", "Fail", "Element Not Located After 5 Seconds"))
		else:
			results.append(("User ID", "Pass", ""))

	print(tabulate(results, headers = ["Section", "Result", "Comment"], tablefmt="fancy_grid"))
	results = []

	##### SESSION API #####

	print("Session API")

	try:
		WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.LINK_TEXT, "Refresh"))).click()
	except TimeoutException:
		results.append(("Session Link", "Fail", "Element Not Located After 5 Seconds"))
	else:
		results.append(("Session Link", "Pass", ""))

		try:
			WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.LINK_TEXT, "Click!"))).click()
		except TimeoutException:
			results.append(("Session Refresh Link", "Fail", "Element Not Located After 5 Seconds"))
		else:
			results.append(("Session Refresh Link", "Pass", ""))

			try:
				WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, ".//*[text()='Session Refreshed']")))
			except TimeoutException:
				results.append(("Refresh", "Fail", "Element Not Located After 5 Seconds"))
			else:
				results.append(("Refresh", "Pass", ""))

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