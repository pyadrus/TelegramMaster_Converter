import asyncio
import os
from datetime import datetime

from loguru import logger  # https://github.com/Delgan/loguru
from opentele.api import UseCurrentSession  # https://opentele.readthedocs.io/en/latest/#installation
from opentele.tl import TelegramClient
from rich import print  # https://rich.readthedocs.io/en/stable/appendix/colors.html

from config.config_manager import read_config, write_config, write_config2, read_config_tdata

logger.add("log/log.log")


def scan_session_files(session_path) -> list:
    """
    Возвращает список имен учетных записей по указанному пути сеанса.
    :param session_path: Путь к сеансу.
    :return: Список имен учетных записей.
    """
    entities = []  # Список имен учетных записей.
    for entry in os.scandir(session_path):
        if entry.is_file() and entry.name.endswith(".session"):
            file = os.path.splitext(entry.name)[0]  # Имя файла.
            print(f"Found accounts: {file}.session")
            entities.append(file)  # Добавляем имя файла в список.
    return entities  # Возвращаем список аккаунтов.


async def convert_session_to_tdata() -> None:
    """
    Преобразует файлы сеанса по указанному пути сеанса в файлы tdata.
    :return: None
    """
    session_path = read_config()  # Путь к сеансу
    logger.info(f"{session_path}")
    entities = scan_session_files(session_path)  # Список имен учетных записей.
    for e in entities:
        logger.debug(e)
        client = TelegramClient(f"{session_path}/{e}")
        logger.info(f"{client}")
        tdesk = await client.ToTDesktop(flag=UseCurrentSession)  # Получаем tdesk
        logger.info(f"{tdesk}")
        logger.info(f"Saving Tdata/tdata")
        tdata_path = read_config_tdata()  # Путь к tdata
        tdesk.SaveTData(f"{tdata_path}/{e}/tdata")  # Сохраняем tdata


async def wait_and_read():
    """
    Ожидает ввода команды и выполняет ее.
    :return: None
    """
    seen_files = set()

    while True:
        for entry in os.scandir('session'):
            if entry.is_file() and entry.name.endswith(".session"):
                if entry.path not in seen_files:
                    seen_files.add(entry.path)
                    # Файл появился, узнать текущее время
                    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    # Вывод информации о новом сеансе
                    print(f'[{current_time}] : {entry.name}')

        await asyncio.sleep(1)


async def main():
    """
    Основное меню программы
    :return: None
    """
    print('[medium_violet_red]TelegramMaster_Converter 28.02.2024 v.0.0.1\n\n'
          '[red][1] - Запустить конвертацию\n'
          '[red][2] - Путь к папке с сессиями\n'
          '[red][3] - Путь к папке с tdata\n'
          '[red][4] - Запуск конвертера в асинхронном режиме\n\n')

    user_input = input('Выберите пункт меню: ')
    if user_input == '1':  # Запустить конвертацию
        print('[chartreuse2]Запуск конвертации')
        await convert_session_to_tdata()

    elif user_input == '2':  # Путь к папке с сессиями
        print('[chartreuse2]Запись пути к папке с сессиями')
        user_input = input("Введите путь к папке с сессиями: ")
        session_path = rf"{user_input}"
        write_config(session_path)

    elif user_input == '3':  # Путь к папке с tdata
        print('[chartreuse2]Запись пути к папке с tdata')
        user_input = input("Введите путь к папке с tdata: ")
        tdata_path = rf"{user_input}"
        write_config2(tdata_path)

    elif user_input == '4':  # Запуск конвертера в асинхронном режиме
        print('[chartreuse2] Запуск конвертации в асинхронном режиме')
        await wait_and_read()  # Запускаем задачу на чтение файла


asyncio.run(main())
