import player

def initiation_phase(round, player_1: player.Pilot, player_2: player.Pilot):
    # first_player, second_player = get_player_order(player_1, player_2)
    if round == 3:
        print("round 3 means we take off health!")
        player_1.remove_health(4)


    print(f"""
    Initiation Phase!
    (Round #{round})
        First player: 
            {player_1.__dict__}
        Second player:
            {player_2.__dict__}
    """)

def get_player_order(p1, p2):
    if all([p1.is_first_player, p2.is_first_player]):
        raise "Error setting alpha order"

    return p1, p2 if p1.is_first_player else p2, p1