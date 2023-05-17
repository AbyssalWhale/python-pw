from playwright.sync_api import Page
from Models.POM.components.ComponentBase import ComponentBase

class Genres_Component(ComponentBase):
    def __init__(self, playwrightPage: Page, componentTitle: str):
        super().__init__(playwrightPage, componentTitle)

    def click_genre_button(self, genreName: str):
        with self.p_Page.expect_response(f"**/api/games**&genres=**") as response_info:
            self.p_Page.locator(f"//ul//button[text()='{genreName}']").click()
        assert response_info.value.ok
        genre_games = response_info.value.json()
        return genre_games