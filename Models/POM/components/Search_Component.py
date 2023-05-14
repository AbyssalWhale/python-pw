from playwright.sync_api import Page
from Models.POM.components.ComponentBase import ComponentBase


class Search_Component(ComponentBase):
    def __init__(self, playwrightPage: Page, componentTitle: str):
        super().__init__(playwrightPage, componentTitle)

    def Input_Search_Field(self, gameName: str):
        self.p_Page.input_searchgame = self.p_Page.locator("//input[@placeholder='Search games...']")
        self.p_Page.input_searchgame.fill(gameName)
        self.p_Page.input_searchgame.press("Enter")
        return self