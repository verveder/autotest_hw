from playwright.sync_api import Page
from src.data import APIGW_PRODUCT_URL, LOCATOR_APIGW_ADVANTAGES, LOCATOR_APIGW_USER_GUIDE, LOCATOR_APIGW_ADVANTAGES_TITLE
from src.pages.base_page import BasePage


class ProductPageAPIGW(BasePage):
    """Describes product page for API GW"""
    def __init__(self, page: Page):
        super().__init__(page)
        self.url = APIGW_PRODUCT_URL
        self.advantages_section = self.locator(LOCATOR_APIGW_ADVANTAGES)
        self.user_guide_section = self.locator(LOCATOR_APIGW_USER_GUIDE)
        self.advantages_title = self.locator(LOCATOR_APIGW_ADVANTAGES_TITLE)

    def open_section_advantages(self):
        self.advantages_section.click()
        self.page.wait_for_load_state()

    def open_section_user_guide(self):
        self.user_guide_section.click()
        self.page.wait_for_load_state()
        return self.page
