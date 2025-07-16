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
  if (page.url() != URLS.WORKSTUDIO_AUTOMATE_LOGIN) {
    await page.getByLabel("Favorites", { exact: true }).click();
    await page.getByLabel("Tenon - Automate - Tenon Automate", { exact: true }).click();
  }
});

test.afterAll(async () => {
  await page.close();
});

test.describe("Smoke Tests", async () => {
  test("Verify Audience Builder Components", async () => {
    await page.getByRole("button", { name: "Audience" }).click();
    await expect(page.getByRole("button", { name: "Lists" })).toBeVisible();
    await page.getByRole("button", { name: "Lists" }).click();
    await expect(page.getByRole("heading", { name: "Lists" })).toBeVisible();
    await expect(
      page.getByRole("button", { name: "List", exact: true })
    ).toBeVisible();
    await page.getByText("Playwright").click();
    await expect(page.getByRole("button", { name: "Save List" })).toBeVisible();
    await expect(
      page.getByRole("button", { name: "Clear Filters" })
    ).toBeVisible();
    await expect(
      page.getByRole("button", { name: "Add a Filter Group" })
    ).toBeVisible();
    await expect(
      page.getByText("Filter Group 1")
    ).toBeVisible();
    await expect(
      page.getByText("Where")
    ).toBeVisible();
    await expect(
      page.getByPlaceholder("Field")
    ).toBeVisible();
    await expect(
      page.locator('.search-input-text-disabled:has-text("Operation")')
    ).toBeVisible();
    await expect(
      page.locator('.search-input-text-disabled:has-text("Option")')
    ).toBeVisible();
  });

  test("Create List", async () => {
    await page.getByPlaceholder("Field").fill("First Name");
    await page.locator('.complex-filter-select-field-drop-down:has-text("First Name")').click()
    await page.getByPlaceholder("Option").fill("Nick");
    page.getByRole("button", { name: "Add a Filter Group" }).click();
    await page.getByPlaceholder("Field").nth(1).fill("First Name");
    await page.locator('.complex-filter-select-field-drop-down:has-text("First Name")').click()
    await page.getByPlaceholder("Option").fill("Will");
  });
});
