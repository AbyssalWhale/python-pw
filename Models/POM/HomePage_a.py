from playwright.async_api import Page

from Models.POM.PageBase_a import PageBaseA


class HomePageA(PageBaseA):

    def __init__(self, p_page: Page, page_title='Vite + React + TS'):
        self.url = "http://awoha.xyz/"
        super().__init__(playwright_page=p_page, page_title=page_title)

    async def open_and_check_load(self):
        await self.p_page.goto(self.url)

        self.label_title_table = self.p_page.locator(selector="//h1[@class='chakra-heading css-r90ria']")
        self.label_title_genres = self.p_page.locator(selector="xpath=//h2[@class='chakra-heading css-14kr7y7']")