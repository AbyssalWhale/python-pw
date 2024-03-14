from playwright.async_api import Page
from Models.POM.components.component_base_a import ComponentBaseA


class SearchComponent(ComponentBaseA):
    def __init__(self, playwright_page: Page, component_title: str):
        super().__init__(playwright_page=playwright_page, component_title=component_title)

    def input_search_field(self, game_name: str):
        self.p_page.input_search_game = self.p_page.locator("//input[@placeholder='Search games...']")
        self.p_page.input_search_game.fill(game_name)
        self.p_page.input_search_game.press("Enter")
        self.p_page.wait_for_load_state("domcontentloaded")
        return self
