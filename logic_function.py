import random
from input_validation import valid_name,valid_num
from json_functions import load_game_history,save_game
from output import show_round,show_start_game

def roll_dice():
    return random.randint(1,6)

def calculate_winner(player_score, computer_score):
    if player_score > computer_score:
        return 'player'
    elif computer_score > player_score:
        return 'computer'
    else:
        return 'draw'


def play_round():
    player = roll_dice()
    computer = roll_dice()
    winner =  calculate_winner(player,computer)
    return {
            'round':0,
            "player_dice": player,
            "computer_dice": computer,
            "winner": winner
        }

def start_game():
    name = valid_name()
    rounds_number = valid_num(10)
    show_start_game(name,rounds_number)
    current_round = 0
    computer_score = 0
    plyer_score = 0
    results = []
    for i in range(rounds_number):

        round_dict = play_round()
        if round_dict['winner'] == 'player':
            round_dict['winner'] = name
            plyer_score +=1
        elif round_dict['winner'] == 'computer':
            computer_score +=1
        current_round +=1
        round_dict['round'] = current_round
        results.append(round_dict)
        show_round(round_dict,name)
    winner = calculate_winner(computer_score=computer_score,player_score=plyer_score )
    if winner == 'player':
        winner = name
    game=  {
    "player_name": name,
    "rounds": rounds_number,
    "player_score": plyer_score,
    "computer_score": computer_score,
    "winner": winner,
    "results":results}
    save_game(game)
    return game

        
def display_game_history(history):
    if not history:
        print('No games yet')
    else:
        count_game = 0
        for game in history:
            count_game += 1
            print(f"""
    ================================
            GAME {count_game}
    ================================
    plyer name: {game['player_name']}
    rounds number: {game['rounds']}
    player_score: {game["player_score"]}
    computer_score: {game["computer_score"]}
    winner: {game['winner']}

            """)




def display_statistics(history):
    if not history:
        print( 'No games yet')
    else:
        all_games = len(history)
        computer_win = len([game for game in history if game['winner']=='computer' ])
        draw = len([game for game in history if game['winner']=='draw'])
        player_win = all_games -computer_win - draw
        player_win_percentage = round(100 / all_games  * player_win,2)
        print(f"""
    ================================
            GAME HISTORY
    ================================
    all games: {all_games} games
    computer win: {computer_win} times
    player win: {player_win} times
    player_win_percentage: {player_win_percentage} %
    """)





