from playwright.sync_api import Page
from models.POM.components.component_base import ComponentBase


class SearchComponent(ComponentBase):
    def __init__(self, playwright_page: Page, component_title: str):
        super().__init__(playwright_page, component_title)

    def input_search_field(self, game_name: str):
        self.p_Page.input_search_game = self.p_Page.locator("//input[@placeholder='Search games...']")
        self.p_Page.input_search_game.fill(game_name)
        self.p_Page.input_search_game.press("Enter")
        self.p_Page.wait_for_load_state("domcontentloaded")
        return self
