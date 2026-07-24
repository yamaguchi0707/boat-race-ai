from datetime import datetime

import json

from predict import make_prediction

print("=== ボートレースAI起動 ===")

print(

    "実行日時:",

    datetime.now()

)

print("\nデータ更新完了")

venue = "大村"

for race in range(1, 13):

    print("\n======================")

    print(

        f"■ {venue} {race}R 解析開始"

    )

    print("======================")

    with open(

        "official_data.json",

        encoding="utf-8"

    ) as f:

        data = json.load(f)

    players = data.get(

        "players",

        []

    )

    result = make_prediction(

        players,

        venue

    )

    print("\n■選手評価")

    for item in result["順位評価"]:

        print(

            f'{item["boat"]}号艇 {item["score"]}点'

        )

    print("\n■予想")

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

    print("\n■買い目15点")

    for i, ticket in enumerate(

        result["買い目15点"],

        1

    ):

        print(

            f"{i}. {ticket}"

        )

print("\n======================")

print("=== 全12R解析終了 ===")
