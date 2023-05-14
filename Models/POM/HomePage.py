from playwright.sync_api import Page
from .PagesBase import PageBase
from .AboutUsPage import AboutUsPage

class HomePage(PageBase):

    #label_title = "//h1[contains(text(), 'Bakhmut center of professional and technical education')]"
    #label_titleDescription = "//p[contains(text(), 'A wonderful and amazing story of a kind of forge of working personnel.')]"

    def __init__(self, pomPage: Page, pomTitle = 'Vite + React + TS'):
        self.url = "http://awoha.xyz/"
        super().__init__(playwrightPage=pomPage, pageTitle=pomTitle)
        self.p_Page.goto(self.url)

        self.label_title_table = self.p_Page.locator(selector="//h1[@class='chakra-heading css-r90ria']")
        self.label_title_genres = self.p_Page.locator(selector="xpath=//h2[@class='chakra-heading css-14kr7y7']")
    
    def Input_SearchGame_Field(self, gameName: str):
        self.p_Page.input_searchgame = self.p_Page.locator("//input[@placeholder='Search games...']")
        self.p_Page.input_searchgame.fill(gameName)
        self.p_Page.input_searchgame.press("Enter")
        return self
    
    def Get_CardsTitles(self):
        elements = self.p_Page.locator("//h2[@class='chakra-heading css-1xix1js']")
        return elements
