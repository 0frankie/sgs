from src.game.characters.ability import Ability


class Character:
    def __init__(self, name: str, health: int, abilities: [Ability]):
        self._name = name
        self._health = health
        self._abilities = abilities

    @property
    def name(self):
        return self._name

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, new_health):
        self._health = new_health

    @property
    def abilities(self):
        return self._abilities