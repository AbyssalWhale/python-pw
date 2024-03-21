import conftest
from Models.POM.HomePage import HomePage
from typing import Generator
from playwright.sync_api import expect
from playwright.sync_api import Playwright, APIRequestContext
from playwright.async_api import async_playwright
from datetime import datetime
import pytest
import aiofiles
import json
import allure
import os

from Models.POM.HomePage_a import HomePageA

test_run_config = None
test_run_content_folder = None
api_request_context = None
home_page = None


@pytest.fixture(scope="session", autouse=False)
def one_time_set_up():
    _read_api_header()
    conftest.test_run_content_folder = get_project_root() + '\\TestResults\\' + datetime.now().strftime(
        "%Y-%m-%d_%H-%M-%S")
    if not os.path.exists(conftest.test_run_content_folder):
        os.makedirs(conftest.test_run_content_folder)


@pytest.fixture(scope="session")
def set_up(one_time_set_up, playwright: Playwright):
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context(
        record_video_dir=f"{conftest.test_run_content_folder}/",
        record_video_size={"width": 640, "height": 480}
    )

    page = context.new_page()
    home_page = HomePage(page)

    expect(home_page.p_Page).to_have_title(home_page.page_title)
    expect(home_page.label_title_table).to_be_visible()
    expect(home_page.label_title_genres).to_be_visible()

    conftest.home_page = home_page

    yield conftest.home_page

    conftest.home_page.p_Page.close()
    context.close()
    print(f"Video Record: {page.video.path()}")


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
            raise Exception("Could not find project root directory.")
        current_dir = parent_dir
    return current_dir


class Fixtures:

    one_time_set_up = None

    @allure.title("One Time SetUp")
    @pytest.fixture(scope="session", autouse=True)
    async def one_time_setup(self):
        with allure.step("reading config"):
            self.proj_path = await self.__get_project_root()
            config_path = os.path.join(self.proj_path, "configs", "api_headers.json")
            self.test_run_config = await self.__read_from_json(filepath=config_path)
        with allure.step("create test result dir"):
            #self.test_results_dir = os.path.join(proj_path, "TestResults", datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))
            self.test_results_dir = os.path.join(self.proj_path, "Temp_TestResults", datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))
            if not os.path.exists(self.test_results_dir):
                os.makedirs(self.test_results_dir)

        return self

    @allure.title("Home Page Set Up")
    @pytest.fixture(scope="session", autouse=False)
    async def set_up_home_page(self, one_time_setup):
        self.one_time_setup = await one_time_setup
        with allure.step("init playwright"):
            self.playwright = await async_playwright().start()
            self.browser = await self.playwright.firefox.launch(headless=False)
            self.context = await self.browser.new_context()
            self.page = await self.context.new_page()
        with allure.step("init Home Page"):
            self.home_page = HomePageA(p_page=self.page)
            await self.home_page.open_and_check_load()
            await self.home_page.assert_is_page_loaded()


        return self


    @allure.title("Rest API Set Up")
    @pytest.fixture(scope="session", autouse=False)
    async def set_up_api(self):
        with allure.step("init playwright"):
            playwright = await async_playwright().start()
            browser = await playwright.firefox.launch(headless=False)
            self.playwright_request_context = await browser.new_context(base_url="https://api.rawg.io/api/")
            self.api_request_context = self.playwright_request_context.request
            proj_path = await self.__get_project_root()
            api_headers_path = os.path.join(proj_path, "configs", "api_headers.json")
            self.api_headers = await self.__read_from_json(api_headers_path)
        return self

    async def __read_from_json(self, filepath):
        async with aiofiles.open(filepath, mode='r') as file:
            data = await file.read()
            return json.loads(data)

    async def __get_project_root(self):
        current_dir = os.path.abspath(os.path.dirname(__file__))
        while not os.path.isfile(os.path.join(current_dir, 'conftest.py')):
            parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
            if parent_dir == current_dir:
                raise Exception("Could not find project root directory.")
            current_dir = parent_dir
        return current_dir


class TestSamples(Fixtures):
    @pytest.mark.asyncio
    @pytest.mark.parametrize("genre_under_test", ["Action"])
    async def test_example(self, set_up_home_page, set_up_api, genre_under_test):
        self.set_up_home_page = await set_up_home_page
        self.set_up_api = await set_up_api
        #test_game_category_can_be_selected
        with allure.step("gather genre info"):
            genres_response = await self.set_up_api.api_request_context.get("genres", params=self.set_up_api.api_headers)
            assert genres_response.ok
            genres_data = await genres_response.json()
            genres_data = genres_data["results"]
            genre_data = next((genre for genre in genres_data if genre['name'] == genre_under_test), None)
        with allure.step("gather games info"):
            params = self.set_up_api.one_time_setup.test_run_config
            params.update({"genres": genre_data["id"]})
            games_response = await self.set_up_api.api_request_context.get("genres", params=params)
            assert games_response.ok
            games_data = await games_response.json()
            games_data = games_data["results"]
