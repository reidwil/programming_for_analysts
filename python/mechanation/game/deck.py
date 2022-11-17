from mechs.mech import MechBuilder, get_mechs

class Deck:
    def __init__(self) -> None:
        self.deck = self.build_deck()

    def build_deck(self):
        return [MechBuilder(deck) for deck in get_mechs()]

    def show_deck(self):
        for card in self.deck:
            print(card)


deck = Deck()
deck.show_deck()