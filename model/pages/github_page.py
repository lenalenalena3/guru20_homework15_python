import allure
from selene import browser, be



class GitHubPage:
    def __init__(self):
        self._sign_in_web = browser.element('//a[@href="/login"][not(contains(@class, "mobile"))]')
        self._sign_in_mob = browser.element('//a[@href= "/login" and contains(@class, "mobile")]')

    @allure.step("Открыть страницу")
    def open_page(self):
        browser.open("/")

    @allure.step("Нажать на кнопку sign in")
    def button_login_click_web(self):
        self._sign_in_web.should(be.visible).click()

    @allure.step("Нажать на кнопку sign in")
    def button_login_click_mobile(self):
        self._sign_in_mob.should(be.visible).click()
