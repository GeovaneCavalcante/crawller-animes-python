
from threading import Thread

import requests
from threading import Thread
from bs4 import BeautifulSoup

from ..entities.anime import Anime
from ..repositories.animes_repository import AnimesRepository
from ..helpers import cleaner
from ..entities.season import Season
from ..entities.episode import Episode


class PageParser:

    def __init__(self) -> None:
        self.animes_repository = AnimesRepository()

    def get_all_pagination(self):
        url = 'https://animesonline.cc/anime/'

        request_page = requests.get(url)

        soup = BeautifulSoup(request_page.text, 'html.parser')

        content_pagination = soup.find(class_='pagination')
        raw_pagination = content_pagination.find('span').text

        range_pagination = cleaner.clear_pagination_text(raw_pagination)

        for page_number in range(range_pagination[0], range_pagination[1]+1):
            try:
                self.get_all_animes_by_page(page_number)
            except Exception as error:
                print(error)
                print('Error page: ', page_number)

    def get_all_animes_by_page(self, number_page):
        print("Página ======== %d" % number_page)
        url = 'https://animesonline.cc/anime/page/%d/' % number_page

        request_page = requests.get(url)

        soup = BeautifulSoup(request_page.text, 'html.parser')

        content_anime_list = soup.find(class_='items')

        try:
            raw_material = content_anime_list.findAll('article')
        except:
            raise('Method: get_all_animes_by_page, raw_material, anime_link: %s' %
                  url)

        animes_list = []

        for raw_anime in raw_material:
            raw_title = raw_anime.find('h3')

            link_content = raw_anime.find(class_='poster')
            link_anime = link_content.find('a')['href']
            info_anime = self.get_anime_detail(link_anime)
            anime = {
                'category': 'dublados',
                'banner': raw_anime.find('img')['src'],
                'name': raw_title.find('a').string,
                'note': raw_anime.find(class_='rating').text.strip(),
                'description': info_anime['description'],
                'genres': info_anime['genres'],
                'year': info_anime['year'],
                'seasons': info_anime['seasons'],
            }
            self.animes_repository.create(anime)
            animes_list.append(anime)

    def get_anime_detail(self, link_anime):
        print("Link ---- ", link_anime)
        request_page = requests.get(link_anime)

        soup = BeautifulSoup(request_page.text, 'html.parser')

        content_description = soup.find(class_='wp-content')

        content_genres = soup.find(class_='sgeneros')

        try:
            raw_genres = content_genres.findAll('a')
        except:
            raise('Method: get_anime_detail, get_genres, anime_link: %s' %
                  link_anime)

        genres = [genre.text for genre in raw_genres]

        try:
            raw_seasons = soup.find(
                "div", {"id": "seasons"}).findAll(class_='se-c')
        except:
            raise('Method: get_anime_detail, get_seasons, anime_link: %s' %
                  link_anime)

        seasons = []
        for raw_season in raw_seasons:
            content_number_season = raw_season.find(class_='se-q')
            number_season = content_number_season.find('span').text
            episodes_season = self.get_episodes_by_season(raw_season)

            info_season = {
                'number': number_season,
                'episodes': episodes_season
            }
            seasons.append(info_season)

        info_anime = {
            'description': content_description.find('p').text,
            'genres': genres,
            'year': soup.find(class_='date').text,
            'seasons': seasons
        }

        return info_anime

    def get_episodes_by_season(self, season) -> 'list[Episode]':
        content_episode = season.find(class_='episodios')

        try:
            raw_episodes = content_episode.findAll('li')
        except:
            raise('Method: get_episodes_by_season, raw_episodes')

        episodes = []
        for raw_episode in raw_episodes:
            number_episode = raw_episode.find(
                class_='numerando').text.split('-')[-1].strip()
            date_episode = raw_episode.find(
                class_='date').text

            content_preview = raw_episode.find(class_='imagen')
            preview = content_preview.find('img')['src']

            content_link_episode = raw_episode.find(class_='episodiotitle')
            link_episode = content_link_episode.find('a')['href']

            info_players = self.get_players_by_episode(link_episode)
            info_episode = {
                'number': number_episode,
                'date': date_episode,
                'preview': preview,
                'players': info_players
            }

            if info_players is not None:
                episodes.append(info_episode)

        return episodes

    def get_players_by_episode(self, link_episode):
        request_page = requests.get(link_episode)

        soup = BeautifulSoup(request_page.text, 'html.parser')
        content_options = soup.find(class_='options')

        try:
            raw_options = content_options.findAll(class_='options')
        except:
            raise('Method: get_players_by_episode, raw_options, episode_link: %s' %
                  link_episode)

        players = {}

        for raw_option in raw_options:
            description_option = str(raw_option.text.strip())
            option = raw_option['href'][1:]
            content_player = soup.find("div", {"id": option})

            try:
                link_player = content_player.find('iframe')['src']
            except:
                link_player = content_player.find('source')['src']

            if description_option.lower() == 'dublado':
                players['dubbed'] = link_player

            if description_option.lower() == 'legendado':
                players['subtitled'] = link_player

        return players
