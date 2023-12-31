import pytest
from playwright.sync_api import Page, sync_playwright
from src.pages.home_page import HomePage
from src.pages.services_page import ServicesPage
from src.pages.product_page_apigw import ProductPageAPIGW
from src.pages.user_guide_apigw import UserGuideAPIGW


@pytest.fixture(scope='function')
def chromium_page() -> Page:
    with sync_playwright() as playwright:
        chromium = playwright.chromium.launch(headless=True)
        yield chromium.new_page()


@pytest.fixture(scope='function')
def playwright_home_page(chromium_page: Page):
    return HomePage(chromium_page)


@pytest.fixture(scope='function')
def playwright_services_page(chromium_page: Page):
    return ServicesPage(chromium_page)


@pytest.fixture(scope='function')
def playwright_product_apigw_page(chromium_page: Page):
    return ProductPageAPIGW(chromium_page)


@pytest.fixture(scope='function')
def playwright_user_guide_apigw(chromium_page: Page):
    return UserGuideAPIGW(chromium_page)
