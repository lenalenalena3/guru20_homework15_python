import allure
import pytest
from selene import browser

from model.pages.application import app

@pytest.mark.parametrize("width, height",
                         [("1280", "720"), ("1920", "1080"), ("2560", "1140"), ("360", "640"), ("375", "667"),
                          ("414", "736")])
@pytest.mark.parametrize("version", ["desktop", "mobile"])
@allure.title("Проверка нажатия на кнопку Sign In")
@allure.description("Открытие страницы -> Нажатие на кнопку Sign In")
def test_github_1(browser_manager, version, width, height):
    if version == "desktop" and int(width) < 1280:
        pytest.skip(reason="соотношение сторон мобильное")
    if version == "mobile" and int(width) >= 1280:
        pytest.skip(reason="соотношение сторон десктопное")
    browser.config.window_width = width
    browser.config.window_height = height
    app.github_page.open_page()
    if version == "desktop":
        app.github_page.button_login_click_web()
    else:
        app.github_page.button_login_click_mobile()
    app.login_page.should_open_page()


