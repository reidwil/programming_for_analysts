from mechs.mech import BaseMech, Mech

class Pilot():
    def __init__(self, health, is_first_player = False):
        self.health = health
        self.is_first_player = is_first_player
        self.is_winner = False
        self.mechs: list(Mech) = []

    def show_mechs(self):
        for mech in self.mechs:
            print(f"\n\nName:\t{mech.name}\nHealth:\t{mech.health}\nTier:\t{mech.tier}")

    def add_mech(self, mech: Mech):
        self.mechs.append(mech)

    def remove_health(self, amount: int):
        self.health = self.health - amount

    def add_health(self, amount: int):
        self.health = self.health + amount


if __name__=='__main__': ...