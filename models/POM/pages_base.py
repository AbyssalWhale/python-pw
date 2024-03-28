from abc import ABCMeta, abstractmethod
from playwright.sync_api import Page

class PageBase(object, metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, playwrightPage: Page, pageTitle: str):
        self.p_Page = playwrightPage
        self.page_title = pageTitle