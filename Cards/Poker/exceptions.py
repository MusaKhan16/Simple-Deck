class InvalidCardNumber(Exception):
    def __init__(self, num):
        super().__init__(
            f"Your card cannot be greater than 10 or smaller than 2\n Your cards number: {num}"
        )


class InvalidTrade(Exception):
    def __init__(self, trade):
        super().__init__(
            f"Your trade cannot go through since one of the Decks either doesnt have a card it is trying to give OR it already has a card it is trying to recieve\nThe Trade: {trade}"
        )


class InvalidDeck(Exception):
    pass
