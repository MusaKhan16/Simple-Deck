from Poker import *


def main():
    # Testing Trades
    Deck1, Deck2 = Deck(), Deck.from_iterable([Spades(10), Spades(4)])

    Deck1.throw_card(Spades(10))

    Deck.trade_cards(Trade((Deck1, Joker()), (Deck2, Spades(10))))

    assert Joker() in Deck2.cards and Spades(10) in Deck1.cards


if __name__ == "__main__":
    main()
