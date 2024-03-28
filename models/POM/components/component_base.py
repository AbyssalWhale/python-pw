from abc import ABCMeta, abstractmethod
from playwright.sync_api import Page

class ComponentBase(object, metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, playwrightPage: Page, componentTitle: str):
        self.p_Page = playwrightPage
        self.component_title = componentTitle