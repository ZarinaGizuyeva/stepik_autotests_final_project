from pages.login_page import LoginPage

class TestLoginPage:
    def setup_method(self):
        self.login_page = LoginPage(self.browser)

    def test_should_be_login_url(self, browser):
        self.login_page.open()
        self.login_page.should_be_login_url()

    def test_should_be_login_form(self, browser):
        self.login_page.open()
        self.login_page.should_be_login_form()

    def test_should_be_register_form(self, browser):
        self.login_page.open()
        self.login_page.should_be_register_form()