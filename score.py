import json

def calculate_rank_score(player):

    rank = player.get("rank", "")

    if rank == "A1":

        return 20

    elif rank == "A2":

        return 10

    elif rank == "B1":

        return 5

    return 2

def calculate_win_rate_score(player):

    return float(

        player.get(

            "national_win_rate",

            0

        )

    ) * 5

def calculate_second_rate_score(player):

    return float(

        player.get(

            "national_second_rate",

            0

        )

    ) * 0.3

def calculate_st_score(player):

    st = float(

        player.get(

            "average_st",

            0

        )

    )

    if st <= 0.12:

        return 15

    elif st <= 0.15:

        return 10

    elif st <= 0.18:

        return 5

    return 0

def calculate_motor_score(player):

    return float(

        player.get(

            "motor_second_rate",

            0

        )

    ) * 0.4

def calculate_exhibition_score(player):

    exhibition = float(

        player.get(

            "exhibition_time",

            0

        )

    )

    if exhibition <= 0:

        return 0

    if exhibition <= 6.75:

        return 15

    elif exhibition <= 6.85:

        return 8

    return 0

def calculate_venue_score(venue):

    try:

        with open(

            "data/venue_data.json",

            "r",

            encoding="utf-8"

        ) as f:

            venue_data = json.load(f)

        info = venue_data.get(

            venue,

            {}

        )

        return info.get(

            "inside_bonus",

            0

        )

    except Exception:

        return 0

def calculate_score(player, venue="大村"):

    score = 0

    score += calculate_rank_score(player)

    score += calculate_win_rate_score(player)

    score += calculate_second_rate_score(player)

    score += calculate_st_score(player)

    score += calculate_motor_score(player)

    score += calculate_exhibition_score(player)

    score += calculate_venue_score(venue)

    return round(score, 1)

def calculate_all_scores(players, venue="大村"):

    results = []

    for player in players:

        results.append({

            "boat": player["boat"],

            "score": calculate_score(

                player,

                venue

            )

        })

    results.sort(

        key=lambda x: x["score"],

        reverse=True

    )

    return results
