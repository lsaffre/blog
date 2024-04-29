"""
Trying to show why the logging module needs an async interface.
"""

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

import asyncio
from time import sleep

from asgiref.sync import sync_to_async


info = logger.info
ainfo = sync_to_async(logger.info)

async def task1():
    info("- Run task1")
    sleep(1)

async def task2(name):
    info("- Run %s", name)
    sleep(1)


async def main():
    # await ainfo("Start task runner ")
    info("Start task runner ")
    count = 0
    while count < 2:
        count += 1
        # await ainfo("Start loop %s.", count)
        info("Start loop %s.", count)
        await task1()
        await task2("foo")
        await task2("bar")

    # await ainfo("Done task runner ")
    info("Done task runner ")

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
