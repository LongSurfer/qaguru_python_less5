from selene.support.shared import browser
import pytest


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.browser_name = 'chrome'
    browser.config.base_url = 'https://demoqa.com/'
    browser.config.hold_browser_open = True


@pytest.fixture(scope='function', autouse=True)
def browser_size():
    browser.config.window_width = 1777
    browser.config.window_height = 1000