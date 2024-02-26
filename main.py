import asyncio
import os
from loguru import logger  # https://github.com/Delgan/loguru
from opentele.api import UseCurrentSession  # https://opentele.readthedocs.io/en/latest/#installation
from opentele.tl import TelegramClient

logger.add("log/log.log")


def scan_session_files():
    entities = []  # Создаем словарь с именами найденных аккаунтов в папке session
    for x in os.listdir(path="session"):
        if x.endswith(".session"):
            file = os.path.splitext(x)[0]
            print(f"Найденные аккаунты: {file}.session")  # Выводим имена найденных аккаунтов
            entities.append(file)
    return entities


async def main():
    entities = scan_session_files()
    for e in entities:
        logger.debug(e)
        client = TelegramClient(f"session/{e}")
        logger.info(f"{client}")
        tdesk = await client.ToTDesktop(flag=UseCurrentSession)
        logger.info(f"{tdesk}")
        logger.info(f"Сохранение данных в Tdata/tdata")
        tdesk.SaveTData("Tdata/tdata")


asyncio.run(main())
