import allure
import pytest

from model.pages.application import app

@pytest.mark.parametrize("browser_manager_version", ["desktop"], indirect=True)
@allure.title("Проверка нажатия на кнопку Sign In (desktop)")
@allure.description("Открытие страницы -> Нажатие на кнопку Sign In")
def test_github_2(browser_manager_version):
    browser, version, width, height = browser_manager_version
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