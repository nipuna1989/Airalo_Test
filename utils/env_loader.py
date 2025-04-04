from pathlib import Path
from dotenv import load_dotenv


def load_env_variables():
    env_path = Path(__file__).resolve().parent.parent / '.env'
    if not env_path.exists():
        raise FileNotFoundError(".env file not found in project root.")
    load_dotenv(dotenv_path=env_path)

