from deck import build_deck, Card
from player import Players

# This should take an array of cards (*cards)
def arena_battle(card_1: Card, card_2: Card):
    print(f"{card_1.name} \t {card_1.power}")
    print("\n\n \t")
    print(f"{card_2.name} \t {card_2.power}")

    if card_1.power == card_2.power:
        print("Both cards lose - EQUAL POWER")
        card_1.damaged_counter = 2
        card_2.damaged_counter = 2
    elif card_1.power > card_2.power:
        print(f"{card_1.name} WINS")
        card_1.damaged_counter = 1
        card_2.damaged_counter = 2
    elif card_2.power > card_1.power:
        print(f"{card_2.name} WINS")
        card_1.damaged_counter = 2
        card_2.damaged_counter = 1
    else: 
        print("  :: ERROR :: Power issue between cards")


def after_battle(card_1, card_2):
    print("\n\t\tENTERING AFTER BATTLE PHASE")
    for card in (card_1, card_2):
        if card.damaged_counter:
            if card.damaged_counter == 1:
                card.damaged_counter = None
            else:
                card.damaged_counter = card.damaged_counter - 1
        print(f"{card.name} has {card.damaged_counter} damage counters.")
        
        print("")

def run():
    
    players = Players(['reid', 'hank'])
    for player in players.players:
        print(f"{player.name}")
    deck = build_deck()
    card_1 = deck.draw()
    card_2 = deck.draw()
    arena_battle(card_1, card_2)
    after_battle(card_1, card_2)

if __name__=='__main__':
    run()