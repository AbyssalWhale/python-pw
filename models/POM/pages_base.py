from abc import ABCMeta, abstractmethod
from playwright.sync_api import Page


class PageBase(object, metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, playwright_page: Page, page_title: str):
        self.playw_page = playwright_page
        self.page_title = page_title
