import requests
from dotenv import load_dotenv
import os
from data.constant_data import TOKEN_URL, CLIENT_ID, CLIENT_SECRET
from utils.payload_factory import get_token_payload


def get_access_token():
    """
    Retrieves a valid OAuth2 access token using client credentials.

    Sends a POST request to the token endpoint with client ID and secret,
    and returns the access token from the response.

    Raises:
        HTTPError: If the response status is not successful.
        ValueError: If the access token is missing from the response.

    Returns:
        str: The access token for authenticated API requests.
    """
    payload = get_token_payload(CLIENT_ID, CLIENT_SECRET)
    headers = {"Accept": "application/json"}

    response = requests.post(TOKEN_URL, data=payload, headers=headers)
    response.raise_for_status()

    token = response.json().get("data", {}).get("access_token")
    if not token:
        raise ValueError("Access token not found in response.")
    return token
