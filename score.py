def calculate_score(player):

    score = 0

    # 全国成績

    score += (

        player["national_win_rate"]

        * 1.5

    )

    score += (

        player["national_second_rate"]

        * 0.5

    )

    score += (

        player["national_third_rate"]

        * 0.3

    )

    # 当地成績

    score += (

        player["local_win_rate"]

        * 1.0

    )

    score += (

        player["local_second_rate"]

        * 0.3

    )

    # ST評価

    if player["average_st"] <= 0.12:

        score += 15

    elif player["average_st"] <= 0.15:

        score += 8

    elif player["average_st"] >= 0.18:

        score -= 5

    # ST順位

    if player["st_rank"] <= 3:

        score += 5

    # モーター評価

    score += (

        player["motor_second_rate"]

        * 0.3

    )

    score += (

        player["motor_third_rate"]

        * 0.2

    )

    # 展示タイム評価

    diff = (

        player["exhibition_time"]

        -

        player["average_exhibition_time"]

    )

    if diff <= -0.05:

        score += 10

    elif diff <= -0.02:

        score += 5

    elif diff >= 0.05:

        score -= 5

    return round(score, 1)
