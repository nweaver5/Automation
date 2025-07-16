import { Builder } from "selenium-webdriver";

import fs from "fs";

async function sleep(ms) {
  await new Promise((resolve) => setTimeout(resolve, ms));
}

async function driverSetup() {
  const driver = await new Builder().forBrowser("chrome").build();
  return driver;
}

async function getUrl(driver) {
  let getURL = driver.getCurrentUrl();
  let currentURL = (await getURL).toString();
  return currentURL;
}

async function highlightElement(driver, element) {
  return driver.executeScript(
    "arguments[0].setAttribute('style', 'background: red; border: 2px solid green;');",
    element
  );
}

async function takeScreenshot(driver) {
  return driver.takeScreenshot().then((image) => {
    fs.writeFileSync(`./output/error.png`, image, "base64", (err) => {
      if (err) console.log(err);
    });
  });
}

async function catchError(driver, error, message) {
  console.error(error, message);
  await takeScreenshot(driver);
  await driver.quit();
}

async function clickOn(driver, element, waitTime) {
  let entity = await driver.executeScript(element);
  await driver.actions().click(entity).perform();
  await sleep(waitTime);
}

export {
  sleep,
  driverSetup,
  getUrl,
  highlightElement,
  takeScreenshot,
  catchError,
  clickOn,
};
