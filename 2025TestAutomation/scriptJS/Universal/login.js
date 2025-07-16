import { By, Key, until } from "selenium-webdriver";
import assert from "assert";
import * as CONSTANTS from "./constants.js";
import * as universalHelpers from "../Universal/helpers.js";

async function loginWithRetry(driver) {
  try {
    await driver.get(CONSTANTS.LOGIN_URL);
    await driver.manage().setTimeouts({ implicit: 10000 });

    let currentURL = await universalHelpers.getUrl(driver);
    while (currentURL === CONSTANTS.LOGIN_URL) {
      let loginFrame = await driver.executeScript(
        CONSTANTS.SN_GSFT_MAIN_SELECTOR
      );
      if (!loginFrame) {
        throw new Error("Login frame not found");
      }
      await driver.switchTo().frame("gsft_main");

      const username = await driver.findElement(By.id("user_name"));
      const password = await driver.findElement(By.id("user_password"));
      const login = await driver.findElement(By.id("sysverb_login"));

      await driver
        .actions()
        .sendKeys(username, "test.automate")
        .sendKeys(password, "Ten0nAutomat1on!")
        .click(login)
        .perform();
      await universalHelpers.sleep(5000);

      currentURL = await universalHelpers.getUrl(driver);
    }
  } catch (error) {
    await universalHelpers.catchError(driver, error, "Login failed");
  }
}

async function navigateToTenon(driver) {
  const filter = await driver.executeScript(CONSTANTS.SN_FILTER_SELECTOR);
  await driver
    .actions()
    .click()
    .sendKeys(filter, "Tenon Work")
    .sendKeys(filter, Key.ENTER)
    .perform();

  const tenonWork = await driver.findElement(By.linkText("Tenon Work"));

  await driver.actions().click(tenonWork).perform();
  const tabs = await driver.getAllWindowHandles();
  await driver.switchTo().window(tabs[1]);
  await universalHelpers.sleep(3000);
}

async function verifyDashboard(driver) {
  let header = await driver.executeScript(CONSTANTS.TITLE_SELECTOR);
  assert(
    (await header.getText()) === "Dashboard",
    `Header text is ${await header.getText()}`
  );
}

export default async function login(driver) {
  try {
    await loginWithRetry(driver);
    await universalHelpers.sleep(1000);
    await navigateToTenon(driver);
    await verifyDashboard(driver);
  } catch (error) {
    await universalHelpers.catchError(driver, error, "Login failed");
  }
}
