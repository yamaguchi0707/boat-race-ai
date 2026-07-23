from venue import get_venue_score

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

        "players": []

    }

    # 6艇入力欄

    player_data = [

        [1, "選手名"],

        [2, "選手名"],

        [3, "選手名"],

        [4, "選手名"],

        [5, "選手名"],

        [6, "選手名"]

    ]

    for boat, name in player_data:

        race["players"].append({

            "boat": boat,

            "number": 0000,

            "name": name,

            "rank": "A1",

            "age": 0,

            "term": 0,

            "area": "",

            "win_rate": 0,

            "second_rate": 0,

            "third_rate": 0,

            "st": 0.00,

            "motor_rate": 0,

            "exhibition_time": 0.00,

            "average_exhibition_time": 0.00

        })

    return race
