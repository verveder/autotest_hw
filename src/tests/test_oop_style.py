from playwright.sync_api import expect
from src.pages.pages import HomePage, ServicesPage, ProductPageAPIGW


class TestNavigationToProductPage:
    """
    Describes class designed for testing navigation
    from home page to product page
    """
    def test_open_apigw_page_via_services_infrastructure(
            self,
            playwright_home_page: HomePage,
            playwright_services_page: ServicesPage,
            playwright_product_apigw_page: ProductPageAPIGW
    ):
        """
        Tests navigation from home page to API GW product page
        via Services screen, Infrastructure section
        """
        playwright_home_page.navigate_to_page()
        playwright_home_page.open_services_screen()
        playwright_services_page.go_to_infrastructure_section()
        opened_page = playwright_services_page.open_apigw_card()
        expect(opened_page).to_have_url(playwright_product_apigw_page.url)
