import os

from configparser import ConfigParser

from aw_core.config import load_config

default_config = ConfigParser()
default_config["server"] = {
    "host": "localhost",
    "port": os.environ["PORT"],
    "storage": os.environ["STORAGE"],
    "cors_origins": os.environ["CORS_ORIGINS"]
}
default_config["server-testing"] = {
    "host": "localhost",
    "port": "5666",
    "storage": "peewee",
    "cors_origins": ""
}

config = load_config("aw-server", default_config)
