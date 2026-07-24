import csv

import json

def convert_json_to_csv(

    json_file="official_data.json",

    csv_file="players.csv"

):

    with open(json_file, "r", encoding="utf-8") as f:

        data = json.load(f)

    players = data.get("players", [])

    fieldnames = [

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

        "average_exhibition_time",

    ]

    with open(csv_file, "w", newline="", encoding="utf-8") as f:

        writer = csv.DictWriter(f, fieldnames=fieldnames)

        writer.writeheader()

        for player in players:

            row = {key: player.get(key, "") for key in fieldnames}

            writer.writerow(row)

if __name__ == "__main__":

    convert_json_to_csv()
