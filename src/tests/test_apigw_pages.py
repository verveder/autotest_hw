from playwright.sync_api import expect
from src.pages.home_page import HomePage
from src.pages.services_page import ServicesPage
from src.pages.product_page_apigw import ProductPageAPIGW
from src.pages.user_guide_apigw import UserGuideAPIGW
from src.data import WRONG_URL


class TestPagesAPIGW:
    """
    Describes class designed for testing navigation
    from home page to API GW product page,
    and navigation on API GW page itself
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

    def test_open_section_apigw_advantages(
            self,
            playwright_product_apigw_page: ProductPageAPIGW
    ):
        """
        Tests opening the "Product Advantages" section
        on API GW product page
        """
        playwright_product_apigw_page.navigate_to_page()
        playwright_product_apigw_page.open_section_advantages()
        expect(playwright_product_apigw_page.advantages_title).to_be_visible()

    def test_open_apigw_user_guide(
            self,
            playwright_product_apigw_page: ProductPageAPIGW,
            playwright_user_guide_apigw: UserGuideAPIGW
    ):
        """
        Tests opening API GW user guide section
        on API GW product page
        """
        playwright_product_apigw_page.navigate_to_page()
        opened_page = playwright_product_apigw_page.open_section_user_guide()
        expect(opened_page).to_have_title(playwright_user_guide_apigw.title)

    def test_check_user_guide_apigw_url(
            self,
            playwright_user_guide_apigw: UserGuideAPIGW
    ):
        """
        Checks url for API GW User Guide,
        designed to fail after executing
        (and not to be skipped by @pytest.mark.xfail)
        """
        playwright_user_guide_apigw.navigate_to_page()
        assert playwright_user_guide_apigw.url == WRONG_URL
