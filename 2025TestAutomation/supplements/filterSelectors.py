from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from TestAutomation.supplements.loginSelectors import *

import time


def tasks_side_selector(driver):
   cadso_ui_menu = driver.execute_script('return arguments[0].querySelector("cadso-ui-menu")', shadow_root_selector(driver))
   cadso_ui_menu_root = driver.execute_script('return arguments[0].shadowRoot', cadso_ui_menu)
   cadso_menu = cadso_ui_menu_root.find_element(By.CSS_SELECTOR, "div[class='cadso-menu']")
   cadso_menu_container = cadso_menu.find_element(By.CSS_SELECTOR, "div[class='cadso-menu-container']")
   
   return cadso_menu_container

def filter_selector(driver):
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
    now_uxf_page_simple_container3 = driver.execute_script('return arguments[0].querySelector("now-uxf-page-simple-container")', now_uxf_page_simple_container_div2)
    now_uxf_page_simple_container_div3 = now_uxf_page_simple_container3.find_element(By.CSS_SELECTOR, "div")
    now_uxf_page_simple_container4 = driver.execute_script('return arguments[0].querySelector("now-uxf-page-simple-container")', now_uxf_page_simple_container_div3)
    now_uxf_page_simple_container_div4 = now_uxf_page_simple_container4.find_element(By.CSS_SELECTOR, "div")
    cadso_complex_list_filter = driver.execute_script('return arguments[0].querySelector("cadso-complex-list-filter")', now_uxf_page_simple_container_div4)
    cadso_complex_list_filter_root = driver.execute_script('return arguments[0].shadowRoot', cadso_complex_list_filter)

    cadso_complex_list_filter_root_div = cadso_complex_list_filter_root.find_element(By.CSS_SELECTOR, "div")

    return cadso_complex_list_filter_root_div

def createFilter(driver, rowNumber, fieldCondition, operationCondition, optionCondition):
  actions = ActionChains(driver)
  cadso_complex_list_filter_root_div = filter_selector(driver)

  # Creating Filter
  custom_filter_container_open = cadso_complex_list_filter_root_div.find_element(By.CSS_SELECTOR, "div[class='custom-filter-container open']")
  custom_filter_header = custom_filter_container_open.find_element(By.CSS_SELECTOR, "div[class='custom-filter-header']")
  createNewFilterButton = custom_filter_header.find_element(By.CSS_SELECTOR, "button")

  createNewFilterButton.click()
  driver.implicitly_wait(30)
  time.sleep(1)

  complex_filter_container_open = cadso_complex_list_filter_root_div.find_element(By.CSS_SELECTOR, "div[class='complex-filter-container open']")
  complex_filter_body = complex_filter_container_open.find_element(By.CSS_SELECTOR, "div[class='complex-filter-body ']")
  complex_filter_add_filter_container = complex_filter_body.find_element(By.CSS_SELECTOR, "div[class='complex-filter-add-filter-container']")
  addConditionButton = complex_filter_add_filter_container.find_element(By.CSS_SELECTOR, "div[class='complex-filter-add-filter-button']")
  addConditionButton.click()
  driver.implicitly_wait(30)
  time.sleep(1)

  complex_filter_rows = complex_filter_body.find_elements(By.CSS_SELECTOR, "div[class='complex-filter-row']")
  complex_filter_row = complex_filter_rows[rowNumber]
  complex_filter = complex_filter_row.find_element(By.CSS_SELECTOR, "div[class='complex-filter']")
  select_inputs = complex_filter.find_element(By.CSS_SELECTOR, "div[class='select-inputs']")

  # Field Condition
  complex_filter_select_field_container = select_inputs.find_element(By.CSS_SELECTOR, "div[class='complex-filter-select-field-container']")
  complex_filter_search_input_container0 = complex_filter_select_field_container.find_element(By.CSS_SELECTOR, "div[class='complex-filter-search-input-container']")
  dropDownArrow0 = complex_filter_search_input_container0.find_element(By.CSS_SELECTOR, "div[class='complex-filter-search-input-icon'")
  dropDownArrow0.click()
  driver.implicitly_wait(30)
  time.sleep(1)

  complex_filter_select_field_drop_down_open = complex_filter_select_field_container.find_element(By.CSS_SELECTOR, "div[class='complex-filter-select-field-drop-down open']")
  listOfFields = complex_filter_select_field_drop_down_open.find_element(By.CSS_SELECTOR, "div")
  xpath0 = "div[text()= '%s']" % (fieldCondition)
  fieldOption = listOfFields.find_element(By.XPATH, xpath0)
  actions.move_to_element(fieldOption).perform()
  fieldOption.click()
  driver.implicitly_wait(30)
  time.sleep(1)

  # Operation Condition
  complex_filter_select_operation_container = select_inputs.find_element(By.CSS_SELECTOR, "div[class='complex-filter-select-operation-container']")
  complex_filter_search_input_container1 = complex_filter_select_operation_container.find_element(By.CSS_SELECTOR, "div[class='complex-filter-search-input-container']")
  dropDownArrow1 = complex_filter_search_input_container1.find_element(By.CSS_SELECTOR, "div[class='complex-filter-search-input-icon'")
  dropDownArrow1.click()
  driver.implicitly_wait(30)
  time.sleep(1)

  complex_filter_select_operation_drop_down_open = complex_filter_select_operation_container.find_element(By.CSS_SELECTOR, "div[class='complex-filter-select-operation-drop-down open']")
  xpath1 = "div[text()= '%s']" % (operationCondition)
  operationOption = complex_filter_select_operation_drop_down_open.find_element(By.XPATH, xpath1)
  actions.move_to_element(operationOption).perform()
  operationOption.click()
  driver.implicitly_wait(30)
  time.sleep(1)

  # Option Condition
  complex_filter_select_option_container = select_inputs.find_element(By.CSS_SELECTOR, "div[class='complex-filter-select-option-container']")

  if (fieldCondition == "Story Points"):
    complex_filter_string_container = complex_filter_select_option_container.find_element(By.CSS_SELECTOR, "div[class='complex-filter-string-container']")
    complex_filter_string_input = complex_filter_string_container.find_element(By.CSS_SELECTOR, "input[class='complex-filter-string-input']")
    complex_filter_string_input.send_keys("2")
  else:
    complex_filter_option_container = complex_filter_select_option_container.find_element(By.CSS_SELECTOR, "div[class='complex-filter-option-container']")
    complex_filter_search_input_container_select_option = complex_filter_option_container.find_element(By.CSS_SELECTOR, "div[class='complex-filter-search-input-container selectOption']")
    dropDownArrow2 = complex_filter_search_input_container_select_option.find_element(By.CSS_SELECTOR, "div[class='complex-filter-search-input-icon'")
    dropDownArrow2.click()
    time.sleep(1)

    complex_filter_select_option_drop_down_open = complex_filter_option_container.find_element(By.CSS_SELECTOR, "div[class='complex-filter-select-option-drop-down open']")

    dropDownOptions = complex_filter_select_option_drop_down_open.find_elements(By.CSS_SELECTOR, "div[class='complex-filter-select-option-drop-down-options']")

    for e in dropDownOptions:
      if optionCondition == e.text:
        optionOption = e
    actions.move_to_element(optionOption).perform()
    optionOption.click()
    driver.implicitly_wait(30)
  
  time.sleep(1)

def saveCondition(driver):
  # Saving Filter
  cadso_complex_list_filter_root_div = filter_selector(driver)
  complex_filter_container_open = cadso_complex_list_filter_root_div.find_element(By.CSS_SELECTOR, "div[class='complex-filter-container open']")
  complex_filter_body = complex_filter_container_open.find_element(By.CSS_SELECTOR, "div[class='complex-filter-body ']")
  complex_filter_footer = complex_filter_body.find_element(By.CSS_SELECTOR, "div[class='complex-filter-footer']")
  complex_filter_footer_buttons = complex_filter_footer.find_element(By.CSS_SELECTOR, "div[class='complex-filter-footer-buttons']")
  complex_filter_footer_butns = complex_filter_footer_buttons.find_element(By.CSS_SELECTOR, "div[class='complex-filter-btns']")
  saveFilterButton = complex_filter_footer_butns.find_element(By.CSS_SELECTOR, "button[class='complex-btn save']")
  saveFilterButton.click()
  driver.implicitly_wait(30)
  time.sleep(1)

def addACondition(driver):
  cadso_complex_list_filter_root_div = filter_selector(driver)
  complex_filter_container_open = cadso_complex_list_filter_root_div.find_element(By.CSS_SELECTOR, "div[class='complex-filter-container open']")
  complex_filter_body = complex_filter_container_open.find_element(By.CSS_SELECTOR, "div[class='complex-filter-body ']")
  complex_filter_add_filter_container = complex_filter_body.find_element(By.CSS_SELECTOR, "div[class='complex-filter-add-filter-container']")
  complex_filter_add_filter_button = complex_filter_add_filter_container.find_element(By.CSS_SELECTOR, "div[class='complex-filter-add-filter-button']")
  complex_filter_add_filter_button.click()
  driver.implicitly_wait(30)
  time.sleep(1)

# TODO: Find out how to find Access option by text
def saveFilter(driver, name, access):
  actions = ActionChains(driver)
  cadso_complex_list_filter_root_div = filter_selector(driver)
  custom_filter_modal_container_open = cadso_complex_list_filter_root_div.find_element(By.CSS_SELECTOR, "div[class='custom-filter-modal-container open']")
  custom_filter_modal = custom_filter_modal_container_open.find_element(By.CSS_SELECTOR, "div[class='custom-filter-modal']")
  custom_filter_modal_body = custom_filter_modal.find_element(By.CSS_SELECTOR, "div[class='custom-filter-modal-body']")
  custom_filter_modal_content = custom_filter_modal_body.find_element(By.CSS_SELECTOR, "div[class='custom-filter-modal-content']")
  modal_input_container = custom_filter_modal_content.find_element(By.CSS_SELECTOR, "div[class='modal-input-container']")
  modal_input = modal_input_container.find_element(By.CSS_SELECTOR, "div[class='modal-input']")
  modal_input_text = modal_input.find_element(By.CSS_SELECTOR, "input")

  modal_input_text.send_keys(name)
  driver.implicitly_wait(30)
  time.sleep(1)

  custom_filter_modal_body_access = custom_filter_modal_content.find_element(By.CSS_SELECTOR, "div[class='custom-filter-modal-body-access']")
  access_menu_container = custom_filter_modal_body_access.find_element(By.CSS_SELECTOR, "div[class='access-menu-container']")
  modal_access_menu = access_menu_container.find_element(By.CSS_SELECTOR, "div[class='modal-access-menu']")
  modal_access_menu.click()
  time.sleep(1)

  dropdown_access_active = modal_access_menu.find_element(By.CSS_SELECTOR, "div[class='dropdown access active']")
  dropdown_menu_access = dropdown_access_active.find_element(By.CSS_SELECTOR, "div[class='dropdown-menu access']")
  dropdown_body = dropdown_menu_access.find_element(By.CSS_SELECTOR, "div[class='dropdown-body']")

  listOfAccess = dropdown_body.find_elements(By.CSS_SELECTOR, "div[class='dropdown-options access']")
  
  # for e in listOfAccess:
  #   if access == e.text:
  #     actions.move_to_element(e).perform()
  #     e.click()
  
  if access == "Everyone":
    listOfAccess[2].click()
  if access == "Private":
    listOfAccess[0].click()

  custom_filter_modal_footer = custom_filter_modal.find_element(By.CSS_SELECTOR, "div[class='custom-filter-modal-footer']")
  saveFilterButton1 = custom_filter_modal_footer.find_element(By.CSS_SELECTOR, "button[class='custom-filter-modal-save']")
  saveFilterButton1.click()
  driver.implicitly_wait(30)
  time.sleep(1)

def clearFilter(driver, flag):
  cadso_complex_list_filter_root_div = filter_selector(driver)
  complex_filter_container_open = cadso_complex_list_filter_root_div.find_element(By.CSS_SELECTOR, "div[class='complex-filter-container open']")
  complex_filter_body_saved_condition_body = complex_filter_container_open.find_element(By.CSS_SELECTOR, "div[class='complex-filter-body saved-condition-body']")
  saved_condition_header = complex_filter_body_saved_condition_body.find_element(By.CSS_SELECTOR, "div[class='saved-condition-header']")
  saved_condition_remove = saved_condition_header.find_element(By.CSS_SELECTOR, "div[class='saved-condition-remove']")
  tooltip_container_filter_body = saved_condition_remove.find_element(By.CSS_SELECTOR, "div[class='tooltip-container']")
  littleX = tooltip_container_filter_body.find_element(By.CSS_SELECTOR, "button[class='saved-condition-remove-icon']")

  if flag:
    littleX.click()
    time.sleep(1)

  complex_filter_header = complex_filter_container_open.find_element(By.CSS_SELECTOR, "div[class='complex-filter-header']")
  complex_filter_exit = complex_filter_header.find_element(By.CSS_SELECTOR, "div[class='complex-filter-exit']")
  tooltip_container_filter_header = complex_filter_exit.find_element(By.CSS_SELECTOR, "div[class='tooltip-container']")
  bigX = tooltip_container_filter_header.find_element(By.CSS_SELECTOR, "button[class='complex-exit-btn']")
  bigX.click()
  time.sleep(1)

  if flag:
    filterButton = cadso_complex_list_filter_root_div.find_element(By.CSS_SELECTOR, "button")
    filterButton.click()
    time.sleep(1)

def savedFilter(driver, type):
  cadso_complex_list_filter_root_div = filter_selector(driver)
  custom_filter_container_open = cadso_complex_list_filter_root_div.find_element(By.CSS_SELECTOR, "div[class='custom-filter-container open']")

  if (type == "Public"):
    custom_filter_list_custom_filter_list_public_filters = custom_filter_container_open.find_element(By.CSS_SELECTOR, "div[class='custom-filter-list custom-filter-list-public filters']")
    custom_filters_list = custom_filter_list_custom_filter_list_public_filters.find_element(By.CSS_SELECTOR, "div[class='custom-filters-list']")
  else:
    custom_filter_list_custom_filter_list_private_filters = custom_filter_container_open.find_element(By.CSS_SELECTOR, "div[class='custom-filter-list custom-filter-list-private filters']")
    custom_filters_list = custom_filter_list_custom_filter_list_private_filters.find_element(By.CSS_SELECTOR, "div[class='custom-filters-list']")
  
  custom_filters_item = custom_filters_list.find_element(By.CSS_SELECTOR, "div[class='custom-filters-item']")
  custom_filters_item_name = custom_filters_item.find_element(By.CSS_SELECTOR, "div[class='custom-filters-item-name']")
  tooltip_container_filter_list = custom_filters_item_name.find_element(By.CSS_SELECTOR, "div[class='tooltip-container']")
  custom_filters_item_name_text = tooltip_container_filter_list.find_element(By.CSS_SELECTOR, "div[class='custom-filters-item-name-text']")
  return custom_filters_item_name_text

def verifyPrivate(driver, name):
  filter = savedFilter(driver, "Private")
  actualName = filter.text
  if name == actualName:
    print("Private filter success.")

def verifyPublic(driver, name):
  filter = savedFilter(driver, "Public")
  actualName = filter.text
  if name == actualName:
    print("Public filter success.")