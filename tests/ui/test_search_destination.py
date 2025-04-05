import pytest

from data.load_test_data import TEST_DATA


@pytest.mark.parametrize(
    "destination, expected_details, package_index",
    [
        (
            TEST_DATA["search_destination"],
            TEST_DATA["package_details"],
            TEST_DATA["package_index"],
        )
    ],
)
def test_search_destination(
    page,
    home_page,
    esim_selection_page,
    package_details_popup,
    destination,
    expected_details,
    package_index,
):
    """
    IMPORTANT: This test script has been created specifically for testing the functionality with default Euro currency.

    Steps:
    1. Navigate to the Airalo homepage
    2. Search for a destination.
    3. Select an eSIM package from the search results.
    4. Verify the package details popup.

    :param page: Playwright page object.
    :param home_page: Fixture returning the HomePage object.
    :param esim_selection_page: Fixture returning the EsimSelectionPage object.
    :param package_details_popup: Fixture returning the PackageDetailsPopup object.
    :param destination: Destination to search for.
    :param expected_details: Expected package details for verification.
    :param package_index: Index of the package to select from the search results.
    """

    # 1. Go to Airalo homepage
    home_page.navigate_to_home_page()
    # 2. Search for destination
    home_page.search_for_destination(destination)
    # 3. Select eSIM package
    esim_selection_page.click_buy_now(package_index)
    # 4. Verify package details
    package_details_popup.verify_package_details(expected_details)
