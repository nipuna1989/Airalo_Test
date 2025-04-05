from data.load_test_data import TEST_DATA


def test_search_destination(page, home_page, esim_selection_page, package_details_popup):
    """
    IMPORTANT: This test script has been created specifically for testing the functionality with the Euro currency.

    Steps:
    1. Navigate to the homepage and search for a destination.
    2. Select an eSIM package from the search results.
    3. Verify the package details popup.

    :param page: Playwright page object.
    :param home_page: Fixture returning the HomePage object.
    :param esim_selection_page: Fixture returning the EsimSelectionPage object.
    :param package_details_popup: Fixture returning the PackageDetailsPopup object.
    """
    destination = TEST_DATA["search_destination"]
    expected_details = TEST_DATA["package_details"]

    # Step 1: Go to homepage and search
    home_page.navigate_to_home_page()
    home_page.search_for_destination(destination)

    # Step 2: Select eSIM
    esim_selection_page.click_buy_now(2)

    # Step 3: Verify package details
    package_details_popup.verify_package_details(expected_details)
