import asyncio
import getpass
from nio import AsyncClient

# username = "@luc.saffre:matrix.org"
username = "luc.saffre"
passwd = getpass.getpass("Password for {}:".format(username))

async def main():
    # https://riot.im/app/#/room/#lino-core:matrix.org
    client = AsyncClient("https://matrix.org", username)
    await client.login(passwd)
    await client.room_send(
        # room_id="!lino-core:matrix.org",
        room_id="!BhOVybUXrTqHDfwjWd:matrix.org",
        message_type="m.room.message",
        content={
            "msgtype": "m.text",
            "body": "Once again: Hello World"
        }
        # ignore_unverified_devices=False
    )
    await client.close()

asyncio.get_event_loop().run_until_complete(main())
