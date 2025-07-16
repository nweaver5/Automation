import { login, logout } from "../Universal/index.js";
import createPrivateFilter from "./createPrivateFilter.js";
import createPublicFilter from "./createPublicFilter.js";
import multipleConditions from "./multipleConditions.js";
import selectAndSwapFilter from "./selectAndSwap.js";
import { driverSetup } from "../Universal/helpers.js";
import editSavedFilter from "./editSavedFilter.js";
import discardChanges from "./discardChanges.js";
import editNamePermission from "./editNamePermission.js";
import deleteFilter from "./deleteFilter.js";

const driver = await driverSetup();

login(driver)
  .then(() => createPrivateFilter(driver))
  .then(() => createPublicFilter(driver))
  .then(() => multipleConditions(driver))
  .then(() => selectAndSwapFilter(driver))
  .then(() => editSavedFilter(driver))
  .then(() => discardChanges(driver))
  .then(() => editNamePermission(driver))
  .then(() => deleteFilter(driver))
  //.then(() => logout(driver));

