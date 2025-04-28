from conftest import generate_login_password
from .base_page import BasePage
from .locators import LoginPageLocators
import faker
import pytest


class LoginPage(BasePage):
    url = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"

    @pytest.mark.usefixtures("generate_login_password")
    def register_new_user(self, generate_login_password):
        self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL).send_keys(generate_login_password[0])
        self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD).send_keys(generate_login_password[1])
        self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_CONFIRM).send_keys(generate_login_password[1])
        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.url, "The url is not login page"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
