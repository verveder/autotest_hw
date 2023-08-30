from playwright.sync_api import Playwright, expect

# URLs in use
MAIN_URL = "https://cloud.ru/ru"
APIGW_PRODUCT_URL = "https://cloud.ru/ru/products/oblachnyj-api-gateway-hosting"

# XPath's locators for elements in use
LOCATOR_SERVICES = "//*[@data-qa='header_nav_item'][text()='Сервисы']"
LOCATOR_INFRASTRUCTURE = "//*[contains(@class, 'OZqKu')][text()='Инфраструктура']"
LOCATOR_APIGW = "//h2[text()='Инфраструктура']/following-sibling::a[contains(@href, 'api-gateway')]"


def test_open_apigw_page_via_services_infrastructure(playwright: Playwright):
    """
    Tests navigation from home page to API GW product page
    via Services screen, Infrastructure section
    """
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    service_button = page.locator(LOCATOR_SERVICES)
    infrastructure_button = page.locator(LOCATOR_INFRASTRUCTURE)
    apigw_card = page.locator(LOCATOR_APIGW)

    page.goto(MAIN_URL)
    service_button.click()
    infrastructure_button.click()
    apigw_card.click()
    expect(page).to_have_url(APIGW_PRODUCT_URL)
