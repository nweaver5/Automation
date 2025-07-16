const LOGIN_URL = "https://tenonworkshop.service-now.com/navpage.do";

const CADSO_NAV_HEADER = `document.querySelector("macroponent-aededa80c782201072b211d4d8c2604c").shadowRoot.querySelector("sn-canvas-appshell-main").shadowRoot.querySelector("macroponent-355f43e047f8f510b0361ae8036d4355").shadowRoot.querySelector("macroponent-67ee2538534501108135ddeeff7b121b").querySelector("cadso-nav-header")`;
const AVATAR_DROPDOWN_SELECTOR = `return ${CADSO_NAV_HEADER}.shadowRoot.querySelector("div")`;
const TITLE_SELECTOR = `return ${CADSO_NAV_HEADER}.shadowRoot.querySelector(".title")`;

const SN_GSFT_MAIN_SELECTOR = `return document.querySelector("#gsft_main")`;
const SN_FILTER_SELECTOR = `return document.querySelector("#filter")`;

export {
  LOGIN_URL,
  TITLE_SELECTOR,
  AVATAR_DROPDOWN_SELECTOR,
  SN_GSFT_MAIN_SELECTOR,
  SN_FILTER_SELECTOR,
};
