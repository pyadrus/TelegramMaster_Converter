import asyncio

from loguru import logger  # https://github.com/Delgan/loguru
from opentele.api import UseCurrentSession
from opentele.tl import TelegramClient

logger.add("log/log.log")


async def main():
    client = TelegramClient("77074966424.session")
    logger.info(f"{client}")

    tdesk = await client.ToTDesktop(flag=UseCurrentSession)

    tdesk.SaveTData("tdata")


asyncio.run(main())
