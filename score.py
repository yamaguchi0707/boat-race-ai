def calculate_score(player):

    score = 0

    # 級別評価

    rank = player.get(

        "rank",

        ""

    )

    if rank == "A1":

        score += 20

    elif rank == "A2":

        score += 10

    elif rank == "B1":

        score += 5

    else:

        score += 2

    # 全国勝率評価

    win_rate = float(

        player.get(

            "national_win_rate",

            0

        )

    )

    score += win_rate * 5

    # 全国2連率

    second_rate = float(

        player.get(

            "national_second_rate",

            0

        )

    )

    score += second_rate * 0.3

    # ST評価

    st = float(

        player.get(

            "average_st",

            0

        )

    )

    if st <= 0.12:

        score += 15

    elif st <= 0.15:

        score += 10

    elif st <= 0.18:

        score += 5

    # モーター評価

    motor = float(

        player.get(

            "motor_second_rate",

            0

        )

    )

    score += motor * 0.4

    # 展示タイム評価

    exhibition = float(

        player.get(

            "exhibition_time",

            0

        )

    )

    if exhibition > 0:

        if exhibition <= 6.75:

            score += 15

        elif exhibition <= 6.85:

            score += 8

    return round(

        score,

        1

    )

def calculate_all_scores(players):

    results = []

    for player in players:

        score = calculate_score(

            player

        )

        results.append(

            {

                "boat": player["boat"],

                "score": score

            }

        )

    results.sort(

        key=lambda x: x["score"],

        reverse=True

    )

    return results
