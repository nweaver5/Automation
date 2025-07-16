import { By } from "selenium-webdriver";
import assert from "assert";
import { CADSO_MENU_SELECTOR, COMPLEX_FILTER_SELECTORS } from "./constants.js";
import * as filterHelpers from "./helpers.js";
import * as universalHelpers from "../Universal/helpers.js";


async function deletePrivateFilter(driver, name) {
  try {
    const privateFilterListItems = await driver.executeScript(
      COMPLEX_FILTER_SELECTORS.PRIVATE_SAVED_FILTERS_LIST_SELECTOR
    );
    let filterFound = false;
    for (let i = 0; i < privateFilterListItems.length; i++) {
      if (
        (await privateFilterListItems[i].getText()) === name) {
        filterFound = true;

        const hoverable = privateFilterListItems[i];
        const actions = driver.actions({async: true});
        await actions.move({origin: hoverable}).perform();

        const deleteButton = await driver.executeScript(
          filterHelpers.deleteSelectedFilter("private", i)
        );

        await driver.actions().click(deleteButton).perform();
        
        let deleteFilter = await driver.executeScript(
          COMPLEX_FILTER_SELECTORS.DELETE_FILTER_SELECTOR
        )
        await driver.actions().click(deleteFilter).perform();

      }
    }
    assert(filterFound === true, "Saved filter not found");
  } catch (error) {
    console.error(error, "Deleting Filter Failed");
    await universalHelpers.takeScreenshot(driver);
    await driver.quit();
  }
}

async function deletePublicFilter(driver, name) {
  try {
    const publicFilterListItems = await driver.executeScript(
      COMPLEX_FILTER_SELECTORS.PUBLIC_SAVED_FILTERS_LIST_SELECTOR
    );
    let filterFound = false;
    for (let i = 0; i < publicFilterListItems.length; i++) {
      if (
        (await publicFilterListItems[i].getText()) === name) {
        filterFound = true;

        const hoverable = publicFilterListItems[i];
        const actions = driver.actions({async: true});
        await actions.move({origin: hoverable}).perform();

        const deleteButton = await driver.executeScript(
          filterHelpers.deleteSelectedFilter("public", i)
        );

        await driver.actions().click(deleteButton).perform();
        universalHelpers.clickOn(driver, COMPLEX_FILTER_SELECTORS.DELETE_FILTER_SELECTOR, 0);

      }
    }
    assert(filterFound === true, "Saved filter not found");
  } catch (error) {
    console.error(error, "Deleting Filter Failed");
    await universalHelpers.takeScreenshot(driver);
    await driver.quit();
  }
}

async function verifyFilter(driver, name) {
  try {
    const publicFilterListItems = await driver.executeScript(
      COMPLEX_FILTER_SELECTORS.PUBLIC_SAVED_FILTERS_LIST_SELECTOR
    );

    const privateFilterListItems = await driver.executeScript(
      COMPLEX_FILTER_SELECTORS.PRIVATE_SAVED_FILTERS_LIST_SELECTOR
    );

    assert(filterHelpers.checkForFilter(publicFilterListItems, name), "Saved public filter found (Not deleted)");
    assert(filterHelpers.checkForFilter(privateFilterListItems, name), "Saved private filter found (Not deleted)");

  } catch (error) {
    console.error(error, "Verify Filter Failed");
    await universalHelpers.takeScreenshot(driver);
    await driver.quit();
  }
}

export default async function deleteFilter(driver) {
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

    // Deleting and Verifying Automation Filters
    deletePrivateFilter(driver, "Automation Filter Private");
    verifyFilter(driver, "Automation Filter Private");
    await universalHelpers.sleep(1000);

    deletePublicFilter(driver, "Automation Filter Delete Me");
    verifyFilter(driver, "Automation Filter Delete Me");
    await universalHelpers.sleep(1000);

    deletePublicFilter(driver, "Automation Filter Public");
    verifyFilter(driver, "Automation Filter Public");
    await universalHelpers.sleep(1000);

    //Verifying Filters

    console.log("Deleting filter successful.")
  } catch (error) {
    console.error(error, "Deleting filter failed.");
    await universalHelpers.takeScreenshot(driver);
    await driver.quit();
  }
}
