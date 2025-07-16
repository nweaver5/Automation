import { By } from "selenium-webdriver";
import assert from "assert";
import { CADSO_MENU_SELECTOR, COMPLEX_FILTER_SELECTORS, TASK_LIST_SELECTORS } from "./constants.js";
import * as filterHelpers from "./helpers.js";
import * as universalHelpers from "../Universal/helpers.js";


async function selectPrivateFilter(driver) {
  try {
    const privateFilterListItems = await driver.executeScript(
      COMPLEX_FILTER_SELECTORS.PRIVATE_SAVED_FILTERS_LIST_SELECTOR
    );
    let filterFound = false;
    for (let i = 0; i < privateFilterListItems.length; i++) {
      if (
        (await privateFilterListItems[i].getText()) ===
        "Automation Filter Private"
      ) {
        filterFound = true;
        await driver.actions().click(privateFilterListItems[i]).perform();
        break;
      }
    }
    assert(filterFound === true, "Saved filter not found");

  } catch (error) {
    console.error(error, "Verify Filter Failed");
    await universalHelpers.takeScreenshot(driver);
    await driver.quit();
  }
}

async function changeFilter(driver){

  await filterHelpers.selectDropdownValue(
    driver,
    "is",
    filterHelpers.getComplexFilterRowAndField(0, "operation"),
    1
  );

  let input = await driver.executeScript(
    `return ${COMPLEX_FILTER_SELECTORS.COMPLEX_FILTER_CONTAINER}.querySelector(".complex-filter-search-input-container.selectOption").querySelector("input")`
  );
  await driver.executeScript("arguments[0].value='';", input);
  await driver
    .actions()
    .sendKeys(input, "Open")
    .perform();
  await universalHelpers.sleep(1000);

  await filterHelpers.selectDropdownValue(
    driver,
    "Open",
    filterHelpers.getComplexFilterRowAndField(0, "option"),
    2
  );
  await universalHelpers.sleep(5000);

  universalHelpers.clickOn(driver, COMPLEX_FILTER_SELECTORS.CUSTOM_FILTER_SAVE_CHANGES_SELECTOR, 1000);

  universalHelpers.clickOn(driver, COMPLEX_FILTER_SELECTORS.CLOSE_BUTTON_SELECTOR, 1000);
}

async function verifyData(driver, number) {
  try {
    let totalTasks = await driver.executeScript(
      TASK_LIST_SELECTORS.ACTIONS_TOTAL_NUM_SELECTED_SELECTOR
    );
    let totalTasksText = await totalTasks.getText();
    let matches = totalTasksText.match(/(\d+)/);

    assert(matches[0] == number);

  } catch (error) {
    console.error(error, "Unable to verify data");
  }
}

export default async function editSavedFilter(driver) {
  try {
    // Navigating to Tasks
    const cadsoUiMenu = await driver.executeScript(CADSO_MENU_SELECTOR);
    const sideNavItems = await cadsoUiMenu.findElements(By.tagName("button"));
    await driver.actions().click(sideNavItems[2]).perform();
    await universalHelpers.sleep(5000);

    // Clicking on Filter button
    const cadsoComplexListFilter = await driver.executeScript(
      `return ${COMPLEX_FILTER_SELECTORS.CADSO_COMPLEX_LIST_FILTER}`
    );
    
    const filterButton = await cadsoComplexListFilter.findElement(
      By.css(".complex-filter-button ")
    );
    await driver.actions().click(filterButton).perform();
    await universalHelpers.sleep(1000);

    // Selecting Automation Private Filter
    selectPrivateFilter(driver);
    await universalHelpers.sleep(1000);
    
    changeFilter(driver);
    await universalHelpers.sleep(10000);

    // Clicking Select 
    universalHelpers.clickOn(driver, TASK_LIST_SELECTORS.SELECT_ALL_CHECKBOX_SELECTOR);
    await universalHelpers.sleep(1000);

    // Verifying data
    verifyData(driver, 25);

    // Unselecting
    universalHelpers.clickOn(driver, TASK_LIST_SELECTORS.SELECT_ALL_CHECKBOX_SELECTOR);
    await universalHelpers.sleep(1000);

    // Clicking Filter
    await driver.actions().click(filterButton).perform();
    await universalHelpers.sleep(2000);

    // Clearing Filter
    universalHelpers.clickOn(driver, COMPLEX_FILTER_SELECTORS.SAVED_FILTER_CLOSE_BUTTON_SELECTOR, 1000);

    //Closing Filter Pop up
    universalHelpers.clickOn(driver, COMPLEX_FILTER_SELECTORS.CLOSE_BUTTON_SELECTOR, 1000);

    console.log("Edit Saved Filter successful.")
  } catch (error) {
    console.error(error, "Edit Saved Filter failed.");
    await universalHelpers.takeScreenshot(driver);
    await driver.quit();
  }
}
