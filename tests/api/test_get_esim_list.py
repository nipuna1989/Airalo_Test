import requests
from data.constant_data import ORDER_URL, ESIMS_URL
from data.api_test_data import PACKAGE_ID, ORDER_QUANTITY, ESIMS_QUERY_PARAMS
from utils.logger import logger


def test_verify_esims(auth_headers):
    """
    Test to verify the eSIMs associated with a given package ID.
    """
    logger.info("Fetching eSIMs to verify package match...")
    response = requests.get(ESIMS_URL, headers=auth_headers, params=ESIMS_QUERY_PARAMS)

    assert (
        response.status_code == 200
    ), f"Failed to fetch eSIMs. Status: {response.status_code}, Response: {response.text}"

    esims = response.json().get("data", [])
    matching_esims = [
        esim
        for esim in esims
        if esim.get("simable", {}).get("package_id") == PACKAGE_ID
    ]

    assert len(matching_esims) >= ORDER_QUANTITY, (
        f"Expected at least {ORDER_QUANTITY} eSIMs with package_id '{PACKAGE_ID}', "
        f"but found {len(matching_esims)}"
    )

    logger.info(f"Verified {len(matching_esims)} eSIMs with package_id '{PACKAGE_ID}'.")
