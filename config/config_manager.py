import json


def read_config():
    """Reads the path from the JSON file."""
    with open('session_path.json', 'r', encoding='utf-8') as json_file:
        config = json.load(json_file)
        return config['session_path']


def read_config_tdata():
    """Reads the path from the JSON file."""
    with open('tdata_path.json', 'r', encoding='utf-8') as json_file:
        config = json.load(json_file)
        return config['tdata_path']


def write_config(session_path):
    """Writes the path to the JSON file."""
    data = {'session_path': session_path}
    with open('session_path.json', 'w+', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)


def write_config2(tdata_path):
    """Writes the path to the JSON file."""
    data = {'tdata_path': tdata_path}
    with open('tdata_path.json', 'w+', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)
