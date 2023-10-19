import os

from dotenv import load_dotenv

load_dotenv()

#  API constants
DEVICE_ID = "A"
AMPLITUDE_API_KEY = os.environ.get("AMPLITUDE_API_KEY")
BOT_API_KEY = os.environ.get("BOT_API_KEY")

#  messages
WELCOME_MESSAGE = "НАПИШИ ЕГО!"
HELP_MESSAGE = "НАПИШИ ЕГО!"

# log config
LOGGING_FORMAT = "%(asctime)s - [%(levelname)s] - %(name)s - " \
                 "(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"

#  db constants
POSTGRES_DB = os.environ.get("POSTGRES_DB")
POSTGRES_USER = os.environ.get("POSTGRES_USER")
POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
POSTGRES_HOST = os.environ.get("POSTGRES_HOST")
POSTGRES_PORT = os.environ.get("POSTGRES_PORT")

