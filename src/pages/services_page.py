from playwright.sync_api import Page
from src.data import LOCATOR_INFRASTRUCTURE, LOCATOR_APIGW
from src.pages.base_page import BasePage


class ServicesPage(BasePage):
    """Describes home page with opened Services screen"""
    def __init__(self, page: Page):
        super().__init__(page)
        self.infrastructure_section_button = self.locator(LOCATOR_INFRASTRUCTURE)
        self.apigw_card_in_infrastructure_section = self.locator(LOCATOR_APIGW)

    def go_to_infrastructure_section(self):
        """Goes to Infrastructure section of Services screen"""
        self.infrastructure_section_button.click()
        self.page.wait_for_load_state()

    def open_apigw_card(self):
        """Clicks on API GW card and goes to API GW product page"""
        self.apigw_card_in_infrastructure_section.click()
        self.page.wait_for_load_state()
        return self.page
