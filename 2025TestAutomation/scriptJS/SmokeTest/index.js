import login from "../Universal/login.js";
import { driverSetup } from "../Universal/helpers.js";
import verifyDashboard from "./verifyDashboard.js";
import verifyTasks from "./verifyTasks.js";
import verifyRequests from "./verifyRequests.js";
import verifyAdminSettings from "./verifyAdminSettings.js";
import verifyGoals from "./verifyGoals.js";
import verifyAllSprints from "./verifyAllSprints.js";
import verifyAllProjects from "./verifyAllProjects.js";
import verifyAllCampaigns from "./verifyAllCampaigns.js";

const driver = await driverSetup();

login(driver)
  .then(() => verifyDashboard(driver))
  .then(() => verifyTasks(driver))
  .then(() => verifyRequests(driver))
  .then(() => verifyAdminSettings(driver))
  .then(() => verifyGoals(driver))
  .then(() => verifyAllSprints(driver))
  .then(() => verifyAllProjects(driver))
  .then(() => verifyAllCampaigns(driver));


