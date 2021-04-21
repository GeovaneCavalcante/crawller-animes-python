
from threading import Thread

import requests
from threading import Thread
from bs4 import BeautifulSoup

from ..entities.anime import Anime
from ..repositories.animes_repository import AnimesRepository
from ..helpers import cleaner
from ..entities.season import Season
from ..entities.episode import Episode


class ManagerAnimes:

    def __init__(self) -> None:
        self.animes_repository = AnimesRepository()

    def check_saved_anime(self, name_anime: str):
        anime = self.animes_repository.get_anime_by_name(
            name_anime)

        return anime
