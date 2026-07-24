from datetime import datetime

from converter import convert_data

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

    print(f"■ {venue} {race}R 解析開始")

    print("======================")

    players = convert_data(race)

    result = make_prediction(players)

    print("\n■選手評価")

    for player in result["scores"]:

        print(

            f'{player["boat"]}号艇 {player["score"]}点'

        )

    print("\n■予想")

    print(

        "本命:",

        result["main"]

    )

    print(

        "中穴:",

        result["middle"]

    )

    print(

        "穴:",

        result["hole"]

    )

    print("\n■買い目15点")

    for i, buy in enumerate(

        result["buy"],

        1

    ):

        print(

            f"{i}. {buy}"

        )

print("\n======================")

print("=== 全12R解析終了 ===")
