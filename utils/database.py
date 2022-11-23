from motor import motor_asyncio

from config import load_config

config = load_config()


class MongoDB:
    def __init__(self):
        if config.bot.debug:
            self.client = motor_asyncio.AsyncIOMotorClient(host='localhost', port=27017)
        else:
            self.client = motor_asyncio.AsyncIOMotorClient(
                host=config.db.host,
                port=config.db.port,
                username=config.db.username,
                password=config.db.password,
            )
        self.db = self.client[config.db.database]

    async def add_some_data(self):
        self.db.test.insert_one({"name": "test"})
