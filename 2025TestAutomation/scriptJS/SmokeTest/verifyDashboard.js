import assert from "assert";
import {
  DASHBOARD_STATS_BAR_SELECTORS,
  ACTIVE_TASKS_LIST_SELECTORS,
  RECENT_PROJECTS_SELECTORS,
} from "../SmokeTest/constants.js";
import * as CONSTANTS from "../SmokeTest/constants.js";
import * as universalHelpers from "../Universal/helpers.js";

async function verifyTitle(driver) {
  try {
    let headerText = await driver.executeScript(CONSTANTS.TITLE_SELECTOR);

    assert(headerText == "Dashboard");
  } catch (error) {
    console.error(error, "Unable to verify Dashboard");
    await universalHelpers.takeScreenshot(driver);
    await driver.quit();
  }
}

async function verifyPopulate(driver) {
  try {
    // Verifying In Progress Tasks
    let inProgressTasksNumber = await driver.executeScript(
      `return ${DASHBOARD_STATS_BAR_SELECTORS.IN_PROGRESS_TASKS}.querySelector("span.numbers")`
    );

    // Verifying Completed Tasks
    let completedTasksNumber = await driver.executeScript(
      `return ${DASHBOARD_STATS_BAR_SELECTORS.COMPLETED_TASKS}.querySelector("span.numbers")`
    );

    // Verifying Overdue Tasks
    let overdueTasksNumber = await driver.executeScript(
      `return ${DASHBOARD_STATS_BAR_SELECTORS.OVERDUE_TASKS}.querySelector("span.numbers")`
    );

    assert(inProgressTasksNumber != 0);
    assert(completedTasksNumber != 0);
    assert(overdueTasksNumber != 0);
  } catch (error) {
    console.error(error, "Unable to verify populated Dashboard tasks");
  }
}

async function verifyActiveTasks(driver) {
  try {
    let containerTaskList = await driver.executeScript(
      `return ${ACTIVE_TASKS_LIST_SELECTORS.CONTAINER_TASK_LIST}.querySelectorAll(".task-item.pointer").length`
    );

    let containerHeaderText = await driver.executeScript(
      `return ${ACTIVE_TASKS_LIST_SELECTORS.CONTAINER_HEADER}.querySelector("span").textContent`
    );
    let activeTasksCount = containerHeaderText.match(/(\d+)/);

    assert(
      containerTaskList == activeTasksCount[0],
      "Active Tasks is not populated."
    );
  } catch (error) {
    console.error(error, "Unable to verify populated Active Tasks");
  }
}

async function verifyRecentProjects(driver) {
  try {
    let listOfProjects = await driver.executeScript(
      `return ${RECENT_PROJECTS_SELECTORS.LIST_OF_PROJECTS}.length`
    );

    assert(listOfProjects != 0);
  } catch (error) {
    console.error(error, "Unable to verify populated Recent Projects");
  }
}

export default async function verifyDashboard(driver) {
  try {
    await verifyTitle(driver);
    await verifyPopulate(driver);
    await verifyActiveTasks(driver);
    await verifyRecentProjects(driver);

    console.log("Dashboard verification is successful.");
  } catch (error) {
    console.error(error, "Verify Dashboard Failed");
    await universalHelpers.takeScreenshot(driver);
    await driver.quit();
  }
}
