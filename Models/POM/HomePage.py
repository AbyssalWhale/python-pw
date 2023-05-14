from playwright.sync_api import Page
from Models.POM.components.Search_Component import Search_Component
from Models.POM.components.Table_Component import Table_Component
from .PagesBase import PageBase

class HomePage(PageBase):

    def __init__(self, pomPage: Page, pomTitle = 'Vite + React + TS'):
        self.url = "http://awoha.xyz/"
        super().__init__(playwrightPage=pomPage, pageTitle=pomTitle)
        self.p_Page.goto(self.url)

        self.label_title_table = self.p_Page.locator(selector="//h1[@class='chakra-heading css-r90ria']")
        self.label_title_genres = self.p_Page.locator(selector="xpath=//h2[@class='chakra-heading css-14kr7y7']")
        self.search_component = Search_Component(playwrightPage=pomPage, componentTitle="Game Search")
        self.table_component = Table_Component(playwrightPage=pomPage, componentTitle="Game Table")
