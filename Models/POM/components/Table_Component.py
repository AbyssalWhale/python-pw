from playwright.sync_api import Page
from Models.POM.components.ComponentBase import ComponentBase


class Table_Component(ComponentBase):
    def __init__(self, playwrightPage: Page, componentTitle: str):
        super().__init__(playwrightPage, componentTitle)

    def Get_CardsTitles(self):
        elements = self.p_Page.locator("//h2[@class='chakra-heading css-1xix1js']")
        return elements