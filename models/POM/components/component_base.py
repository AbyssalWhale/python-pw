from abc import ABCMeta, abstractmethod
from playwright.sync_api import Page


class ComponentBase(object, metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, playwright_page: Page, component_title: str):
        self.p_Page = playwright_page
        self.component_title = component_title
