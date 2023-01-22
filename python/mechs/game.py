from deck import build_deck
from player import Players

def initialize_game(player_list):
    deck = build_deck()
    players = Players(player_list)
    for player in players.players:
        for _ in range(3):
            player.deck.append(deck.draw())
    return players
