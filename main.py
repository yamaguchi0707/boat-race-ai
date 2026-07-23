from fetch import create_test_data, save_official_data

from predict import make_prediction

print("=== ボートレースAI起動 ===")

# データ更新

data = create_test_data()

save_official_data(data)

print("\nデータ更新完了")

# AI解析

result = make_prediction()

print("\n■開催場")

print(

    result["venue"]

)

print("\n■選手評価")

for player in result["順位評価"]:

    print(

        f"{player['boat']}号艇 "

        f"{player['score']}点"

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

    result["買い目"],

    1

):

    print(

        f"{i}. {ticket}"

    )

print("\n=== 解析終了 ===")
