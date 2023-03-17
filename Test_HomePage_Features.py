import re
from playwright.sync_api import Playwright, Page, expect
import pytest
from Models.POM.HomePage import HomePage
import pytest

#report - pip install pytest-reporter-html1
#rerun report with result - pytest -k test_homepage_canbeopened --report=report.html --template=html1/index.html

#run by name - pytest -k test_homepage_canbeopened
def test_homepage_canbeopened(set_up):
    home_Page = set_up

    #Assert
    expect(home_Page.p_Page).to_have_title(home_Page.page_title)
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
    expect(home_Page.p_Page).to_have_title(home_Page.page_title)
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
    expect(home_Page.p_Page).to_have_title(home_Page.page_title)