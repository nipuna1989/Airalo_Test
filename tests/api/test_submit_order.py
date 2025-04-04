import requests
from data.constant_data import ORDER_URL
from utils.payload_factory import get_order_payload
from utils.logger import logger


def test_get_esim_list(auth_headers):
    """
    Test to create an order for a specific eSIM package.
    """
    payload = get_order_payload()
    response = requests.post(ORDER_URL, json=payload, headers=auth_headers)

    assert response.status_code == 200, f"Order creation failed: {response.text}"
    logger.info("Order creation successful.")
