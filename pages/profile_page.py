from .base_page import BasePage
from .locators import ProfilePageLocators


class ProfilePage(BasePage):
    url = "http://selenium1py.pythonanywhere.com/ru/accounts/profile/"

    def delete_profile(self, generate_login_password):
        self.browser.find_element(*ProfilePageLocators.DELETE_PROFILE_BUTTON).click()
        self.browser.find_element(*ProfilePageLocators.DELETE_PROFILE_PASS_FIELD).send_keys(generate_login_password[1])
        self.browser.find_element(*ProfilePageLocators.DELETE_PROFILE_CONFIRM_BUTTON).click()