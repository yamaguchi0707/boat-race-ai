from predict import make_prediction

def run_backtest():

    result = make_prediction()

    print("\n=== バックテスト ===")

    print("開催場:", result["venue"])

    print("本命:", result["本命"])

    print("中穴:", result["中穴"])

    print("穴:", result["穴"])

    print("\n買い目")

    for i, buy in enumerate(result["買い目"], 1):

        print(f"{i}. {buy}")
