import pytest

from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.main_page import MainPage


@pytest.mark.login_guest
class TestMainPage:
    def setup_method(self):
        self.main_page = MainPage(self.browser)

    def test_guest_can_go_to_login_page(self, browser):
        self.main_page.open()
        self.main_page.go_to_login_page()
        login_page = LoginPage(self.browser)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        self.main_page.open()
        self.main_page.should_be_login_link()

    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        self.main_page.open()
        self.main_page.go_to_basket_page()
        basket_page = BasketPage(self.browser)
        basket_page.should_be_empty_basket()
        basket_page.should_be_message_that_basket_empty()

