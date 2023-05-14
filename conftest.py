import re
from playwright.sync_api import Playwright, Page, expect
import pytest
from Models.POM.HomePage import HomePage
import pytest

@pytest.fixture(scope="function")
def set_up(playwright: Playwright):
    browser = playwright.webkit.launch(headless=True)
    page = browser.new_page()
    home_Page = HomePage(page)

    expect(home_Page.p_Page).to_have_title(home_Page.page_title)
    expect(home_Page.label_title_table).to_be_visible()
    expect(home_Page.label_title_genres).to_be_visible()

    yield home_Page

    home_Page.p_Page.close()