from playwright.sync_api import Page
from src.data import API_GW_USER_GUIDE_URL, APIGW_USER_GUIDE_TITLE
from src.pages.base_page import BasePage


class UserGuideAPIGW(BasePage):
    """
    Describes class for API GW User Guide
    """
    def __init__(self, page: Page):
        super().__init__(page)
        self.url = API_GW_USER_GUIDE_URL
        self.title = APIGW_USER_GUIDE_TITLE
