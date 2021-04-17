from re import S
from pymongo import MongoClient


class Database(object):
    def __init__(self):
        self._client = MongoClient(
            'mongodb+srv://geovane:novembro123@cluster0.su9vu.mongodb.net')  # configure db url
        self._db = self._client['animedb']

    def getDatabase(self):
        return self._db
