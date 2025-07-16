import { By } from "selenium-webdriver";
import assert from "assert";
import * as CONSTANTS from "./constants.js";
import * as helpers from "./helpers.js";

export default async function logout(driver) {
  try {
    const avatarDropdown = await driver.executeScript(
      CONSTANTS.AVATAR_DROPDOWN_SELECTOR
    );
    await driver.actions().click(avatarDropdown).pause(1000).perform();

    const logoutButton = await avatarDropdown.findElement(
      By.linkText("Logout")
    );
    await driver.actions().click(logoutButton).pause(5000).perform();

    const loginFrame = await driver.executeScript(
      CONSTANTS.SN_GSFT_MAIN_SELECTOR
    );
    assert(await loginFrame.isDisplayed(), "login frame not displayed");
    console.log("Logout successful");
  } catch (error) {
    await helpers.catchError(driver, error, "Logout failed");
  } finally {
    await driver.quit();
  }
}
