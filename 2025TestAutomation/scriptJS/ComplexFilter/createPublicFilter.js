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
    "Status",
    filterHelpers.getComplexFilterRowAndField(0, "field"),
    0
  );
  await filterHelpers.selectDropdownValue(
    driver,
    "is not",
    filterHelpers.getComplexFilterRowAndField(0, "operation"),
    1
  );
  return filterHelpers.selectDropdownValue(
    driver,
    "Upcoming",
    filterHelpers.getComplexFilterRowAndField(0, "option"),
    2
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
    .sendKeys(filterNameInput, "Automation Filter Public")
    .perform();

  await filterHelpers.selectDropdownAccess(driver, "Everyone");

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
    const publicFilterListItems = await driver.executeScript(
      COMPLEX_FILTER_SELECTORS.PUBLIC_SAVED_FILTERS_LIST_SELECTOR
    );

    assert(filterHelpers.checkForFilter(publicFilterListItems, "Automation Filter Public"), "Filter not found");
  } catch (error) {
    console.error(error, "Verify Filter Failed");
    await universalHelpers.takeScreenshot(driver);
    await driver.quit();
  }
}

export default async function createPublicFilter(driver) {
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

    console.log("Create Public Filter successful.");
  } catch (error) {
    console.error(error, "Create Public Filter Failed");
    await universalHelpers.takeScreenshot(driver);
    await driver.quit();
  }
}
