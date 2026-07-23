from data import get_race_data

from score import calculate_score

from weather import weather_score

def course_bonus(boat):

    bonus = {

        1: 15,

        2: 8,

        3: 6,

        4: 10,

        5: 3,

        6: 0

    }

    return bonus.get(boat, 0)

def venue_bonus(boat, venue_data):

    bonus = 0

    if boat == 1:

        bonus += venue_data.get(

            "inside_strength",

            0

        )

    return bonus

def make_prediction():

    race = get_race_data()

    venue_data = race["venue_data"]

    weather = race["weather"]

    results = []

    for player in race["players"]:

        score = calculate_score(player)

        # コース補正

        score += course_bonus(

            player["boat"]

        )

        # 水面補正

        score += venue_bonus(

            player["boat"],

            venue_data

        )

        # 天候補正

        score += weather_score(

            player["boat"],

            weather

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

        key=lambda x: x["score"],

        reverse=True

    )

    return {

        "venue": race["venue"],

        "順位評価": results,

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
