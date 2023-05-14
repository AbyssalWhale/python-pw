import re
from playwright.sync_api import Playwright, Page, expect
import pytest
from Models.POM.HomePage import HomePage
import pytest

@pytest.fixture(scope="function")
def set_up(playwright: Playwright):
    browser = playwright.webkit.launch(headless=False, slow_mo=1000)
    page = browser.new_page()
    home_Page = HomePage(page)

    yield home_Page

    home_Page.p_Page.close()