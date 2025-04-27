from attr.validators import instance_of

from src.game.cards.card import Card
from src.game.player import Player

class Basic(Card):
    def indirect(self, ctx):
        pass

class Kill(Basic):
    def action(self, other: Player):
        # auto uses dodge; change to player choice later
        if isinstance(other.cards[0], Dodge):
            other.cards.remove(D)
            print("They dodged!")
        else:
            other.health -= 1
            print("The attack succeeded!")

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
            print("Other player health is now " + other.health)
        # needs logic to remove card from player after playing a card
        # lest the function return false
        else:
            pass

    def indirect(self, ctx):
        pass

K = Kill()
D = Dodge()
P = Peach()