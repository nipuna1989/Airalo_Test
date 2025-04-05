import requests
from utils.logger import logger
from utils.payload_factory import get_order_payload
from data.constant_data import ORDER_URL
from data.api_test_data import PACKAGE_ID, ORDER_QUANTITY, ORDER_TYPE


def test_get_esim_list(auth_headers):
    """
    Test to create an order for a specific eSIM package.
    """
    # Generate the payload for the order
    payload = get_order_payload()
    logger.info(f"Sending order payload: {payload}")

    # Send POST request to create the order
    response = requests.post(ORDER_URL, json=payload, headers=auth_headers)
    logger.info(f"Received response status: {response.status_code}")
    logger.debug(f"Full response body: {response.text}")

    # Assert that the order creation request is successful (status code 200)
    assert response.status_code == 200, f"Order creation failed: {response.text}"

    # Extract data from the response JSON
    resp_json = response.json()
    data = resp_json.get("data", {})
    sims = data.get("sims", [])

    # Verify that the response data matches the expected package_id, quantity, type, and description
    assert data.get("package_id") == PACKAGE_ID, "package_id mismatch"
    assert int(data.get("quantity", 0)) == ORDER_QUANTITY, "quantity mismatch"
    assert data.get("type") == ORDER_TYPE, "Expected type 'sim'"
    assert payload["description"] in data.get("description", ""), "description mismatch"

    # Assert that the number of SIMs matches the expected quantity
    assert len(sims) == ORDER_QUANTITY, f"Expected {ORDER_QUANTITY} SIMs, got {len(sims)}"

    logger.info(f"Order created successfully with {len(sims)} SIM(s).")

