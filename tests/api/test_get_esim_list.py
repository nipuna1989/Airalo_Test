import requests
from utils.logger import logger
from data.constant_data import ESIMS_URL, ESIMS_QUERY_PARAMS
from data.api_test_data import PACKAGE_ID, ORDER_QUANTITY


def test_verify_esims(auth_headers):
    """
    Test to verify the eSIMs associated with a given package ID.
    """
    # Send GET request to fetch eSIMs for verification
    logger.info("Fetching eSIMs to verify package match...")
    response = requests.get(ESIMS_URL, headers=auth_headers, params=ESIMS_QUERY_PARAMS)

    # Ensure the response is successful (status code 200)
    assert (
        response.status_code == 200
    ), f"Failed to fetch eSIMs. Status: {response.status_code}, Response: {response.text}"

    # Extract the 'data' field containing eSIMs and filter by package_id
    esims = response.json().get("data", [])
    matching_esims = [
        esim
        for esim in esims
        if esim.get("simable", {}).get("package_id") == PACKAGE_ID
    ]

    # Verify that the number of matching eSIMs is at least the expected quantity
    assert len(matching_esims) >= ORDER_QUANTITY, (
        f"Expected at least {ORDER_QUANTITY} eSIMs with package_id '{PACKAGE_ID}', "
        f"but found {len(matching_esims)}"
    )

    logger.info(f"Verified {len(matching_esims)} eSIMs with package_id '{PACKAGE_ID}'.")
