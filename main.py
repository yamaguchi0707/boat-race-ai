from datetime import datetime

from predict import make_prediction

from backtest import run_backtest

MODE = "predict"

# MODE = "backtest"

print("=== ボートレースAI起動 ===")

print("実行日時:", datetime.now())

if MODE == "predict":

    result = make_prediction()

    print("\nデータ更新完了")

    print("\n■開催場")

    print(result["venue"])

    print("\n■選手評価")

    for player in result["順位評価"]:

        print(

            f'{player["boat"]}号艇 {player["score"]}点'

        )

    print("\n■予想")

    print("本命:", result["本命"])

    print("中穴:", result["中穴"])

    print("穴:", result["穴"])

    print("\n■買い目15点")

    for i, buy in enumerate(result["買い目"], 1):

        print(f"{i}. {buy}")

elif MODE == "backtest":

    run_backtest()

print("\n=== 解析終了 ===")
