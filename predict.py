from score import calculate_all_scores

def course_bonus(boat):

    bonus = {

        1: 20,

        2: 8,

        3: 10,

        4: 12,

        5: 5,

        6: 3

    }

    return bonus.get(

        boat,

        0

    )

def water_bonus(player):

    bonus = 0

    wind = float(

        player.get(

            "wind_speed",

            0

        )

    )

    wave = float(

        player.get(

            "wave_height",

            0

        )

    )

    # 強風時はダッシュ勢評価

    if wind >= 5:

        if player["boat"] in [4,5,6]:

            bonus += 8

    # 波がある場合は技量差

    if wave >= 3:

        if player.get("rank") == "A1":

            bonus += 5

    return bonus

def make_prediction(players, venue="大村"):

    results = []

    for player in players:

        base = calculate_all_scores(

            [player]

        )[0]["score"]

        total = (

            base

            + course_bonus(

                player["boat"]

            )

            + water_bonus(

                player

            )

        )

        results.append(

            {

                "boat": player["boat"],

                "score": round(

                    total,

                    1

                )

            }

        )

    results.sort(

        key=lambda x:x["score"],

        reverse=True

    )

    ranking = [

        r["boat"]

        for r in results

    ]

    first = ranking[0]

    second = ranking[1]

    third = ranking[2]

    prediction = {

        "venue": venue,

        "順位評価": results,

        "本命":

            f"{first}-{second}-{third}",

        "中穴":

            f"{first}-{third}-{second}",

        "穴":

            f"{ranking[3]}-{first}-{second}"

    }

    return prediction
