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

        players

    )

    print("\n■予測結果")

    print(

        "本命:",

        result.get(

            "main",

            "-"

        )

    )

    print(

        "中穴:",

        result.get(

            "middle",

            "-"

        )

    )

    print(

        "穴:",

        result.get(

            "hole",

            "-"

        )

    )

    if "ranking" in result:

        print(

            "\n■選手評価"

        )

        for p in result["ranking"]:

            print(

                f'{p["boat"]}号艇 {p["score"]}点'

            )

print("\n======================")

print("=== 全12R解析終了 ===")
