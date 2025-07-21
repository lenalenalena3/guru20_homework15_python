import allure

from model.pages.application import app

@allure.title("Проверка нажатия на кнопку Sign In (desktop)")
@allure.description("Открытие страницы -> Нажатие на кнопку Sign In")
def test_github_desktop(browser_manager_desktop):
    app.github_page.open_page()
    app.github_page.button_login_click_web()
    app.login_page.should_open_page()

@allure.title("Проверка нажатия на кнопку Sign In (mobile")
@allure.description("Открытие страницы -> Нажатие на кнопку Sign In")
def test_github_mobile(browser_manager_mobile):
    app.github_page.open_page()
    app.github_page.button_login_click_mobile()
    app.login_page.should_open_page()