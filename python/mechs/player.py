from dataclasses import dataclass
from enum import Enum
import itertools

from deck import build_deck

@dataclass
class Player():
    name: str
    id: Enum
    resources: list
    deck: list

class Players(Player):

    id_iterator = itertools.count()

    def __init__(self, players: list):
        self.players: list[Player] = []
        self.initialize_players(players)

    def initialize_players(self, players):
        for player in players:
            self.players.append(Player(name=player, id=next(self.id_iterator), resources=[], deck=[]))

    def total_players(self):
        return max([player.id for player in self.players])

    def draw_cards(self):
        deck = build_deck()
        for player in self.players:
            while len(player.deck) < 4:
                player.deck.append(deck.draw())

if __name__=='__main__':
    worthy_opponents = ['reid', 'trey', 'hank', 'swaggy p']
    players_obj = Players(worthy_opponents)
    players_obj.draw_cards()
    for player in players_obj.players:
        print(player.name, player.id, [card.name for card in player.deck])