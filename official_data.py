import json

from datetime import datetime

OUTPUT_FILE = "official_data.json"

def create_player(boat):

    return {

        "boat": boat,

        "name": "",

        "rank": "",

        "national_win_rate": 0,

        "national_second_rate": 0,

        "average_st": 0,

        "motor_second_rate": 0,

        "exhibition_time": 0

    }

def create_races():

    races = []

    for race_number in range(1, 13):

        players = []

        for boat in range(1, 7):

            players.append(

                create_player(boat)

            )

        races.append({

            "race_number": race_number,

            "players": players

        })

    return races

def save_data():

    data = {

        "venue": "大村",

        "update_time": str(

            datetime.now()

        ),

        "races": create_races()

    }

    with open(

        OUTPUT_FILE,

        "w",

        encoding="utf-8"

    ) as f:

        json.dump(

            data,

            f,

            ensure_ascii=False,

            indent=4

        )

    print(

        "official_data.json 12R作成完了"

    )

if __name__ == "__main__":

    save_data()
