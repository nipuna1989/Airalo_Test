import requests
from data.constant_data import ORDER_URL
from utils.payload_factory import get_order_payload
from data.api_test_data import PACKAGE_ID, ORDER_QUANTITY
from utils.logger import logger


def test_get_esim_list(auth_headers):
    """
    Test to create an order for a specific eSIM package.
    """
    payload = get_order_payload()
    logger.info(f"Sending order payload: {payload}")

    response = requests.post(ORDER_URL, json=payload, headers=auth_headers)
    logger.info(f"Received response status: {response.status_code}")
    logger.debug(f"Full response body: {response.text}")

    assert response.status_code == 200, f"Order creation failed: {response.text}"

    resp_json = response.json()
    data = resp_json.get("data", {})
    sims = data.get("sims", [])

    assert data.get("package_id") == PACKAGE_ID, "package_id mismatch"
    assert int(data.get("quantity", 0)) == ORDER_QUANTITY, "quantity mismatch"
    assert data.get("type") == "sim", "Expected type 'sim'"
    assert payload["description"] in data.get("description", ""), "description mismatch"

    assert len(sims) == ORDER_QUANTITY, f"Expected {ORDER_QUANTITY} SIMs, got {len(sims)}"

    logger.info(f"Order created successfully with {len(sims)} SIM(s).")

