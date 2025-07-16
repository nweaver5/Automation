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
    '\\Documents\\QA-Automation\\Demosite Automation\\Logs\\v2app\\')

site_list = ['https://hxweb01.healthx.com/qav2app.asp',
             'https://hxweb02.healthx.com/qav2app.asp',
             'https://hxweb03.healthx.com/qav2app.asp',
             'https://hxweb04.healthx.com/qav2app.asp',
             'https://hxweb05.healthx.com/qav2app.asp',
             'https://hxweb06.healthx.com/qav2app.asp',
             'https://hxweb07.healthx.com/qav2app.asp']
log_count = 1


def log_results(results):
    print(tabulate(results,
                   headers=["Section", "Result", "Comment"],
                   tablefmt="fancy_grid"))


def login(driver):
    print("LOGIN")
    results = []
    try:
        driver.find_element_by_id(
            "StdLoginControl_UserName").send_keys('qatest.samjones')
    except exceptions as e:
        msg = reader.error_lookup(e)
        print(msg)
        driver.quit()

    try:
        password_XPATH = """
        .//*[@id='StdLoginControl']/table/tbody/tr/td/table/tbody/tr[3]/td[2]/input
        """
        driver.find_element_by_xpath(password_XPATH).send_keys('american')
    except exceptions as e:
        msg = reader.error_lookup(e)
        print(msg)
        driver.quit()

    try:
        login_XPATH = """
        .//*[@id='StdLoginControl']/table/tbody/tr/td/table/tbody/tr[4]/td/input
        """
        driver.find_element_by_xpath(login_XPATH).click()
    except exceptions as e:
        print("Login Button Not Found")
        driver.quit()
    else:
        results.append(("Login", "Pass", ""))

    newFrame = driver.find_element_by_name('hxcontents')
    driver.switch_to.frame(newFrame)


def eligibility(driver):
    print("ELIGIBILITY SECTION")
    results = []
    try:
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(
                (By.LINK_TEXT, "EligibilitySearch 2.0 (Member)"))).click()
    except exceptions as e:
        msg = reader.error_lookup(e)
        results.append(("Elig Search Link", "Fail", msg))
    else:
        results.append(("Elig Search Link", "Pass", ""))

        driver.switch_to.default_content()
        newFrame = driver.find_element_by_name('main')
        driver.switch_to.frame(newFrame)

        try:
            WebDriverWait(driver, 5).until(
                EC.presence_of_element_located(
                    (By.LINK_TEXT, "Sam Jones"))).click()
        except exceptions as e:
            msg = reader.error_lookup(e)
            results.append(("Sam Jones Link", "Fail", msg))
        else:
            results.append(("Sam Jones Link", "Pass", ""))

            try:
                elem = """
                .//*[@id='ViewPanel']/span/table/tbody/tr/td/table/tbody/tr/td
                """
                WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((
                        By.XPATH, elem)))
            except exceptions as e:
                msg = reader.error_lookup(e)
                results.append(("Sam Jones Page", "Fail", msg))
            else:
                results.append(("Sam Jones Page", "Pass", ""))

                try:
                    WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located(
                            (By.LINK_TEXT, "Print View"))).click()
                except exceptions as e:
                    msg = reader.error_lookup(e)
                    results.append(("Print View Link", "Fail", msg))
                else:
                    results.append(("Print View Link", "Pass", ""))

                    driver.switch_to_window(driver.window_handles[-1])

                    try:
                        WebDriverWait(driver, 5).until(
                            EC.presence_of_element_located((
                                By.LINK_TEXT, "Close Window"))).click()
                    except exceptions as e:
                        msg = reader.error_lookup(e)
                        results.append(("Print View Exit", "Fail", msg))
                    else:
                        results.append(("Print View Exit", "Pass", ""))

    log_results(results)

    driver.switch_to_window(driver.window_handles[-1])
    driver.switch_to.default_content()
    newFrame = driver.find_element_by_name('hxcontents')
    driver.switch_to.frame(newFrame)


def claims(driver):
    print("CLAIMS SECTION")
    results = []
    try:
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(
                (By.LINK_TEXT, "ClaimSearch 2.0 (Member)"))).click()
    except exceptions as e:
        msg = reader.error_lookup(e)
        results.append(("Claim Search Link", "Fail", msg))
    else:
        results.append(("Claim Search Link", "Pass", ""))

        driver.switch_to.default_content()
        newFrame = driver.find_element_by_name('main')
        driver.switch_to.frame(newFrame)

        try:
            WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((
                    By.ID, "QuickSearchButton"))).click()
        except exceptions as e:
            msg = reader.error_lookup(e)
            results.append(("Search Link", "Fail", msg))
        else:
            results.append(("Search Link", "Pass", ""))

            try:
                WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((
                        By.LINK_TEXT, "N636186001"))).click()
            except exceptions as e:
                msg = reader.error_lookup(e)
                results.append(("Claim Link", "Fail", msg))
            else:
                results.append(("Claim Link", "Pass", ""))

                try:
                    elem = """
                    .//*[@id='DocumentPanel']/span/table/tbody/tr/td/table/tbody/tr[1]/td/table/tbody/tr[4]/td[3]/font
                    """
                    claimCheck = WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located((
                            By.XPATH, elem))).text

                    if claimCheck == 'N636186001':
                        results.append(("Claim Link Page", "Pass", ""))
                    else:
                        results.append((
                            "Claim Link Page",
                            "Fail",
                            "Link Didn't Load Proper Claim Page"
                            ))
                except exceptions as e:
                    msg = reader.error_lookup(e)
                    results.append(("Print View Link", "Fail", msg))

    log_results(results)

    driver.switch_to.default_content()
    newFrame = driver.find_element_by_name('top')
    driver.switch_to.frame(newFrame)


def logout(driver):
    print("LOGOUT")
    results = []
    try:
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((
                By.LINK_TEXT, "Logoff"))).click()
        driver.find_element_by_id("StdLoginControl_UserName")
    except exceptions as e:
        msg = reader.error_lookup(e)
        results.append(("Logoff", "Fail", msg))
    else:
        results.append(("Logoff", "Pass", ""))

    log_results(results)


def main(site, log_count):
    output_file = os.path.join(
        log_path,
        "v2check_automation_chrome_hxweb0" + str(log_count) + "_" +
        time.strftime("%m-%d-%H-%M") + ".log")
    output = open(output_file, 'w', encoding='utf-8')
    sys.stdout = output
    driver = webdriver.Chrome(
        executable_path='C:\Python34\Scripts\chromedriver.exe')

    start = time.time()
    driver.get(site)

    print("Chrome - hxweb0" + str(log_count) + "\n")

    login(driver)
    eligibility(driver)
    claims(driver)
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
