from src.game.cards.card import Card
from src.game.characters.character import Character
from src.game.rules.roles import Role

#random module can be used to draw random cards (basic, special, character)

class Player:
    used_kill = False
    def __init__(self, role: Role, character: Character):
        self._role = role
        self._character = character
        self._health = character.health + 1 if self._role == Role.EMPEROR else character.health
        self._cards = []
        self._max_health = character.health

    @property
    def role(self):
        return self._role

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, health):
        self._health = health

    @property
    def cards(self):
        return self._cards

    def append_cards(self, cards: [Card]):
        self._cards.append(cards[0])
        self._cards.append(cards[1])

    @property
    def character(self):
        return self._character

    @property
    def max_health(self):
        return self._max_health

    def play(self, index: int, other: "Player"):
        card = self._cards[index]
        if card.action(other):
            self.cards.pop(index)