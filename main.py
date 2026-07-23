
from predict import make_prediction

print("=== ボートレースAI起動 ===")

result = make_prediction()

print("\n■選手評価")

for player in result["順位評価"]:

    print(

        f"{player['boat']}号艇 : {player['score']:.1f}点"

    )

print("\n■予想")

print("本命:", result["本命"])

print("中穴:", result["中穴"])

print("穴:", result["穴"])

print("\n=== 解析終了 ===")
