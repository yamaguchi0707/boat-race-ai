import json

from datetime import datetime

def save_official_data(data):

    file_name = "official_data.json"

    with open(

        file_name,

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

    data = {

        "update_time": str(datetime.now()),

        "venue": "大村",

        "race_number": 1,

        "players": [

            {

                "boat": 1,

                "name": "選手A",

                "rank": "A1"

            },

            {

                "boat": 2,

                "name": "選手B",

                "rank": "A2"

            }

        ]

    }

    return data

if __name__ == "__main__":

    data = create_test_data()

    save_official_data(data)

    print(

        "official_data.json 作成完了"

    )
