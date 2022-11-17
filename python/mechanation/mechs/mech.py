from pathlib import Path
import json
from dataclasses import dataclass

# This should move to another file eventually as it will get quite large
@dataclass
class BaseMech:
    name: str
    health: int
    tier: int
    # effect: EffectObject

def get_mechs():
    """Looks for all mechs """
    dir = Path.cwd() / "mechs"
    for file in dir.iterdir():
        if file.suffix == '.json':
            yield file.open().read()

class MechBuilder(BaseMech):
    def __init__(self, schema: dict):
        self.set_attrs(json.loads(schema))

    def __repr__(self):
        kws = [f"{key}={value!r}" for key, value in self.__dict__.items()]
        return "{}({})".format(type(self).__name__, ", ".join(kws))

    def set_attrs(self, obj: dict):
        self.__dict__.update(obj)


if __name__=='__main__':
    mechs = []
    for mech in get_mechs():
        mechs.append(Mechbuilder(mech).metadata)
    print(mechs)