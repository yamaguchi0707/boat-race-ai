import csv

import json

FIELDS = [

    "boat",

    "number",

    "name",

    "rank",

    "age",

    "term",

    "branch",

    "national_win_rate",

    "national_second_rate",

    "national_third_rate",

    "local_win_rate",

    "local_second_rate",

    "local_third_rate",

    "average_st",

    "st_rank",

    "motor_number",

    "motor_second_rate",

    "motor_third_rate",

    "exhibition_time",

    "average_exhibition_time"

]

DEFAULT = {

    "number": 0,

    "name": "",

    "rank": "",

    "age": 0,

    "term": 0,

    "branch": "",

    "national_win_rate": 0,

    "national_second_rate": 0,

    "national_third_rate": 0,

    "local_win_rate": 0,

    "local_second_rate": 0,

    "local_third_rate": 0,

    "average_st": 0,

    "st_rank": 0,

    "motor_number": 0,

    "motor_second_rate": 0,

    "motor_third_rate": 0,

    "exhibition_time": 0,

    "average_exhibition_time": 0

}

def convert_json_to_csv():

    print("=== データ変換開始 ===")

    with open(

        "official_data.json",

        "r",

        encoding="utf-8"

    ) as f:

        data = json.load(f)

    players = data.get(

        "players",

        []

    )

    with open(

        "players.csv",

        "w",

        newline="",

        encoding="utf-8"

    ) as f:

        writer = csv.DictWriter(

            f,

            fieldnames=FIELDS

        )

        writer.writeheader()

        count = 0

        for boat in range(1, 7):

            player = DEFAULT.copy()

            player["boat"] = boat

            for item in players:

                if item.get("boat") == boat:

                    player.update(item)

            writer.writerow(player)

            count += 1

    print("players.csv作成完了")

    print("生成データ:", count, "艇")

if __name__ == "__main__":

    convert_json_to_csv()
