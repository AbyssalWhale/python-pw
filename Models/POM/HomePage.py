from playwright.sync_api import Page

class HomePage:
    def __init__(self, page: Page):
        self.url = "http://awoha.xyz/"
        self.p_Page = page
        self.p_Page.goto(self.url)