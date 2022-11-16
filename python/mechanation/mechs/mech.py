import json
from dataclasses import dataclass

@dataclass
class BaseMech:
    name: str
    health: int
    tier: int
    # effect: EffectObject 


class Mech(BaseMech):
    def __init__(self, mech_name: str):
        self.mech_dict = self.lookup(mech_name)
        self.set_attrs(self.mech_dict)

    def lookup(self, name: str) -> dict:
        with open(f'./mechs/{name}.json', 'r') as item:
            data = json.load(item)
        return data

    def __repr__(self):
        kws = [f"{key}={value!r}" for key, value in self.__dict__.items()]
        return "{}({})".format(type(self).__name__, ", ".join(kws))
        

    def set_attrs(self, obj: dict):
        self.__dict__.update(obj['metadata'])


guardian = Mech('guardian')
dawnbringer = Mech('dawnbringer')