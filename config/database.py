from re import S
from pymongo import MongoClient


class Database(object):
    def __init__(self):
        self._client = MongoClient(
            '')  # configure db url
        # self._client = MongoClient(
        #     'mongodb://localhost:27017/')  # configure db url
        self._db = self._client['animedb']

    def getDatabase(self):
        return self._db
