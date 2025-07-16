import { By } from "selenium-webdriver";
import assert from "assert";
import { CADSO_MENU_SELECTOR, COMPLEX_FILTER_SELECTORS } from "./constants.js";
import * as filterHelpers from "./helpers.js";
import * as universalHelpers from "../Universal/helpers.js";

async function createFilter(driver) {
  const createFilterButton = await driver.executeScript(
    COMPLEX_FILTER_SELECTORS.CREATE_BUTTON_SELECTOR
  );
  await driver.actions().click(createFilterButton).perform();

  const addConditionButton = await driver.executeScript(
    COMPLEX_FILTER_SELECTORS.ADD_CONDITION_BUTTON_SELECTOR
  );
  await driver.actions().click(addConditionButton).perform();

  await filterHelpers.selectDropdownValue(
    driver,
    "Story Points",
    filterHelpers.getComplexFilterRowAndField(0, "field"),
    0
  );
  await filterHelpers.selectDropdownValue(
    driver,
    "greater than or is",
    filterHelpers.getComplexFilterRowAndField(0, "operation"),
    1
  );

  let optionInput = await driver.executeScript(
    COMPLEX_FILTER_SELECTORS.OPTION_NUMERICAL_INPUT_SELECTOR
  );
  await driver.actions().sendKeys(optionInput, "2").perform();

  await driver.actions().click(addConditionButton).perform();

  /* SECOND ROW */

  await filterHelpers.selectDropdownValue(
    driver,
    "Assignment group",
    filterHelpers.getComplexFilterRowAndField(1, "field"),
    2
  );
  await filterHelpers.selectDropdownValue(
    driver,
    "is",
    filterHelpers.getComplexFilterRowAndField(1, "operation"),
    3
  );
  return filterHelpers.selectDropdownValue(
    driver,
    "Account-Based Marketers",
    filterHelpers.getComplexFilterRowAndField(1, "option"),
    4
  );
}

async function saveFilter(driver) {
  const saveButton = await driver.executeScript(
    COMPLEX_FILTER_SELECTORS.SAVE_BUTTON_SELECTOR
  );
  await driver.actions().click(saveButton).perform();
  const filterNameInput = await driver.executeScript(
    COMPLEX_FILTER_SELECTORS.FILTER_NAME_INPUT_SELECTOR
  );
  await driver
    .actions()
    .sendKeys(filterNameInput, "Automation Filter Multiple Conditions")
    .perform();

  await filterHelpers.selectDropdownAccess(driver, "Private");

  const saveFilterModalButton = await driver.executeScript(
    COMPLEX_FILTER_SELECTORS.SAVE_FILTER_MODAL_BUTTON_SELECTOR
  );
  await driver.actions().click(saveFilterModalButton).perform();
  await universalHelpers.sleep(2000);

  const savedFilterCloseButton = await driver.executeScript(
    COMPLEX_FILTER_SELECTORS.SAVED_FILTER_CLOSE_BUTTON_SELECTOR
  );
  await driver.actions().click(savedFilterCloseButton).perform();
}

async function verifyFilter(driver) {
  try {
    const privateFilterListItems = await driver.executeScript(
      COMPLEX_FILTER_SELECTORS.PRIVATE_SAVED_FILTERS_LIST_SELECTOR
    );
    assert(filterHelpers.checkForFilter(privateFilterListItems, "Automation Filter Multiple Conditions"), "Filter not found");
  } catch (error) {
    console.error(error, "Verify Filter Failed");
    await universalHelpers.takeScreenshot(driver);
    await driver.quit();
  }
}

export default async function multipleConditions(driver) {
  try {
    const cadsoUiMenu = await driver.executeScript(CADSO_MENU_SELECTOR);
    const sideNavItems = await cadsoUiMenu.findElements(By.tagName("button"));
    await driver.actions().click(sideNavItems[2]).perform();
    await universalHelpers.sleep(5000);

    const cadsoComplexListFilter = await driver.executeScript(
      `return ${COMPLEX_FILTER_SELECTORS.CADSO_COMPLEX_LIST_FILTER}`
    );
    const filterButton = await cadsoComplexListFilter.findElement(
      By.css(".complex-filter-button ")
    );

    await driver.actions().click(filterButton).perform();

    await createFilter(driver);
    await saveFilter(driver);
    await universalHelpers.sleep(3000);

    const closeFilterButton = await driver.executeScript(
      COMPLEX_FILTER_SELECTORS.CLOSE_BUTTON_SELECTOR
    );
    await driver
      .actions()
      .click(closeFilterButton)
      .pause(1000)
      .click(filterButton)
      .perform();

    verifyFilter(driver);
    await universalHelpers.sleep(2000);

    console.log("Create Multiple Conditions successful.");
  } catch (error) {
    console.error(error, "Create Multiple Filter Conditions Failed");
    await universalHelpers.takeScreenshot(driver);
    await driver.quit();
  }
}
