from dotenv import load_dotenv
import os


def load_env_variables():
    """
    Loads environment variables from a .env file.
    """
    env_path = os.path.join(os.getcwd(), ".env")
    if os.path.exists(env_path):
        load_dotenv(dotenv_path=env_path)
    else:
        raise FileNotFoundError(".env file not found in project root.")
