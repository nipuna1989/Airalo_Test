import requests
from utils.logger import logger
from data.constant_data import ESIMS_URL
from data.api_test_data import (
    PACKAGE_ID,
    ORDER_QUANTITY,
    CORRECT_ESIMS_QUERY_PARAMS,
    INCORRECT_ESIMS_QUERY_PARAMS,
    INVALID_AUTH_HEADER,
)
from utils.schema_loader import load_schema
from conftest import validate_response_schema

# Load the schema from the JSON file
expected_schema = load_schema("data/schema/get_esim_list_schema.json")


def test_verify_esims(auth_headers):
    """
    Test to verify the eSIMs associated with a given package ID.
    """
    # 1. Send GET request to fetch eSIMs for verification
    logger.info("Fetching eSIMs to verify package match...")
    response = requests.get(
        ESIMS_URL, headers=auth_headers, params=CORRECT_ESIMS_QUERY_PARAMS
    )

    # 2. Ensure the response is successful (status code 200)
    assert (
        response.status_code == 200
    ), f"Failed to fetch eSIMs. Status: {response.status_code}, Response: {response.text}"

    # 3. Extract the response JSON
    resp_json = response.json()

    # 4. Validate the response JSON against the expected schema
    validate_response_schema(resp_json, expected_schema, logger)

    # 5. Extract the 'data' field containing eSIMs and filter by package_id
    esims = response.json().get("data", [])
    matching_esims = [
        esim
        for esim in esims
        if esim.get("simable", {}).get("package_id") == PACKAGE_ID
    ]

    # 6. Verify that the number of matching eSIMs is at least the expected quantity
    assert len(matching_esims) >= ORDER_QUANTITY, (
        f"Expected at least {ORDER_QUANTITY} eSIMs with package_id '{PACKAGE_ID}', "
        f"but found {len(matching_esims)}"
    )

    logger.info(f"Verified {len(matching_esims)} eSIMs with package_id '{PACKAGE_ID}'.")


def test_verify_sim_with_invalid_token():
    """
    Test to verify the behavior when an invalid token is used for authentication.
    """

    # 1. Send GET request with invalid 'limit' parameter
    logger.info("Sending request with invalid 'limit' parameter...")
    response = requests.get(
        ESIMS_URL, headers=INVALID_AUTH_HEADER, params=INCORRECT_ESIMS_QUERY_PARAMS
    )

    # 2. Ensure the response is unsuccessful (status code == 401)
    assert (
        response.status_code == 401
    ), f" Incorrect Status: {response.status_code}, Response: {response.text}"

    # 3. Validate the error response JSON
    resp_json = response.json()
    logger.info(f"Response received: {resp_json}")

    # 4. Assert that the response contains the correct error message
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


def test_verify_sim_with_invalid_limit_parameter(auth_headers):
    """
    Test to verify the behavior when the 'limit' parameter is invalid (non-integer).
    """

    # 1. Send GET request with invalid 'limit' parameter
    logger.info("Sending request with invalid 'limit' parameter...")
    response = requests.get(
        ESIMS_URL, headers=auth_headers, params=INCORRECT_ESIMS_QUERY_PARAMS
    )

    # 2. Ensure the response is unsuccessful (status code == 422)
    assert (
        response.status_code == 422
    ), f"Incorrect Status: {response.status_code}, Response: {response.text}"

    # 3. Validate the error response JSON
    resp_json = response.json()
    logger.info(f"Response received: {resp_json}")

    # 4. Assert that the response contains the 'data' and 'meta' fields with correct error messages
    assert "data" in resp_json, "Error response doesn't contain 'data' field"
    assert (
        "limit" in resp_json["data"]
    ), "Error response 'data' field doesn't contain 'limit'"
    assert (
        resp_json["data"]["limit"] == "The limit must be an integer."
    ), f"Unexpected 'limit' error message: {resp_json['data']['limit']}"

    assert "meta" in resp_json, "Error response doesn't contain 'meta' field"
    assert (
        "message" in resp_json["meta"]
    ), "Error response doesn't contain 'message' field"
    assert (
        resp_json["meta"]["message"] == "the parameter is invalid"
    ), f"Unexpected error message: {resp_json['meta']['message']}"

    logger.info(
        "Test passed: Invalid 'limit' parameter correctly rejected with proper error response."
    )
