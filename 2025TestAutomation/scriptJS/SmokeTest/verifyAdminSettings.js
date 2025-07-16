import assert from "assert";
import { 
  TAB_SELECTORS,
  ADMIN_SETTINGS_SELECTORS,
} from "../SmokeTest/constants.js";
import * as CONSTANTS from "../SmokeTest/constants.js";
import * as universalHelpers from "../Universal/helpers.js";
import * as smokeTestHelpers from "../SmokeTest/helpers.js";

async function verifyList(driver){
  // Verifying Admin Settings List
  let groupsList = await driver.executeScript(
    `return ${ADMIN_SETTINGS_SELECTORS.GROUPS_LIST_ROWS}.length`
  );
  assert(groupsList != 0);
}

async function verifyUsers(driver){
  let usersTab = await driver.executeScript(
    `return ${TAB_SELECTORS.BOARD_ACCEPTED_USERS_TAB}`
  );
  await driver.actions().click(usersTab).perform();
  await universalHelpers.sleep(4000);
  await driver.get(driver.getCurrentUrl());
  await universalHelpers.sleep(4000);

  // Verifying Users Admin Settings List
  let usersList = await driver.executeScript(
    `return ${ADMIN_SETTINGS_SELECTORS.USERS_LIST_ROWS}.length`
  );
  assert(usersList != 0);
}

async function verifyProjectTemplates(driver){
  let projectTemplatesTab = await driver.executeScript(
    `return ${TAB_SELECTORS.CALENDAR_DECLINED_PROJECTTEMPLATES_TAB}`
  );
  await driver.actions().click(projectTemplatesTab).perform();
  await universalHelpers.sleep(4000);
  await driver.get(driver.getCurrentUrl());
  await universalHelpers.sleep(4000);

  // Verifying Project Templates Admin Settings List
  let projectTemplatesList = await driver.executeScript(
    `return ${ADMIN_SETTINGS_SELECTORS.PROJECT_TEMPLATES_LIST_ROWS}.length`
  );
  assert(projectTemplatesList != 0);

  let createNewButton = await driver.executeScript(
    ADMIN_SETTINGS_SELECTORS.CREATE_NEW_PROJECT_SELECTOR
  );
  await universalHelpers.clickOn(driver, ADMIN_SETTINGS_SELECTORS.CREATE_NEW_PROJECT_SELECTOR, 2000);

  let headerText = await driver.executeScript(CONSTANTS.TITLE_SELECTOR);
  assert(headerText == "Create New Record");

}

export default async function verifyAdminSettings(driver) {
  try {
    await smokeTestHelpers.verifyTitle(driver, 4, "Admin Settings");
    await verifyList(driver);
    await universalHelpers.sleep(5000);
    await smokeTestHelpers.verifyTabs(driver, "Groups", "Users", "Project Templates");
    await universalHelpers.sleep(5000);
    await verifyUsers(driver);
    await universalHelpers.sleep(10000);
    await verifyProjectTemplates(driver);
    await universalHelpers.sleep(10000);

    console.log("Admin Settings verification is successful.");
  } catch (error) {
    console.error(error, "Verify Admin Settings Failed");
    await universalHelpers.takeScreenshot(driver);
    await driver.quit();
  }
}
