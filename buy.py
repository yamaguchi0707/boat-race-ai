from odds import odds_score

def generate_buy(results, odds_data):

    tickets = []

    score_map = {}

    for item in results:

        score_map[item["boat"]] = item["score"]

    boats = list(score_map.keys())

    for first in boats:

        for second in boats:

            for third in boats:

                if (

                    first != second

                    and first != third

                    and second != third

                ):

                    ticket = (

                        f"{first}-{second}-{third}"

                    )

                    odds = odds_data.get(

                        ticket,

                        30

                    )

                    # 着順ごとの重要度調整

                    race_score = (

                        score_map[first] * 1.5

                        +

                        score_map[second] * 1.0

                        +

                        score_map[third] * 0.7

                    )

                    # オッズ補正

                    total_score = (

                        race_score

                        +

                        odds_score(odds)

                    )

                    tickets.append({

                        "ticket": ticket,

                        "score": total_score,

                        "odds": odds

                    })

    tickets.sort(

        key=lambda x: x["score"],

        reverse=True

    )

    return [

        item["ticket"]

        for item in tickets[:15]

    ]
