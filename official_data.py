import json

from datetime import datetime

def save_official_data(data):

    with open(

        "official_data.json",

        "w",

        encoding="utf-8"

    ) as f:

        json.dump(

            data,

            f,

            ensure_ascii=False,

            indent=4

        )

def create_test_data():

    races = []

    for race_no in range(1, 13):

        races.append({

            "race_number": race_no,

            "players": [

                {

                    "boat": 1,

                    "name": "選手A",

                    "rank": "A1",

                    "national_win_rate": 7.0,

                    "national_second_rate": 40,

                    "average_st": 0.12,

                    "motor_second_rate": 40,

                    "exhibition_time": 6.80

                },

                {

                    "boat": 2,

                    "name": "選手B",

                    "rank": "A2",

                    "national_win_rate": 6.0,

                    "national_second_rate": 30,

                    "average_st": 0.15,

                    "motor_second_rate": 35,

                    "exhibition_time": 6.85

                }

            ]

        })

    return {

        "update_time": str(datetime.now()),

        "venue": "大村",

        "races": races

    }

if __name__ == "__main__":

    data = create_test_data()

    save_official_data(data)

    print(

        "official_data.json 作成完了"
