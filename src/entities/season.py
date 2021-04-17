from .episode import Episode


class Season:
    number: str
    episodes: list[Episode]

    def __init__(self, **kwargs) -> None:
        self.number = kwargs.get('number')
        self.episodes = kwargs.get('episodes')
