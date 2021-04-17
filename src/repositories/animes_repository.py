from config.database import Database
from ..entities.anime import Anime


class AnimesRepository:

    def __init__(self):
        self.db = Database().getDatabase()

    def create(self, anime: Anime) -> str:

        anime_collection = self.db["animes"]
        anime_inserted = anime_collection.insert_one(anime)

        return anime_inserted.inserted_id

    def create_many(self, animes: 'list[Anime]') -> 'list[str]':

        anime_collection = self.db["animes"]
        anime_inserted = anime_collection.insert_many(animes)

        return anime_inserted.inserted_ids
