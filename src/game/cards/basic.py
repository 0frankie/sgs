from src.game.cards.card import Card
from src.game.player import Player

class Basic(Card):
    def action(self, other: Player) -> bool:
        pass

    def indirect(self, ctx):
        pass

class Kill(Basic):
    def action(self, other: Player) -> bool:
        # auto uses dodge; change to player choice later
        if D in other.cards:
            other.cards.remove(D)
            print("They dodged!")
        else:
            other.health -= 1
            print("The attack succeeded!")
        return True
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
            print(other.character.name, "health is now", other.health)
            return True
        # needs logic to remove card from player after playing a card
        # lest the function return false
        else:
            print(other.character.name, "has max health. Peach wasn't consumed.")
            return False

    def indirect(self, ctx):
        pass

K = Kill()
D = Dodge()
P = Peach()