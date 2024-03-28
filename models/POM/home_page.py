from playwright.sync_api import Page
from models.POM.components.search_component import SearchComponent
from models.POM.components.table_component import TableComponent
from .pages_base import PageBase
from .components.genres_component import GenresComponent


class HomePage(PageBase):

    def __init__(self, pom_page: Page, pom_title='Vite + React + TS'):
        self.url = "http://awoha.xyz/"
        super().__init__(playwright_page=pom_page, page_title=pom_title)
        self.playw_page.goto(self.url)

        self.label_title_table = self.playw_page.locator(selector="//h1[@class='chakra-heading css-r90ria']")
        self.label_title_genres = self.playw_page.locator(selector="xpath=//h2[@class='chakra-heading css-14kr7y7']")
        self.search_component = SearchComponent(playwright_page=pom_page, component_title="Game Search")
        self.table_component = TableComponent(playwright_page=pom_page, component_title="Game Table")
        self.genre_component = GenresComponent(playwright_page=pom_page, component_title="Genres List")
