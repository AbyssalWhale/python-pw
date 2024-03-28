from playwright.sync_api import Page
from models.POM.components.component_base import ComponentBase


class GenresComponent(ComponentBase):
    def __init__(self, playwright_page: Page, component_title: str):
        super().__init__(playwright_page, component_title)

    def click_genre_button(self, genre_name: str):
        with self.p_Page.expect_response(f"**/api/games**&genres=**") as response_info:
            self.p_Page.locator(f"//ul//button[text()='{genre_name}']").click()
        assert response_info.value.ok
        genre_games = response_info.value.json()
        return genre_games
