from src.game.cards.card import Card
from src.game.player import Player


class Basic(Card):
    def action(self, other: Player):
        pass
    def indirect(self, ctx):
        pass

class Kill(Basic):
    def action(self, other: Player):
        # auto uses dodge; change to player choice later
        if other.cards.__contains__(Dodge):
            other.cards.remove(Dodge)
        else:
            other.health -= 1

    def indirect(self, ctx):
        pass

class Dodge(Basic):
    # dodges cannot be played during your turn
    def indirect(self, ctx):
        pass

class Peach(Basic):
    def action(self, other: Player):
        if other.health < other.max_health:
            other.health += 1
        # needs logic to remove card from player after playing a card
        # lest the function return false
        else:
            pass

    def indirect(self, ctx):
        pass