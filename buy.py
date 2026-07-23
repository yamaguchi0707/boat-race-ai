from odds import odds_score

def generate_buy(results, odds_data):

    tickets = []

    boats = []

    for item in results:

        boats.append(

            item["boat"]

        )

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

                        999

                    )

                    score = (

                        results[0]["score"]

                        +

                        odds_score(odds)

                    )

                    tickets.append({

                        "ticket": ticket,

                        "odds": odds,

                        "score": score

                    })

    tickets.sort(

        key=lambda x: x["score"],

        reverse=True

    )

    return [

        item["ticket"]

        for item in tickets[:15]

    ]
