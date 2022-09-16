from motor import motor_asyncio

from config import load_config

config = load_config()


class MongoDB:
    def __init__(self):
        self.client = motor_asyncio.AsyncIOMotorClient("mongodb://{}:{}@{}:{}".format(
            config.db.username, config.db.password, config.db.host, config.db.port))
        self.db = self.client[config.db.database]

    async def add_some_data(self):
        self.db.test.insert_one({"name": "test"})
