import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import faker

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome', help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='en', help="Choose language: ru, en, fr etc.")

@pytest.fixture(autouse=True)
def browser(request):
    browser = webdriver.Chrome()
    options = Options()
    options.add_argument('--headless')
    request.cls.browser = browser
    yield
    browser.quit()

@pytest.fixture()
def generate_login_password(request):
    f = faker.Faker()
    email = f.email()
    password = f.password()
    return email, password






    # browser_name = request.config.getoption("browser_name")
    # language = request.config.getoption("language")
    # browser = None
    # options = Options()
    # options.add_argument('--headless')
    # options.add_experimental_option('prefs', {'intl.accept_languages': language})
    #
    # options_firefox = OptionsFirefox()
    # options_firefox.set_preference("intl.accept_languages", language)
    # if browser_name == "chrome":
    #     print("\nstart chrome browser for test..")
    #     browser = webdriver.Chrome(options=options)
    # elif browser_name == "firefox":
    #     print("\nstart firefox browser for test..")
    #     browser = webdriver.Firefox(options=options_firefox)
    # else:
    #     raise pytest.UsageError("--browser_name should be chrome or firefox")
    # yield browser
    # print("\nquit browser..")