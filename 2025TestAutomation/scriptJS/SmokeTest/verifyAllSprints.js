import assert from "assert";
import { 
  MENU_LIST_ITEMS_SELECTORS,
  TASK_LIST_CONTAINER_SELECTORS,
} from "../SmokeTest/constants.js";
import * as universalHelpers from "../Universal/helpers.js";
import * as smokeTestHelpers from "../SmokeTest/helpers.js";

export default async function verifyAllSprints(driver) {
  try {
    await smokeTestHelpers.verifyTitle(driver, 15, "All Sprints");
    await universalHelpers.sleep(5000);
    await smokeTestHelpers.isPopulatedList(driver, TASK_LIST_CONTAINER_SELECTORS.SPRINT_TASK_LIST_CONTAINER);
    await universalHelpers.sleep(5000);
    await smokeTestHelpers.verifySelected(driver, 4, TASK_LIST_CONTAINER_SELECTORS.SPRINT_TASK_LIST_CONTAINER);
    await universalHelpers.sleep(5000);

    console.log("View All Sprints verification is successful.");
  } catch (error) {
    console.error(error, "Verify View All Sprints Failed");
    await universalHelpers.takeScreenshot(driver);
    await driver.quit();
  }
}
