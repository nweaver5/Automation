import { test, expect } from "@playwright/test";
import { URLS, USERS } from "./constants";

let page;
test.beforeAll(async ({ browser }) => {
  // login
  page = await browser.newPage();
  await page.goto(URLS.WORKSTUDIO_AUTOMATE_LOGIN);
  await page.getByLabel("User name").fill(USERS.ADMIN_USERNAME);
  await page.getByLabel("Password", { exact: true }).fill(USERS.PASSWORD);
  await page.getByRole("button", { name: "Log in" }).click();
});

test.afterAll(async () => {
  await page.close();
});

const clickFirstItemInList = async (checkTitle) => {
  const itemName = await page.locator(".field-container").nth(0).textContent();
  await page.locator(".list-row").first().click();
  if (checkTitle) {
    await expect(page.locator(".title.input")).toHaveValue(itemName);
  } else {
    return itemName;
  }
  return;
};

test.describe("Smoke Tests", async () => {
  test("Verify Home", async () => {
    await expect(page.getByRole("button", { name: "Home" })).toBeVisible();
    await expect(page.getByRole("heading", { name: "Home" })).toBeVisible();
    await expect(
      page.getByRole("heading", { name: "Email Send Activity" })
    ).toBeVisible();
    await expect(
      page.getByRole("heading", { name: "Recent Email Sends" })
    ).toBeVisible();
  });

  test("Verify Emails", async () => {
    const emailsButton = await page
      .getByRole("button", { name: "Emails" })
      .nth(0);
    await expect(emailsButton).toBeVisible();
    await emailsButton.click();
    await expect(page.getByRole("heading", { name: "Emails" })).toBeVisible();
    await expect(
      page.getByRole("button", { name: "Email", exact: true })
    ).toBeVisible();
    if (await page.getByLabel("No Emails, Yet")) {
      return true;
    } else {
      await lickFirstItemInList(true);
      await expect(
        page.getByRole("button", { name: "Save Draft" })
      ).toBeVisible();
      await expect(
        page.getByRole("button", { name: "Schedule" })
      ).toBeVisible();
      await expect(page.getByRole("button", { name: "Design" })).toBeVisible();
      await expect(
        page.getByRole("button", { name: "Send Settings" })
      ).toBeVisible();
      await page.locator(".nav-title-back-button").click();
      await expect(page.getByRole("heading", { name: "Emails" })).toBeVisible();
    }
  });

  test("Verify Audience", async () => {
    await page.getByRole("button", { name: "Audience" }).click();
    await expect(page.getByRole("button", { name: "Lists" })).toBeVisible();
    await expect(page.getByRole("button", { name: "Leads" })).toBeVisible();
    await expect(page.getByRole("button", { name: "Contacts" })).toBeVisible();
    await page.getByRole("button", { name: "Lists" }).click();
    await expect(page.getByRole("heading", { name: "Lists" })).toBeVisible();
    await expect(
      page.getByRole("button", { name: "List", exact: true })
    ).toBeVisible();
    await clickFirstItemInList(true);
    await expect(page.getByRole("button", { name: "Save List" })).toBeVisible();
    await expect(
      page.getByRole("button", { name: "Clear Filters" })
    ).toBeVisible();
    await expect(
      page.getByRole("button", { name: "Add a condition" })
    ).toBeVisible();
    await expect(
      page.getByRole("button", { name: "Add a Filter Group" })
    ).toBeVisible();
    await page.locator(".nav-title-back-button").click();
    await page.getByRole("button", { name: "Leads" }).click();
    await expect(page.getByRole("heading", { name: "Leads" })).toBeVisible();
    // leads is broken, update when it's fixed
    // await page.reload();
    // const itemName = await clickFirstItemInList(false);
    // await page.locator(".customer-header").toHaveValue(itemName);
    await page.getByRole("button", { name: "Contacts" }).click();
    await expect(page.getByRole("heading", { name: "Contacts" })).toBeVisible();
    //TODO: Update when contacts page is implemented
  });

  test("Verify Content", async () => {
    await page.getByRole("button", { name: "Content" }).click();
    await expect(
      page.getByRole("button", { name: "Email Templates" })
    ).toBeVisible();
    await expect(
      page.getByRole("button", { name: "Landing Pages" })
    ).toBeVisible();
    await page.getByRole("button", { name: "Email Templates" }).click();
    await expect(
      page.getByRole("heading", { name: "Email Templates" })
    ).toBeVisible();
    await expect(
      page.getByRole("button", { name: "Email", exact: true })
    ).toBeVisible();
    await page.reload();
    await clickFirstItemInList(true);
    await expect(page.getByRole("button", { name: "Save" })).toBeVisible();
    await expect(
      page.getByRole("button", { name: "Review & Schedule" })
    ).toBeVisible();
    await page.locator(".nav-title-back-button").click();
    await page.getByRole("button", { name: "Landing Pages" }).click();
    await expect(
      page.getByRole("heading", { name: "Landing Pages" })
    ).toBeVisible();
    await expect(
      page.getByRole("button", { name: "Landing Page", exact: true })
    ).toBeVisible();
    await page.reload();
    await clickFirstItemInList(true);
    await expect(page.getByRole("button", { name: "Save" })).toBeVisible();
    await page.locator(".nav-title-back-button").click();
  });

  test("Verify Reports", async () => {
    await page.getByRole("button", { name: "Reports" }).click();
    await expect(page.getByRole("heading", { name: "Reports" })).toBeVisible();
  });
});
