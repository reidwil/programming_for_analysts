import json
import random
from pathlib import Path
from dataclasses import dataclass
from abc import abstractmethod


# This should move to another file eventually as it will get quite large
@dataclass
class BaseMech:
    name: str
    health: int
    tier: int
    effect: dict
    damage_counter: int = None

@dataclass
class BaseEffects:
    id: str
    data: dict
    event_name: str
    rule: str

    @abstractmethod
    def get_effect(self, id): ...

class Effects(BaseEffects):
    def __init__(self):
        self.effects = json.loads(get_effects_schema())['effects']

    def get_effect(self, id: int):
        for effect in self.effects:
            if effect['id'] == id:
                return effect


def get_effects_schema() -> json:
    """Looks for all mechs """
    dir = Path.cwd() / "mechs"
    for file in dir.iterdir():
        if file.name == 'effects.json':
            return file.open().read()


def get_mechs():
    """Looks for all mechs """
    dir = Path.cwd() / "mechs"
    for file in dir.iterdir():
        if file.suffix == '.json' and file.name != 'effects.json':
            yield file.open().read()

class Card(BaseMech):
    def __init__(self, schema: dict):
        self.set_attrs(json.loads(schema))
        self.damage_counter = None

    def map_effects(self): ...

    def show(self):
        kws = [f"{key}={value!r}" for key, value in self.__dict__.items()]
        print("{}({})".format(type(self).__name__, ", ".join(kws)))

    def set_attrs(self, obj: dict):
        self.__dict__.update(obj)

class Deck():
    def __init__(self):
        self.deck = [Card(mech) for mech in get_mechs()]
        self.shuffle()

    def shuffle(self):
        """
        Shuffle method for the deck. This returns a random choice between two cards for each card in the deck.
        """
        for i in range(len(self.deck)-1, 0, -1):
            r = random.randint(0, i)
            self.deck[i], self.deck[r] = self.deck[r], self.deck[i]

    def draw(self):
        return self.deck.pop()

    def show(self):
        for card in self.deck:
            print(card)

def build_deck():
    return Deck()