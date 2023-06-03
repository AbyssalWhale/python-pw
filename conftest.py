import conftest
from Models.POM.HomePage import HomePage
from typing import Generator
import json
import pytest
import os
from playwright.sync_api import expect
from playwright.sync_api import Playwright, APIRequestContext

test_run_config = None
api_request_context = None
home_page = None
api_request_context = None

@pytest.fixture(scope="session")
def set_up(playwright: Playwright):
    _read_api_header()

    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    home_page = HomePage(page)

    expect(home_page.p_Page).to_have_title(home_page.page_title)
    expect(home_page.label_title_table).to_be_visible()
    expect(home_page.label_title_genres).to_be_visible()

    conftest.home_page = home_page

    yield conftest.home_page

    conftest.home_page.p_Page.close()


@pytest.fixture(scope="session")
def api_request_context(playwright: Playwright) -> Generator[APIRequestContext, None, None]:
    request_context = playwright.request.new_context(base_url="https://api.rawg.io/api/")
    conftest.api_request_context = request_context

    yield conftest.api_request_context
    request_context.dispose()

def _init_Home_Page(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    home_page = HomePage(page)

    expect(home_page.p_Page).to_have_title(home_page.page_title)
    expect(home_page.label_title_table).to_be_visible()
    expect(home_page.label_title_genres).to_be_visible()

    home_page = home_page

    yield home_page

def _read_api_header():
    full_File_Path = f'{get_project_root()}//configs//api_headers.json'
    if os.path.exists(full_File_Path):
        with open(full_File_Path) as f:
            conftest.test_run_config = json.load(f)
    else:
        raise Exception(f"Could not find file with api headers. Path: {full_File_Path}")


def get_project_root():
    current_dir = os.path.abspath(os.path.dirname(__file__))
    while not os.path.isfile(os.path.join(current_dir, 'conftest.py')):
        parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
        if parent_dir == current_dir:
            # Reached the root directory without finding the project marker file
            raise Exception("Could not find project root directory.")
        current_dir = parent_dir
    return current_dir