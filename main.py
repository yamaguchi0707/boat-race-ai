import json

from datetime import datetime

from predict import make_prediction

print("=== ボートレースAI起動 ===")

print(

    "実行日時:",

    datetime.now()

)

# official_data.json読み込み

with open(

    "official_data.json",

    "r",

    encoding="utf-8"

) as f:

    data = json.load(f)

print()

print("データ更新完了")

venue = data.get(

    "venue",

    "不明"

)

races = data.get(

    "races",

    []

)

for race in races:

    race_number = race.get(

        "race_number"

    )

    players = race.get(

        "players",

        []

    )

    print()

    print("======================")

    print(

        f"■ {venue} {race_number}R 解析開始"

    )

    print("======================")

    if len(players) < 6:

        print(

            "選手データ不足"

        )

        continue

    result = make_prediction(

        players,

        venue

    )

    print()

    print("■選手評価")

    for item in result["順位評価"]:

        print(

            f"{item['boat']}号艇 {item['score']}点"

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

    print("■買い目15点")

    for i, ticket in enumerate(

        result["買い目15点"],

        1

    ):

        print(

            f"{i}. {ticket}"

        )

print()

print("======================")

print("=== 全レース解析終了 ===")
