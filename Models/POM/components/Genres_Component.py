from playwright.sync_api import Page
from Models.POM.components.ComponentBase import ComponentBase

class Genres_Component(ComponentBase):
    def __init__(self, playwrightPage: Page, componentTitle: str):
        super().__init__(playwrightPage, componentTitle)

    def click_genre_button(self, genreName: str):
        self.p_Page.locator(f"//ul//button[text()='{genreName}']").click()
        return self