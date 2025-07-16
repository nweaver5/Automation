import { By } from "selenium-webdriver";
import assert from "assert";
import {
  CADSO_MENU_SELECTOR,
  COMPLEX_FILTER_SELECTORS,
  TASK_LIST_SELECTORS,
} from "./constants.js";
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

async function selectPublicFilter(driver) {
  try {
    const publicFilterListItems = await driver.executeScript(
      COMPLEX_FILTER_SELECTORS.PUBLIC_SAVED_FILTERS_LIST_SELECTOR
    );
    let filterFound = false;
    for (let i = 0; i < publicFilterListItems.length; i++) {
      if (
        (await publicFilterListItems[i].getText()) ===
        "Automation Filter Public"
      ) {
        filterFound = true;
        await driver.actions().click(publicFilterListItems[i]).perform();
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

async function verifyData(driver, number) {
  try {
    let totalTasks = await driver.executeScript(
      TASK_LIST_SELECTORS.ACTIONS_TOTAL_NUM_SELECTED_SELECTOR
    );
    let totalTasksText = await totalTasks.getText();
    let matches = totalTasksText.match(/(\d+)/);
    assert(matches[0] == number, "Incorrect data number.");
    
  } catch (error) {
    console.error(error, "Unable to verify data");
  }
}

export default async function selectAndSwapFilter(driver) {
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
    // Closing Filter Pop up
    let closeFilterButton = await driver.executeScript(
      COMPLEX_FILTER_SELECTORS.CLOSE_BUTTON_SELECTOR
    );
    await driver.actions().click(closeFilterButton).pause(1000).perform();

    //Clicking Select
    let selectAll = await driver.executeScript(
      TASK_LIST_SELECTORS.SELECT_ALL_CHECKBOX_SELECTOR
    );
    await driver.actions().click(selectAll).perform();
    await universalHelpers.sleep(1000);

    //Verifying Data
    verifyData(driver, 25);
    await universalHelpers.sleep(1000);

    // Unselecting All
    await driver.actions().click(selectAll).perform();
    await universalHelpers.sleep(1000);

    // Clicking Filter
    await driver.actions().click(filterButton).perform();
    await universalHelpers.sleep(2000);

    // Clearing Private Filter
    const savedFilterCloseButton = await driver.executeScript(
      COMPLEX_FILTER_SELECTORS.SAVED_FILTER_CLOSE_BUTTON_SELECTOR
    );
    await driver.actions().click(savedFilterCloseButton).perform();
    await universalHelpers.sleep(1000);

    //Closing Filter Pop up
    await driver.actions().click(closeFilterButton).perform();

    // Clicking Filter
    await driver.actions().click(filterButton).perform();
    await universalHelpers.sleep(1000);

    // Selecting Automation Public Filter
    selectPublicFilter(driver);
    await universalHelpers.sleep(1000);
    // Closing Filter Pop up
    universalHelpers.clickOn(driver, COMPLEX_FILTER_SELECTORS.CLOSE_BUTTON_SELECTOR, 1000);

    //Clicking Select
    await driver.actions().click(selectAll).perform();
    await universalHelpers.sleep(1000);

    //Verifying Data
    verifyData(driver, 25);
    await universalHelpers.sleep(1000);

    console.log("Select and Swap Filters successful.");
  } catch (error) {
    console.error(error, "Select, Verify and Swap Filter failed.");
    await universalHelpers.takeScreenshot(driver);
    await driver.quit();
  }
}
