from pymongo import MongoClient


class Database(object):
    def __init__(self):
        self.client = MongoClient(
            'mongodb+srv://geovane:novembro123@cluster0.su9vu.mongodb.net/')
        self.db = self.client['animedb']
