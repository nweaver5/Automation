import { By } from "selenium-webdriver";
import assert from "assert";
import { CADSO_MENU_SELECTOR, COMPLEX_FILTER_SELECTORS } from "./constants.js";
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
        "Automation Filter Multiple Conditions"
      ) {
        filterFound = true;

        const hoverable = privateFilterListItems[i];
        const actions = driver.actions({async: true});
        await actions.move({origin: hoverable}).perform();

        const editButton = await driver.executeScript(
          filterHelpers.editSelectedFilter("private", i)
        );
        await driver.actions().click(editButton).perform();
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

async function editFilter(driver){
  const filterNameInput = await driver.executeScript(
    COMPLEX_FILTER_SELECTORS.FILTER_NAME_INPUT_SELECTOR
  );
  await driver.executeScript("arguments[0].value='';", filterNameInput);
  await driver
    .actions()
    .sendKeys(filterNameInput, "Automation Filter Delete Me")
    .perform();

  await filterHelpers.selectDropdownAccess(driver, "Everyone");
  universalHelpers.clickOn(driver, COMPLEX_FILTER_SELECTORS.SAVE_FILTER_MODAL_BUTTON_SELECTOR, 2000);
}
async function verifyFilter(driver) {
  try {
    const publicFilterListItems = await driver.executeScript(
      COMPLEX_FILTER_SELECTORS.PUBLIC_SAVED_FILTERS_LIST_SELECTOR
    );
    
    assert(filterHelpers.checkForFilter(publicFilterListItems, "Automation Filter Delete Me"), "Filter not found");
    
  } catch (error) {
    console.error(error, "Verify Filter Failed");
    await universalHelpers.takeScreenshot(driver);
    await driver.quit();
  }
}

export default async function editNamePermission(driver) {
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
    
    // Editing Selected Automation Private Filter
    editFilter(driver);

    await universalHelpers.sleep(5000)

    // Verifying Filter
    verifyFilter(driver);

    console.log("Editing filter successful.")
  } catch (error) {
    console.error(error, "Editing filter failed.");
    await universalHelpers.takeScreenshot(driver);
    await driver.quit();
  }
}
