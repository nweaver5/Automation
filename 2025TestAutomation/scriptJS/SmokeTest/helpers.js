import { By } from "selenium-webdriver";
import assert from "assert";
import { 
  TAB_SELECTORS,
  TASK_LIST_CONTAINER_SELECTORS,
} from "../SmokeTest/constants.js";
import * as CONSTANTS from "../SmokeTest/constants.js";
import * as universalHelpers from "../Universal/helpers.js";

async function verifyTitle(driver, index, title) {
  try {
    const sideNavItems = await driver.executeScript(
      `return ${CONSTANTS.CADSO_MENU_SELECTOR}.querySelectorAll("button")`
    )
    await driver.actions().click(sideNavItems[index]).perform();
    await universalHelpers.sleep(2000);
    let headerText = await driver.executeScript(CONSTANTS.TITLE_SELECTOR);

    assert(headerText == title);

  } catch (error) {
    console.error(error, "Unable to verify title");
    await universalHelpers.takeScreenshot(driver);
    await driver.quit();
  }
}

async function isHidden(element) {
  return (element.offsetParent != null);
}

async function verifyTabs(driver, tab0, tab1, tab2){
  try {
    let firstTab = await driver.executeScript(
      `return ${TAB_SELECTORS.LIST_NEW_GROUPS_TAB}`
    );
    let fistTabText = await driver.executeScript(
      `return ${TAB_SELECTORS.LIST_NEW_GROUPS_TAB}.textContent`
    );
    assert(isHidden(firstTab), "%s Tab is not visible", tab0);

    if (fistTabText != tab0){
      console.error("%s Tab is not shown", tab0);
      await driver.get(driver.getCurrentUrl());
      await universalHelpers.sleep(5000);
    }
    assert(isHidden(firstTab), "%s Tab is not visible", tab0);

    let secondTab = await driver.executeScript(
      `return ${TAB_SELECTORS.BOARD_ACCEPTED_USERS_TAB}`
    );
    let secondTabText = await driver.executeScript(
      `return ${TAB_SELECTORS.BOARD_ACCEPTED_USERS_TAB}.textContent`
    );
    if (secondTabText != tab1){
      console.error("%s Tab is not shown", tab1);
      await driver.get(driver.getCurrentUrl());
    }
    assert(isHidden(secondTab), "%s Tab is not visible", tab1);

    if (tab2 != null){
      let thirdTab = await driver.executeScript(
        `return ${TAB_SELECTORS.CALENDAR_DECLINED_PROJECTTEMPLATES_TAB}`
      );
      let thirdTabText = await driver.executeScript(
        `return ${TAB_SELECTORS.CALENDAR_DECLINED_PROJECTTEMPLATES_TAB}.textContent`
      );
      if (thirdTabText != tab2){
        console.error("%s Tab is not shown", tab2);
        await driver.get(driver.getCurrentUrl());
      }
      assert(isHidden(thirdTab), "%s Tab is not visible", tab2);
    }

  } catch (error) {
    console.error(error, "Unable to verify tabs");
  }
}

async function isPopulatedList(driver, SELECTOR){
  try {
    let totalNumber = await driver.executeScript(
      SELECTOR
    );
    assert(totalNumber != 0);

  } catch (error) {
    console.error(error, "Unable to check if populated list");
  }
}

async function verifySelected(driver, index, SELECTOR){
  let selected = await driver.executeScript(
    `return ${SELECTOR}.querySelectorAll(".field-value.is-not-editing.string")[${index}]`
  );
  let selectedName = await driver.executeScript(
    `return ${SELECTOR}.querySelectorAll(".field-value.is-not-editing.string")[${index}].textContent`
  );
  await driver.actions().click(selected).perform();
  await universalHelpers.sleep(3000);
  let headerText = await driver.executeScript(CONSTANTS.TITLE_SELECTOR);
  assert(headerText == selectedName);
}

async function verifyBoard(driver){
  let boardTab = await driver.executeScript(
    `return ${TAB_SELECTORS.BOARD_ACCEPTED_USERS_TAB}`
  );
  await driver.actions().click(boardTab).perform();
  await universalHelpers.sleep(5000);

  let boardItemContainers_length = await driver.executeScript(
    `return ${KANBAN_SELECTORS.KANBAN_ITEM_CONTAINERS}.length`
  );

  for (let i = 0; i < boardItemContainers_length; i++){
    let num_of_containers = await driver.executeScript(`return ${KANBAN_SELECTORS.KANBAN_ITEM_CONTAINERS}[${i}].querySelectorAll(".content-container")`);

    if (num_of_containers == 0){
      console.error('Item container #%d is not populated', i);
      break;
    }
  }
}

export {
  verifyTitle,
  isHidden,
  verifyTabs,
  isPopulatedList,
  verifySelected,
  verifyBoard,
}