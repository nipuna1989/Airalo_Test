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
