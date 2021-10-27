from typing import Set, Optional, Iterable
from dataclasses import field, dataclass
from Poker.exceptions import InvalidCardNumber, InvalidTrade, InvalidDeck


@dataclass(frozen=True)
class Card:
    name: str
    num: Optional[int] = None

    def __post_init__(self):
        if not self.num:
            return

        if self.num < 2 or self.num > 10:
            raise InvalidCardNumber(self)

    def __str__(self):
        return self.name if not self.num else f"{self.num} of {self.name}"


@dataclass
class Trade:
    trader_uno: tuple
    trader_two: tuple

    def __post_init__(self):
        trader_one_is_authorized = self.trader_uno[0]._authorize_trade(
            self.trader_uno[1], self.trader_two[1]
        )
        trader_two_is_authorized = self.trader_two[0]._authorize_trade(
            self.trader_two[1], self.trader_uno[1]
        )

        if not all((trader_one_is_authorized, trader_two_is_authorized)):
            raise InvalidTrade(self)


@dataclass(frozen=True)
class Spades(Card):
    def __init__(self, num):
        super().__init__(type(self).__name__, num)


@dataclass(frozen=True)
class Diamonds(Card):
    def __init__(self, num):
        super().__init__(type(self).__name__, num)


@dataclass(frozen=True)
class Hearts(Card):
    def __init__(self, num):
        super().__init__(type(self).__name__, num)


@dataclass(frozen=True)
class Clubs(Card):
    def __init__(self, num):
        super().__init__(type(self).__name__, num)


@dataclass(frozen=True)
class Joker(Card):
    def __init__(self):
        super().__init__(type(self).__name__)


@dataclass(frozen=True)
class Jack(Card):
    def __init__(self):
        super().__init__(type(self).__name__)


@dataclass(frozen=True)
class Queen(Card):
    def __init__(self):
        super().__init__(type(self).__name__)


@dataclass(frozen=True)
class King(Card):
    def __init__(self):
        super().__init__(type(self).__name__)


CARDS = [
    Spades(2),
    Spades(3),
    Spades(4),
    Spades(5),
    Spades(6),
    Spades(7),
    Spades(8),
    Spades(9),
    Spades(10),
    Clubs(2),
    Clubs(3),
    Clubs(4),
    Clubs(5),
    Clubs(6),
    Clubs(7),
    Clubs(8),
    Clubs(9),
    Clubs(10),
    Diamonds(2),
    Diamonds(3),
    Diamonds(4),
    Diamonds(5),
    Diamonds(6),
    Diamonds(7),
    Diamonds(8),
    Diamonds(9),
    Diamonds(10),
    Hearts(2),
    Hearts(3),
    Hearts(4),
    Hearts(5),
    Hearts(6),
    Hearts(7),
    Hearts(8),
    Hearts(9),
    Hearts(10),
    Joker(),
    King(),
    Queen(),
    Jack(),
]


@dataclass(frozen=True)
class Deck:
    _cards: Set[Card] = field(default_factory=lambda: set(CARDS[:]))

    @property
    def cards(self):
        return sorted(self._cards, key=lambda card: str(card))

    def __len__(self):
        return len(self.cards)

    def throw_card(self, card: Card) -> Card:
        self._cards.remove(card)
        return card

    def _trading(self, giving: Card, recieving: Card):
        self._cards.remove(giving)
        self._cards.add(recieving)

    def _authorize_trade(self, giving: Card, recieving: Card):
        return (giving in self._cards) and not (recieving in self._cards)

    def __post_init__(self):
        if not all(isinstance(i, Card) for i in self._cards):
            raise InvalidDeck(
                f"All the items in the Deck are not cards\nYour Deck: {self.cards}"
            )

    @staticmethod
    def trade_cards(trade: Trade):
        trade.trader_uno[0]._trading(trade.trader_uno[1], trade.trader_two[1])
        trade.trader_two[0]._trading(trade.trader_two[1], trade.trader_uno[1])

    @staticmethod
    def from_iterable(iterable: Iterable[Card]):
        return Deck(set(iterable))

    def __str__(self):
        return "\n".join(map(str, self.cards))
