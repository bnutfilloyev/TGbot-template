from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")
ADMINS = env.list("ADMINS")

MONGODB_HOSTNAME = env.str("MONGODB_HOSTNAME")
MONGODB_USERNAME = env.str("MONGODB_USERNAME")
MONGODB_PASSWORD = env.str("MONGODB_PASSWORD")
MONGODB_PORT = env.int("MONGODB_PORT")
