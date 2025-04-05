import json


def load_schema(schema_file_path):
    """Load JSON schema from a file."""
    with open(schema_file_path, "r") as file:
        return json.load(file)
