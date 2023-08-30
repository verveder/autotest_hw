from playwright.sync_api import Page
from src.data import (
    MAIN_URL, APIGW_PRODUCT_URL,
    LOCATOR_SERVICES, LOCATOR_INFRASTRUCTURE, LOCATOR_APIGW
)


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
        self.page.goto(self.url)
        return self


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


class ServicesPage(BasePage):
    """Describes home page with opened Services screen"""
    def __init__(self, page: Page):
        super().__init__(page)
        self.infrastructure_section_button = self.locator(LOCATOR_INFRASTRUCTURE)
        self.apigw_card_in_infrastructure_section = self.locator(LOCATOR_APIGW)

    def go_to_infrastructure_section(self):
        """Goes to Infrastructure section of Services screen"""
        self.infrastructure_section_button.click()

    def open_apigw_card(self):
        """Clicks on API GW card and goes to API GW product page"""
        self.apigw_card_in_infrastructure_section.click()
        return self.page


class ProductPageAPIGW(BasePage):
    """Describes product page for API GW"""
    def __init__(self, page: Page):
        super().__init__(page)
        self.url = APIGW_PRODUCT_URL
