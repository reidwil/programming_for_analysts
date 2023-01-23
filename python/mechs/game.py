from deck import build_deck
from player import Players

def initialize_game(player_list):
    deck = build_deck()
    players = Players(player_list)
    for player in players.players:
        for _ in range(3):
            player.deck.append(deck.draw())
    return players

players = initialize_game(['reid','hank'])

for player in players.players:
    print(f"{player.name}'s deck")
    for card in player.deck:
        print('\n')
        print(card.name, card.power)