from playwright.sync_api import Page
from Models.POM.components.ComponentBase import ComponentBase


class Search_Component(ComponentBase):
    def __init__(self, playwrightPage: Page, componentTitle: str):
        super().__init__(playwrightPage, componentTitle)

    def input_search_field(self, gameName: str):
        self.p_Page.input_search_game = self.p_Page.locator("//input[@placeholder='Search games...']")
        self.p_Page.input_search_game.fill(gameName)
        self.p_Page.input_search_game.press("Enter")
        self.p_Page.wait_for_load_state("domcontentloaded")
        return self
