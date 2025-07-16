from selenium.webdriver.common.by import By
import time

def username_selector(driver):
  return driver.find_element(By.ID, "user_name")

def password_selector(driver):
  return driver.find_element(By.ID, "user_password")

def login_button_selector(driver):
    return driver.find_element(By.ID, "sysverb_login")

def logIn(driver):
  driver.switch_to.frame('gsft_main')
  username_selector(driver).send_keys("test.automate")
  password_selector(driver).send_keys("Ten0nAutomat1on!")
  login_button_selector(driver).click()
  time.sleep(2)

def shadow_root_selector(driver):
    macroponent_0 = driver.execute_script('return document.querySelector("macroponent-355f43e047f8f510b0361ae8036d4355")')
    macroponent_0_root = driver.execute_script('return arguments[0].shadowRoot', macroponent_0)

    macroponent_root_div = macroponent_0_root.find_element(By.CSS_SELECTOR, "div[style='display: contents;']")

    macroponent_1 = driver.execute_script('return arguments[0].querySelector("macroponent-67ee2538534501108135ddeeff7b121b")', macroponent_root_div)

    sn_canvas_root = driver.execute_script('return arguments[0].querySelector("sn-canvas-root")', macroponent_1)

    sn_canvas_layout = driver.execute_script('return arguments[0].querySelector("sn-canvas-layout")', sn_canvas_root)

    sn_layout = driver.execute_script('return arguments[0].querySelector("sn-layout")', sn_canvas_layout)

    cadso_nav_header = driver.execute_script('return arguments[0].querySelector("cadso-nav-header")', sn_layout)
    
    return cadso_nav_header

def header_title_selector(driver):
    cadso_nav_header_root = driver.execute_script('return arguments[0].shadowRoot', shadow_root_selector(driver))

    header_title = cadso_nav_header_root.find_element(By.CSS_SELECTOR, "h1[class='title']")

    return header_title

def avatar_container_selector(driver):
    cadso_nav_avatar = driver.execute_script('return arguments[0].querySelector("cadso-nav-avatar")', shadow_root_selector(driver))

    cadso_nav_avatar_root = driver.execute_script('return arguments[0].shadowRoot', cadso_nav_avatar)

    avatarContainer = cadso_nav_avatar_root.find_element(By.CSS_SELECTOR, "div[class='avatar-component-container']")

    return avatarContainer

