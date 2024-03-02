import json


def read_config():
    """
    Считывает путь из файла JSON.
    :return: dict
    """
    with open('config/session_path.json', 'r', encoding='utf-8') as json_file:
        config = json.load(json_file)
        return config['session_path']


def read_config_tdata():
    """
    Считывает путь из файла JSON.
    :return: dict
    """
    with open('config/tdata_path.json', 'r', encoding='utf-8') as json_file:
        config = json.load(json_file)
        return config['tdata_path']


def write_config(session_path):
    """
    Записывает путь к файлу JSON.
    :param session_path: str
    :return: None
    """
    data = {'session_path': session_path}
    with open('config/session_path.json', 'w+', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)


def write_config2(tdata_path):
    """
    Записывает путь к файлу JSON.
    :param tdata_path: str
    :return: None
    """
    data = {'tdata_path': tdata_path}
    with open('config/tdata_path.json', 'w+', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    read_config()
    read_config_tdata()
