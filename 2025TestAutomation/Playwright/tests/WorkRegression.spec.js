import { test, expect } from "@playwright/test";
import { URLS, USERS } from "./constants";

let page;
test.beforeAll(async ({ browser }) => {
  // login
  page = await browser.newPage();
  await page.goto(process.env.INSTANCE || URLS.WORKSTUDIO_LOGIN);
  await page
    .getByLabel("User name")
    .fill(process.env.USERNAME || USERS.ADMIN_USERNAME);
  await page.getByLabel("Password", { exact: true }).fill(USERS.PASSWORD);
  await page.getByRole("button", { name: "Log in" }).click();
});

test.afterAll(async () => {
  await page.close();
});

test.describe("Smoke Tests", async () => {
  test("Verify Home", async () => {
    // Verify header
    await expect(page.getByRole("heading", { name: "Home" })).toBeVisible();
    // Screenshot comparison
    // await expect(page).toHaveScreenshot(
    //   "Smoke-Tests-Verify-Dashboard-1-chromium-darwin.png"
    // );
    // Verify task activity
    await expect(page.getByTitle("Task Activity")).toBeVisible();
    await expect(page.locator(".numbers").nth(0)).toHaveText(/^[1-9][0-9]*$/);
    await expect(page.locator(".numbers").nth(1)).toHaveText(/^[1-9][0-9]*$/);
    await expect(page.locator(".numbers").nth(2)).toHaveText(/^[1-9][0-9]*$/);
    // Verify active tasks
    await expect(page.locator(".active-tasks").nth(0)).toBeVisible();
    const headerText = await page
      .locator(".active-tasks")
      .nth(0)
      .locator(".header-text")
      .textContent();
    const headerCount = headerText.match(/(\d+)/);
    const tasksCount = await page.locator(".task-item.pointer").count();
    await expect(tasksCount).toEqual(parseInt(headerCount[0]));
    // Verify recent projects
    await expect(page.getByText("Recent Projects")).toBeVisible();
    await expect(
      await page.locator(".container.pointer").count()
    ).toBeGreaterThan(0);
  });

  test("Verify Tasks", async () => {
    // Navigating to Tasks
    await page.getByRole("button", { name: "Tasks" }).click();
    // Verify header
    await expect(page.getByRole("heading", { name: "My Tasks" })).toBeVisible();
    // Verify filter container
    await expect(page.locator(".complex-filter-button").first()).toBeVisible();
    // Verify List, Board & Calendar Tabs
    await expect(
      page.getByRole("button", { name: "Table" }).first()
    ).toBeVisible();
    await expect(
      page.getByRole("button", { name: "Board" }).first()
    ).toBeVisible();
    await expect(
      page.getByRole("button", { name: "Calendar" }).first()
    ).toBeVisible();
    // Verify Tasks List
    await page.locator(".additional-filter-button").click();
    await page.getByText("All Tasks").click();
    await page.locator(".list-row").first().waitFor();
    const tasksCount = await page.locator(".list-row").count();
    await expect(tasksCount).toBeGreaterThan(0);

    // infinite scroll isn't working
    // await page.locator(".list-row").nth(24).hover();
    // await page.mouse.wheel(0, 50);
    // await page.locator(".select-check-box").first().click();
    // await expect(page.getByText("50 selected")).toBeVisible();
    // await page.pause();

    // Verify Selected Task
    // const randomNum = getRandomInt(25);
    // const selectedTaskName = await page
    //   .locator(".list-row")
    //   .nth(randomNum)
    //   .locator(".field-container.string")
    //   .first()
    //   .textContent();
    // console.log("selectedName", selectedTaskName);
    // await page.locator(".list-row").nth(randomNum).click();
    // const sideModal = await page.locator("cadso-side-modal.is-expanded");
    // const sideModalHeader = await sideModal
    //   .locator(".modal-header-title")
    //   .textContent();
    // console.log("sideModalHeader", sideModalHeader);
    // await expect(sideModalHeader).toEqual(selectedTaskName);

    // Verify Board
    // await page.getByRole('button', { name: 'Board' }).click();
    // await page.locator('.kanban').first().waitFor();
    // await expect(page.locator(".kanban").innerHTML()).toBeTruthy();
  });

  test("Verify Requests", async () => {
    // Navigating to Requests
    await page.getByRole("button", { name: "Requests" }).click();
    await page.reload();
    // Verify header
    await expect(page.getByRole("heading", { name: "Requests" })).toBeVisible();
    // Verify New, Accepted & Declined Tabs
    await expect(page.getByRole("button", { name: "New" })).toBeVisible();
    await expect(page.getByRole("button", { name: "Accepted" })).toBeVisible();
    await expect(page.getByRole("button", { name: "Declined" })).toBeVisible();

    // Check if No Requests
    if (await page.getByText("No Requests, yet")) {
      console.log("There are no requests.");
    } else {
      // Verify Requests Settings List
      await page.reload();
      await page.locator(".list-row").first().waitFor();
      const requestsCount = await page.locator(".list-row").count();
      await expect(requestsCount).toBeGreaterThan(0);

      // Verify Selected Request
      const selectedRequestName = await page
        .locator(".list-row")
        .first()
        .locator(".field-value.is-not-editing.string")
        .first()
        .textContent();
      console.log(selectedRequestName);
      await page.locator(".list-row").first().click();
      await expect(
        page.getByRole("heading", { name: selectedRequestName })
      ).toBeVisible();
      await page.getByRole("button", { name: "Requests" }).click();
    }
  });

  test("Verify Admin Settings", async () => {
    // Navigating to Admin Settings
    await page.getByRole("button", { name: "Admin Settings" }).click();
    await page.reload();
    // Verify header
    await expect(
      page.getByRole("heading", { name: "Admin Settings" })
    ).toBeVisible();
    // Verify Groups, Users & Project Templates
    await expect(page.getByRole("button", { name: "Groups" })).toBeVisible();
    await expect(page.getByRole("button", { name: "Users" })).toBeVisible();
    await expect(
      page.getByRole("button", { name: "Project Templates" })
    ).toBeVisible();
    // Verify Groups Settings List
    await page.locator(".list-row").first().waitFor();
    const groupsCount = await page.locator(".list-row").count();
    await expect(groupsCount).toBeGreaterThan(0);
    // Verify Users Settings List
    await page.getByRole("button", { name: "Users" }).click();
    await page.locator(".list-row").first().waitFor();
    const usersCount = await page.locator(".list-row").count();
    await expect(usersCount).toBeGreaterThan(0);
    // Verify Project Templates
    await page.getByRole("button", { name: "Project Templates" }).click();
    const projectsCount = await page.locator(".list-row").count();
    await expect(projectsCount).toBeGreaterThan(0);
    // Verify Create New Project
    await expect(
      page.getByRole("button", { name: "Create New" })
    ).toBeVisible();
    await page.getByRole("button", { name: "Create New" }).click();
    await expect(
      page.getByRole("heading", { name: "Create New Record" })
    ).toBeVisible();
    await page.getByRole("button", { name: "Cancel" }).click();
  });

  test("Verify Goals", async () => {
    // Navigating to Goals
    await page.getByRole("button", { name: "Goals" }).click();
    // Verify header
    await expect(page.getByRole("heading", { name: "Goals" })).toBeVisible();
    // Verify filter container
    await expect(page.locator(".complex-filter-button").first()).toBeVisible();

    // Verify Create New Goal
    await page.getByRole("button", { name: "Goal", exact: true }).click();
    await expect(
      page.getByRole("heading", { name: "Create New Record" })
    ).toBeVisible();
    await page.getByRole("button", { name: "Cancel" }).click();

    // Verify Groups Settings List
    await page.reload();
    await page.locator(".list-row").first().waitFor();
    const goalsCount = await page.locator(".list-row").count();
    await expect(goalsCount).toBeGreaterThan(0);

    // Verify Selected Goal
    const selectedGoalName = await page
      .locator(".list-row")
      .first()
      .locator(".field-value.is-not-editing.string")
      .first()
      .textContent();
    console.log(selectedGoalName);
    await page.locator(".list-row").first().click();
    await expect(
      page.getByRole("heading", { name: selectedGoalName })
    ).toBeVisible();
    await page.getByRole("button", { name: "Goals" }).click();
  });

  test("Verify All Sprints", async () => {
    // Check if View all Sprints button exists
    if (await page.getByRole("button", { name: "View all Sprints" })) {
      // Navigating to View all Sprints
      await page.getByRole("button", { name: "View all Sprints" }).click();
      await page.reload();
      // Verify header
      await expect(
        page.getByRole("heading", { name: "Sprints" })
      ).toBeVisible();
      // Verify filter container
      await expect(page.locator(".complex-filter-button")).toBeVisible();
      // Verify Sprints List
      await page.locator(".list-row").first().waitFor();
      const sprintsCount = await page.locator(".list-row").count();
      await expect(sprintsCount).toBeGreaterThan(0);
      // Verify Selected Sprint
      const selectedSprintName = await page
        .locator(".list-row")
        .first()
        .locator(".field-container.string")
        .first()
        .textContent();
      console.log(selectedSprintName);
      await page.locator(".list-row").first().click();
      await expect(
        page.locator(".title.input", { name: selectedSprintName })
      ).toBeVisible();
    } else {
      console.log("No sprints");
    }
  });

  test("Verify All Projects", async () => {
    // Check if View all Projects button exists
    if (await page.getByRole("button", { name: "View all Projects" })) {
      // Navigating to View all Projects
      await page.getByRole("button", { name: "View all Projects" }).click();
      await page.reload();
      // Verify header
      await expect(
        page.getByRole("heading", { name: "Projects" })
      ).toBeVisible();
      // Verify List & Board Tabs
      await expect(page.getByRole("button", { name: "Table" })).toBeVisible();
      await expect(page.getByRole("button", { name: "Board" })).toBeVisible();
      // Verify filter container
      await expect(
        page.locator(".complex-filter-button").first()
      ).toBeVisible();
      // Verify Projects List
      await page.locator(".list-row").first().waitFor();
      const projectsCount = await page.locator(".list-row").count();
      await expect(projectsCount).toBeGreaterThan(0);
      // Verify Selected Project
      const selectedProjectName = await page
        .locator(".list-row")
        .first()
        .locator(".field-container.string.can-write")
        .textContent();
      console.log(selectedProjectName);
      await page.locator(".list-row").first().click();
      await expect(
        page.locator(".title.input", { name: selectedProjectName })
      ).toBeVisible();
    } else {
      console.log("There are no projects");
    }
  });

  test("Verify All Campaigns", async () => {
    if (await page.getByRole("button", { name: "View all Campaigns" })) {
      // Navigating to View all Campaigns
      await page.getByRole("button", { name: "View all Campaigns" }).click();
      await page.reload();
      // Verify header
      await expect(
        page.getByRole("heading", { name: "Campaigns" })
      ).toBeVisible();
      // Verify filter container
      await expect(
        page.locator(".complex-filter-button").first()
      ).toBeVisible();
      // Verify Create Campaign
      await expect(
        page.getByRole("button", { name: "Campaign" })
      ).toBeVisible();
      // Verify Campaigns List
      await page.locator(".list-row").first().waitFor();
      const campaignsCount = await page.locator(".list-row").count();
      await expect(campaignsCount).toBeGreaterThan(0);
      // Verify Selected Campaign
      const selectedCampaignName = await page
        .locator(".list-row")
        .first()
        .locator(".field-container.string.can-write")
        .first()
        .textContent();
      console.log(selectedCampaignName);
      await page.locator(".list-row").first().click();
      await expect(
        page.locator(".title.input", { name: selectedCampaignName })
      ).toBeVisible();
    } else {
      console.log("There are no campaigns");
    }
  });
});
