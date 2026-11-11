from input_validation import valid_num
from logic_function import start_game,display_game_history,display_statistics
from output import display_game_results
from json_functions import load_game_history
def menu():
    print("""
================================
        ROLL DICE
================================

    1. Start New Game
    2. View Game History
    3. View Statistics
    4. Exit

    Choose an option:
        """)

def main():
    is_active = True
    while is_active:
        menu()
        choice = valid_num(4)
        if choice == 1:
            game = start_game()
            display_game_results(game)
        elif choice == 2:
            games = load_game_history()
            display_game_history(games)
        elif choice == 3:
            games = load_game_history()
            display_statistics(games)
        elif choice == 4:
            print('goodbye')
            is_active = False
main()