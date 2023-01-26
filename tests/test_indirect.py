"""
Переопределите параметр с помощью indirect
"""
import pytest
from selene.support.shared import browser
from selene import be, have


@pytest.fixture(params=["1920*1080", "990*960"])
def window_size(request):
    if request.param == "1920*1080":
        browser.config.window_width = 1920
        browser.config.window_height = 1080
    elif request.param == "990*960":
        browser.config.window_width = 990
        browser.config.window_height = 960


@pytest.mark.parametrize("window_size", ["1920*1080"], indirect=True)
def test_github_desktop(window_size):
    browser.open('https://github.com/')
    browser.element('[href="/login"]').click()
    assert browser.element("[class='auth-form-body mt-3']").should(have.text("Username or email address"))


@pytest.mark.parametrize("window_size", ["990*960"], indirect=True)
def test_github_mobile(window_size):
    browser.open('https://github.com/')
    browser.element('.Button-label > div:first-child').click()
    browser.element('[href="/login"]').click()
    assert browser.element("[class='auth-form-body mt-3']").should(have.text("Username or email address"))
