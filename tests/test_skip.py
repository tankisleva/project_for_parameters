"""
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""
import pytest
from selene.support.shared import browser
from selene import have


@pytest.mark.parametrize("window_width,window_height",
                         [pytest.param(1920, 1080),
                          pytest.param(990, 960)
                          ])
def test_github_desktop(window_width, window_height):
    if window_width == 990:
        pytest.skip(reason='Пропускаем мобильную версию в данном тесте')
    browser.config.window_width = window_width
    browser.config.window_height = window_height
    browser.open('https://github.com/')
    browser.element('[href="/login"]').click()
    assert browser.element("[class='auth-form-body mt-3']").should(have.text("Username or email address"))


@pytest.mark.parametrize("window_width,window_height",
                         [pytest.param(1920, 1080, id="desktop version"),
                          pytest.param(990, 960, id="mobile_version")
                          ])
def test_github_mobile(window_width,window_height):
    if window_width == 1920:
        pytest.skip(reason='Пропускаем десктопную версию в данном тесте')
    browser.config.window_width = window_width
    browser.config.window_height = window_height
    browser.open('https://github.com/')
    browser.element('.Button-label > div:first-child').click()
    browser.element('[href="/login"]').click()
    assert browser.element("[class='auth-form-body mt-3']").should(have.text("Username or email address"))