from abc import ABCMeta, abstractmethod
from playwright.async_api import Page


class ComponentBaseA(object, metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, playwright_page: Page, component_title: str):
        self.p_page = playwright_page
        self.component_title = component_title
