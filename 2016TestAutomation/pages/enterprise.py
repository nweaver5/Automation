from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from .base_page import BasePage
from steps.base_module import BaseModule
from selenium.webdriver.support.ui import Select


class Enterprise(BasePage):
    users_tab = (By.CSS_SELECTOR, 'AccountNameActions > li:nth-child(2)')
    roles_tab = (By.CSS_SELECTOR, 'AccountNameActions > li:nth-child(3)')
    groups_tab = (By.CSS_SELECTOR, 'AccountNameActions > li:nth-child(4)')
    add_item_button = (By.CSS_SELECTOR, 'MainContent>ng-view>div:nth-child(1)>div>div.fancy-button.blue.right')
    username = (By.ID, 'UsernameField')
    displayname = (By.ID, 'DisplayNameField')
    email = (By.ID, 'NewEmailField')
    user_role_select2 = (By.XPATH, '//*[@id="AddUserModal"]/div/ng-transclude/div[1]/div[4]/div/div[1]/div[1]/ul/li/input')
    user_save_button = (By.ID, 'SaveUserButton')
    rolename = (By.ID, 'RoleNameField')
    role_select = (By.XPATH, '//*[@id="AddRoleModal"]/div/ng-transclude/div[1]/div[2]/div[1]/div[1]/span[3]')
    role_save_button = (By.CSS_SELECTOR, 'AddRoleModal>div>ng-transclude>div.modal-popup-footer.ng-scope>div>div:nth-child(1)')
    groupname = (By.ID, 'GroupNameField')
    group_manager_select2 = (By.XPATH, '//*[@id="AddGroupModal"]/div/ng-transclude/div[1]/div[2]/div/div/div/ul/li/input')
    group_member_select2 = (By.XPATH, '//*[@id="AddGroupModal"]/div/ng-transclude/div[1]/div[3]/div/div/ul/li/input')
    group_save_button = (By.CSS_SELECTOR, 'AddGroupModal>div>ng-transclude>div.modal-popup-footer.ng-scope>div>div:nth-child(1)')

    #GET ITEMS

    def get_users_tab(self):
        return self.driver.find_element(*self.users_tab)

    def get_roles_tab(self):
        return self.driver.find_element(*self.roles_tab)

    def get_groups_tab(self):
        return self.driver.find_element(*self.groups_tab)

    def get_add_item_button(self):
        return self.driver.find_element(*self.add_item_button)

    def get_username(self):
        return self.driver.find_element(*self.username)

    def get_displayname(self):
        return self.driver.find_element(*self.displayname)

    def get_email(self):
        return self.driver.find_element(*self.email)

    def get_user_role_select(self):
        return self.driver.find_element(*self.user_role_select2)

    def get_user_save_button(self):
        return self.driver.find_element(*self.user_save_button)

    def get_rolename(self):
        return self.driver.find_element(*self.rolename)

    def get_role_select(self):
        return self.driver.find_element(*self.role_select)

    def get_role_save_button(self):
        return self.driver.find_element(*self.role_save_button)

    def get_groupname(self):
        return self.driver.find_element(*self.groupname)

    def get_group_manager_select(self):
        return self.driver.find_element(*self.group_manager_select2)

    def get_group_member_select(self):
        return self.driver.find_element(*self.group_member_select2)

    def get_group_save_button(self):
        return self.driver.find_element(*self.group_save_button)

    #ACTION ITEMS

    def click_users_tab(self):
        self.get_users_tab().click()

    def click_roles_tab(self):
        self.get_roles_tab().click()

    def click_groups_tab(self):
        self.get_groups_tab().click()

    def click_add_item_button(self):
        self.get_add_item_button().click()

    def set_username(self, keys):
        self.get_username().send_keys(keys)

    def set_displayname(self, keys):
        self.get_displayname().send_keys(keys)

    def set_email(self, keys):
        self.get_email().send_keys(keys)

    def set_user_role_select(self, keys):
        self.get_user_role_select().send_keys(keys)

    def press_user_role_select_enter(self):
        self.get_user_role_select().send_keys(Keys.RETURN)

    def click_user_save_button(self):
        self.get_user_save_button().click()

    def set_rolename(self, keys):
        self.get_rolename().send_keys(keys)

    def click_role_select(self):
        self.get_role_select().click()

    def click_role_save_button(self):
        self.get_role_save_button().click()

    def set_groupname(self, keys):
        self.get_groupname().send_keys(keys)

    def set_group_manager_select(self, keys):
        self.get_group_manager_select().send_keys(keys)

    def press_group_manager_select_enter(self):
        self.get_group_manager_select().send_keys(Keys.RETURN)

    def set_group_member_select(self, keys):
        self.get_group_member_select().send_keys(keys)

    def press_group_member_select_enter(self):
        self.get_group_member_select().send_keys(Keys.RETURN)

    def click_group_save_button(self):
        self.get_group_save_button().click()
