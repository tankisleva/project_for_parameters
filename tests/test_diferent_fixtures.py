"""
Сделайте разные фикстуры для каждого теста
"""

import pytest
from selene.support.shared import browser
from selene import have


@pytest.fixture
def setup_desktop():
    browser.config.window_height = 1080
    browser.config.window_width = 1920
    yield
    browser.quit()


@pytest.fixture
def setup_mobile():
    browser.config.window_width = 960
    browser.config.window_height = 990
    yield
    browser.quit()


def test_open_desktop(setup_desktop):
    browser.open('https://github.com/')
    browser.element('[href="/login"]').click()
    assert browser.element("[class='auth-form-body mt-3']").should(have.text("Username or email address"))


def test_open_mobile(setup_mobile):
    browser.open('https://github.com/')
    browser.element('.Button-label > div:first-child').click()
    browser.element('[href="/login"]').click()
    assert browser.element("[class='auth-form-body mt-3']").should(have.text("Username or email address"))
