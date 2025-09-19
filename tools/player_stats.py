import json

def get_player_stats(query: str) -> str:
    with open("data/players.json", "r") as f:
        players = json.load(f)
    for player in players:
        if query.lower() in player["name"].lower():
            return f"{player['name']} - Runs: {player['runs']}, Wickets: {player['wickets']}, Matches: {player['matches']}"
    return "No player stats found for your query."
