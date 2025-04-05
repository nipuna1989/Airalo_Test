from playwright.sync_api import Page, expect
from utils.logger import logger
from pages.base_page import BasePage


class PackageDetailsPopup(BasePage):
    """
    Page Object Model for the Package Details Popup.
    Encapsulates locators and verification logic for eSIM package information.
    """

    def __init__(self, page: Page):
        """
        Initializes the PackageDetailsPopup object.

        :param page: Playwright Page instance used to interact with the browser.
        """
        super().__init__(page)
        self.popup = page.locator("div[data-testid='sim-detail-header']")

        # Define locators for individual package detail fields
        self.title = self.popup.locator(
            "div[data-testid='sim-detail-operator-title'] p"
        )
        self.coverage = self.popup.locator("p[data-testid='COVERAGE-value']")
        self.data = self.popup.locator("p[data-testid='DATA-value']")
        self.validity = self.popup.locator("p[data-testid='VALIDITY-value']")
        self.price = self.popup.locator("p[data-testid='PRICE-value']")

    def verify_package_details(self, expected_details: dict):
        """
        Verifies that all displayed eSIM package details match the expected values.

        :param expected_details: Dictionary with expected text values.
            Example:
            {
                "title": "Moshi Moshi",
                "coverage": "Japan",
                "data": "1 GB",
                "validity": "7 Days",
                "price": "4.50 €"
            }
        """
        logger.info("Waiting for package details popup to be visible...")
        self.wait_for_element(self.popup)

        logger.info("Verifying package details...")

        # Check if each displayed package detail matches the expected value
        expect(self.title, "Title mismatch").to_have_text(expected_details["title"])
        expect(self.coverage, "Coverage mismatch").to_have_text(
            expected_details["coverage"]
        )
        expect(self.data, "Data mismatch").to_have_text(expected_details["data"])
        expect(self.validity, "Validity mismatch").to_have_text(
            expected_details["validity"]
        )
        expect(self.price, "Price mismatch").to_have_text(expected_details["price"])

        logger.info("All package details match expected values.")
