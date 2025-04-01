from selenium.common import StaleElementReferenceException

from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    def add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def should_be_product_correct_name_in_basket(self):
        try:
            product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
            product_name_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_BASKET)
            assert product_name_in_basket.text == product_name.text, "Wrong product name in basket"
        except StaleElementReferenceException:
            return False

    def should_be_product_correct_price_in_basket(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        basket_price_message = self.browser.find_element(*ProductPageLocators.BASKET_PRICE_MESSAGE)
        assert product_price.text in basket_price_message.text, "Wrong product price in basket"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE_BASKET), \
            "Success message is presented, but should not be"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE_BASKET), \
            "Success message is presented, but should disappear"
