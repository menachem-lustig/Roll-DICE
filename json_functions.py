from pathlib import Path
import json

path = Path(__file__).parent / "game_history.json"

def load_game_history():
    with open(path, "r", encoding="utf-8") as file:
        games = json.load(file)                    
    return games


def save_game(game):
    games = load_game_history()
    games.append(game)
    with open(path, "w", encoding="utf-8") as file:
        json.dump(games, file, indent=2, ensure_ascii=False)




