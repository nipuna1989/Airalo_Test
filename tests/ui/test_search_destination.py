from pages.home_page import HomePage
from pages.esim_selection_page import EsimSelectionPage
from pages.package_details_popup import PackageDetailsPopup
from data.test_data import TEST_DATA


def test_search_destination(page):
    """
    IMPORTANT: This test script has been created specifically for testing the functionality with the Euro currency.
    Test to search for a destination in the search box and verify navigation to the correct page.
    """
    destination = TEST_DATA["search_destination"]
    expected_details = TEST_DATA["package_details"]

    # Step 1: Go to homepage and search
    home_page = HomePage(page)
    home_page.navigate_to_home_page()
    home_page.search_for_destination(destination)

    # Step 2: Select eSIM
    esim_selection_page = EsimSelectionPage(page)
    esim_selection_page.click_buy_now(2)

    # Step 3: Verify package details
    package_details_popup = PackageDetailsPopup(page)
    package_details_popup.verify_package_details(expected_details)
