from playwright.sync_api import Page
from .PagesBase import PageBase
from .AboutUsPage import AboutUsPage

class HomePage(PageBase):

    #label_title = "//h1[contains(text(), 'Bakhmut center of professional and technical education')]"
    #label_titleDescription = "//p[contains(text(), 'A wonderful and amazing story of a kind of forge of working personnel.')]"

    def __init__(self, pomPage: Page, pomTitle = 'Main Page'):
        self.url = "http://awoha.xyz/"
        super().__init__(playwrightPage=pomPage, pageTitle=pomTitle)
        self.p_Page.goto(self.url)

        self.label_title = self.p_Page.locator(selector="xpath=//h1[contains(text(), 'Bakhmut center of professional and technical education')]")
        self.label_titleDescription = self.p_Page.locator(selector="xpath=//p[contains(text(), 'A wonderful and amazing story of a kind of forge of working personnel.')]")

    def Click_MoreAboutUs_Button(self):
        self.p_Page.get_by_text("More about us").click()
        return AboutUsPage(pomPage=self.p_Page)
