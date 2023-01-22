from deck import build_deck
from player import Players

# players = Players()

deck = build_deck()
card_1 = deck.draw()
card_2 = deck.draw()

# This should take an array of cards (*cards)
def arena_battle(card_1, card_2):
    print(f"{card_1.name} \t {card_1.power}")
    print("\n\n \t")
    print(f"{card_2.name} \t {card_2.power}")

    if card_1.power == card_2.power:
        print("Both cards lose - EQUAL POWER")
        card_1.damaged_counter = 2
        card_2.damaged_counter = 2
    if card_1.power > card_2.power:
        print(f"{card_1.name} WINS")
        card_1.damaged_counter = 1
        card_2.damaged_counter = 2
    if card_2.power > card_1.power:
        print(f"{card_2.name} WINS")
        card_1.damaged_counter = 2
        card_2.damaged_counter = 1
    # card_2.show()

arena_battle(card_1, card_2)

card_1.show()
card_2.show()


def after_battle(card_1, card_2):
    print("\n---- ENTERING AFTER BATTLE PHASE\n")
    

after_battle(card_1, card_2)