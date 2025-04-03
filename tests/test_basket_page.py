import pytest
from pages.basket_page import BasketPage

class TestBasketPage:
    def setup_method(self):
        self.basket_page = BasketPage(self.browser)

    def test_should_be_basket_url(self, browser):
        self.basket_page.open()
        self.basket_page.should_be_basket_url()
    def test_basket_should_be_empty(self, browser):
        self.basket_page.open()
        self.basket_page.should_be_empty_basket()
        self.basket_page.should_be_message_that_basket_empty()
    def test_guest_can_click_continue_shopping_link(self, browser):
        self.basket_page.open()
        self.basket_page.should_be_clickable_continue_shopping_link()