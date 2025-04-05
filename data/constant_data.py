import os
from utils.env_loader import load_env_variables

# Load environment variables from .env file
load_env_variables()

# -------------------------
# UI Constants
# -------------------------
BASE_URL = "https://www.airalo.com"
DEFAULT_TIMEOUT = 5000  # milliseconds
URL_TIMEOUT = 10000      # milliseconds

# -------------------------
# API Constants
# -------------------------
BASE_API_URL = "https://sandbox-partners-api.airalo.com/v2"

TOKEN_URL = f"{BASE_API_URL}/token"
ORDER_URL = f"{BASE_API_URL}/orders"
ESIMS_URL = f"{BASE_API_URL}/sims"

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

# Params for fetching eSIMs
ESIMS_QUERY_PARAMS = {
    "limit": 100,
    "include": "order"
}


