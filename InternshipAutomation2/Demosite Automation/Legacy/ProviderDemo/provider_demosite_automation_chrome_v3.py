import time
import os
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException as exceptions
from tabulate import tabulate
from Utility.error_reader import reader

userProfile = os.environ['USERPROFILE']
scriptPath = os.path.dirname(userProfile +
    '\\Documents\\QA-Automation\\Demosite Automation\\ProviderDemo\\ChromeLogs\\')
log_count = 1
sites = [
    'https://hxweb01.healthx.com/provider_template.aspx',
    'https://hxweb02.healthx.com/provider_template.aspx',
    'https://hxweb03.healthx.com/provider_template.aspx',
    'https://hxweb04.healthx.com/provider_template.aspx',
    'https://hxweb05.healthx.com/provider_template.aspx',
    'https://hxweb06.healthx.com/provider_template.aspx',
    'https://hxweb07.healthx.com/provider_template.aspx'
]


def print_log_label(results):
    print(tabulate(results,
                   headers=["Section", "Result", "Comment"],
                   tablefmt="fancy_grid"))


def return_home(driver):
    results = []
    try:
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((
                By.XPATH, ".//*[@id='hxUserMenu']/li[1]/a"))).click()
    except exceptions:
        results.append((
            "Home Button", "Fail", "Element Not Located After 5 Seconds"))
        print_log_label(results)
        driver.quit()
    else:
        results.append(("Home Button", "Pass", ""))
    print_log_label(results)


def login(driver):
    print("LOGIN")
    results = []
    try:
        driver.find_element_by_id(
            "username").send_keys('plan.provider.template')
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
    else:
        results.append(("Login", "Pass", ""))

    print_log_label(results)


def eligibility(driver):
    # ELIGIBILITY SECTION #

    print("ELIGIBILITY SECTION")
    results = []
    detail_XPATH = """
    //*[@id='aspnetForm']/div[5]/div[3]/div[3]/div[3]/div[1]/table[1]/tbody/tr[4]/td[4]
    """
    elig_link_XPATH = """
        //*[@id='aspnetForm']/div[5]/div[2]/div/table/tbody/tr[5]/td[1]/p/a
        """

    memberID_XPATH = """
        //*[@id='aspnetForm']/div[5]/div[2]/div/table/tbody/tr[5]/td[4]/p
        """

    try:
        viewAllPatientsLink = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((
                By.LINK_TEXT, "View All Patients")))
        viewAllPatientsLink.click()
    except exceptions as e:
        msg = reader.error_lookup(e)
        results.append(("Provider Dashboard", "Fail", msg))
    try:
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, "eligSearchHeader")))
        driver.find_element_by_xpath(".//*[@id='hxUserMenu']/li[1]/a").click()
    except exceptions as e:
        msg = reader.error_lookup(e)
        results.append(("Eligibility Header", "Fail", msg))
    else:
        results.append(("Eligibility Header", "Pass", ""))

        try:
            elig_link = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, elig_link_XPATH)))
            memberID = driver.find_element_by_xpath(
                memberID_XPATH).text
            WebDriverWait(driver, 10).until_not(
                    lambda s: s.find_element_by_class_name(
                        'hppModalBackground').is_displayed())
            elig_link.click()
            elig_check = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((
                    By.XPATH, detail_XPATH)))
        except exceptions as e:
            msg = reader.error_lookup(e)
            results.append(("Elig Link " + elig_link.text, "Fail", msg))

        try:
            if memberID == elig_check.text:
                results.append(("Elig Link " + memberID, "Pass", ""))
                driver.back()
            else:
                results.append((
                    "Elig Link " + memberID,
                    "Fail", "Link Went To Incorrect Page"))
                driver.back()
        except exceptions as e:
            msg = reader.error_lookup(e)
            results.append(("Elig Link " + memberID, "Fail", msg))
            driver.back()

        WebDriverWait(driver, 10).until_not(
            lambda s: s.find_element_by_class_name(
                'hppModalBackground').is_displayed())
        try:
            WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((
                    By.ID, "memberID"))).send_keys('11111111100')
        except exceptions as e:
            msg = reader.error_lookup(e)
            results.append((
                "Elig Search", "Fail", msg))
        else:
            WebDriverWait(driver, 10).until_not(
                lambda s: s.find_element_by_class_name(
                    'hppModalBackground').is_displayed())
            driver.find_element_by_xpath(
                ".//*[@id='aspnetForm']/div[5]/div[1]/div[1]/div/div[6]/button"
                ).click()
            time.sleep(3)
            search_XPATH = """
            .//*[@id='aspnetForm']/div[5]/div[2]/div/table/tbody/tr[2]/td[4]/p
            """
            eligSearchCheck = driver.find_element_by_xpath(search_XPATH).text

            if eligSearchCheck == '11111111100':
                results.append(("Elig Search", "Pass", ""))
            else:
                results.append((
                    "Elig Search",
                    "Fail",
                    "Search Resulted In Incorrect Account"))

    print_log_label(results)
    return_home(driver)


def newsletter(driver):
    # NEWSLETTER ITEM #
    print("NEWSLETTER SECTION")
    results = []

    try:
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((
                By.LINK_TEXT, "Spring Newsletter")))
    except exceptions as e:
        msg = reader.error_lookup(e)
        results.append(("Newsletter Content Item", "Fail", msg))
    else:
        results.append(("Newsletter Content Item", "Pass", ""))
    print_log_label(results)


def payments(driver):
    # PAYMENTS SECTION #
    print("PAYMENTS SECTION")
    results = []
    try:
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((
                By.XPATH, ".//*[@id='hxUserMenu']/li[3]/a"))).click()
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((
                By.XPATH,
                ".//*[@id='svc_132fe0b2-1ce3-484a-adeb-4272ae2b374f']/a"
                ))).click()
    except exceptions as e:
        msg = reader.error_lookup(e)
        results.append(("Payments Link", "Fail", msg))
    else:
        results.append(("Payments Link", "Pass", ""))

        time.sleep(1)

        try:
            WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((
                    By.XPATH,
                    ".//*[@id='aspnetForm']/div[3]/div[1]/div/div[4]/button"
                    ))).click()
        except exceptions as e:
            msg = reader.error_lookup(e)
            results.append(("Payments Search Button", "Fail", msg))
        else:
            results.append(("Payments Search Button", "Pass", ""))

            time.sleep(1)
            results_XPATH = """
            .//*[@id='aspnetForm']/div[3]/div[2]/div/table/tbody/tr[2]/td[1]
            """
            try:
                WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((
                        By.XPATH, results_XPATH)))
            except exceptions as e:
                msg = reader.error_lookup(e)
                results.append(("Payments Search Results", "Fail", msg))
            else:
                results.append(("Payments Search Results", "Pass", ""))

    print_log_label(results)
    return_home(driver)


def claims(driver):
    # CLAIMS SECTION #
    print("CLAIMS SECTION")
    results = []
    try:
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((
                By.XPATH, ".//*[@id='hxUserMenu']/li[4]/a"))).click()
    except exceptions as e:
        msg = reader.error_lookup(e)
        results.append(("Claims Button", "Fail", msg))
        print_log_label(results)
        driver.quit()
    else:
        results.append(("Claims Button", "Pass", ""))

        time.sleep(1)

        try:
            WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((
                    By.ID, "claimNumbers"))).send_keys('N636186001')
        except exceptions as e:
            msg = reader.error_lookup(e)
            results.append(("Claims Search", "Fail", msg))
        else:
            results.append(("Claims Search", "Pass", ""))

            time.sleep(1)

            try:
                WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.ID, "searchControl")))
            except exceptions as e:
                msg = reader.error_lookup(e)
                results.append(("Claims Search Button", "Fail", msg))
            else:
                results.append(("Claims Search Button", "Pass", ""))

                time.sleep(1)

                try:
                    WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located((
                            By.LINK_TEXT, "N636186001"))).click()
                except exceptions as e:
                    msg = reader.error_lookup(e)
                    results.append(("Claims Search Results", "Fail", msg))
                else:
                    results.append(("Claims Search Results", "Pass", ""))

                    time.sleep(1)

                    try:
                        claimsSearchCheck = WebDriverWait(driver, 5).until(
                            EC.presence_of_element_located((
                                By.XPATH,
                                ".//*[@id='viewArea']/div[1]/div/h3"))).text

                        if claimsSearchCheck == "Claim #N636186001":
                            results.append((
                                "Claims Search Results Page", "Pass", ""))
                        else:
                            results.append((
                                "Claims Search Results Page",
                                "Fail",
                                "Search Resulted In Incorrect Claim"))
                    except exceptions as e:
                        msg = reader.error_lookup(e)
                        results.append((
                            "Claims Search Results Page", "Fail", msg))

    print_log_label(results)
    return_home(driver)


def authorizations(driver):
    # AUTHORIZATIONS SECTION #
    print("AUTHORIZATIONS SECTION")
    results = []
    try:
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((
                By.XPATH, ".//*[@id='hxUserMenu']/li[5]/a"))).click()
    except exceptions as e:
        msg = reader.error_lookup(e)
        results.append(("Auth Button", "Fail", msg))
        print_log_label(results)
        driver.quit()
    else:
        results.append(("Auth Button", "Pass", ""))

        time.sleep(3)

        try:
            WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((
                    By.ID, "searchControl"))).click()
        except exceptions as e:
            msg = reader.error_lookup(e)
            results.append(("Auth Search Button", "Fail", msg))
        else:
            results.append(("Auth Search Button", "Pass", ""))

            time.sleep(1)
            auth_results_XPATH = """
            .//*[@id='resultContainer']/table/tbody/tr[2]/td[1]/p/a
            """
            try:
                authResultsLink = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((
                        By.XPATH, auth_results_XPATH)))
                authResultsLinkText = authResultsLink.text
                authResultsLink.click()
            except exceptions as e:
                msg = reader.error_lookup(e)
                results.append(("Auth Search Results", "Fail", msg))
            else:
                results.append(("Auth Search Results", "Pass", ""))

                driver.switch_to_active_element()

                time.sleep(1)

                try:
                    authResultsCheck = WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located((
                            By.XPATH,
                            ".//*[@id='viewArea']/table[1]/tbody/tr/td[2]"
                            ))).text

                    if authResultsCheck == authResultsLinkText:
                        results.append((
                            "Auth Search Results Page", "Pass", ""))
                    else:
                        results.append((
                            "Auth Search Results Page",
                            "Fail",
                            "Search Resulted In Incorrect Claim"))
                except exceptions as e:
                    msg = reader.error_lookup(e)
                    results.append(("Auth Search Results Page", "Fail", msg))

                time.sleep(1)

                try:
                    driver.find_element_by_xpath(
                        "html/body/div[4]/div[1]/a").click()
                except exceptions as e:
                    msg = reader.error_lookup(e)
                    results.append(("Exit Button", "Fail", msg))
                    print_log_label(results)
                    driver.quit()

    print_log_label(results)
    return_home(driver)


def careplans(driver):
    # CARE PLAN #
    print("CARE PLAN")
    results = []
    try:
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((
                By.XPATH, ".//*[@id='hxUserMenu']/li[6]/a"))).click()
    except exceptions as e:
        msg = reader.error_lookup(e)
        results.append(("Care Plan Button", "Fail", msg))
        print_log_label(results)
        driver.quit()
    else:
        results.append(("Care Plan Button", "Pass", ""))

        time.sleep(1)

        try:
            WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((
                    By.ID, "memberID"))).send_keys('11111111100')
            WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((
                    By.ID, "dob"))).send_keys('01/05/1962')
        except exceptions as e:
            msg = reader.error_lookup(e)
            results.append(("Care Plan Data Fields", "Fail", msg))
        else:
            results.append(("Care Plan Data Fields", "Pass", ""))

            time.sleep(1)

            try:
                WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((
                        By.ID, "submit"))).click()
            except exceptions as e:
                msg = reader.error_lookup(e)
                results.append(("Care Plan Search", "Fail", msg))
            else:
                results.append(("Care Plan Search", "Pass", ""))

                time.sleep(1)

                try:
                    carePlanResults = WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located((
                            By.ID, "memberID_detail"))).text

                    if carePlanResults == '11111111100':
                        results.append(("Care Plan Results", "Pass", ""))
                    else:
                        results.append((
                            "Care Plan Results",
                            "Fail",
                            "Incorrect Search Results"))
                except exceptions as e:
                    msg = reader.error_lookup(e)
                    results.append(("Care Plan Results", "Fail", msg))

    print_log_label(results)
    return_home(driver)


def messages(driver):
    # MESSAGES AND PROFILE #
    print("MESSAGES AND PROFILE")
    results = []
    try:
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((
                By.XPATH,
                ".//*[@id='basicShell']/header/nav[1]/ul/li[1]/a"
                ))).click()
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

        results.append(("Messages Main Page", "Pass", ""))
        msg_saved_XPATH = """
        .//*[@id='ctl00_MainContent_uxMessagingOptions']/ul/li[3]/a
        """
        try:
            WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((
                    By.XPATH, msg_saved_XPATH))).click()
        except exceptions as e:
            msg = reader.error_lookup(e)
            results.append(("Messages Saved Page Link", "Fail", msg))
        else:
            results.append(("Messages Saved Page Link", "Pass", ""))

        msg_grid_XPATH = """
        .//*[@id='ctl00_MainContent_uxMessageGrid']/tbody/tr[2]/td[2]
        """
        try:
            WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((
                    By.XPATH, msg_grid_XPATH)))
        except exceptions as e:
            msg = reader.error_lookup(e)
            results.append(("Messages Saved Page", "Fail", msg))
        else:
            results.append(("Messages Saved Page", "Pass", ""))

        msg_search_XPATH = """
        .//*[@id='ctl00_MainContent_uxMessagingOptions']/ul/li[4]/a
        """
        try:
            WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((
                    By.XPATH, msg_search_XPATH))).click()
        except exceptions as e:
            msg = reader.error_lookup(e)
            results.append(("Messages Search Page Link", "Fail",  msg))

        results.append(("Messages Search Page Link", "Pass", ""))

        try:
            WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((
                    By.LINK_TEXT,
                    "Tracking Number Search"))).click()
        except exceptions as e:
            msg = reader.error_lookup(e)
            results.append(("Messages Search Page", "Fail", msg))

        results.append(("Messages Search Page", "Pass", ""))

        msg_search_box = """
        .//*[@id='ctl00_MainContent_uxTrackingNumberSearchForm_ctl02_uxTrackingNumberText_textbox']
        """
        msg_search_button = """
        .//*[@id='ctl00_MainContent_uxTrackingNumberSearchForm_ctl03_uxTrackingNumberSearchButton']
        """
        tracking_number = '3529347'
        try:
            WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((
                    By.XPATH, msg_search_box))).send_keys(tracking_number)
            WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((
                    By.XPATH, msg_search_button))).click()
        except exceptions as e:
            msg = reader.error_lookup(e)
            results.append(("Messages Search Button", "Fail", msg))
        else:
            results.append(("Messages Search Button", "Pass", ""))

        try:
            messagesSearchCheck = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((
                    By.XPATH,
                    ".//*[@id='ctl00_MainContent_uxInformationLabel']/b"
                    ))).text

            if messagesSearchCheck == "Tracking # 3529347":
                results.append(("Messages Search", "Pass", ""))
            else:
                results.append((
                    "Messages Search",
                    "Fail", "Search Didn't Yield Proper Results"))
        except exceptions as e:
            msg = reader.error_lookup(e)
            results.append(("Messages Search", "Fail", msg))

    try:
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Profile"))).click()
    except exceptions as e:
        msg = reader.error_lookup(e)
        results.append(("Profile Button", "Fail", msg))
    else:
        results.append(("Profile Button", "Pass", ""))
        profile_page_XPATH = """
        .//*[@id='ctl00_MainContent_accountInfo_TopTable_Row1_Cell1']
        """
        try:
            WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((
                    By.XPATH, profile_page_XPATH)))
        except exceptions as e:
            msg = reader.error_lookup(e)
            results.append(("Profile Page", "Fail", msg))
        else:
            results.append(("Profile Page", "Pass", ""))
    print_log_label(results)
    return_home(driver)


def logout(driver):
    # LOGOUT #
    results = []
    try:
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((
                By.LINK_TEXT, "Logout"))).click()
    except exceptions as e:
        msg = reader.error_lookup(e)
        results.append(("Logout Button", "Fail", msg))
        print_log_label(results)
        driver.quit()
    else:
        results.append(("Logout Button", "Pass", ""))

    try:
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((
                By.ID, "username")))
    except exceptions as e:
        msg = reader.error_lookup(e)
        results.append(("Logout", "Fail", msg))
    else:
        results.append(("Logout", "Pass", ""))

    print_log_label(results)


def main(site, log_count):
    outputFile = os.path.join(
        scriptPath,
        "provider_demosite_automation_chrome_hxweb0" + str(log_count) + "_"
        + time.strftime("%m-%d-%H-%M") + ".log")
    output = open(outputFile, 'w', encoding='utf-8')
    sys.stdout = output
    driver = webdriver.Chrome(
        executable_path='C:\Python34\Scripts\chromedriver.exe')

    start = time.time()
    driver.get(site)

    print("Chrome - hxweb0" + str(log_count) + "\n")
    login(driver)
    eligibility(driver)
    newsletter(driver)
    payments(driver)
    claims(driver)
    authorizations(driver)
    careplans(driver)
    messages(driver)
    logout(driver)

    end = time.time() - start
    print("\nTotal Elapsed Test Time %.2f" % end)

    output.close()
    sys.stdout = sys.__stdout__
    driver.quit()
    log_count = log_count + 1
    return log_count

for site in sites:
    log_count = main(site, log_count)
