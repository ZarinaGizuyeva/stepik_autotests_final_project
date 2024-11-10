from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def should_be_product_correct_name_in_basket(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        basket_message = self.browser.find_element(*ProductPageLocators.AFTER_ADD_TO_BASKET_MESSAGE)
        assert product_name.text in basket_message.text, "Wrong product name in basket"

    def should_be_product_correct_price_in_basket(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        basket_price_message = self.browser.find_element(*ProductPageLocators.BASKET_PRICE_MESSAGE)
        assert product_price.text in basket_price_message.text, "Wrong product price in basket"