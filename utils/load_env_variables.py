from dotenv import load_dotenv
from pathlib import Path


def load_env_variables():
    """
    Loads environment variables from a .env file located in the project root directory.

    :raises FileNotFoundError: If the .env file does not exist in the project root.
    """
    # Define the path to the .env file (located in the project root)
    env_path = Path(__file__).resolve().parent.parent / '.env'

    # Check if the .env file exists and raise an error if it doesn't
    if not env_path.exists():
        raise FileNotFoundError(".env file not found in project root.")

    # Load the environment variables from the .env file
    load_dotenv(dotenv_path=env_path)