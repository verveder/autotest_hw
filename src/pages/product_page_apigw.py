from playwright.sync_api import Page
from src.data import APIGW_PRODUCT_URL
from src.pages.base_page import BasePage


class ProductPageAPIGW(BasePage):
    """Describes product page for API GW"""
    def __init__(self, page: Page):
        super().__init__(page)
        self.url = APIGW_PRODUCT_URL
