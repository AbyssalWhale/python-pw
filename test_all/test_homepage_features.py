import re
from playwright.sync_api import Playwright, Page, expect

import conftest
from models.POM.home_page import HomePage
import pytest


# report - pip install pytest-reporter-html1
# rerun report with result - pytest -k test_homepage_can_be_opened --report=report.html --template=html1/index.html

# run by name - pytest -k test_homepage_can_be_opened
# pytest -m regression - to run regression tests
# pytest -m "not smoke" - to not run
@pytest.mark.regression
def test_homepage_can_be_opened(set_up):
    home_page = conftest.home_page

    # Assert
    expect(home_page.p_Page).to_have_title(home_page.page_title)
    expect(home_page.label_title_table).to_be_visible()
    expect(home_page.label_title_genres).to_be_visible()


@pytest.mark.skip(reason="duplicate")
def test_homepage_to_skip(playwright: Playwright):
    # Arrange
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    home_page = HomePage(page)


@pytest.mark.xfail(reason="feature in development")
def test_homepage_to_skip(playwright: Playwright):
    # Arrange
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    home_page = HomePage(page)

    # Assert
    expect(home_page.p_Page).to_have_title(home_page.page_title)