import re
from playwright.sync_api import Playwright, Page, expect
import pytest
from Models.POM.HomePage import HomePage

#pip install pytest-xdist
#run: pytest .\1_GetStarted.py --headed --numprocesses auto

# @pytest.fixture(scope="session")
# def browser_context_args(browser_context_args, playwright):
#     iphone_11 = playwright.devices['iPhone 11 Pro']
#     return {
#         **browser_context_args,
#         **iphone_11,
#     }

def test_homepage(playwright: Playwright):
    #Arrange
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    home_Page = HomePage(page)

    #Assert
    expect(home_Page.p_Page).to_have_title(re.compile("Main Page"))
    expect(home_Page.label_title).to_be_visible()
    expect(home_Page.label_titleDescription).to_be_visible()