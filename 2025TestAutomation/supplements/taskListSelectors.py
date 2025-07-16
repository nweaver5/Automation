from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from TestAutomation.supplements.loginSelectors import *

import time

def taskList_selector(driver):
    sn_canvas_main = driver.execute_script('return arguments[0].querySelector("sn-canvas-main")', shadow_root_selector(driver))
    sn_canvas_main_root = driver.execute_script('return arguments[0].shadowRoot', sn_canvas_main)
    sn_canvas_main_root_main = sn_canvas_main_root.find_element(By.CSS_SELECTOR, "main")
    sn_canvas_screens = driver.execute_script('return arguments[0].querySelectorAll("sn-canvas-screen")', sn_canvas_main_root_main)
    sn_canvas_screen = sn_canvas_screens[-1]
    sn_canvas_screen_root = driver.execute_script('return arguments[0].shadowRoot', sn_canvas_screen)
    sn_canvas_screen_section = sn_canvas_screen_root.find_element(By.CSS_SELECTOR, "section")
    screen_action_transformer = driver.execute_script('return arguments[0].querySelector("screen-action-transformer-de33ea8647a86110a1052a02e26d434f")', sn_canvas_screen_section)
    macroponent0 = driver.execute_script('return arguments[0].querySelector("macroponent-d633ea8647a86110a1052a02e26d434d")', screen_action_transformer)
    macroponent_root = driver.execute_script('return arguments[0].shadowRoot', macroponent0)
    macroponent_root_div = macroponent_root.find_element(By.CSS_SELECTOR, "div[style='display: contents;']")
    macroponent1 = driver.execute_script('return arguments[0].querySelector("macroponent-67ee2538534501108135ddeeff7b121b")', macroponent_root_div)
    now_uxf_page = driver.execute_script('return arguments[0].querySelector("now-uxf-page")', macroponent1)
    now_uxf_page_div = now_uxf_page.find_element(By.CSS_SELECTOR, "div")
    now_uxf_page_simple_container0 = driver.execute_script('return arguments[0].querySelector("now-uxf-page-simple-container")', now_uxf_page_div)
    now_uxf_page_simple_container_div0 = now_uxf_page_simple_container0.find_element(By.CSS_SELECTOR, "div")
    now_uxf_page_simple_container1 = driver.execute_script('return arguments[0].querySelector("now-uxf-page-simple-container")', now_uxf_page_simple_container_div0)
    now_uxf_page_simple_container_div1 = now_uxf_page_simple_container1.find_element(By.CSS_SELECTOR, "div")
    now_uxf_page_simple_container2 = driver.execute_script('return arguments[0].querySelector("now-uxf-page-simple-container")', now_uxf_page_simple_container_div1)
    now_uxf_page_simple_container_div2 = now_uxf_page_simple_container2.find_element(By.CSS_SELECTOR, "div")

    cadso_ui_list = driver.execute_script('return arguments[0].querySelector("cadso-ui-list")', now_uxf_page_simple_container_div2)

    cadso_ui_list_root = driver.execute_script('return arguments[0].shadowRoot', cadso_ui_list)

    return cadso_ui_list_root
