import pytest
from selene import browser

from model.utils import attach

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)  # Сохраняем отчет в узел теста

@pytest.fixture()
def browser_manager(request):
    browser.config.base_url = 'https://github.com'
    yield browser
    skip_marker = request.node.get_closest_marker("skip") or request.node.get_closest_marker("skipif")
    was_skipped = hasattr(request.node, "rep_call") and request.node.rep_call.skipped
    if not skip_marker and not was_skipped:
        attach.add_screenshot(browser)
    browser.quit()


@pytest.fixture(params=[(1280, 720), (1920, 1080), (2560, 1140), (360, 640), (375, 667), (414, 736)])
def resolution(request):
    return request.param


@pytest.fixture(params=["desktop", "mobile"])
def browser_manager_version(request, resolution):
    width, height = resolution
    version = request.param
    browser.config.base_url = 'https://github.com'
    yield browser, version, width, height
    skip_marker = request.node.get_closest_marker("skip") or request.node.get_closest_marker("skipif")
    was_skipped = hasattr(request.node, "rep_call") and request.node.rep_call.skipped
    if not skip_marker and not was_skipped:
        attach.add_screenshot(browser)
    browser.quit()


@pytest.fixture(params=[(1280, 720), (1920, 1080), (2560, 1140)])
def browser_manager_desktop(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height
    browser.config.base_url = 'https://github.com'
    yield browser
    attach.add_screenshot(browser)
    browser.quit()


@pytest.fixture(params=[(360, 640), (375, 667), (414, 736)])
def browser_manager_mobile(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height
    browser.config.base_url = 'https://github.com'
    yield browser
    attach.add_screenshot(browser)
    browser.quit()
