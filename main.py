import asyncio

import os

from loguru import logger  # https://github.com/Delgan/loguru
from opentele.api import UseCurrentSession  # https://opentele.readthedocs.io/en/latest/#installation
from opentele.tl import TelegramClient

from config.config_manager import read_config, write_config

logger.add("log/log.log")


def scan_session_files(session_path):
    """Returns a list of account names in the specified session path."""
    entities = []
    for entry in os.scandir(session_path):
        if entry.is_file() and entry.name.endswith(".session"):
            file = os.path.splitext(entry.name)[0]
            print(f"Found accounts: {file}.session")
            entities.append(file)
    return entities


async def main():
    """Main function"""
    print('TelegramMaster_Converter\n'
          '[1] - Запустить конвертацию\n'
          '[2] - Настройки\n')

    user_input = input('Выберите пункт меню: ')
    if user_input == '1':
        print('Запуск конвертации')

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

    elif user_input == '2':
        print('Настройки')

        user_input = input("Введите путь к папке с сессиями: ")
        session_path = rf"{user_input}"
        write_config(session_path)


asyncio.run(main())
