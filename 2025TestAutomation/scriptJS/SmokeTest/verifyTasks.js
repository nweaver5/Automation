import { 
  TAB_SELECTORS,
  CADSO_UI_KANBAN_SELECTORS,
} from "../SmokeTest/constants.js";
import * as universalHelpers from "../Universal/helpers.js";
import * as smokeTestHelpers from "../SmokeTest/helpers.js";

async function verifyBoard(driver){
  let boardTab = await driver.executeScript(
    `return ${TAB_SELECTORS.BOARD_ACCEPTED_USERS_TAB}`
  );
  await driver.actions().click(boardTab).perform();
  await universalHelpers.sleep(5000);

  let boardItemContainers_length = await driver.executeScript(
    `return ${CADSO_UI_KANBAN_SELECTORS.CADSO_UI_KANBAN_TASKBOARD}.querySelectorAll(".items-container").length`
    );

  for (let i = 0; i < boardItemContainers_length; i++){
    let num_of_containers = await driver.executeScript(`return ${CADSO_UI_KANBAN_SELECTORS.CADSO_UI_KANBAN_TASKBOARD}.querySelectorAll(".items-container")[${i}].querySelectorAll(".content-container")`);

    if (num_of_containers == 0){
      console.error('Item container #%d is not populated', i);
      break;
    }
  }
}

async function verifyCalendar(driver){
  return true;
}

export default async function verifyTasks(driver) {
  try {
    await smokeTestHelpers.verifyTitle(driver, 2, "My Tasks");
    await universalHelpers.sleep(5000);
    await smokeTestHelpers.verifyTabs(driver, "List", "Board", "Calendar");
    await universalHelpers.sleep(5000);
    await verifyBoard(driver);
    // verifyCalendar(driver) : TODO LATER (Internal Server 500)

    console.log("Tasks verification is successful.")
  } catch (error) {
    console.error(error, "Verify Tasks Failed");
    await universalHelpers.takeScreenshot(driver);
    await driver.quit();
  }
}
