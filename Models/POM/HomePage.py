from playwright.sync_api import Page

class HomePage:

    #label_title = "//h1[contains(text(), 'Bakhmut center of professional and technical education')]"
    #label_titleDescription = "//p[contains(text(), 'A wonderful and amazing story of a kind of forge of working personnel.')]"

    def __init__(self, page: Page):
        self.url = "http://awoha.xyz/"
        self.p_Page = page
        self.p_Page.goto(self.url)

        self.label_title = self.p_Page.locator(selector="xpath=//h1[contains(text(), 'Bakhmut center of professional and technical education')]")
        self.label_titleDescription = self.p_Page.locator(selector="xpath=//p[contains(text(), 'A wonderful and amazing story of a kind of forge of working personnel.')]")