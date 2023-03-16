import re
from playwright.sync_api import Playwright, Page, expect
import pytest
from Models.POM.HomePage import HomePage
import pytest

#pytest -k test_homepage_canbeopened
def test_homepage_canbeopened(playwright: Playwright):
    #Arrange
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    home_Page = HomePage(page)

    #Assert
    expect(home_Page.p_Page).to_have_title("Main Page")
    expect(home_Page.label_title).to_be_visible()
    expect(home_Page.label_titleDescription).to_be_visible()

#pytest -m smoke - to run
#pytest -m "not smoke" - to run
@pytest.mark.smoke
def test_homepage_refressionmarker(playwright: Playwright):
    #Arrange
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    home_Page = HomePage(page)

    #Assert
    expect(home_Page.p_Page).to_have_title("Main Page")
    expect(home_Page.label_title).to_be_visible()
    expect(home_Page.label_titleDescription).to_be_visible()

@pytest.mark.skip(reason="duplicate")
def test_homepage_toskip(playwright: Playwright):
    #Arrange
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    home_Page = HomePage(page)


@pytest.mark.xfail(reason="feature in development")
def test_homepage_toskip(playwright: Playwright):
    #Arrange
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    home_Page = HomePage(page)

    #Assert
    expect(home_Page.p_Page).to_have_title("Main Page!")