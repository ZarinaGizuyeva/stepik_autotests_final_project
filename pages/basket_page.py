from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    url = "http://selenium1py.pythonanywhere.com/ru/basket/"
    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCTS_LIST_IN_BASKET), "Products in basket, but should be empty basket"

    def should_be_message_that_basket_empty(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_MESSAGE), "No message that basket is empty, but should be"