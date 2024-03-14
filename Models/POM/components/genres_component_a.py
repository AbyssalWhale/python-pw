from playwright.async_api import Page
from Models.POM.components.component_base_a import ComponentBaseA


class GenresComponent(ComponentBaseA):
    def __init__(self, playwright_page: Page, component_title: str):
        super().__init__(playwright_page=playwright_page, component_title=component_title)

    def click_genre_button(self, genre_name: str):
        with self.p_page.expect_response(f"**/api/games**&genres=**") as response_info:
            self.p_page.locator(f"//ul//button[text()='{genre_name}']").click()
        assert response_info.value.ok
        genre_games = response_info.value.json()
        return genre_games
