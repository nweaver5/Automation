import { 
  TASK_LIST_CONTAINER_SELECTORS,
} from "../SmokeTest/constants.js";
import * as universalHelpers from "../Universal/helpers.js";
import * as smokeTestHelpers from "../SmokeTest/helpers.js";

export default async function verifyAllCampaigns(driver) {
  try {
    await smokeTestHelpers.verifyTitle(driver, 33, "All Campaigns");
    await universalHelpers.sleep(5000);
    await smokeTestHelpers.isPopulatedList(driver, TASK_LIST_CONTAINER_SELECTORS.CAMPAIGN_TASK_LIST_CONTAINER);
    await universalHelpers.sleep(5000);
    await smokeTestHelpers.verifySelected(driver, 4, TASK_LIST_CONTAINER_SELECTORS.CAMPAIGN_TASK_LIST_CONTAINER);
    await universalHelpers.sleep(5000);

    console.log("View All Campaigns verification is successful.");
  } catch (error) {
    console.error(error, "Verify View All Campaigns Failed");
    await universalHelpers.takeScreenshot(driver);
    await driver.quit();
  }
}
