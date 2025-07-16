import { COMPLEX_FILTER_SELECTORS } from "./constants.js";

async function selectDropdownValue(
  driver,
  value,
  dropdownSelector,
  dropdownIndex 
) {
  const dropDownArrow = await driver.executeScript(
    COMPLEX_FILTER_SELECTORS.DROPDOWN_ARROW_SELECTOR
  );
  await driver.actions().click(dropDownArrow[dropdownIndex]).perform();

  const dropdownList = await driver.executeScript(dropdownSelector);

  let option;
  for (let i = 0; i < dropdownList.length; i++) {
    if ((await dropdownList[i].getText()) === value) {
      option = dropdownList[i];
      break;
    }
  }
  return driver.actions().click(option).perform();
}

async function selectDropdownAccess(driver, value) {
  const accessMenu = await driver.executeScript(
    COMPLEX_FILTER_SELECTORS.ACCESS_DROPDOWN_SELECTOR
  );
  await driver.actions().click(accessMenu).perform();

  const accessTypes = await driver.executeScript(
    COMPLEX_FILTER_SELECTORS.ACCESS_TYPES_SELECTOR
  );

  let option;
  for (let i = 0; i < accessTypes.length; i++) {
    const dropdownText = await accessTypes[i].getText();
    if (dropdownText.includes(value)) {
      option = accessTypes[i];
      break;
    }
  }

  return driver.actions().click(option).perform();
}

function getComplexFilterRowAndField(rowIndex, optionType) {
  if (rowIndex > 0) {
    return `return ${COMPLEX_FILTER_SELECTORS.COMPLEX_FILTER_CONTAINER}.querySelector(".complex-filter-body").querySelectorAll(".complex-filter-row")[${rowIndex}].querySelector(".complex-filter-select-${optionType}-drop-down.open").querySelectorAll("div")`;
  }
  return `return ${COMPLEX_FILTER_SELECTORS.COMPLEX_FILTER_CONTAINER}.querySelector(".complex-filter-select-${optionType}-drop-down.open").querySelectorAll("div")`;
}

function deleteSelectedFilter(filterType, rowIndex) {
  return `return ${COMPLEX_FILTER_SELECTORS.CUSTOM_FILTER_CONTAINER}.querySelector(".custom-filter-list.custom-filter-list-${filterType}.filters").querySelectorAll(".custom-filters-item")[${rowIndex}].querySelectorAll(".custom-filter-icon")[1]`
}

function editSelectedFilter(filterType, rowIndex) {
  return `return ${COMPLEX_FILTER_SELECTORS.CUSTOM_FILTER_CONTAINER}.querySelector(".custom-filter-list.custom-filter-list-${filterType}.filters").querySelectorAll(".custom-filters-item")[${rowIndex}].querySelectorAll(".custom-filter-icon")[0]`
}

async function checkForFilter(filterArray, name){
  let filterFound = false;
  for (let i = 0; i < filterArray.length; i++) {
    if ((await filterArray[i].getText()) === name) {
      filterFound = true;
      break;
    }
  }
  return filterFound;
}

export {
  selectDropdownValue,
  selectDropdownAccess,
  getComplexFilterRowAndField,
  deleteSelectedFilter,
  editSelectedFilter,
  checkForFilter,
};
