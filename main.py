import asyncio
import os
from loguru import logger  # https://github.com/Delgan/loguru
from opentele.api import UseCurrentSession  # https://opentele.readthedocs.io/en/latest/#installation
from opentele.tl import TelegramClient
from configparser import ConfigParser
import json

logger.add("log/log.log")


# def read_config():
#     """Reads the path from the INI file."""
#     config = ConfigParser()
#     config.read('config.ini')  # Adjust the file name if needed
#     return config.get('Paths', 'session_path')


def scan_session_files(session_path):
    """Returns a list of account names in the specified session path."""
    entities = []
    for entry in os.scandir(session_path):
        if entry.is_file() and entry.name.endswith(".session"):
            file = os.path.splitext(entry.name)[0]
            print(f"Found accounts: {file}.session")
            entities.append(file)
    return entities


def read_config():
    """Reads the path from the JSON file."""
    with open('config.json', 'r', encoding='utf-8') as json_file:
        config = json.load(json_file)
        return config['session_path']


async def main():
    """Main function"""
    user_input = input("Введите путь к папке с сессиями: ")
    session_path = rf"{user_input}"

    # Write session_path to a JSON file
    with open('config.json', 'w', encoding='utf-8') as json_file:
        json.dump({'session_path': session_path}, json_file, ensure_ascii=False, indent=4)

    session_path = read_config()
    logger.info(f"{session_path}")
    entities = scan_session_files(session_path)
    for e in entities:
        logger.debug(e)
        client = TelegramClient(f"{session_path}/{e}")
        logger.info(f"{client}")
        tdesk = await client.ToTDesktop(flag=UseCurrentSession)
        logger.info(f"{tdesk}")
        logger.info(f"Saving Tdata/tdata")
        tdesk.SaveTData("Tdata/tdata")


asyncio.run(main())
