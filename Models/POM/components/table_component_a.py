from playwright.async_api import Page, expect
from Models.POM.components.component_base_a import ComponentBaseA


class TableComponent(ComponentBaseA):
    def __init__(self, playwright_page: Page, component_title: str):
        super().__init__(playwright_page=playwright_page, component_title=component_title)

    def Get_CardsTitles(self):
        self.p_page.wait_for_load_state("domcontentloaded")

        skeleton_locator = "chakra-skeleton css-1uzecpb"
        is_skeleton_visible = self.p_page.locator(skeleton_locator).is_visible()
        if is_skeleton_visible:
            expect(skeleton_locator).toHaveCount(0)

        elements = self.p_page.locator("//h2[@class='chakra-heading css-1xix1js']")
        return elements

    def get_game_cards_amount(self, card_title: str):
        result = self.p_page.locator(f"//h2[text()='{card_title}']")
        return result
