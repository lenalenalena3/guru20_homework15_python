import allure
from selene import browser, have


class LoginPage:
    def __init__(self):
        self._title = browser.element('//h1[contains(@class,"module__authFormHeaderTitle")]')

    @allure.step("Проверить что открылась страница 'Sign in to GitHub'")
    def should_open_page(self):
        self._title.should(have.text('Sign in to GitHub'))
