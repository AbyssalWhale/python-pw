from playwright.async_api import Page
from Models.POM.components.component_base_a import ComponentBaseA


class GenresComponent(ComponentBaseA):
    def __init__(self, playwright_page: Page, component_title: str):
        super().__init__(playwright_page=playwright_page, component_title=component_title)

    async def click_genre_button(self, genre_name: str):
        async with self.p_page.expect_response("**/api/games**&genres=**") as response_info:
            await self.p_page.locator(f"//ul//button[text()='{genre_name}']").click()
        response = await response_info.value
        assert response.ok
        genre_games = await response.json()
        return genre_games
