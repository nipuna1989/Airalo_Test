from urllib.parse import urlparse

from playwright.sync_api import Page

from data.constant_data import DEFAULT_TIMEOUT, URL_TIMEOUT
from utils.logger import logger


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def wait_for_element(self, locator, state="visible", timeout=DEFAULT_TIMEOUT):
        """
        Waits for an element to be in a specific state.

        :param locator: Playwright Locator object
        :param state: State to wait for (e.g., 'visible', 'attached'). default is 'visible'
        :param timeout: Optional timeout in ms. Default is 5 seconds.
        """
        logger.debug(f"Waiting for element to be {state} with timeout {timeout}ms.")
        locator.wait_for(state=state, timeout=timeout)

    def wait_for_url_path_and_validate(self, expected_path: str, timeout=URL_TIMEOUT):
        """
        Waits for the page URL to match the expected path and asserts it's correct.

        :param expected_path: Expected URL path (e.g., "/japan-esim")
        :param timeout: Timeout in ms. Default is 10 seconds.
        """
        logger.debug(f"Waiting for URL to match path: {expected_path}")
        self.page.wait_for_url(f"**{expected_path}", timeout=timeout)

        actual_path = urlparse(self.page.url).path
        logger.info(f"Expected path: {expected_path}")
        logger.info(f"Actual path: {actual_path}")

        assert (
            actual_path == expected_path
        ), f"Expected to navigate to '{expected_path}', but got '{actual_path}'"

        logger.info("URL validation successful.")

    def goto(self, url: str):
        """
        Navigate to a URL and wait for full page load.

        :param url: URL to navigate to
        """
        logger.info(f"Navigating to {url}")
        self.page.goto(url)
        self.page.wait_for_load_state("load")
        logger.info(f"Page loaded: {self.page.url}")
