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
    user_profile
    + '\\Documents\\QA-Automation\\Demosite Automation\\Logs\\Member\\')
log_count = 1
site_list = ['https://hxweb01.healthx.com/newsweetness.aspx',
             'https://hxweb02.healthx.com/newsweetness.aspx',
             'https://hxweb03.healthx.com/newsweetness.aspx',
             'https://hxweb04.healthx.com/newsweetness.aspx',
             'https://hxweb05.healthx.com/newsweetness.aspx',
             'https://hxweb06.healthx.com/newsweetness.aspx',
             'https://hxweb07.healthx.com/newsweetness.aspx']


def log_results(results):
    print(tabulate(results,
                   headers=["Section", "Result", "Comment"],
                   tablefmt="fancy_grid"))


def return_home(driver):
    results = []
    try:
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((
                By.XPATH, ".//*[@id='hxUserMenu']/li[1]/a"))).click()
    except exceptions as e:
        msg = reader.error_lookup(e)
        results.append(("Home Button", "Fail", msg))
        log_results(results)
        driver.quit()
    else:
        results.append(("Home Button", "Pass", ""))
    log_results(results)


def login(driver):
    print("LOGIN")
    results = []
    try:
        driver.find_element_by_id("username").send_keys('Plan.member14')
    except exceptions as e:
        msg = reader.error_lookup(e)
        print(msg)
        driver.quit()

    try:
        driver.find_element_by_name("password").send_keys('american1')
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
    time.sleep(2)

    try:
        driver.find_element_by_link_text("Skip to Home Page").click()
    except exceptions as e:
        msg = reader.error_lookup(e)
        results.append(("Splash Screen", "Fail", msg))
        log_results(results)
        driver.quit()
    except exceptions as e:
        msg = reader.error_lookup(e)
        results.append(("Splash Screen", "Fail", msg))
        log_results(results)
        driver.quit()
    else:
        results.append(("Login", "Pass", ""))
        results.append(("Splash Screen", "Pass", ""))
        log_results(results)


def elig_dashboard(driver):
    print("ELIGIBILITY DASHBOARD")
    results = []
    coverage_names = ["Elizabeth Jones",
                      "Daniel Jones",
                      "Alicia Jones"]

    try:
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, "ContentItem200_2")))
    except exceptions as e:
        msg = reader.error_lookup(e)
        results.append(("Coverage Section", "Fail", msg))
    else:
        results.append((
            "Coverage Section", "Pass", ""))

    try:
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((
                By.LINK_TEXT, "View all Coverage & Benefits"))).click()
    except exceptions as e:
        msg = reader.error_lookup(e)
        results.append(("View All Link", "Fail", msg))
    else:
        results.append(("View All Link", "Pass", ""))
    try:
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((
                By.LINK_TEXT, "Schedule of Benefits")))
    except exceptions as e:
        msg = reader.error_lookup(e)
        results.append(("View All Link Page", "Fail", msg))
    else:
        results.append(("View All Link Page", "Pass", ""))
        driver.back()

    for name in coverage_names:

        try:
            WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((
                    By.LINK_TEXT, name))).click()
        except exceptions as e:
            msg = reader.error_lookup(e)
            results.append((name + " Link", "Fail", msg))
        else:
            results.append((name + " Link", "Pass", ""))
        try:
            WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((
                    By.ID, "ctl00_MainContent_uxMessageLabel")))
        except exceptions as e:
            msg = reader.error_lookup(e)
            results.append((name + " Link Page", "Fail", msg))
        else:
            results.append((name + " Link Page", "Pass", ""))
            driver.back()

    log_results(results)


def balances(driver):
    print("BALANCE SECTION")
    results = []

    try:
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((
                By.ID, "ContentItem200_3")))
    except exceptions as e:
        msg = reader.error_lookup(e)
        results.append(("Balances Section", "Fail", msg))
    else:
        results.append(("Balances Section", "Pass", ""))

    log_results(results)
    results = []


def claims_dashboard(driver):
    print("CLAIMS DASHBOARD")
    results = []
    # CLAIMS SECTION #
    claims = ["4557784597",
              "9156395414",
              "4021764337",
              "6755069099",
              "1674315135",
              "7973735542",
              "8128013376",
              "9982984085",
              "1382195851",
              "5572922122"]

    claim_line_PATH = ".//*[@id='serviceContainer']/div[2]/div[3]/div[1]/h3"

    try:
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((
                By.ID, "ContentItem200_4")))
    except exceptions as e:
        msg = reader.error_lookup(e)
        results.append(("Claims Section", "Fail", msg))
    else:
        results.append(("Claims Section", "Pass", ""))

    try:
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(
                (By.LINK_TEXT, "Proceed to my Claims"))).click()
    except exceptions as e:
        msg = reader.error_lookup(e)
        results.append(("Claims Link", "Fail", msg))
    else:
        results.append(("Claims Link", "Pass", ""))

    try:
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((
                By.XPATH, ".//*[@id='serviceContainer']/div[2]/div/div[2]")))
    except exceptions as e:
        msg = reader.error_lookup(e)
        results.append(("Claims Link Page", "Fail", msg))
    else:
        results.append(("Claims Link Page", "Pass", ""))

    try:
        driver.find_element_by_link_text("Member Claims Submission").click()
    except exceptions as e:
        msg = reader.error_lookup(e)
        results.append(("Claims Form Link", "Fail", msg))
    else:
        results.append(("Claims Form Link", "Pass", ""))
    try:
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((
                By.ID, "ctl00_MainContent_uxForm_ctl03_uxFormSubmitButton")))
    except exceptions as e:
        msg = reader.error_lookup(e)
        results.append(("Claims Form", "Fail", msg))
    else:
        results.append(("Claims Form", "Pass", ""))
        driver.back()

    for claim in claims:

        try:
            WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((
                    By.LINK_TEXT, claim))).click()
        except exceptions as e:
            msg = reader.error_lookup(e)
            results.append(("Claims Link " + claim, "Fail", msg))
        else:
            try:
                claim_check = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, claim_line_PATH))
                    ).text

                if claim_check == ("Claim #" + claim):
                    results.append(("Claims Link " + claim, "Pass", ""))
                    driver.back()

            except exceptions as e:
                msg = reader.error_lookup(e)
                results.append(("Claims Link " + claim, "Fail", msg))

    log_results(results)
    return_home(driver)


def payments(driver):
    # PAYMENTS SECTION #
    print("PAYMENTS SECTION")
    results = []
    try:
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, "ContentItem200_5")))
    except exceptions as e:
        msg = reader.error_lookup(e)
        results.append(("Payments Section", "Fail", msg))
    else:
        results.append(("Payments Section", "Pass", ""))

    try:
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((
            By.XPATH, ".//*[@id='hxUserMenu']/li[4]/a"))).click()
    except exceptions as e:
        msg = reader.error_lookup(e)
        results.append(("Payments Link", "Fail", msg))
    else:
        results.append(("Payments Link", "Pass", ""))

    try:
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, "aspnetForm")))
    except exceptions as e:
        msg = reader.error_lookup(e)
        results.append(("Payments Page", "Fail", msg))
    else:
        results.append(("Payments Page", "Pass", ""))

    log_results(results)
    return_home(driver)


def authorizations(driver):
    # AUTHORIZATIONS SECTION #
    results = []
    print("AUTHORIZATIONS SECTION")
    auth_PATH = [
     ".//*[@id='ctl00_MainContent_uxAuthorizationsGrid']/tbody/tr[2]/td[1]/a",
     ".//*[@id='ctl00_MainContent_uxAuthorizationsGrid']/tbody/tr[3]/td[1]/a",
     ".//*[@id='ctl00_MainContent_uxAuthorizationsGrid']/tbody/tr[4]/td[1]/a",
     ".//*[@id='ctl00_MainContent_uxAuthorizationsGrid']/tbody/tr[5]/td[1]/a",
     ".//*[@id='ctl00_MainContent_uxAuthorizationsGrid']/tbody/tr[7]/td[1]/a",
     ".//*[@id='ctl00_MainContent_uxAuthorizationsGrid']/tbody/tr[8]/td[1]/a",
     ".//*[@id='ctl00_MainContent_uxAuthorizationsGrid']/tbody/tr[9]/td[1]/a",
     ".//*[@id='ctl00_MainContent_uxAuthorizationsGrid']/tbody/tr[10]/td[1]/a",
     ".//*[@id='ctl00_MainContent_uxAuthorizationsGrid']/tbody/tr[11]/td[1]/a"]

    auth_check_PATH = """
    .//*[@id='serviceContainer']/div[2]/div[3]/div[2]/table/tbody/tr[2]/td[2]/p
    """
    try:
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((
                By.XPATH, ".//*[@id='hxUserMenu']/li[5]/a"))).click()
    except exceptions as e:
        msg = reader.error_lookup(e)
        results.append(("Authorizations Link", "Fail", msg))
    else:
        results.append(("Authorizations Link", "Pass", ""))
    try:
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((
                By.LINK_TEXT, "View your Care Plan")))
    except exceptions as e:
        msg = reader.error_lookup(e)
        results.append(("Authorizations Page", "Fail", msg))
    else:
        results.append(("Authorizations Page", "Pass", ""))

    for path in auth_PATH:

        try:
            auth_link = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, path)))
            auth_link_text = auth_link.text
            auth_link.click()
            auth_check = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((
                    By.XPATH, auth_check_PATH))).text

            if auth_check == auth_link_text:
                results.append(("Auth Link " + path, "Pass", ""))
                driver.back()
        except exceptions as e:
            msg = reader.error_lookup(e)
            results.append(("Auth Link " + path, "Fail", msg))

    log_results(results)
    return_home(driver)


def provider(driver):
    # PROVIDE SECTION #
    results = []
    print("PROVIDER SECTION")

    try:
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((
                By.XPATH, ".//*[@id='hxUserMenu']/li[6]/a"))).click()
    except exceptions as e:
        msg = reader.error_lookup(e)
        results.append(("Provider Tool Link", "Fail", msg))
    else:
        results.append(("Provider Tool Link", "Pass", ""))

    try:
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((
                By.XPATH, ".//*[@id='submitProvSearch']")))
    except exceptions as e:
        msg = reader.error_lookup(e)
        results.append(("Provider Tool", "Fail", msg))
    else:
        results.append(("Provider Tool", "Pass", ""))

    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((
            By.ID, "providerZip"))).send_keys("54601")
    time.sleep(3)
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((
            By.ID, "submitProvSearch"))).click()
    time.sleep(10)

    try:
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, "resultsList")))
    except exceptions as e:
        msg = reader.error_lookup(e)
        results.append(("Provider Results", "Fail", msg))
    else:
        results.append(("Provider Results", "Pass", ""))

    print(tabulate(results,
                   headers=["Section", "Result", "Comment"],
                   tablefmt="fancy_grid"))
    results = []

    try:
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((
                By.XPATH, ".//*[@id='hxUserMenu']/li[1]/a"))).click()
    except exceptions as e:
        msg = reader.error_lookup(e)
        results.append(("Home Button", "Fail", msg))
        print(tabulate(results,
                       headers=["Section", "Result", "Comment"],
                       tablefmt="fancy_grid"))
        driver.quit()
    else:
        results.append(("Home Button", "Pass", ""))


def wellness(driver):
    # WELLNESS #
    results = []
    try:
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((
                By.XPATH, ".//*[@id='hxUserMenu']/li[7]/a"))).click()
    except exceptions as e:
        msg = reader.error_lookup(e)
        results.append(("Welness Button", "Fail", msg))
    else:
        results.append(("Welness Button", "Pass", ""))

    try:
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((
                By.XPATH, ".//*[@id='serviceContainer']/div[2]")))
    except exceptions as e:
        msg = reader.error_lookup(e)
        results.append(("Wellness Page", "Fail", msg))
    else:
        results.append(("Wellness Page", "Pass", ""))

    log_results(results)
    return_home(driver)


def side_menu(driver):
    # SIDE MENU #
    results = []
    print("SIDE MENU")

    link_text = ["Print or Request an ID Card",
                 "Enrollment Form",
                 "Prescription Benefit",
                 "Change My PCP",
                 "Change Name and/or Address"]
    page_path = [
     ".//*[@id='idcardtemplate']/table[1]/tbody/tr[2]/td[2]/table/tbody/tr[1]/td[1]/img",
     ".//*[@id='ctl00_MainContent_uxForm_ctl03_uxFormSubmitButton']",
     ".//*[@id='top']/div[1]",
     ".//*[@id='ctl00_MainContent_uxProviderViewControl_uxTabPanel']/div[2]/div[4]/fieldset[1]/legend",
     ".//*[@id='ctl00_MainContent_uxForm_ctl03_uxFormSubmitButton']"]
    i = 0
    for link in link_text:
        try:
            WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((
                    By.LINK_TEXT, link))).click()
        except exceptions as e:
            msg = reader.error_lookup(e)
            results.append(("Side Menu Link " + link, "Fail", msg))
        else:
            results.append(("Side Menu Link " + link, "Pass", ""))

        try:
            WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((
                    By.XPATH, page_path[i])))
        except exceptions as e:
            msg = reader.error_lookup(e)
            results.append(("Side Menu Page " + link, "Fail", msg))
        else:
            results.append(("Side Menu Page " + link, "Pass", ""))
            driver.back()
        i = i + 1
    log_results(results)


def messages(driver):
    # MESSAGES AND PROFILE #

    print("MESSAGES AND PROFILE")
    results = []
    try:
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((
                By.XPATH,
                ".//*[@id='basicShell']/header/nav[1]/ul/li[1]/a"))).click()
    except exceptions as e:
        msg = reader.error_lookup(e)
        results.append(("Messages Button", "Fail", msg))
    else:
        results.append(("Messages Button", "Pass", ""))

    try:
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, "main")))
    except exceptions as e:
        msg = reader.error_lookup(e)
        results.append(("Messages Main Page", "Fail", msg))
    else:
        results.append(("Messages Main Page", "Pass", ""))

    try:
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((
                By.XPATH,
                ".//*[@id='ctl00_MainContent_uxMessagingOptions']/ul/li[2]/a"
                ))).click()
    except exceptions as e:
        msg = reader.error_lookup(e)
        results.append(("Messages Saved Page Link", "Fail", msg))
    else:
        results.append(("Messages Saved Page Link", "Pass", ""))

    try:
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((
                By.XPATH,
                ".//*[@id='ctl00_MainContent_uxMessageGrid']/tbody/tr[2]/td[2]"
                )))
    except exceptions as e:
        msg = reader.error_lookup(e)
        results.append(("Messages Saved Page", "Fail", msg))
    else:
        results.append(("Messages Saved Page", "Pass", ""))

    try:
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((
                By.XPATH,
                ".//*[@id='ctl00_MainContent_uxMessagingOptions']/ul/li[4]/a"
                ))).click()
    except exceptions as e:
        msg = reader.error_lookup(e)
        results.append(("Messages Search Page Link", "Fail", msg))
    else:
        results.append(("Messages Search Page Link", "Pass", ""))

    try:
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((
                By.LINK_TEXT, "Tracking Number Search"))).click()
    except exceptions as e:
        msg = reader.error_lookup(e)
        results.append(("Messages Search Page", "Fail", msg))
    else:
        results.append(("Messages Search Page", "Pass", ""))

    try:
        elem = """
        .//*[@id='ctl00_MainContent_uxTrackingNumberSearchForm_ctl02_uxTrackingNumberText_textbox']
        """
        click = """
        .//*[@id='ctl00_MainContent_uxTrackingNumberSearchForm_ctl03_uxTrackingNumberSearchButton']
        """
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((
                By.XPATH, elem))).send_keys('3502821')
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((
                By.XPATH, click))).click()
    except exceptions as e:
        msg = reader.error_lookup(e)
        results.append(("Messages Search Button", "Fail", msg))
    else:
        results.append(("Messages Search Button", "Pass", ""))

    try:
        messagesSearchCheck = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((
                By.XPATH,
                ".//*[@id='ctl00_MainContent_uxInformationLabel']/b"))).text

        if messagesSearchCheck == "Tracking # 3502821":
            results.append(("Messages Search", "Pass", ""))
        else:
            results.append(("Messages Search", "Fail",
                            "Search Didn't Yield Proper Results"))
    except exceptions as e:
        msg = reader.error_lookup(e)
        results.append(("Messages Search", "Fail", msg))

    try:
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((
                By.LINK_TEXT, "Profile"))).click()
    except exceptions as e:
        msg = reader.error_lookup(e)
        results.append(("Profile Button", "Fail", msg))
    else:
        results.append(("Profile Button", "Pass", ""))

    try:
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((
                By.XPATH,
                ".//*[@id='ctl00_MainContent_accountInfo_TopTable_Row1_Cell1']"
                )))
    except exceptions as e:
        msg = reader.error_lookup(e)
        results.append(("Profile Page", "Fail", msg))
    else:
        results.append(("Profile Page", "Pass", ""))

    log_results(results)


def logout(driver):
    # LOGOUT #

    print("LOGOUT")
    results = []
    try:
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Logout"))).click()
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


def main(site, log_count):
    output_file = os.path.join(
        log_path, "member_demosite_automation_chrome_hxweb0" + str(log_count)
        + "_" + time.strftime("%m-%d-%H-%M") + ".log")
    output = open(output_file, 'w', encoding='utf-8')
    sys.stdout = output

    driver = webdriver.Chrome(
        executable_path='C:\Python34\Scripts\chromedriver.exe')

    start = time.time()
    driver.get(site)

    print("Chrome - hxweb0" + str(log_count) + "\n")

    login(driver)
    elig_dashboard(driver)
    balances(driver)
    claims_dashboard(driver)
    payments(driver)
    authorizations(driver)
    provider(driver)
    wellness(driver)
    side_menu(driver)
    messages(driver)
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
