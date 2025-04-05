import json
import os

# Get the absolute path of ui_test_data.json
TEST_DATA_FILE = os.path.join(os.path.dirname(__file__), "ui_test_data.json")


def load_test_data():
    """
    Loads test data from ui_test_data.json.

    :return: Dictionary containing test data.
    """
    with open(TEST_DATA_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


# Load data once so we can import it elsewhere
TEST_DATA = load_test_data()
