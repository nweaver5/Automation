from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

def driver_setup():
    driver = webdriver.Chrome()
    return driver

def headless_driver_setup():
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")

    service = Service(executable_path = "./chromedriver")
    return webdriver.Chrome(options=chrome_options)