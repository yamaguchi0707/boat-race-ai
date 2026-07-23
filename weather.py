def weather_score(boat, weather):

    score = 0

    wind = weather.get("wind", 0)

    direction = weather.get("direction", "")

    # 無風・弱風

    if wind <= 2:

        if boat == 1:

            score += 5

    # 向かい風

    elif "向かい風" in direction:

        # まくり・まくり差し有利

        if boat in [3, 4]:

            score += 5

        if boat == 1:

            score -= 2

    # 追い風

    elif "追い風" in direction:

        # イン・差し有利

        if boat == 1:

            score += 5

        if boat == 2:

            score += 3

    return score

def weather_comment(weather):

    wind = weather.get("wind", 0)

    direction = weather.get("direction", "")

    if wind >= 5:

        return f"強風 {direction}。展開波乱注意"

    elif wind >= 3:

        return f"{direction}。攻め艇注意"

    else:

        return "穏やかな水面"
