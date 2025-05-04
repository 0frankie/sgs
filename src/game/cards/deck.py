from random import shuffle

from src.game.cards.basic import K, D, P
from src.game.cards.card import Card
from src.game.player import Player



class Deck:
    def __init__(self):
        self._deck = [K, K, K, P, K, P, P, K, K, K, K, P, D]
        self._played_cards = []

    @property
    def deck(self):
        return self._deck

    def shuffle_deck(self):
        shuffle(self._played_cards)
        self._deck = self._played_cards
        self._played_cards = []

    def give_cards(self, player: Player):
        player.append_cards([self._deck[-2], self._deck[-1]])
        # pops the last two cards
        self._deck.pop(); self._deck.pop()

    def start_cards(self, player):
        self.give_cards(player); self.give_cards(player)

    def played_cards_append(self, card: Card):
        self._played_cards.append(card)