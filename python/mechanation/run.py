from phases.initiation import initiation_phase
from player import Pilot
from mechs.mech import guardian, dawnbringer

def declare_winner(players):
    return [player for player in players if player.is_winner]

def run():

    player_1 = Pilot(20, True)
    player_2 = Pilot(20)
    player_1.add_mech(guardian)
    player_2.add_mech(dawnbringer)
    round = 1
    winner = False
    while not winner:
    
        initiation_phase(round, player_1=player_1, player_2=player_2)
        
        # arena_phase()
        # pilot_phase()
        # scrap_phase()
        # print('hello! (a few times now)')
        round += 1
        if round == 20:
            print("Final round!!!!!!")
            initiation_phase(round, player_1=player_1, player_2=player_2)
            break


if __name__=='__main__':
    run()