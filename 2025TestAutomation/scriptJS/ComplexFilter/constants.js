const CADSO_NAV_HEADER = `document.querySelector("macroponent-aededa80c782201072b211d4d8c2604c").shadowRoot.querySelector("sn-canvas-appshell-main").shadowRoot.querySelector("macroponent-355f43e047f8f510b0361ae8036d4355").shadowRoot.querySelector("macroponent-67ee2538534501108135ddeeff7b121b").querySelector("cadso-nav-header")`;
const SN_CANVAS_SCREEN_LAST_OF_TYPE = `${CADSO_NAV_HEADER}.querySelector("sn-canvas-main").shadowRoot.querySelector("sn-canvas-screen:last-of-type").shadowRoot`;
const CADSO_COMPLEX_LIST_FILTER = `${SN_CANVAS_SCREEN_LAST_OF_TYPE}.querySelector("macroponent-d633ea8647a86110a1052a02e26d434d").shadowRoot.querySelector("cadso-complex-list-filter").shadowRoot.querySelector("div")`;
const CADSO_MENU_SELECTOR = `return ${CADSO_NAV_HEADER}.querySelector("cadso-ui-menu").shadowRoot.querySelector("div")`;
const CUSTOM_FILTER_CONTAINER = `${CADSO_COMPLEX_LIST_FILTER}.querySelector(".custom-filter-container.open")`;
const COMPLEX_FILTER_CONTAINER = `${CADSO_COMPLEX_LIST_FILTER}.querySelector(".complex-filter-container.open")`;
const TASK_LIST_CONTAINER = `${SN_CANVAS_SCREEN_LAST_OF_TYPE}.querySelector("section").querySelector("screen-action-transformer-de33ea8647a86110a1052a02e26d434f").querySelector("macroponent-d633ea8647a86110a1052a02e26d434d").shadowRoot.querySelector("div").querySelector("cadso-ui-list").shadowRoot`;

const COMPLEX_FILTER_SELECTORS = {
  CUSTOM_FILTER_CONTAINER,
  COMPLEX_FILTER_CONTAINER,
  CADSO_COMPLEX_LIST_FILTER,
  CREATE_BUTTON_SELECTOR: `return ${CUSTOM_FILTER_CONTAINER}.querySelector(".custom-filter-button")`,
  CLOSE_BUTTON_SELECTOR: `return ${COMPLEX_FILTER_CONTAINER}.querySelector(".complex-exit-btn")`,
  ADD_CONDITION_BUTTON_SELECTOR: `return ${COMPLEX_FILTER_CONTAINER}.querySelector(".complex-filter-add-filter-button")`,
  DROPDOWN_ARROW_SELECTOR: `return ${COMPLEX_FILTER_CONTAINER}.querySelectorAll(".complex-filter-search-input-icon")`,
  OPTION_NUMERICAL_INPUT_SELECTOR: `return ${COMPLEX_FILTER_CONTAINER}.querySelector(".complex-filter-select-option-container").querySelector("input")`,
  SAVE_BUTTON_SELECTOR: `return ${COMPLEX_FILTER_CONTAINER}.querySelector(".complex-btn.save")`,
  FILTER_NAME_INPUT_SELECTOR: `return ${CADSO_COMPLEX_LIST_FILTER}.querySelector(".custom-filter-modal").querySelector("input")`,
  SAVE_FILTER_MODAL_BUTTON_SELECTOR: `return ${CADSO_COMPLEX_LIST_FILTER}.querySelector(".custom-filter-modal").querySelector(".custom-filter-modal-save")`,
  SAVED_FILTER_CLOSE_BUTTON_SELECTOR: `return ${CADSO_COMPLEX_LIST_FILTER}.querySelector(".complex-filter-body.saved-condition-body").querySelector(".saved-condition-remove-icon")`,
  PRIVATE_SAVED_FILTERS_LIST_SELECTOR: `return ${CUSTOM_FILTER_CONTAINER}.querySelector(".custom-filter-list.custom-filter-list-private.filters").querySelectorAll(".custom-filters-item")`,
  PUBLIC_SAVED_FILTERS_LIST_SELECTOR: `return ${CUSTOM_FILTER_CONTAINER}.querySelector(".custom-filter-list.custom-filter-list-public.filters").querySelectorAll(".custom-filters-item")`,
  ACCESS_DROPDOWN_SELECTOR: `return ${CADSO_COMPLEX_LIST_FILTER}.querySelector(".dropdown.access")`,
  ACCESS_TYPES_SELECTOR: `return ${CADSO_COMPLEX_LIST_FILTER}.querySelector(".dropdown.access").querySelector(".dropdown-body").querySelectorAll(".dropdown-options.access")`,
  CUSTOM_FILTER_SAVE_CHANGES_SELECTOR: `return ${COMPLEX_FILTER_CONTAINER}.querySelector(".custom-btn.save-change")`,
  CUSTOM_FILTER_DISCARD_CHANGES_SELECTOR: `return ${COMPLEX_FILTER_CONTAINER}.querySelector(".custom-btn.discard")`,
  FIELD_INPUT_SELECTOR: `return ${COMPLEX_FILTER_CONTAINER}.querySelectorAll(".complex-filter-row")[0].querySelectorAll("input")[0].getAttribute('value')`,
  OPERATION_INPUT_SELECTOR: `return ${COMPLEX_FILTER_CONTAINER}.querySelectorAll(".complex-filter-row")[0].querySelectorAll("input")[1].getAttribute('value')`,
  OPTION_INPUT_SELECTOR: `return ${COMPLEX_FILTER_CONTAINER}.querySelectorAll(".complex-filter-row")[0].querySelectorAll("input")[2].getAttribute('value')`,
  DELETE_FILTER_SELECTOR: `return ${CADSO_COMPLEX_LIST_FILTER}.querySelector(".btn.btn-delete")`,
};

const TASK_LIST_SELECTORS = {
  SELECT_ALL_CHECKBOX_SELECTOR: `return ${TASK_LIST_CONTAINER}.querySelector(".select-check-box")`,
  ACTIONS_TOTAL_NUM_SELECTED_SELECTOR: `return ${TASK_LIST_CONTAINER}.querySelector(".action-menu-selected")`,
};

export {
  CADSO_MENU_SELECTOR,
  COMPLEX_FILTER_SELECTORS,
  TASK_LIST_SELECTORS,
};
