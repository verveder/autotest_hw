from playwright.sync_api import Page
from src.data import MAIN_URL


class BasePage:
    """Defines BasePage class"""
    def __init__(self, page: Page):
        self.page = page
        self.locator = self.page.locator
        self.url = MAIN_URL

    def navigate_to_page(self):
        """
        Goes to self.url
        (default value: MAIN_URL from data module)
        """
        self.page.goto(self.url, wait_until="load")
        return self
