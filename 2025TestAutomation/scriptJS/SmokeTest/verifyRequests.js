import * as universalHelpers from "../Universal/helpers.js";
import * as smokeTestHelpers from "../SmokeTest/helpers.js";

export default async function verifyRequests(driver) {
  try {
    await smokeTestHelpers.verifyTitle(driver, 3, "Requests");
    await universalHelpers.sleep(5000);

    await smokeTestHelpers.verifyTabs(driver, "New", "Accepted", "Declined");
    await universalHelpers.sleep(5000);

    console.log("Requests verification is successful.")
  } catch (error) {
    console.error(error, "Verify Requests Failed");
    await universalHelpers.takeScreenshot(driver);
    await driver.quit();
  }
}
