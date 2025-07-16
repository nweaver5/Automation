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
scriptPath = os.path.dirname(userProfile + '\\Desktop\\Demosite Automation\\V2Check\\ChromeLogs\\')
outputFile = os.path.join(scriptPath, "v2check_automation_chrome_hxweb02_" + time.strftime("%m-%d-%H-%M") + ".log")
output = open(outputFile, 'w', encoding='utf-8')
sys.stdout = output

def main():
	driver = webdriver.Chrome(executable_path='C:\Python34\Scripts\chromedriver.exe')
	#driver = webdriver.Firefox()
	#driver = webdriver.Ie(executable_path='C:\Python34\Scripts\IEDriverServer.exe')

	results = []

	start = time.time()
	driver.get('https://hxweb02.healthx.com/qav2app.asp')

	print("Chrome - hxweb02\n")
	print("LOGIN")

	try:
		driver.find_element_by_id("StdLoginControl_UserName").send_keys('qatest.samjones')
	except NoSuchElementException:
		print("Login Not Found")
		driver.quit()

	try:
		driver.find_element_by_xpath(".//*[@id='StdLoginControl']/table/tbody/tr/td/table/tbody/tr[3]/td[2]/input").send_keys('american')
	except NoSuchElementException:
		print("Password Not Found")
		driver.quit()

	try:
		driver.find_element_by_xpath(".//*[@id='StdLoginControl']/table/tbody/tr/td/table/tbody/tr[4]/td/input").click()
	except NoSuchElementException:
		print("Login Button Not Found")
		driver.quit()
	else:
		results.append(("Login", "Pass", ""))

	time.sleep(1)

	newFrame = driver.find_element_by_name('hxcontents')
	driver.switch_to.frame(newFrame)

	print("ELIGIBILITY SECTION")

	try:
		WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.LINK_TEXT, "EligibilitySearch 2.0 (Member)"))).click()
	except TimeoutException:
		results.append(("Elig Search Link", "Fail", "Element Not Located After 5 Seconds"))
	else:
		results.append(("Elig Search Link", "Pass", ""))

		driver.switch_to.default_content()
		newFrame = driver.find_element_by_name('main')
		driver.switch_to.frame(newFrame)

		try:
			WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.LINK_TEXT, "Sam Jones"))).click()
		except TimeoutException:
			results.append(("Sam Jones Link", "Fail", "Element Not Located After 5 Seconds"))
		else:
			results.append(("Sam Jones Link", "Pass", ""))

			try:
				WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='ViewPanel']/span/table/tbody/tr/td/table/tbody/tr/td")))
			except TimeoutException:
				results.append(("Sam Jones Page", "Fail", "Element Not Located After 5 Seconds"))
			else:
				results.append(("Sam Jones Page", "Pass", ""))

				try:
					WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.LINK_TEXT, "Print View"))).click()
				except TimeoutException:
					results.append(("Print View Link", "Fail", "Element Not Located After 5 Seconds"))
				else:
					results.append(("Print View Link", "Pass", ""))

					driver.switch_to_window(driver.window_handles[-1])

					try:
						WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.LINK_TEXT, "Close Window"))).click()
					except TimeoutException:
						results.append(("Print View Exit", "Fail", "Element Not Located After 5 Seconds"))
					else:
						results.append(("Print View Exit", "Pass", ""))

	print(tabulate(results, headers = ["Section", "Result", "Comment"], tablefmt="fancy_grid"))
	results = []

	driver.switch_to_window(driver.window_handles[-1])
	driver.switch_to.default_content()
	newFrame = driver.find_element_by_name('hxcontents')
	driver.switch_to.frame(newFrame)

	print("CLAIMS SECTION")

	try:
		WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.LINK_TEXT, "ClaimSearch 2.0 (Member)"))).click()
	except TimeoutException:
		results.append(("Claim Search Link", "Fail", "Element Not Located After 5 Seconds"))
	else:
		results.append(("Claim Search Link", "Pass", ""))

		driver.switch_to.default_content()
		newFrame = driver.find_element_by_name('main')
		driver.switch_to.frame(newFrame)

		try:
			WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "QuickSearchButton"))).click()
		except TimeoutException:
			results.append(("Search Link", "Fail", "Element Not Located After 5 Seconds"))
		else:
			results.append(("Search Link", "Pass", ""))

			try:
				WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.LINK_TEXT, "N636186001"))).click()
			except TimeoutException:
				results.append(("Claim Link", "Fail", "Element Not Located After 5 Seconds"))
			else:
				results.append(("Claim Link", "Pass", ""))

				try:
					claimCheck = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, ".//*[@id='DocumentPanel']/span/table/tbody/tr/td/table/tbody/tr[1]/td/table/tbody/tr[4]/td[3]/font"))).text

					if claimCheck == 'N636186001':
						results.append(("Claim Link Page", "Pass", ""))
					else:
						results.append(("Claim Link Page", "Fail", "Link Didn't Load Proper Claim Page"))
				except TimeoutException:
					results.append(("Print View Link", "Fail", "Element Not Located After 5 Seconds"))

	print(tabulate(results, headers = ["Section", "Result", "Comment"], tablefmt="fancy_grid"))
	results = []

	driver.switch_to.default_content()
	newFrame = driver.find_element_by_name('top')
	driver.switch_to.frame(newFrame)

	print("LOGOFF")

	try:
		WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.LINK_TEXT, "Logoff"))).click()
		driver.find_element_by_id("StdLoginControl_UserName")
	except TimeoutException:
		results.append(("Logoff", "Fail", "Unable to Logoff, Element Not Located After 5 Seconds"))
	else:
		results.append(("Logoff", "Pass", ""))

	print(tabulate(results, headers = ["Section", "Result", "Comment"], tablefmt="fancy_grid"))
	results = []
				
	end = time.time() - start
	print("\nTotal Elapsed Test Time %.2f" % end)

	output.close()
	sys.stdout = sys.__stdout__
	driver.quit()
	
main()