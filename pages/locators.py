from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form.well")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form.well")

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "h1")
    AFTER_ADD_TO_BASKET_MESSAGE = (By.CSS_SELECTOR, ".alert-success .alertinner")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    BASKET_PRICE_MESSAGE = (By.CSS_SELECTOR, ".alert-info .alertinner")