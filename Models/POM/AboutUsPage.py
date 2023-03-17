from playwright.sync_api import Page
from .PagesBase import PageBase

class AboutUsPage(PageBase):
    
    def __init__(self, pomPage: Page, pomTitle = 'Out history'):
        super().__init__(playwrightPage=pomPage, pageTitle=pomTitle)
        self.label_ourStory = self.p_Page.locator("h1.storyHeader") 