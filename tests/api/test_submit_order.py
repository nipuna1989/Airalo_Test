import requests
from utils.logger import logger
from utils.payload_factory import get_order_payload
from data.constant_data import ORDER_URL
from data.api_test_data import (
    PACKAGE_ID,
    ORDER_QUANTITY,
    ORDER_TYPE,
    INVALID_AUTH_HEADER,
    INVALID_PACKAGE_ID,
    EXCEEDING_ORDER_QUANTITY,
)
from utils.schema_loader import load_schema
from conftest import validate_response_schema


# Load the schema from the JSON file
expected_schema = load_schema("data/schema/submit_order_schema.json")


def test_submit_order(auth_headers):
    """
    Test to create an order for a specific eSIM package and validate the response.
    """
    # 1. Generate the payload for the order
    payload = get_order_payload()
    logger.info(f"Sending order payload: {payload}")

    # 2. Send POST request to create the order
    response = requests.post(ORDER_URL, json=payload, headers=auth_headers)
    logger.info(f"Received response status: {response.status_code}")

    # 3. Assert that the order creation request is successful (status code 200)
    assert response.status_code == 200, f"Order creation failed: {response.text}"

    # 4. Extract data from the response JSON
    resp_json = response.json()

    # 5. Validate the response JSON against the expected schema
    validate_response_schema(resp_json, expected_schema, logger)

    # 6. Extract relevant data for further assertions
    data = resp_json.get("data", {})
    sims = data.get("sims", [])

    # 7. Verify that the response data matches the expected package_id, quantity, type, and description
    assert data.get("package_id") == PACKAGE_ID, "package_id mismatch"
    assert int(data.get("quantity", 0)) == ORDER_QUANTITY, "quantity mismatch"
    assert data.get("type") == ORDER_TYPE, "Expected type 'sim'"
    assert payload["description"] in data.get("description", ""), "description mismatch"

    # 8. Assert that the number of SIMs matches the expected quantity
    assert (
        len(sims) == ORDER_QUANTITY
    ), f"Expected {ORDER_QUANTITY} SIMs, got {len(sims)}"

    # 9. Log the successful creation
    logger.info(f"Order created successfully with {len(sims)} SIM(s).")


def test_submit_order_with_invalid_token():
    """
    Test to create an order with an invalid token and validate the error response.
    """
    # 1. Generate the payload for the order
    payload = get_order_payload()
    logger.info(f"Sending order payload: {payload}")

    # 2. Send POST request to create the order
    response = requests.post(ORDER_URL, json=payload, headers=INVALID_AUTH_HEADER)
    logger.info(f"Received response status: {response.status_code}")

    # 3. Ensure the response is unsuccessful (status code == 401)
    assert (
        response.status_code == 401
    ), f" Incorrect Status: {response.status_code}, Response: {response.text}"

    # 4. Validate the error response JSON
    resp_json = response.json()
    logger.info(f"Response received: {resp_json}")

    # 5. Assert that the response contains the correct error message
    assert "meta" in resp_json, "Error response doesn't contain 'meta' field"
    assert (
        "message" in resp_json["meta"]
    ), "Error response doesn't contain 'message' field"
    assert (
        resp_json["meta"]["message"] == "Unauthenticated."
    ), f"Unexpected error message: {resp_json['meta']['message']}"

    logger.info(
        "Test passed: Invalid authentication correctly returns 401 Unauthenticated."
    )


def test_submit_order_invalid_package_id(auth_headers):
    """
    Test to create an order with an invalid package_id and validate the error response.
    """
    # 1. Generate the payload for the order with an invalid package_id
    payload = get_order_payload()
    payload["package_id"] = (
        INVALID_PACKAGE_ID  # Replace the correct package_id with the invalid one
    )
    logger.info(f"Sending order payload with invalid package_id: {payload}")

    # 2. Send POST request to create the order
    response = requests.post(ORDER_URL, json=payload, headers=auth_headers)
    logger.info(f"Received response status: {response.status_code}")

    # 3. Assert that the order creation request fails (status code 422 for invalid parameters)
    assert (
        response.status_code == 422
    ), f"Expected status code 422 for invalid package_id, but got {response.status_code}. Response: {response.text}"

    # 4. Extract data from the response JSON
    resp_json = response.json()

    # 5. Validate the error response structure
    assert "code" in resp_json, "Error response doesn't contain 'code' field"
    assert "reason" in resp_json, "Error response doesn't contain 'reason' field"
    assert (
        resp_json["code"] == 34
    ), f"Unexpected error code: {resp_json['code']}, expected 34"
    expected_reason = "The requested eSIM package is invalid or it is currently out of stock. Please try again later."
    assert (
        resp_json["reason"] == expected_reason
    ), f"Unexpected error reason: {resp_json['reason']}, expected: {expected_reason}"
    # 6. Log the error message for tracking
    logger.info(
        f"Error validation passed. Code: {resp_json['code']}, Reason: {resp_json['reason']}"
    )


def test_submit_order_exceed_quantity(auth_headers):
    """
    Test to create an order with an invalid package_id and validate the error response.
    """
    # 1. Generate the payload for the order with an exceeding quantity
    payload = get_order_payload()
    payload["quantity"] = EXCEEDING_ORDER_QUANTITY  # Replace the qty with exceed value
    logger.info(f"Sending order payload with exceed qty: {payload}")

    # 2. Send POST request to create the order
    response = requests.post(ORDER_URL, json=payload, headers=auth_headers)
    logger.info(f"Received response status: {response.status_code}")

    # 3. Assert that the order creation request fails (status code 422 for invalid parameters)
    assert (
        response.status_code == 422
    ), f"Expected status code 422 for invalid package_id, but got {response.status_code}. Response: {response.text}"

    # 4. Extract data from the response JSON
    resp_json = response.json()
    logger.info(f"Response received: {resp_json}")

    # 5. Validate the error response structure
    assert "data" in resp_json, "Error response doesn't contain 'data' field"
    assert (
        "quantity" in resp_json["data"]
    ), "Error response 'data' field doesn't contain 'quantity' field"
    assert (
        resp_json["data"]["quantity"] == "The quantity may not be greater than 50."
    ), f"Unexpected error message for 'quantity': {resp_json['data']['quantity']}"
    assert "meta" in resp_json, "Error response doesn't contain 'meta' field"
    assert (
        "message" in resp_json["meta"]
    ), "Error response doesn't contain 'message' field"
    assert (
        resp_json["meta"]["message"] == "the parameter is invalid"
    ), f"Unexpected error message in 'meta': {resp_json['meta']['message']}"

    # 6. Log the error message for tracking
    logger.info("Error response validated successfully. 'Quantity' exceeded limit.")
