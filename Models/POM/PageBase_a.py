from abc import ABCMeta, abstractmethod
from playwright.async_api import Page


class PageBaseA(object, metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, playwright_page: Page, page_title: str):
        self.p_page = playwright_page
        self.page_title = page_title
