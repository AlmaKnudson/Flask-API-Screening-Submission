import ssl
import os
from dotenv import load_dotenv

from pymongo import MongoClient

load_dotenv()


# Secrets should be stored in environment variables and loaded from AWS Secrets Manager
# or Azure Key Vault into .env, but this will suffice for now


class Config:
    def __getitem__(self, item):
        return getattr(self, item)

    def __setitem__(self, key, value):
        return setattr(self, key, value)

    ENV = os.environ.get("FLASK_ENV")
    DEBUG = True
    TESTING = False
    MONGODB_USERNAME = os.environ.get("MONGODB_USERNAME")  # User expires in a week (Dec 15, 2020)
    MONGODB_PASSWORD = os.environ.get("MONGODB_PASSWORD")
    DATABASE_NAME = os.environ.get("DATABASE_NAME")
    DATABASE = MongoClient(
        host=f'mongodb+srv://{MONGODB_USERNAME}:{MONGODB_PASSWORD}{os.environ.get("DATABASE_DOMAIN")}/{DATABASE_NAME}?retryWrites=true&w=majority',
        serverSelectionTimeoutMS=3000,
        ssl=True,
        tlsAllowInvalidCertificates=True # Disable SSL as this is not prod
    )[DATABASE_NAME]
    LOG_FILENAME = os.environ.get("LOG_FILENAME")
