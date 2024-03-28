from playwright.sync_api import Page, expect
from models.POM.components.component_base import ComponentBase


class Table_Component(ComponentBase):
    def __init__(self, playwrightPage: Page, componentTitle: str):
        super().__init__(playwrightPage, componentTitle)

    def Get_CardsTitles(self):
        self.p_Page.wait_for_load_state("domcontentloaded")

        skeleton_locator = "chakra-skeleton css-1uzecpb"
        is_skeleton_visible = self.p_Page.locator(skeleton_locator).is_visible()
        if(is_skeleton_visible):
            expect(skeleton_locator).toHaveCount(0);

        elements = self.p_Page.locator("//h2[@class='chakra-heading css-1xix1js']")
        return elements

    def get_game_cards_amount(self, card_title: str):
        result = self.p_Page.locator(f"//h2[text()='{card_title}']")
        return result
