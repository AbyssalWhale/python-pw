from playwright.sync_api import Playwright, Page, expect
import conftest
from Models.POM.HomePage import HomePage
from typing import Generator
import json
import sys
import pytest
from playwright.sync_api import Playwright, APIRequestContext

test_run_config = None

@pytest.fixture(scope="function")
def set_up(playwright: Playwright):
    with open(f'{sys.path[1]}\\..\\configs\\api_headers.json') as f:
        conftest.test_run_config = json.load(f)

    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page()
    home_page = HomePage(page)

    expect(home_page.p_Page).to_have_title(home_page.page_title)
    expect(home_page.label_title_table).to_be_visible()
    expect(home_page.label_title_genres).to_be_visible()

    yield home_page

    home_page.p_Page.close()


@pytest.fixture(scope="session")
def api_request_context(playwright: Playwright) -> Generator[APIRequestContext, None, None]:
    request_context = playwright.request.new_context(base_url="https://api.rawg.io/api/")
    yield request_context
    request_context.dispose()