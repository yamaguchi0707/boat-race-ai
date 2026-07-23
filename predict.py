from data import get_race_data

from score import calculate_score

from weather import weather_score

from buy import generate_buy

def course_score(boat, venue):

    score = 0

    # イン有利場補正

    strong_inside = [

        "大村",

        "徳山",

        "芦屋",

        "下関"

    ]

    if boat == 1:

        if venue in strong_inside:

            score += 15

        else:

            score += 8

    # 2コース差し補正

    if boat == 2:

        score += 3

    return score

def make_prediction():

    race = get_race_data()

    results = []

    for player in race["players"]:

        score = calculate_score(player)

        score += course_score(

            player["boat"],

            race["venue"]

        )

        score += weather_score(

            player["boat"],

            race["weather"]

        )

        results.append({

            "boat": player["boat"],

            "name": player["name"],

            "score": round(

                score,

                1

            )

        })

    results.sort(

        key=lambda x:x["score"],

        reverse=True

    )

    buys = generate_buy(

        results,

        race["odds"]

    )

    return {

        "venue":

        race["venue"],

        "順位評価":

        results,

        "買い目":

        buys,

        "本命":

        f"{results[0]['boat']}-"

        f"{results[1]['boat']}-"

        f"{results[2]['boat']}",

        "中穴":

        f"{results[0]['boat']}-"

        f"{results[2]['boat']}-"

        f"{results[1]['boat']}",

        "穴":

        f"{results[3]['boat']}-"

        f"{results[0]['boat']}-"

        f"{results[1]['boat']}"

    }
