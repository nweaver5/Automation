import assert from "assert";
import { 
  TASK_LIST_CONTAINER_SELECTORS,
  MENU_LIST_ITEMS_SELECTORS,
  TAB_SELECTORS,
  CADSO_UI_KANBAN_SELECTORS,
} from "../SmokeTest/constants.js";
import * as CONSTANTS from "../SmokeTest/constants.js";
import * as universalHelpers from "../Universal/helpers.js";
import * as smokeTestHelpers from "../SmokeTest/helpers.js";

async function verifyBoard(driver){
  let boardTab = await driver.executeScript(
    `return ${TAB_SELECTORS.BOARD_ACCEPTED_USERS_TAB}`
  );
  await driver.actions().click(boardTab).perform();
  await universalHelpers.sleep(5000);

  //let boardColumns = await driver.executeScript(`return ${KANBAN_SELECTORS.KANBAN_COLUMNS}`);
  let boardItemContainers_length = await driver.executeScript(
    `return ${CADSO_UI_KANBAN_SELECTORS.CADSO_UI_KANBAN_PROJECTSBOARD}.querySelectorAll(".items-container").length`
    );

  for (let i = 0; i < boardItemContainers_length; i++){
    let num_of_containers = await driver.executeScript(`return ${CADSO_UI_KANBAN_SELECTORS.CADSO_UI_KANBAN_PROJECTSBOARD}.querySelectorAll(".items-container")[${i}].querySelectorAll(".content-container")`);

    if (num_of_containers == 0){
      console.error('Item container #%d is not populated', i);
      break;
    }
  }
}

export default async function verifyAllProjects(driver) {
  try {
    await smokeTestHelpers.verifyTitle(driver, 24, "All Projects");
    await universalHelpers.sleep(5000);
    await smokeTestHelpers.isPopulatedList(driver, TASK_LIST_CONTAINER_SELECTORS.PROJECT_TASK_LIST_CONTAINER);
    await universalHelpers.sleep(5000);
    await smokeTestHelpers.verifyTabs(driver, "List", "Board", null);
    await universalHelpers.sleep(5000);
    await verifyBoard(driver);
    await universalHelpers.sleep(8000);

    let listTab = await driver.executeScript(
      `return ${TAB_SELECTORS.LIST_NEW_GROUPS_TAB}`
    );
    await driver.actions().click(listTab).perform();
    await universalHelpers.sleep(5000);

    await smokeTestHelpers.verifySelected(driver, 4, TASK_LIST_CONTAINER_SELECTORS.PROJECT_TASK_LIST_CONTAINER);
    await universalHelpers.sleep(5000);

    console.log("View All Projects verification is successful.");
  } catch (error) {
    console.error(error, "Verify View All Projects Failed");
    await universalHelpers.takeScreenshot(driver);
    await driver.quit();
  }
}
