def show_round(round_dict,name):
    if round_dict['winner'] == 'computer':
        statement = 'Computer win the round!'
    elif round_dict['winner'] == 'draw':
        statement = 'Draw'
    else:
        statement = f"{name} win the round!"
    print(f"""
    ---------- ROUND {round_dict['round']} ----------

    :  {name}  🎲 {round_dict["player_dice"]}
    Computer: 🎲 {round_dict["computer_dice"]}

    {statement}
    """)
def show_start_game(name,rounds):
    print(f"""
================================
          NEW GAME
================================

Player name: {name}
Number of rounds: {rounds}
""")

def display_game_results(game):
    print(f"""
================================
          GAME OVER
================================

{game["player_name"]}:    {game['player_score']} points
Computer: {game['computer_score']} points

WINNER: {game['winner']}!

Game saved successfully!

    """)
