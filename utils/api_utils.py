import requests
import json
from jsonschema import validate, ValidationError
from data.constant_data import TOKEN_URL, CLIENT_ID, CLIENT_SECRET
from data.api_test_data import PACKAGE_ID, ORDER_QUANTITY, ORDER_TYPE, GRANT_TYPE


def get_order_payload(package_id=PACKAGE_ID, quantity=ORDER_QUANTITY, order_type=ORDER_TYPE, description=None):
    """
    Generate payload for creating an order.

    :param package_id: Package ID for the eSIM order.
    :param quantity: Number of eSIMs to order.
    :param order_type: Type of order (default is 'sim').
    :param description: Description for the order (optional).

    :return: dict: Payload for POST /order.
    """
    return {
        "quantity": quantity,
        "package_id": package_id,
        "description": description or f"{quantity} sim {package_id}",
        "type": order_type
    }


def get_token_payload(client_id, client_secret, grant_type=GRANT_TYPE):
    """
    Generate payload for token request.

    :param client_id: Client ID for OAuth2 authentication.
    :param client_secret: Client secret for OAuth2 authentication.
    :param grant_type: Grant type for OAuth2 (default is 'client_credentials').

    :return: dict: Payload for token request.
    """
    return {
        "client_id": client_id,
        "client_secret": client_secret,
        "grant_type": grant_type
    }


def get_access_token():
    """
    Retrieves a valid OAuth2 access token using client credentials.

    Raises:
        HTTPError: If the response status is not successful.
        ValueError: If the access token is missing from the response.

    :return: str: The access token for API authentication.
    """
    # Prepare the payload for the token request using the client ID and secret
    payload = get_token_payload(CLIENT_ID, CLIENT_SECRET)
    headers = {"Accept": "application/json"}

    # # Send the POST request to obtain the access token and handle errors
    response = requests.post(TOKEN_URL, data=payload, headers=headers)
    response.raise_for_status()

    # Parse the response JSON to extract the access token and handle errors
    token = response.json().get("data", {}).get("access_token")
    if not token:
        raise ValueError("Access token not found in response.")

    return token


def load_schema(schema_file_path):
    """Load JSON schema from a file."""
    with open(schema_file_path, "r") as file:
        return json.load(file)


def validate_response_schema(resp_json, expected_schema, logger):
    """
    Validates a given response JSON against the expected schema.

    :param resp_json: The JSON response to validate.
    :param expected_schema: The schema to validate against.
    :param logger: Logger instance for logging validation results.

    :raises ValidationError: If the response does not match the schema.
    """
    try:
        validate(instance=resp_json, schema=expected_schema)
        logger.info("Response matches the expected schema.")
    except ValidationError as e:
        logger.error(f"Response does not match schema: {e.message}")
        logger.error(f"Error at path: {e.path}")
        logger.error(f"Invalid value: {e.instance}")
        raise
