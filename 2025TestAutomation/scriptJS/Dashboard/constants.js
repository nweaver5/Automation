const CADSO_NAV_HEADER = `document.querySelector("macroponent-aededa80c782201072b211d4d8c2604c").shadowRoot.querySelector("sn-canvas-appshell-main").shadowRoot.querySelector("macroponent-355f43e047f8f510b0361ae8036d4355").shadowRoot.querySelector("macroponent-67ee2538534501108135ddeeff7b121b").querySelector("cadso-nav-header")`;
const SN_CANVAS_SCREEN_LAST_OF_TYPE = `${CADSO_NAV_HEADER}.querySelector("sn-canvas-main").shadowRoot.querySelector("sn-canvas-screen:last-of-type").shadowRoot`;
const CADSO_MENU_SELECTOR = `return ${CADSO_NAV_HEADER}.querySelector("cadso-ui-menu").shadowRoot.querySelector("div")`;
const CADSO_UI_TABS = `${CADSO_NAV_HEADER}.shadowRoot.querySelector("cadso-ui-tabs").shadowRoot`
const TASK_LIST_CONTAINER = `${SN_CANVAS_SCREEN_LAST_OF_TYPE}.querySelector("section").querySelector("macroponent-8a6f50dd47b42510a1052a02e26d438e").shadowRoot.querySelector("cadso-ui-list").shadowRoot`;
const TITLE_SELECTOR = `return ${CADSO_NAV_HEADER}.shadowRoot.querySelector(".title").textContent`;
const DASHBOARD_STATS_BAR = `${SN_CANVAS_SCREEN_LAST_OF_TYPE}.querySelector("macroponent-8d0e728a47e86110a1052a02e26d436e").shadowRoot.querySelector("cadso-ui-stats-bar").shadowRoot`;
const TASKBOX_CONTAINER = `${SN_CANVAS_SCREEN_LAST_OF_TYPE}.querySelector("macroponent-8d0e728a47e86110a1052a02e26d436e").shadowRoot.querySelector("cadso-active-task").shadowRoot.querySelector(".taskbox-container")`;
const RECENT_PROJECTS_LIST = `${SN_CANVAS_SCREEN_LAST_OF_TYPE}.querySelector("macroponent-8d0e728a47e86110a1052a02e26d436e").shadowRoot.querySelector("cadso-recent-list").shadowRoot.querySelector(".list.table-blank-state")`;


const DASHBOARD_STATS_BAR_SELECTORS = {
  IN_PROGRESS_TASKS: `${DASHBOARD_STATS_BAR}.querySelector(".stats-row").querySelectorAll(".stats-cell")[0]`,
  COMPLETED_TASKS: `${DASHBOARD_STATS_BAR}.querySelector(".stats-row").querySelectorAll(".stats-cell")[1]`,
  OVERDUE_TASKS: `${DASHBOARD_STATS_BAR}.querySelector(".stats-row").querySelectorAll(".stats-cell")[2]`,
};

const ACTIVE_TASKS_LIST_SELECTORS = {
  CONTAINER_HEADER: `${TASKBOX_CONTAINER}.querySelector(".container-header")`,
  CONTAINER_TASK_LIST: `${TASKBOX_CONTAINER}.querySelector(".container-task-list")`,
};

const RECENT_PROJECTS_SELECTORS = {
  LIST_OF_PROJECTS: `${RECENT_PROJECTS_LIST}.querySelectorAll(".projects")`,
};

const TASK_LIST_CONTAINER_SELECTORS = {
  TASK_LIST_CONTAINER,
  RECORDS_CONTAINER: `${TASK_LIST_CONTAINER}.querySelector(".records-container")`,
  LIST_ROWS: `${TASK_LIST_CONTAINER}.querySelectorAll(".list-row")`
}

const TAB_SELECTORS = {
  CADSO_UI_TABS,
  LIST_NEW_GROUPS_TAB: `${CADSO_UI_TABS}.querySelectorAll(".button-container")[0]`,
  BOARD_ACCEPTED_USERS_TAB: `${CADSO_UI_TABS}.querySelectorAll(".button-container")[1]`,
  CALENDAR_DECLINED_PROJECTTEMPLATES_TAB: `${CADSO_UI_TABS}.querySelectorAll(".button-container")[2]`,
}

const CADSO_UI_KANBAN_SELECTORS = {
  CADSO_UI_KANBAN_TASKBOARD: `${SN_CANVAS_SCREEN_LAST_OF_TYPE}.querySelector("macroponent-a4c62471474de15085d19fd8036d43e4").shadowRoot.querySelector("cadso-ui-kanban").shadowRoot`,
  CADSO_UI_KANBAN_PROJECTSBOARD: `${SN_CANVAS_SCREEN_LAST_OF_TYPE}.querySelector("macroponent-b7ab1a654755a910fc4c1ae8036d43fd").shadowRoot.querySelector("cadso-ui-kanban").shadowRoot`,
}

const ADMIN_SETTINGS_SELECTORS = {
  RECORDS_CONTAINER: `${SN_CANVAS_SCREEN_LAST_OF_TYPE}.querySelector("macroponent-7ddc05468796ed50b656fe66cebb3586").shadowRoot.querySelector("cadso-ui-list").shadowRoot.querySelector(".records-container")`,
  GROUPS_LIST_ROWS: `${SN_CANVAS_SCREEN_LAST_OF_TYPE}.querySelector("macroponent-7ddc05468796ed50b656fe66cebb3586").shadowRoot.querySelector("cadso-ui-list").shadowRoot.querySelector(".records-container").querySelectorAll(".list-row")`,
  USERS_LIST_ROWS: `${SN_CANVAS_SCREEN_LAST_OF_TYPE}.querySelector("macroponent-5e6c958287d6ed50b656fe66cebb35fc").shadowRoot.querySelector("cadso-ui-list").shadowRoot.querySelector(".records-container").querySelectorAll(".list-row")`,
  PROJECT_TEMPLATES_LIST_ROWS: `${SN_CANVAS_SCREEN_LAST_OF_TYPE}.querySelector("macroponent-1bb0909b87fda910b656fe66cebb356d").shadowRoot.querySelector("cadso-ui-list").shadowRoot.querySelector(".records-container").querySelectorAll(".list-row")`,
  CREATE_NEW_PROJECT_SELECTOR: `return ${SN_CANVAS_SCREEN_LAST_OF_TYPE}.querySelector("macroponent-1bb0909b87fda910b656fe66cebb356d").shadowRoot.querySelector("cadso-simple-button").shadowRoot.querySelector("button")`
}

const GOALS_SELECTORS = {
  GOALS_LIST: `${SN_CANVAS_SCREEN_LAST_OF_TYPE}.querySelector("macroponent-c582bc4647463910b0361ae8036d43f8").shadowRoot.querySelector("cadso-ui-list").shadowRoot.querySelector(".records-container").querySelectorAll(".list-row")`,
  CREATE_A_GOAL_SELECTOR: `${SN_CANVAS_SCREEN_LAST_OF_TYPE}.querySelector("macroponent-c582bc4647463910b0361ae8036d43f8").shadowRoot.querySelector("cadso-simple-button").shadowRoot.querySelector("button")`,
}

const MENU_LIST_ITEMS_SELECTORS = {
  VIEW_ALL_SPRINTS_SELECTOR: `return ${CADSO_MENU_SELECTOR}.querySelectorAll(".show")[0].querySelector(".more-link").querySelector(".more-link-button")`,
  VIEW_ALL_PROJECTS_SELECTOR: `return ${CADSO_MENU_SELECTOR}.querySelectorAll(".show")[1].querySelector(".more-link").querySelector(".more-link-button")`,
  VIEW_ALL_CAMPAIGNS_SELECTOR: `return ${CADSO_MENU_SELECTOR}.querySelectorAll(".show")[2].querySelector(".more-link").querySelector(".more-link-button")`,
}

export {
  CADSO_MENU_SELECTOR,
  MENU_LIST_ITEMS_SELECTORS,
  TITLE_SELECTOR,
  DASHBOARD_STATS_BAR_SELECTORS,
  ACTIVE_TASKS_LIST_SELECTORS,
  RECENT_PROJECTS_SELECTORS,
  TASK_LIST_CONTAINER_SELECTORS,
  CADSO_UI_KANBAN_SELECTORS,
  TAB_SELECTORS,
  ADMIN_SETTINGS_SELECTORS,
  GOALS_SELECTORS,
};
