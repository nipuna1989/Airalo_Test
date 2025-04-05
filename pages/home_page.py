from playwright.sync_api import Page
from utils.logger import logger
from pages.base_page import BasePage
from data.constant_data import BASE_URL


class HomePage(BasePage):
    def __init__(self, page: Page):
        """
        Initializes the HomePage object with locators and base methods.
        """
        super().__init__(page)
        self.search_box = page.locator("input[data-testid='search-input']")
        self.auto_suggest_pattern = "span[data-testid='{}-name']"

    def navigate_to_home_page(self):
        """
        Opens the Airalo homepage using the configured base URL.
        """
        logger.info("Navigating to the Airalo homepage...")
        self.goto(BASE_URL)

    def search_for_destination(self, destination: str):
        """
        Searches for a destination and validates navigation.

        :param destination: Destination name (e.g., 'Japan')
        """
        # Wait for the search box to be visible and fill in the destination
        logger.info(f"Searching for destination: {destination}")
        self.wait_for_element(self.search_box)
        self.search_box.fill(destination)
        logger.debug(f"Filled search box with: {destination}")

        # Prepare the auto-suggest selector based on the destination
        auto_suggest_selector = self.auto_suggest_pattern.format(destination)
        auto_suggest_option = self.page.locator(auto_suggest_selector)

        # Wait for the auto-suggest option and click if visible
        self.wait_for_element(auto_suggest_option)
        if auto_suggest_option.is_visible():
            auto_suggest_option.click()
            logger.info(f"Selected auto-suggest option for '{destination}'")
        else:
            logger.error(f"Auto-suggest option for '{destination}' not found.")
            return

        # Validate the URL path after clicking the suggestion
        expected_path = f"/{destination.strip().lower()}-esim"
        self.wait_for_url_path_and_validate(expected_path)
