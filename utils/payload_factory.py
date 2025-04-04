from data.api_test_data import PACKAGE_ID, ORDER_QUANTITY, ORDER_TYPE, GRANT_TYPE


def get_order_payload(package_id=PACKAGE_ID, quantity=ORDER_QUANTITY, order_type=ORDER_TYPE, description=None):
    """
    Generate payload for creating an order.

    Args:
        package_id (str): ID of the eSIM package.
        quantity (int): Number of eSIMs to order.
        order_type (str): Type of order (e.g., 'sim').
        description (str, optional): Optional custom description.

    Returns:
        dict: Payload for POST /orders.
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

    Args:
        client_id (str): API client ID.
        client_secret (str): API client secret.
        grant_type (str): OAuth2 grant type (default: 'client_credentials').

    Returns:
        dict: Payload for POST /token.
    """
    return {
        "client_id": client_id,
        "client_secret": client_secret,
        "grant_type": grant_type
    }
