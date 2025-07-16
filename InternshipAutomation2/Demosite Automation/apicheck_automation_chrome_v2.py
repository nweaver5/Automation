import time
import os
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException as exceptions
from Utility.error_reader import reader
from tabulate import tabulate

user_profile = os.environ['USERPROFILE']
log_path = os.path.dirname(
    user_profile +
    '\\Documents\\QA-Automation\\Demosite Automation\\Logs\\API\\')

site_list = ['https://hxweb01.healthx.com/dev',
             'https://hxweb02.healthx.com/dev',
             'https://hxweb03.healthx.com/dev',
             'https://hxweb04.healthx.com/dev',
             'https://hxweb05.healthx.com/dev',
             'https://hxweb06.healthx.com/dev',
             'https://hxweb07.healthx.com/dev']

log_count = 1


def login(driver):
    print("LOGIN")
    results = []
    try:
        driver.find_element_by_id("username").send_keys('documentation.user')
    except exceptions as e:
        msg = reader.error_lookup(e)
        print(msg)
        driver.quit()

    try:
        driver.find_element_by_name("password").send_keys('american')
    except exceptions as e:
        msg = reader.error_lookup(e)
        print(msg)
        driver.quit()

    try:
        driver.find_element_by_id("loginButton").click()
    except exceptions as e:
        msg = reader.error_lookup(e)
        print(msg)
        driver.quit()

    try:
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((
                By.XPATH, ".//*[@id='hxUserMenu']/li[1]/a")))
    except exceptions as e:
        msg = reader.error_lookup(e)
        results.append(("Login", "Fail", msg))
        log_results(results)
        driver.quit()
    else:
        results.append(("Login", "Pass", ""))

    log_results(results)


def eligibility(driver):
    # ELIGIBILITY SECTION #

    print("Eligibility Section")
    results = []
    try:
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((
                By.XPATH, ".//*[@id='hxUserMenu']/li[3]/a"))).click()
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((
                By.XPATH,
                ".//*[@id='svc_277856eb-8136-4a4a-9202-5f88034f806e']/a"
                ))).click()
    except exceptions as e:
        msg = reader.error_lookup(e)
        results.append(("Eligibility Link", "Fail", msg))
    else:
        results.append(("Eligibility Link", "Pass", ""))

        try:
            WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((
                    By.XPATH,
                    ".//*[text()='\"0c8c57cb-dc2d-413a-acec-226700e368a9\"']"
                    )))
        except exceptions as e:
            msg = reader.error_lookup(e)
            results.append(("Accumulator ID", "Fail", msg))
        else:
            results.append(("Accumulator ID", "Pass", ""))
        try:
            WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((
                    By.XPATH,
                    ".//*[text()='\"56db6094-92cc-4c06-a5c6-686e562b9eca\"']"
                    )))
        except exceptions as e:
            msg = reader.error_lookup(e)
            results.append(("Item ID", "Fail", msg))
        else:
            results.append(("Item ID", "Pass", ""))
        try:
            WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((
                    By.XPATH,
                    ".//*[text()='\"7cf82977-b4d1-4a04-90aa-253643e7e753\"']"
                    )))
        except exceptions as e:
            msg = reader.error_lookup(e)
            results.append(("Eligibility ID", "Fail", msg))
        else:
            results.append(("Eligibility ID", "Pass", ""))

    log_results(results)


def claims(driver):
    # CLAIMS API #

    print("Claims API")
    results = []
    try:
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((
                By.LINK_TEXT, "MemberDateSearch"))).click()
    except exceptions as e:
        msg = reader.error_lookup(e)
        results.append(("Claims Link", "Fail", msg))
    else:
        results.append(("Claims Link", "Pass", ""))

        try:
            WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((
                    By.XPATH,
                    ".//*[text()='\"7e0e5a6b-72ec-4452-85a5-fbca7af151b1\"']"
                    )))
        except exceptions as e:
            msg = reader.error_lookup(e)
            results.append(("Claim ID", "Fail", msg))
        else:
            results.append(("Claim ID", "Pass", ""))

    log_results(results)


def user(driver):
    # USER API #

    print("User API")
    results = []
    try:
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.LINK_TEXT, "GetUser"))).click()
    except exceptions as e:
        msg = reader.error_lookup(e)
        results.append(("User Link", "Fail", msg))
    else:
        results.append(("User Link", "Pass", ""))

        try:
            WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((
                    By.XPATH,
                    ".//*[text()='\"cafcd812-40d2-49f8-860b-4f318d8311df\"']"
                    )))
        except exceptions as e:
            msg = reader.error_lookup(e)
            results.append(("User ID", "Fail", msg))
        else:
            results.append(("User ID", "Pass", ""))

    log_results(results)


def session(driver):
    # SESSION API #

    print("Session API")
    results = []
    try:
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((
                By.LINK_TEXT, "Refresh"))).click()
    except exceptions as e:
        msg = reader.error_lookup(e)
        results.append(("Session Link", "Fail", msg))
    else:
        results.append(("Session Link", "Pass", ""))

        try:
            WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((
                    By.LINK_TEXT, "Click!"))).click()
        except exceptions as e:
            msg = reader.error_lookup(e)
            results.append(("Session Refresh Link", "Fail", msg))
        else:
            results.append(("Session Refresh Link", "Pass", ""))

            try:
                WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((
                        By.XPATH, ".//*[text()='Session Refreshed']")))
            except exceptions as e:
                msg = reader.error_lookup(e)
                results.append(("Refresh", "Fail", msg))
            else:
                results.append(("Refresh", "Pass", ""))

    log_results(results)


def logout(driver):
    # LOGOUT #

    print("LOGOUT")
    results = []
    try:
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((
                By.LINK_TEXT, "Logout"))).click()
    except exceptions as e:
        msg = reader.error_lookup(e)
        results.append(("Logout Button", "Fail", msg))
        log_results(results)
        driver.quit()
    else:
        results.append(("Logout Button", "Pass", ""))

    try:
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, "username")))
    except exceptions as e:
        msg = reader.error_lookup(e)
        results.append(("Logout", "Fail", msg))
    else:
        results.append(("Logout", "Pass", ""))

    log_results(results)


def log_results(results):
    print(tabulate(results,
                   headers=["Section", "Result", "Comment"],
                   tablefmt="fancy_grid"))


def main(site, log_count):
    output_file = os.path.join(
        log_path, "apicheck_automation_chrome_hxweb0" + str(log_count) + "_"
        + time.strftime("%m-%d-%H-%M") + ".log")
    output = open(output_file, 'w', encoding='utf-8')
    sys.stdout = output
    start = time.time()
    driver = webdriver.Chrome(
        executable_path='C:\Python34\Scripts\chromedriver.exe')
    driver.get(site)

    print("API Check - Chrome - hxweb0" + str(log_count) + "\n")

    login(driver)
    eligibility(driver)
    claims(driver)
    user(driver)
    session(driver)
    logout(driver)

    end = time.time() - start
    print("\nTotal Elapsed Test Time %.2f" % end)

    output.close()
    sys.stdout = sys.__stdout__
    driver.quit()
    log_count = log_count + 1
    return log_count

for site in site_list:
    log_count = main(site, log_count)
