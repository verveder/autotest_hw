from playwright.sync_api import Page
from src.data import LOCATOR_SERVICES
from src.pages.base_page import BasePage


class HomePage(BasePage):
    """Describes home page of Cloud.ru site"""
    def __init__(self, page: Page):
        super().__init__(page)
        self.services_screen_button = self.locator(LOCATOR_SERVICES)

    def open_services_screen(self):
        """
        Clicks on Services in top navigation bar
        and opens Services screen
        """
        self.services_screen_button.click()
        self.page.wait_for_load_state()
