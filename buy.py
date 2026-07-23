from odds import odds_score

def generate_buy(results):

    tickets = []

    boats = []

    for item in results:

        boats.append(

            item["boat"]

        )

    first = boats[0]

    for second in boats[1:]:

        for third in boats[1:]:

            if (

                first != second

                and first != third

                and second != third

            ):

                tickets.append({

                    "ticket":

                    f"{first}-{second}-{third}",

                    "score":

                    results[0]["score"]

                })

    # オッズ補正用

    for ticket in tickets:

        # 仮オッズ

        # 実データ接続後に変更

        ticket["score"] += odds_score(30)

    tickets.sort(

        key=lambda x: x["score"],

        reverse=True

    )

    return [

        ticket["ticket"]

        for ticket in tickets[:15]

    ]
