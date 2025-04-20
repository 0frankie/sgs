class Character:
    def __init__(self, health, abilities):
        self._health = health
        self._abilities = abilities

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, new_health):
        self._health = new_health

    @property
    def abilities(self):
        return self._abilities