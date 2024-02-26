import json


def read_config():
    """Reads the path from the JSON file."""
    with open('config.json', 'r', encoding='utf-8') as json_file:
        config = json.load(json_file)
        return config['session_path']


def write_config(session_path):
    """Writes the path to the JSON file."""
    with open('config.json', 'w', encoding='utf-8') as json_file:
        json.dump({'session_path': session_path}, json_file, ensure_ascii=False, indent=4)
