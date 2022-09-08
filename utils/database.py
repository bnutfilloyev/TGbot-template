from motor import motor_asyncio
from config import load_config

config = load_config()


class MongoDB:
    client = None
    db = None

    @staticmethod
    def get_client():
        if MongoDB.client is None:
            MONGODB_USERNAME = config.db.username
            MONGODB_PASSWORD = config.db.password
            MONGODB_HOSTNAME = config.db.host
            MONGODB_PORT = config.db.port

            MongoDB.client = motor_asyncio.AsyncIOMotorClient("mongodb://{}:{}@{}:{}".format(
                MONGODB_USERNAME, MONGODB_PASSWORD, MONGODB_HOSTNAME, str(MONGODB_PORT)))
        return MongoDB.client

    @staticmethod
    def get_data_base():
        if MongoDB.db is None:
            client = MongoDB.get_client()
            MongoDB.db = client[config.db.database]

        return MongoDB.db

    @staticmethod
    async def add_some_data():
        db = MongoDB.get_data_base()
        db.test.insert_one({"name": "test"})
