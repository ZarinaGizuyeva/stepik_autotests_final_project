from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini a.btn.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form.well")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form.well")
    REGISTER_EMAIL = (By.CSS_SELECTOR, "input#id_registration-email")
    REGISTER_PASSWORD = (By.CSS_SELECTOR, "input#id_registration-password1")
    REGISTER_PASSWORD_CONFIRM = (By.CSS_SELECTOR, "input#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "button[name=registration_submit]")

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    SUCCESS_MESSAGE_BASKET = (By.CSS_SELECTOR, ".alert-success .alertinner")
    PRODUCT_NAME = (By.CSS_SELECTOR, "h1")
    PRODUCT_NAME_IN_BASKET = (By.CSS_SELECTOR, ".alert-success .alertinner>strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    BASKET_PRICE_MESSAGE = (By.CSS_SELECTOR, ".alert-info .alertinner")

class BasketPageLocators():
    PRODUCTS_LIST_IN_BASKET = (By.CSS_SELECTOR, "form.basket_summary#basket_formset")
    BASKET_EMPTY_MESSAGE = (By.CSS_SELECTOR, ".content #content_inner")