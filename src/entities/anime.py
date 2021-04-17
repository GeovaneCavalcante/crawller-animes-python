from .season import Season


class Anime:
    category: str
    banner: str
    name: str
    note: str
    year: str
    description: str
    genres: list[str]
    seasons: list[Season]

    def __init__(self, **kwargs) -> None:
        self.discount = kwargs.get('discount')
        self.category = kwargs.get('category')
        self.banner = kwargs.get('banner')
        self.name = kwargs.get('name')
        self.note = kwargs.get('note')
        self.year = kwargs.get('year')
        self.description = kwargs.get('description')
        self.genres = kwargs.get('genres')
        self.seasons = kwargs.get('seasons')
