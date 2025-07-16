import assert from "assert";
import { 
  GOALS_SELECTORS,
} from "../SmokeTest/constants.js";
import * as CONSTANTS from "../SmokeTest/constants.js";
import * as universalHelpers from "../Universal/helpers.js";
import * as smokeTestHelpers from "../SmokeTest/helpers.js";

async function verifyAllGoals(driver){
  try {
    // Verifying Goals List
    let goalsNumber = await driver.executeScript(
      `return ${GOALS_SELECTORS.GOALS_LIST}.length`
    );
    assert(goalsNumber != 0);

    //Verifying Create a Goal button
    let createAGoalButton = await driver.executeScript(
      `return ${GOALS_SELECTORS.CREATE_A_GOAL_SELECTOR}`
    );
    assert(smokeTestHelpers.isHidden(createAGoalButton), "Create a Goal button is not visible");

    // Navigate to the first goal
    let firstGoal = await driver.executeScript(
      `return ${GOALS_SELECTORS.GOALS_LIST}[0]`
    );
    await driver.actions().click(firstGoal).perform();
    await universalHelpers.sleep(2000);
    let headerText = await driver.executeScript(CONSTANTS.TITLE_SELECTOR);
    assert(headerText == "Demo Parent Goal");

    return true;

  } catch (error) {
    console.error(error, "Unable to verify All Goals");
  }
}

export default async function verifyGoals(driver) {
  try {
    await smokeTestHelpers.verifyTitle(driver, 6, "All Goals");
    await universalHelpers.sleep(5000);
    verifyAllGoals(driver);
    await universalHelpers.sleep(5000);

    console.log("Goals verification is successful.")
  } catch (error) {
    console.error(error, "Verify Goals Failed");
    await universalHelpers.takeScreenshot(driver);
    await driver.quit();
  }
}
