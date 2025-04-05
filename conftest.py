import pytest
import os

from pages.esim_selection_page import EsimSelectionPage
from pages.home_page import HomePage
from pages.package_details_popup import PackageDetailsPopup
from utils.logger import log_file_path
from utils.get_token import get_access_token
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as p:
        yield p


@pytest.fixture(scope="session")
def browser(playwright_instance):
    browser = playwright_instance.chromium.launch(headless=False)
    yield browser
    browser.close()


@pytest.fixture
def page(browser):
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


def pytest_sessionfinish():
    print("\n" + "="*80)
    print(f"📂 Logs saved at: {os.path.abspath(log_file_path)}")
    print("="*80 + "\n")
