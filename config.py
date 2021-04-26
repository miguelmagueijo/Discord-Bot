import configparser
import pathlib
from configparser import ConfigParser

PRIVATE_CONFIG_PATH = "private/config.ini"
PUBLIC_CONFIG_PATH = "config.ini"

class FilesParser:
    def __init__(self):
        self._privateParser = ConfigParser().read(pathlib.Path(__file__).parent.absolute() / PRIVATE_CONFIG_PATH)
        self._publicParser = ConfigParser().read(pathlib.Path(__file__).parent.absolute() / PUBLIC_CONFIG_PATH)
        self._keys = self._privateParser["Keys"]
        self._botConfig = self._publicParser["BotConfig"]

class BotConfig:
    def __init__(self, botConfig: dict, keys):
        self.prefix = botConfig["prefix"]
        self.token = keys["development"]