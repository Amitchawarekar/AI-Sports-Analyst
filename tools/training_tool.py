def suggest_training(query: str) -> str:
    if "batsman" in query.lower():
        return "Focus on net practice, power-hitting drills, and fitness training."
    elif "bowler" in query.lower():
        return "Work on yorkers, slower balls, and strength conditioning."
    else:
        return "General training: cardio, agility drills, and match simulations."
