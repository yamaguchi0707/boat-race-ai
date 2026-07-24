from datetime import datetime

import csv

from predict import make_prediction

print("=== ボートレースAI起動 ===")

print(

    "実行日時:",

    datetime.now()

)

players = []

with open(

    "players.csv",

    "r",

    encoding="utf-8"

) as f:

    reader = csv.DictReader(f)

    for row in reader:

        row["boat"] = int(

            row["boat"]

        )

        players.append(row)

print()

print("データ更新完了")

venue = "大村"

result = make_prediction(

    players,

    venue

)

print()

print("■開催場")

print(

    result["venue"]

)

print()

print("■選手評価")

for item in result["順位評価"]:

    print(

        f'{item["boat"]}号艇 {item["score"]}点'

    )

print()

print("■予想")

print(

    "本命:",

    result["本命"]

)

print(

    "中穴:",

    result["中穴"]

)

print(

    "穴:",

    result["穴"]

)

print()

print("=== 解析終了 ===")
