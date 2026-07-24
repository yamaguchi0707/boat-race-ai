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

def create_race_data():

    data = {

        "update_time": str(datetime.now()),

        "venue": "大村",

        "race_number": 1,

        "players": [

            {

                "boat": 1,

                "name": "",

                "rank": "",

                "national_win_rate": 0,

                "national_second_rate": 0,

                "average_st": 0,

                "motor_second_rate": 0,

                "exhibition_time": 0

            },

            {

                "boat": 2,

                "name": "",

                "rank": "",

                "national_win_rate": 0,

                "national_second_rate": 0,

                "average_st": 0,

                "motor_second_rate": 0,

                "exhibition_time": 0

            },

            {

                "boat": 3,

                "name": "",

                "rank": "",

                "national_win_rate": 0,

                "national_second_rate": 0,

                "average_st": 0,

                "motor_second_rate": 0,

                "exhibition_time": 0

            },

            {

                "boat": 4,

                "name": "",

                "rank": "",

                "national_win_rate": 0,

                "national_second_rate": 0,

                "average_st": 0,

                "motor_second_rate": 0,

                "exhibition_time": 0

            },

            {

                "boat": 5,

                "name": "",

                "rank": "",

                "national_win_rate": 0,

                "national_second_rate": 0,

                "average_st": 0,

                "motor_second_rate": 0,

                "exhibition_time": 0

            },

            {

                "boat": 6,

                "name": "",

                "rank": "",

                "national_win_rate": 0,

                "national_second_rate": 0,

                "average_st": 0,

                "motor_second_rate": 0,

                "exhibition_time": 0

            }

        ]

    }

    return data

if __name__ == "__main__":

    race_data = create_race_data()

    save_official_data(

        race_data

    )

    print(

        "official_data.json 作成完了"

    )
