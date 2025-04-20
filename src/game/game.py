from rules import roles
from random import randint

from src.game.cards.card import Card
from src.game.rules.roles import Role

#random module can be used to draw random cards (basic, special, character)

from player import Player

num_players = int(input("How many players? "))
result = roles.Role.get_roles(num_players)

players_role = [role for role in result]
#a list of lists; len(list) should be len(players_role) and len(players_health)
#each list: list[0] should be character card, list[1] should be its health value (make a dict),
# list[2] should be its abilities (make a dict), list[3] should be another list of basic and special cards
players_cards = []
#health subject to change; depends on the character card drawn
players_health = (randint(3,5))