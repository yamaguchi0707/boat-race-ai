def calculate_score(player):

    score = 0

    # 全国成績

    score += player["national_win_rate"] * 1.5

    score += player["national_second_rate"] * 0.5

    score += player["national_third_rate"] * 0.3

    # 当地成績

    score += player["local_win_rate"] * 1.2

    score += player["local_second_rate"] * 0.4

    # ST評価

    if player["average_st"] <= 0.12:

        score += 12

    elif player["average_st"] <= 0.15:

        score += 6

    elif player["average_st"] >= 0.18:

        score -= 5

    # ST順位

    if player["st_rank"] == 1:

        score += 8

    elif player["st_rank"] <= 3:

        score += 4

    # モーター評価

    score += player["motor_second_rate"] * 0.5

    score += player["motor_third_rate"] * 0.3

    # 展示タイム評価

    if player["exhibition_time"] > 0:

        diff = (

            player["average_exhibition_time"]

            -

            player["exhibition_time"]

        )

        if diff >= 0.05:

            score += 12

        elif diff >= 0.02:

            score += 6

    # 級別補正

    if player["rank"] == "A1":

        score += 5

    elif player["rank"] == "A2":

        score += 3

    elif player["rank"] == "B1":

        score += 1

    return round(score, 1)
