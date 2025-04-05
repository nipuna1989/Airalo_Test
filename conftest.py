import pytest
from jsonschema import validate, ValidationError

from pages.esim_selection_page import EsimSelectionPage
from pages.home_page import HomePage
from pages.package_details_popup import PackageDetailsPopup
from utils.get_token import get_access_token
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="session")
def playwright_instance():
    """ Fixture to initialize Playwright instance for the session."""
    with sync_playwright() as p:
        yield p


@pytest.fixture(scope="session")
def browser(playwright_instance):
    """ Fixture to launch the browser instance for the session."""
    browser = playwright_instance.chromium.launch(headless=False)
    yield browser
    browser.close()


@pytest.fixture
def page(browser):
    """ Fixture to create a new browser context and page for each test."""
    context = browser.new_context()
    page = context.new_page()
    yield page
    page.close()


@pytest.fixture
def home_page(page):
    """Initialize Airalo home page objects and methods."""
    return HomePage(page)


@pytest.fixture
def esim_selection_page(page):
    """Initialize Airalo search page objects and methods."""
    return EsimSelectionPage(page)


@pytest.fixture
def package_details_popup(page):
    """Initialize Airalo package detail page objects and methods."""
    return PackageDetailsPopup(page)


@pytest.fixture(scope="module")
def auth_headers():
    """Get authenticated headers using a valid OAuth2 token."""
    token = get_access_token()
    return {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json"
    }


def validate_response_schema(resp_json, expected_schema, logger):
    """
    Validates a given response JSON against the expected schema.

    :param resp_json: The JSON response to validate.
    :param expected_schema: The schema to validate against.
    :param logger: Logger instance for logging validation results.

    :raises ValidationError: If the response does not match the schema.
    """
    try:
        validate(instance=resp_json, schema=expected_schema)
        logger.info("Response matches the expected schema.")
    except ValidationError as e:
        logger.error(f"Response does not match schema: {e.message}")
        logger.error(f"Error at path: {e.path}")
        logger.error(f"Invalid value: {e.instance}")

        raise
