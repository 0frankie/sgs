from src.game.cards.deck import Deck
from src.game.characters.wu.sun_shang_xiang import SunShangXiang
from src.game.characters.wu.sun_quan import SunQuan
from src.game.player import Player
from src.game.rules.roles import Role

p1 = Player(Role.EMPEROR, SunQuan())
p2 = Player(Role.REBEL, SunShangXiang())

def print_info() -> str:
    return "P1 HP: " + str(p1.health) + "\n" + "P1: " + str(p1.cards) + "\n" + "P2 HP: " + str(p2.health)  + "\n" + "P2: " + str(p2.cards)

deck = Deck()
deck.start_cards(p1)
deck.start_cards(p2)

print_info()

