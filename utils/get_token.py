import requests
from data.constant_data import TOKEN_URL, CLIENT_ID, CLIENT_SECRET
from utils.payload_factory import get_token_payload


def get_access_token():
    """
    Retrieves a valid OAuth2 access token using client credentials.

    Raises:
        HTTPError: If the response status is not successful.
        ValueError: If the access token is missing from the response.

    Returns:
        str: The access token for authenticated API requests.
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
