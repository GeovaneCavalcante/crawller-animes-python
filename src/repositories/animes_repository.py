from config.database import Database
from ..entities.anime import Anime


class AnimesRepository:

    def __init__(self):
        self.db = Database().getDatabase()

    def get_anime_by_name(self, name_anime: str):
        anime_collection = self.db["animes"]

        return anime_collection.find_one({'name': name_anime})

    def update_one(self, id: str, values):
        anime_collection = self.db["animes"]
        query = {"_id": id}
        values = {"$set": {"seasons": values}}

        anime_collection.update_one(query, values)

    def create(self, anime: Anime) -> str:

        anime_collection = self.db["animes"]
        anime_inserted = anime_collection.insert_one(anime)

        return anime_inserted.inserted_id

    def create_many(self, animes: 'list[Anime]') -> 'list[str]':

        anime_collection = self.db["animes"]
        anime_inserted = anime_collection.insert_many(animes)

        return anime_inserted.inserted_ids
