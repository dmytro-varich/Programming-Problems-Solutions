def ghostbusters(building: str) -> str:
    if ' ' in building:
        return building.replace(' ', '')
    else: 
        return "You just wanted my autograph didn't you?"
