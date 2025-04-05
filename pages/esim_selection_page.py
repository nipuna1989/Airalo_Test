from playwright.sync_api import Page
from utils.logger import logger
from pages.base_page import BasePage


class EsimSelectionPage(BasePage):
    def __init__(self, page: Page):
        """
        Initializes the eSIM Selection Page with the given Playwright page instance.
        """
        super().__init__(page)
        self.esim_packages = page.locator("a[data-testid='sim-package-item']")

    def click_buy_now(self, package_index: int):
        """
        Clicks the 'Buy Now' button for the selected eSIM package.

        :param package_index: The index of the package to select (1 for first, 2 for second, etc.).
        :raises ValueError: If no packages are found or the index is out of range.
        """
        logger.info("Waiting for eSIM packages to be visible...")
        self.wait_for_element(self.esim_packages.first)

        # Check the number of eSIM packages on the page
        count = self.esim_packages.count()
        if count == 0:
            raise ValueError("No eSIM packages found on the page!")
        if package_index < 1 or package_index > count:
            raise ValueError(
                f"Requested package index {package_index} is out of range. Only {count} packages available."
            )

        # Select the correct package based on the index
        selected_package = self.esim_packages.nth(package_index - 1)

        # Click the 'Buy Now' button
        buy_now_button = selected_package.locator(
            "div[data-testid='esim-button'] button"
        )
        self.wait_for_element(buy_now_button)
        buy_now_button.click()

        logger.info(f"Clicked 'Buy Now' for package #{package_index}.")
