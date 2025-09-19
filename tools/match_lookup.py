import json

def get_match_summary(query: str) -> str:
    with open("data/matches.json", "r") as f:
        matches = json.load(f)
    for match in matches:
        if query.lower() in match["match"].lower():
            return match["summary"]
    return "No match summary found for your query."
