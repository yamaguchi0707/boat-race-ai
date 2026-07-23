from venue import get_venue_score

from player_data import get_players

def get_race_data():

    race = {

        "venue": "大村",

        "race_number": 1,

        "venue_data": get_venue_score(

            "大村"

        ),

        "weather": {

            "wind": 2,

            "direction": "向かい風",

            "temperature": 25

        },

        "odds": {

            "1-4-2": 8.5,

            "1-2-4": 12.4,

            "4-1-2": 35.0

        },

        "players": get_players()

    }

    return race
