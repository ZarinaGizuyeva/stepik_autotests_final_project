import pytest

from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.profile_page import ProfilePage


@pytest.mark.usefixtures("browser")
class TestProductPage:
    def setup_method(self):
        self.product_page = ProductPage(self.browser)

    @pytest.mark.need_review
    def test_guest_can_add_product_to_basket(self):
        self.product_page.open()
        self.product_page.add_to_basket()
        self.product_page.should_be_product_correct_name_in_basket()
        self.product_page.should_be_product_correct_price_in_basket()

    @pytest.mark.xfail
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self):
        self.product_page.open()
        self.product_page.add_to_basket()
        self.product_page.should_not_be_success_message()

    def test_guest_cant_see_success_message(self):
        self.product_page.open()
        self.product_page.should_not_be_success_message()

    @pytest.mark.xfail
    def test_message_disappeared_after_adding_product_to_basket(self):
        self.product_page.open()
        self.product_page.add_to_basket()
        self.product_page.should_disappear_success_message()

    def test_guest_should_see_login_link_on_product_page(self):
        self.product_page.open()
        self.product_page.should_be_login_link()

    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(self):
        self.product_page.open()
        self.product_page.go_to_login_page()

    @pytest.mark.need_review
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self):
        self.product_page.open()
        self.product_page.go_to_basket_page()
        self.basket_page = BasketPage(self.browser)
        self.basket_page.should_be_empty_basket()
        self.basket_page.should_be_message_that_basket_empty()

    @pytest.fixture()
    def login(self, generate_login_password):
        self.login_page = LoginPage(self.browser)
        self.login_page.open()
        self.login_page.register_new_user(generate_login_password)
        self.login_page.should_be_authorized_user()
        yield
        self.basket_page = BasketPage(self.browser)
        self.basket_page.go_to_account()
        self.profile_page = ProfilePage(self.browser)
        self.profile_page.open()
        self.profile_page.delete_profile(generate_login_password[1])


    def test_user_can_add_product_to_basket(self, login):
        self.product_page.open()
        self.product_page.add_to_basket()
        self.product_page.should_be_product_correct_name_in_basket()
        self.product_page.should_be_product_correct_price_in_basket()

    @pytest.mark.need_review
    def test_user_cant_see_success_message(self, login):
        self.product_page.open()
        self.product_page.should_not_be_success_message()