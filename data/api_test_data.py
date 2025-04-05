# Data for testing the API
ORDER_QUANTITY = 6
EXCEEDING_ORDER_QUANTITY = 100
PACKAGE_ID = "merhaba-7days-1gb"
INVALID_PACKAGE_ID = "areeba-30days-3gbs"
ORDER_TYPE = "sim"
GRANT_TYPE = "client_credentials"

# Correct params for fetching eSIMs
CORRECT_ESIMS_QUERY_PARAMS = {"limit": 100, "include": "order"}

# Incorrect params for fetching eSIMs
INCORRECT_ESIMS_QUERY_PARAMS = {"limit": "asds", "include": "order"}  # Invalid limit

# Incorrect headers for authentication
INVALID_AUTH_HEADER = {
    "Authorization": "Bearer INVALID_ACCESS_TOKEN",  # Incorrect or expired token
    "Accept": "application/json",
}
