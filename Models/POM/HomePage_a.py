from playwright.async_api import Page
from Models.POM.PageBase_a import PageBaseA
from Models.POM.components.genres_component_a import GenresComponent
from Models.POM.components.search_component_a import SearchComponent
from Models.POM.components.table_component_a import TableComponent


class HomePageA(PageBaseA):

    def __init__(self, p_page: Page, page_title='Vite + React + TS'):
        self.url = "http://awoha.xyz/"
        super().__init__(playwright_page=p_page, page_title=page_title)

    async def open_and_check_load(self):
        await self.p_page.goto(self.url)
        await self._initialize_components()

    async def _initialize_components(self):
        self._label_title_table = self.p_page.locator(selector="//h1[@class='chakra-heading css-r90ria']")
        self._label_title_genres = self.p_page.locator(selector="xpath=//h2[@class='chakra-heading css-14kr7y7']")
        self._search_component = SearchComponent(playwright_page=self.p_page, component_title="Game Search")
        self._table_component = TableComponent(playwright_page=self.p_page, component_title="Game Table")
        self._genre_component = GenresComponent(playwright_page=self.p_page, component_title="Genres List")