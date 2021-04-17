class Episode:
    number: str
    date: str
    preview: str
    players: dict

    def __init__(self, **kwargs) -> None:
        self.number = kwargs.get('number')
        self.date = kwargs.get('date')
        self.preview = kwargs.get('preview')
        self.players = kwargs.get('players')
